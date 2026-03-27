Uma aplicação interativa desenvolvida em Python e Streamlit para experimentação, avaliação e refinamento de prompts utilizando modelos fundacionais através do AWS Bedrock.

Este projeto demonstra, na prática, o impacto da engenharia de prompts na qualidade das respostas geradas por IA, comparando lado a lado a saída de um prompt "cru" contra um prompt "refinado".

---

## 1. Arquitetura e Separação de Responsabilidades

O sistema foi desenhado com foco em desacoplamento e fail-fast, dividindo as responsabilidades nas seguintes camadas:

### Interface (UI)

* O arquivo `app.py` gerencia o estado da aplicação Streamlit
* Responsável por formulários de submissão
* Layout de comparação de resultados lado a lado

### Infraestrutura (AWS)

* Módulo: `app/infra/aws/bedrock_client.py`
* Encapsula a lógica do `boto3`
* Isola autenticação e invocação dos modelos da Anthropic (Claude)

### Configuração (Core)

* Módulo: `app/core/settings.py`
* Utiliza `pydantic-settings`
* Validação rigorosa das variáveis de ambiente
* Estratégia fail-fast: falha na inicialização caso credenciais estejam ausentes

---

## 2. Pré-requisitos

Para rodar o projeto localmente, sua máquina precisa de:

* **Python**: versão >= 3.12 (definido no `pyproject.toml`)
* **Credenciais AWS**: usuário IAM com permissão `bedrock:InvokeModel`
* **Acesso a Modelos**:

  * Modelo padrão: `global.anthropic.claude-haiku-4-5-20251001-v1:0`
  * Deve estar habilitado no console do AWS Bedrock na região configurada

---

## 🔹 3. Variáveis de Ambiente (.env)

Crie um arquivo `.env` na raiz do projeto.

O Pydantic validará a presença das chaves de infraestrutura.

### Exemplo mínimo viável:

```env
# ================================
# ☁️ Infraestrutura AWS Bedrock
# ================================
AWS_REGION="us-east-1"
AWS_ACCESS_KEY_ID="sua_access_key"
AWS_SECRET_ACCESS_KEY="sua_secret_key"
BEDROCK_MODEL_ID="global.anthropic.claude-haiku-4-5-20251001-v1:0"

# ================================
# 📌 Identidade e Servidor (Opcional)
# ================================
APP_NAME="Prompt Refinement Lab"
ENVIRONMENT="development"
HOST="0.0.0.0"
PORT=8000
```

---

## 4. Instalação e Execução

Recomenda-se o uso de um ambiente virtual (`.venv`).

### 1. Instalação das dependências

```bash
pip install -r requirements.txt
# ou via uv/poetry se configurado
```

### 2. Iniciando a aplicação Streamlit

Existem duas formas de iniciar o projeto:

#### Opção A (Direto pela UI na raiz)

```bash
streamlit run app.py
```

#### Opção B (Via orquestrador principal)

```bash
python app/main.py
```

> Nota: Se utilizar o `main.py`, verifique se o caminho do `subprocess.run` aponta corretamente para o arquivo Streamlit.

---

## 5. Fluxo de Uso (Workflow)

### 1. Input

O usuário insere um comando base na interface.

### 2. Refinamento

O `BedrockClient` intercepta o texto e aplica um prompt de sistema especializado para aprimorar a instrução original.

### 3. Invocação Paralela

O modelo (Claude) é invocado duas vezes:

* Uma com o prompt original
* Outra com o prompt refinado

### 4. Análise

Os resultados são exibidos em duas colunas, permitindo comparação direta e auditoria visual da eficácia da engenharia de prompts.

---

---

## 6. Uso com Node.js + TypeScript

Para usuários que desejam utilizar o AWS Bedrock com Node.js e TypeScript, abaixo está um exemplo equivalente ao client Python.

### Instalação

```bash
npm install @aws-sdk/client-bedrock-runtime dotenv
```

### Implementação

```ts
import { BedrockRuntimeClient, InvokeModelCommand } from "@aws-sdk/client-bedrock-runtime";
import * as dotenv from "dotenv";

dotenv.config();

interface Settings {
  awsAccessKeyId: string;
  awsSecretAccessKey: string;
  awsRegion: string;
}

const settings: Settings = {
  awsAccessKeyId: process.env.AWS_ACCESS_KEY_ID!,
  awsSecretAccessKey: process.env.AWS_SECRET_ACCESS_KEY!,
  awsRegion: process.env.AWS_REGION!,
};

function buildRefinementPrompt(userPrompt: string): string {
  return `
Você é um especialista em engenharia de prompt.

Reescreva o prompt abaixo para torná-lo mais claro, específico e eficaz.

Regras:
- Preserve a intenção original
- Adicione contexto relevante
- Defina formato de saída
- Reduza ambiguidades

Retorne apenas o prompt refinado.

Prompt original:
${userPrompt}
`;
}

export class BedrockClient {
  private client: BedrockRuntimeClient;

  constructor() {
    this.client = new BedrockRuntimeClient({
      region: settings.awsRegion,
      credentials: {
        accessKeyId: settings.awsAccessKeyId,
        secretAccessKey: settings.awsSecretAccessKey,
      },
    });
  }

  async invoke(prompt: string): Promise<string> {
    const modelId =
      process.env.BEDROCK_MODEL_ID ??
      "global.anthropic.claude-haiku-4-5-20251001-v1:0";

    const body = JSON.stringify({
      anthropic_version: "bedrock-2023-05-31",
      messages: [
        {
          role: "user",
          content: prompt,
        },
      ],
    });

    const command = new InvokeModelCommand({
      modelId,
      body,
      contentType: "application/json",
      accept: "application/json",
    });

    const response = await this.client.send(command);

    const responseBody = JSON.parse(
      new TextDecoder().decode(response.body)
    );

    return responseBody.content[0].text;
  }

  async refinePrompt(userPrompt: string): Promise<string> {
    const prompt = buildRefinementPrompt(userPrompt);
    return this.invoke(prompt);
  }
}
```

### Observações

* O SDK v3 da AWS utiliza arquitetura modular (melhor para bundle size)
* O `InvokeModelCommand` exige serialização manual do body
* O parsing da resposta depende do formato específico do modelo (Anthropic neste caso)

# FastAPI Template

📦 Template genérico de API com **FastAPI**, **Pydantic Settings** e suporte cross-platform para setup automático.

Este template oferece uma **estrutura inicial completa** para projetos Python com FastAPI, incluindo:

- Configurações via `.env`
- Endpoints básicos (`/` e `/health`)
- Middleware CORS configurável
- Scripts para setup e execução em **Windows, Linux e macOS**
- Estrutura pronta para expansão (routers, serviços, core)

---

## 🔹 Estrutura do projeto

```
fastapi-template/
├─ app/
│ ├─ init.py
│ ├─ main.py # App FastAPI principal
│ └─ core/
│ ├─ init.py
│ └─ settings.py # Configurações da API e modelos Pydantic
├─ .env # Variáveis de ambiente
├─ requirements.txt # Dependências do projeto
├─ setup.sh # Setup Linux/macOS
├─ setup.ps1 # Setup Windows PowerShell
├─ setup.bat # Setup Windows CMD
├─ dev.bat # Roda FastAPI no Windows
└─ README.md # Documentação
```

---

## 🔹 Variáveis de ambiente (`.env`)

Exemplo mínimo:

```env
# ================================
# 📌 Identidade da aplicação
# ================================
APP_NAME="FastAPI Template"
DESCRIPTION="Template para APIs python com FastAPI"
ENVIRONMENT=development   # development | production | testing

# ================================
# ⚙️ Configurações do servidor
# ================================
HOST=0.0.0.0
PORT=8000
DEBUG=False

# ================================
# 🌍 CORS
# ================================
ALLOWED_ORIGINS=["*"]
ALLOWED_CREDENTIALS=True
ALLOWED_METHODS=["*"]
ALLOWED_HEADERS=["*"]
```

> O `Pydantic Settings` mapeia automaticamente essas variáveis para `app.core.settings.Settings`.

___

## 🔹 Scripts de setup

**Linux/macOS**

```bash
./setup.sh
```

- Cria `.venv` se não existir
- Ativa .venv
- Atualiza pip
- Instala dependências
- Instruções para rodar `uvicorn` no final

**Windows PowerShell**

```powershell
Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass
.\setup.ps1
```

**Windows CMD**

```cmd
setup.bat
```

**Rodar aplicação**

```bash
uvicorn app.main:app --reload
```
___

## 🔹 Endpoints básicos

| Endpoint | Método |                                              Descrição |
| :------- | :----: | -----------------------------------------------------: |
| /        |  GET   | Retorna informações do app e servidor {`RootResponse`} |
| /health  |  GET   |                 Health check da API {`HealthResponse`} |

**Modelos de resposta**

```json
// RootResponse
{
  "application": {
    "name": "FastAPI Template",
    "description": "Template genérico de API",
    "environment": "development"
  },
  "server": {
    "host": "0.0.0.0",
    "port": 8000,
    "debug": false
  }
}

// HealthResponse
{
  "status": "ok",
  "message": "O serviço está funcionando corretamente!"
}
```
___

## 🔹 Dependências principais

- FastAPI
- Uvicorn
- Pydantic Settings
- Python >= 3.12

___

## 🔹 Dependências principais

- `.venv` isolado do sistema
- Configuração CORS pronta para uso
- Separação clara entre core, routers, services
- Script cross-plataform para setup rápido
- Preparado para expansão modular

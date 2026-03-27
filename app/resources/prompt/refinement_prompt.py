def build_refinement_prompt(user_prompt: str) -> str:
    return f"""
Você é um especialista em engenharia de prompts para modelos de linguagem.

Sua tarefa é reescrever o prompt fornecido para maximizar a qualidade da resposta gerada por uma IA.

OBJETIVO:
Transformar um prompt simples em um prompt estruturado, claro e otimizado.

REGRAS DE REESCRITA:
1. Preserve a intenção original do usuário.
2. Torne o pedido mais específico e inequívoco.
3. Adicione contexto relevante quando necessário.
4. Defina explicitamente o formato da resposta esperada.
5. Especifique o nível de detalhe (ex: resumo, explicação completa, passo a passo).
6. Quando aplicável, inclua:
   - exemplos
   - listas ou bullet points
   - estrutura em seções
   - explicação teorica
7. Elimine ambiguidades.

SAÍDA:
- Retorne APENAS o prompt refinado
- NÃO explique nada

PROMPT ORIGINAL:
\"\"\"{user_prompt}\"\"\"
"""

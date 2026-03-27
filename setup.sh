#!/bin/bash
# ======================================
# Setup automático do projeto (Linux/macOS)
# ======================================

# 1️⃣ Criar .venv, se não existir
if [ ! -d ".venv" ]; then
    echo "Criando ambiente virtual .venv..."
    python3 -m venv .venv
else
    echo "Ambiente virtual já existe."
fi

# 2️⃣ Ativar venv
echo "Ativando ambiente virtual..."
source .venv/bin/activate

# 3️⃣ Atualizar pip
echo "Atualizando pip..."
python -m pip install --upgrade pip

# 4️⃣ Instalar dependências
if [ -f "requirements.txt" ]; then
    echo "Instalando dependencias do requirements.txt..."
    pip install -r requirements.txt
else
    echo "Instalando dependencias basicas..."
    pip install fastapi uvicorn "pydantic-settings>=2.10.1"
fi

echo "Setup concluido! Para rodar o dev:"
echo "uvicorn app.main:app --reload"

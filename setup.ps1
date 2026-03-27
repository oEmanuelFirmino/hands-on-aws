# ======================================
# Setup automático do projeto (Windows PowerShell)
# ======================================

# 1️⃣ Criar .venv, se não existir
if (-Not (Test-Path ".venv")) {
    Write-Host "Criando ambiente virtual .venv..."
    python -m venv .venv
} else {
    Write-Host "Ambiente virtual ja existe."
}

# 2️⃣ Ativar venv
Write-Host "Ativando ambiente virtual..."
. .\.venv\Scripts\Activate.ps1

# 3️⃣ Atualizar pip
Write-Host "Atualizando pip..."
python -m pip install --upgrade pip

# 4️⃣ Instalar dependências
if (Test-Path "requirements.txt") {
    Write-Host "Instalando dependencias do requirements.txt..."
    pip install -r requirements.txt
} else {
    Write-Host "Instalando dependencias basicas..."
    pip install fastapi uvicorn "pydantic-settings>=2.10.1"
}

Write-Host "Setup concluido!"
Write-Host "Para rodar a aplicacao:"
Write-Host "`tuvicorn app.main:app --reload"

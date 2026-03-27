@echo off
REM ======================================
REM Setup do projeto FastAPI no Windows CMD
REM ======================================

REM 1️⃣ Criar venv se não existir
IF NOT EXIST ".venv" (
    echo Criando ambiente virtual .venv...
    python -m venv .venv
) ELSE (
    echo Ambiente virtual ja existe.
)

REM 2️⃣ Ativar venv
call .venv\Scripts\activate

REM 3️⃣ Atualizar pip
python -m pip install --upgrade pip

REM 4️⃣ Instalar dependencias
IF EXIST "requirements.txt" (
    echo Instalando dependencias do requirements.txt...
    pip install -r requirements.txt
) ELSE (
    echo Instalando dependencias basicas...
    pip install fastapi uvicorn "pydantic-settings>=2.10.1"
)

echo Setup concluido!
echo Para rodar a aplicacao use:
echo uvicorn app.main:app --reload

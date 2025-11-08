@echo off
echo ========================================
echo Plataforma de Compatibilidad Emocional
echo ========================================
echo.

echo Verificando instalacion de Python...
python --version
if errorlevel 1 (
    echo ERROR: Python no esta instalado
    echo Por favor instala Python 3.8 o superior
    pause
    exit /b 1
)

echo.
echo Instalando dependencias...
cd backend
pip install -r requirements.txt

echo.
echo ========================================
echo Iniciando servidor backend...
echo ========================================
echo.
echo El servidor estara disponible en:
echo http://localhost:8000
echo.
echo Presiona Ctrl+C para detener el servidor
echo.

start http://localhost:8000
uvicorn main:app --reload

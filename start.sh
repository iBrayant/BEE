#!/bin/bash

echo "========================================"
echo "Plataforma de Compatibilidad Emocional"
echo "========================================"
echo ""

echo "Verificando instalación de Python..."
if ! command -v python3 &> /dev/null; then
    echo "ERROR: Python no está instalado"
    echo "Por favor instala Python 3.8 o superior"
    exit 1
fi

python3 --version

echo ""
echo "Instalando dependencias..."
cd backend
pip3 install -r requirements.txt

echo ""
echo "========================================"
echo "Iniciando servidor backend..."
echo "========================================"
echo ""
echo "El servidor estará disponible en:"
echo "http://localhost:8000"
echo ""
echo "Presiona Ctrl+C para detener el servidor"
echo ""

# Abrir navegador (funciona en macOS y Linux)
if [[ "$OSTYPE" == "darwin"* ]]; then
    open http://localhost:8000
elif [[ "$OSTYPE" == "linux-gnu"* ]]; then
    xdg-open http://localhost:8000 2>/dev/null
fi

uvicorn main:app --reload

import sys
import os

# Agregar el directorio backend al path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'backend'))

# Importar la app de FastAPI
from main import app

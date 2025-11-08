import sys
import os

# Agregar el directorio backend al path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'backend'))

from main import app

# Vercel necesita que la app se llame 'app' o se exporte como handler
def handler(request):
    return app(request)

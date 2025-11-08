# 🚀 Instrucciones de Ejecución

## Paso a Paso para Ejecutar la Plataforma

### 1️⃣ Instalar Dependencias

Abre una terminal en la carpeta `backend` y ejecuta:

```bash
cd backend
pip install -r requirements.txt
```

Esto instalará:
- FastAPI (framework web)
- Uvicorn (servidor ASGI)
- Pydantic (validación de datos)
- NumPy (cálculos numéricos)
- Pandas (análisis de datos)

### 2️⃣ Ejecutar el Backend

Desde la carpeta `backend`, ejecuta:

```bash
uvicorn main:app --reload
```

Verás algo como:
```
INFO:     Uvicorn running on http://127.0.0.1:8000 (Press CTRL+C to quit)
INFO:     Started reloader process
INFO:     Started server process
INFO:     Waiting for application startup.
INFO:     Application startup complete.
```

El servidor estará disponible en: `http://localhost:8000`

Puedes verificar que funciona visitando: `http://localhost:8000` en tu navegador.

### 3️⃣ Abrir el Frontend

Simplemente abre el archivo `frontend/index.html` en tu navegador web:

- **Opción 1**: Doble clic en el archivo
- **Opción 2**: Clic derecho → "Abrir con" → Tu navegador preferido
- **Opción 3**: Arrastra el archivo a una ventana del navegador

### 4️⃣ Usar la Plataforma

1. Ajusta los sliders para las respuestas de la Persona A (0-10)
2. Ajusta los sliders para las respuestas de la Persona B (0-10)
3. Haz clic en "🔍 Calcular Compatibilidad"
4. Espera unos segundos mientras la IA procesa
5. Revisa los resultados:
   - Porcentaje de compatibilidad
   - Gráficos radar y de barras
   - Fortalezas y áreas de mejora
   - Recomendaciones personalizadas

### 5️⃣ Probar el Sistema (Opcional)

Para ver un ejemplo detallado del cálculo, ejecuta:

```bash
cd backend
python test_example.py
```

Este script muestra paso a paso:
- Cálculo de lógica difusa
- Ajuste Bayesiano
- Análisis completo

## 🔧 Solución de Problemas

### Error: "ModuleNotFoundError"
**Solución**: Asegúrate de haber instalado las dependencias:
```bash
pip install -r requirements.txt
```

### Error: "Address already in use"
**Solución**: El puerto 8000 está ocupado. Usa otro puerto:
```bash
uvicorn main:app --reload --port 8001
```

Y actualiza en `frontend/app.js` la línea:
```javascript
const API_URL = 'http://localhost:8001/api/compatibilidad';
```

### Error: "CORS policy"
**Solución**: Asegúrate de que el backend esté ejecutándose antes de abrir el frontend.

### El frontend no se conecta al backend
**Solución**: Verifica que:
1. El backend esté ejecutándose (`http://localhost:8000`)
2. No haya errores en la consola del navegador (F12)
3. La URL en `app.js` sea correcta

## 📱 Compatibilidad

- **Navegadores**: Chrome, Firefox, Edge, Safari (versiones recientes)
- **Sistema Operativo**: Windows, macOS, Linux
- **Python**: 3.8 o superior

## 🎓 Conceptos Técnicos Implementados

### Backend (Python)
- **FastAPI**: Framework web moderno y rápido
- **Lógica Difusa**: Funciones de membresía y reglas difusas
- **Modelo Bayesiano**: Inferencia probabilística
- **Pandas**: Análisis y manipulación de datos

### Frontend (JavaScript)
- **Fetch API**: Comunicación asíncrona con el backend
- **Chart.js**: Visualización de datos interactiva
- **CSS Grid**: Layout responsive moderno

## 📊 Ejemplo de Petición API

Puedes probar el API directamente con herramientas como Postman o curl:

```bash
curl -X POST http://localhost:8000/api/compatibilidad \
  -H "Content-Type: application/json" \
  -d '{
    "persona_a": {
      "comunicacion": 8,
      "valores": 9,
      "conflicto": 7,
      "estilo_emocional": 6,
      "tiempo_compartido": 8,
      "intimidad": 7,
      "metas_futuro": 9,
      "apoyo_mutuo": 8
    },
    "persona_b": {
      "comunicacion": 7,
      "valores": 8,
      "conflicto": 6,
      "estilo_emocional": 5,
      "tiempo_compartido": 9,
      "intimidad": 8,
      "metas_futuro": 8,
      "apoyo_mutuo": 7
    }
  }'
```

## 🎯 Próximos Pasos

Una vez que todo funcione, puedes:

1. Experimentar con diferentes respuestas
2. Revisar el código para entender la lógica
3. Modificar las funciones de membresía en `fuzzy.py`
4. Ajustar los pesos de las dimensiones
5. Agregar nuevas dimensiones emocionales

¡Disfruta explorando la IA aplicada a la compatibilidad emocional! 💕

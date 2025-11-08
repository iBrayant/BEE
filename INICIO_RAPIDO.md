# 🚀 Inicio Rápido - 3 Pasos

## ⚡ Ejecución Rápida

### Windows
```bash
# Doble clic en:
start.bat
```

### Linux/Mac
```bash
chmod +x start.sh
./start.sh
```

---

## 📝 Ejecución Manual (3 pasos)

### 1️⃣ Instalar Dependencias
```bash
cd backend
pip install -r requirements.txt
```

### 2️⃣ Iniciar Backend
```bash
uvicorn main:app --reload
```
✅ Servidor corriendo en: `http://localhost:8000`

### 3️⃣ Abrir Frontend
Doble clic en: `frontend/index.html`

---

## 🎯 Uso

1. **Ajusta los sliders** para ambas personas (0-10)
2. **Haz clic** en "🔍 Calcular Compatibilidad"
3. **Revisa** los resultados:
   - Porcentaje de compatibilidad
   - Gráficos radar y barras
   - Fortalezas y áreas de mejora
   - Recomendaciones

---

## 🧪 Probar el Sistema

```bash
cd backend
python test_example.py
```

Esto mostrará un ejemplo completo del cálculo paso a paso.

---

## 📚 Documentación

- **README.md**: Descripción general
- **INSTRUCCIONES.md**: Guía detallada
- **CONCEPTOS_IA.md**: Teoría de IA
- **EJEMPLOS_USO.md**: Casos de prueba
- **FAQ.md**: Preguntas frecuentes

---

## ⚠️ Problemas Comunes

### Error: "pip no se reconoce"
```bash
python -m pip install -r requirements.txt
```

### Error: "Puerto 8000 ocupado"
```bash
uvicorn main:app --reload --port 8001
```
Y actualiza `API_URL` en `frontend/app.js`

### Frontend no se conecta
1. Verifica que el backend esté corriendo
2. Abre la consola del navegador (F12)
3. Revisa errores de CORS

---

## 🎓 Conceptos de IA Implementados

✅ **Lógica Difusa**: Funciones de membresía y reglas  
✅ **Modelo Bayesiano**: Inferencia probabilística  
✅ **Pandas**: Análisis de datos  
✅ **Visualización**: Gráficos interactivos  

---

## 📊 Estructura del Proyecto

```
proyecto/
├── backend/
│   ├── main.py              # FastAPI server
│   ├── requirements.txt     # Dependencias
│   └── core/
│       ├── fuzzy.py         # Lógica difusa
│       ├── probabilistic.py # Modelo Bayesiano
│       └── analyzer.py      # Análisis
└── frontend/
    ├── index.html           # Interfaz
    ├── styles.css           # Estilos
    └── app.js               # Lógica JS
```

---

## 🔥 Ejemplo de Petición API

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

---

## ✨ ¡Listo!

Ya tienes una plataforma completa de compatibilidad emocional con IA funcionando.

**Próximos pasos:**
1. Experimenta con diferentes respuestas
2. Revisa el código para entender la lógica
3. Modifica y personaliza según tus necesidades
4. Aprende sobre lógica difusa y modelos Bayesianos

---

**¿Necesitas ayuda?** Revisa `FAQ.md` o `INSTRUCCIONES.md`

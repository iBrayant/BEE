# ❓ Preguntas Frecuentes (FAQ)

## 📋 General

### ¿Qué es esta plataforma?
Es una aplicación web educativa que evalúa la compatibilidad emocional entre dos personas usando técnicas de Inteligencia Artificial: Lógica Difusa y Modelos Probabilísticos Bayesianos.

### ¿Es gratis?
Sí, es completamente gratuito y de código abierto. Puedes usarlo, modificarlo y aprender de él.

### ¿Necesito crear una cuenta?
No. La plataforma no requiere login ni almacena datos. Todo funciona en memoria.

### ¿Es un diagnóstico profesional?
No. Es una herramienta educativa y de reflexión. No reemplaza la terapia de pareja profesional.

---

## 🔧 Instalación y Configuración

### ¿Qué necesito para ejecutar el proyecto?
- Python 3.8 o superior
- Un navegador web moderno (Chrome, Firefox, Edge, Safari)
- Conexión a internet (solo para descargar dependencias)

### ¿Cómo instalo las dependencias?
```bash
cd backend
pip install -r requirements.txt
```

### ¿Puedo usar un entorno virtual?
Sí, es recomendado:
```bash
python -m venv venv
# Windows:
venv\Scripts\activate
# Linux/Mac:
source venv/bin/activate
pip install -r requirements.txt
```

### Error: "pip no se reconoce como comando"
Asegúrate de que Python esté en tu PATH. Intenta:
```bash
python -m pip install -r requirements.txt
```

---

## 🚀 Ejecución

### ¿Cómo inicio el servidor?
```bash
cd backend
uvicorn main:app --reload
```

### ¿En qué puerto corre el servidor?
Por defecto en el puerto 8000: `http://localhost:8000`

### ¿Puedo cambiar el puerto?
Sí:
```bash
uvicorn main:app --reload --port 8001
```
Y actualiza `API_URL` en `frontend/app.js`.

### Error: "Address already in use"
El puerto 8000 está ocupado. Usa otro puerto o cierra la aplicación que lo está usando.

### ¿Cómo abro el frontend?
Simplemente abre `frontend/index.html` en tu navegador (doble clic o arrastrar al navegador).

### ¿Necesito un servidor web para el frontend?
No, puedes abrir el HTML directamente. Pero si prefieres, puedes usar:
```bash
# Python
python -m http.server 8080
# Node.js
npx http-server frontend
```

---

## 🧠 Funcionamiento de la IA

### ¿Qué es la lógica difusa?
Es una técnica que maneja incertidumbre usando valores graduales en lugar de binarios (verdadero/falso). Permite modelar conceptos como "similar" o "diferente" de forma más natural.

### ¿Cómo funciona la lógica difusa aquí?
1. Calcula la diferencia entre respuestas: |A - B|
2. Fuzzifica la diferencia usando funciones de membresía
3. Aplica reglas difusas (SI muy_similar ENTONCES 100%)
4. Defuzzifica para obtener un score numérico

### ¿Qué es el modelo Bayesiano?
Es un método probabilístico que actualiza creencias basándose en evidencia. Ajusta el score difuso considerando la consistencia entre dimensiones.

### ¿Por qué el score Bayesiano difiere del difuso?
El modelo Bayesiano añade o resta puntos según la consistencia:
- Alta consistencia (respuestas uniformes) → bonus
- Baja consistencia (respuestas variables) → penalización

### ¿Qué significa "consistencia"?
Es qué tan uniformes son los scores entre dimensiones. Si todas las dimensiones tienen scores similares, la consistencia es alta.

### ¿Cómo se calculan los pesos?
Cada dimensión tiene un peso predefinido:
- Comunicación y Valores: 1.5 (críticas)
- Conflicto, Intimidad, Metas, Apoyo: 1.2 (importantes)
- Estilo Emocional, Tiempo: 1.0 (normales)

### ¿Puedo cambiar los pesos?
Sí, edita el diccionario `pesos` en `backend/core/fuzzy.py` línea 95.

---

## 📊 Interpretación de Resultados

### ¿Qué significa cada nivel de compatibilidad?
- **85-100% (Excelente)**: Muy alta alineación emocional
- **70-84% (Buena)**: Sintonía sólida con diferencias manejables
- **55-69% (Moderada)**: Requiere comunicación activa
- **40-54% (Baja)**: Diferencias significativas
- **0-39% (Muy Baja)**: Perspectivas muy diferentes

### ¿Un score bajo significa que la relación no funcionará?
No necesariamente. El score indica similitud en respuestas, no éxito de la relación. Las diferencias pueden ser complementarias.

### ¿Qué son las "fortalezas"?
Las 3 dimensiones con mayor compatibilidad (scores más altos).

### ¿Qué son las "áreas de mejora"?
Las 3 dimensiones con menor compatibilidad (scores más bajos).

### ¿Las recomendaciones son personalizadas?
Sí, se generan automáticamente basándose en las dimensiones con scores bajos.

---

## 🎨 Personalización

### ¿Puedo agregar más dimensiones?
Sí, pero requiere modificar:
1. `PersonResponses` en `backend/main.py`
2. Formulario en `frontend/index.html`
3. `dimension_names` en `backend/core/analyzer.py`

### ¿Puedo cambiar las preguntas?
Sí, edita las etiquetas `<label>` en `frontend/index.html`. Las preguntas son solo descriptivas.

### ¿Puedo modificar los colores?
Sí, edita `frontend/styles.css`. Los colores principales están en:
- `body`: Gradiente de fondo
- `.btn-calcular`: Botón principal
- Clasificación: En `backend/core/analyzer.py` línea 25-50

### ¿Puedo cambiar el idioma?
Sí, traduce los textos en:
- `frontend/index.html`: Interfaz
- `backend/core/analyzer.py`: Recomendaciones
- Documentación: Archivos .md

---

## 🔬 Técnicas Avanzadas

### ¿Puedo agregar una red neuronal?
Sí, hay un ejemplo en `CONCEPTOS_IA.md`. Podrías entrenarla para aprender pesos óptimos automáticamente.

### ¿Puedo usar otros algoritmos de IA?
Sí, el código es modular. Puedes reemplazar o complementar:
- Lógica difusa con clustering (K-means)
- Modelo Bayesiano con regresión
- Análisis con machine learning

### ¿Puedo almacenar datos históricos?
Sí, pero requiere agregar una base de datos (SQLite, PostgreSQL). Actualmente todo es en memoria.

### ¿Puedo hacer análisis de múltiples parejas?
Sí, podrías implementar clustering para comparar con parejas similares.

---

## 🐛 Solución de Problemas

### El frontend no se conecta al backend
**Solución:**
1. Verifica que el backend esté ejecutándose (`http://localhost:8000`)
2. Abre la consola del navegador (F12) y busca errores
3. Verifica que `API_URL` en `app.js` sea correcto
4. Revisa que CORS esté habilitado en `main.py`

### Error: "ModuleNotFoundError: No module named 'fastapi'"
**Solución:**
```bash
pip install -r requirements.txt
```

### Error: "CORS policy: No 'Access-Control-Allow-Origin'"
**Solución:** El backend debe estar ejecutándose antes de abrir el frontend.

### Los gráficos no se muestran
**Solución:**
1. Verifica que Chart.js se cargue (revisa consola del navegador)
2. Asegúrate de tener conexión a internet (Chart.js se carga desde CDN)
3. Descarga Chart.js localmente si no tienes internet

### Error: "uvicorn: command not found"
**Solución:**
```bash
pip install uvicorn
# O usa:
python -m uvicorn main:app --reload
```

### Los sliders no se actualizan
**Solución:** Asegúrate de que `app.js` esté cargado correctamente. Revisa la consola del navegador.

---

## 📈 Rendimiento

### ¿Qué tan rápido es el sistema?
Típicamente <100ms para calcular compatibilidad.

### ¿Puedo procesar múltiples peticiones simultáneamente?
Sí, FastAPI es asíncrono y maneja múltiples peticiones concurrentes.

### ¿Hay límite de peticiones?
No hay límite implementado, pero puedes agregar rate limiting si lo despliegas públicamente.

---

## 🔒 Seguridad y Privacidad

### ¿Se almacenan mis respuestas?
No. Todo se procesa en memoria y se descarta después de la respuesta.

### ¿Es seguro usar esta plataforma?
Sí, para uso local. Si lo despliegas públicamente, considera:
- HTTPS
- Rate limiting
- Validación adicional de entrada

### ¿Puedo usar esto en producción?
Es un proyecto educativo. Para producción, considera:
- Agregar autenticación
- Implementar logging
- Usar base de datos
- Agregar tests unitarios
- Configurar monitoreo

---

## 🎓 Educación

### ¿Es bueno para aprender IA?
Sí, implementa conceptos fundamentales de forma práctica y explicada.

### ¿Qué conceptos puedo aprender?
- Lógica difusa
- Modelos probabilísticos Bayesianos
- Análisis de datos con Pandas
- Desarrollo de APIs con FastAPI
- Visualización de datos

### ¿Hay ejercicios o tareas?
Puedes:
1. Modificar funciones de membresía
2. Agregar nuevas dimensiones
3. Implementar una red neuronal
4. Crear tests unitarios
5. Mejorar la interfaz

### ¿Dónde puedo aprender más?
- `CONCEPTOS_IA.md`: Teoría detallada
- `EJEMPLOS_USO.md`: Casos prácticos
- Documentación de FastAPI: https://fastapi.tiangolo.com/
- Documentación de Pandas: https://pandas.pydata.org/

---

## 🤝 Contribución

### ¿Puedo contribuir al proyecto?
Sí, es código abierto. Puedes:
- Reportar bugs
- Sugerir mejoras
- Agregar funcionalidades
- Mejorar documentación

### ¿Puedo usar este código en mi proyecto?
Sí, es de código abierto. Úsalo libremente con atribución.

### ¿Puedo modificar el código?
Sí, modifícalo como quieras. Es un proyecto educativo.

---

## 📞 Contacto y Soporte

### ¿Dónde reporto un bug?
Revisa primero:
1. `INSTRUCCIONES.md` - Solución de problemas
2. Esta FAQ
3. Ejecuta `test_example.py` para verificar funcionamiento

### ¿Dónde encuentro más documentación?
- `README.md`: Visión general
- `INSTRUCCIONES.md`: Guía de ejecución
- `CONCEPTOS_IA.md`: Teoría de IA
- `EJEMPLOS_USO.md`: Casos prácticos
- `DIAGRAMA_SISTEMA.txt`: Arquitectura visual

### ¿Hay una comunidad?
Este es un proyecto educativo individual. Puedes compartirlo y discutirlo en foros de IA y desarrollo.

---

## 🔮 Futuro del Proyecto

### ¿Habrá actualizaciones?
Es un proyecto educativo completo. Puedes extenderlo según tus necesidades.

### ¿Qué funcionalidades se podrían agregar?
- Red neuronal para aprender pesos
- Más dimensiones emocionales
- Almacenamiento de historial
- Comparación con otras parejas
- Exportar reporte en PDF
- Soporte multiidioma
- Modo oscuro
- Tests unitarios

### ¿Puedo desplegar esto en la nube?
Sí, puedes desplegarlo en:
- Heroku
- AWS (EC2, Lambda)
- Google Cloud
- Azure
- DigitalOcean

---

¿Tienes más preguntas? Revisa la documentación completa en los archivos .md del proyecto.

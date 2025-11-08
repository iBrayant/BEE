# 📋 Resumen Ejecutivo del Proyecto

## 🎯 Objetivo
Plataforma web que evalúa la compatibilidad emocional entre dos personas usando técnicas de Inteligencia Artificial: **Lógica Difusa** y **Modelos Probabilísticos Bayesianos**.

## 🏗️ Arquitectura

### Backend (Python + FastAPI)
```
backend/
├── main.py                    # Servidor FastAPI, endpoint principal
├── requirements.txt           # Dependencias
├── test_example.py           # Script de prueba con ejemplos
└── core/
    ├── fuzzy.py              # Lógica difusa (funciones de membresía)
    ├── probabilistic.py      # Modelo Bayesiano (ajuste de score)
    └── analyzer.py           # Análisis y generación de insights
```

### Frontend (HTML + CSS + JavaScript)
```
frontend/
├── index.html                # Interfaz de usuario
├── styles.css                # Estilos responsive
└── app.js                    # Lógica de comunicación con API
```

## 🧠 Técnicas de IA Implementadas

### 1. Lógica Difusa (`fuzzy.py`)
- **Funciones de membresía**: Triangulares y trapezoidales
- **Categorías**: Muy Similar, Similar, Diferente, Muy Diferente
- **Reglas difusas**: Mapeo de diferencias a compatibilidad
- **Defuzzificación**: Método del centroide ponderado
- **Pesos por dimensión**: Comunicación y valores tienen mayor peso (1.5x)

### 2. Modelo Bayesiano (`probabilistic.py`)
- **Prior**: Distribución inicial neutral (μ=50, σ=20)
- **Likelihood**: Basado en consistencia entre dimensiones
- **Posterior**: Actualización Bayesiana clásica
- **Ajuste por consistencia**: Bonus/penalización según varianza

### 3. Análisis de Datos (`analyzer.py`)
- **Pandas**: Organización y manipulación de datos
- **Clasificación**: 5 niveles (Excelente, Buena, Moderada, Baja, Muy Baja)
- **Identificación**: Top 3 fortalezas y áreas de mejora
- **Recomendaciones**: Personalizadas según dimensiones débiles

## 📊 Dimensiones Evaluadas (8 total)

| Dimensión | Descripción | Peso |
|-----------|-------------|------|
| Comunicación | Apertura y frecuencia comunicativa | 1.5 |
| Valores | Principios fundamentales compartidos | 1.5 |
| Conflicto | Estilo de manejo de desacuerdos | 1.2 |
| Estilo Emocional | Expresión de emociones | 1.0 |
| Tiempo Compartido | Preferencia de tiempo juntos | 1.0 |
| Intimidad | Necesidad de cercanía física/emocional | 1.2 |
| Metas a Futuro | Alineación de objetivos | 1.3 |
| Apoyo Mutuo | Red de soporte en la relación | 1.2 |

## 🔄 Flujo de Procesamiento

```
1. Usuario ingresa respuestas (0-10) para ambas personas
   ↓
2. Frontend envía JSON al backend vía POST
   ↓
3. Backend - Lógica Difusa:
   - Calcula diferencias absolutas
   - Fuzzifica cada diferencia
   - Aplica reglas difusas
   - Defuzzifica a score por dimensión
   - Calcula score global ponderado
   ↓
4. Backend - Modelo Bayesiano:
   - Calcula consistencia (varianza)
   - Determina likelihood
   - Actualiza posterior
   - Ajusta score final
   ↓
5. Backend - Análisis:
   - Clasifica nivel de compatibilidad
   - Identifica fortalezas/debilidades
   - Genera recomendaciones
   - Prepara datos para gráficos
   ↓
6. Frontend recibe JSON y visualiza:
   - Score principal con color
   - Gráfico radar (comparación de perfiles)
   - Gráfico de barras (compatibilidad por dimensión)
   - Fortalezas y áreas de mejora
   - Recomendaciones personalizadas
```

## 📈 Ejemplo de Cálculo

### Entrada
```json
{
  "persona_a": {"comunicacion": 8, "valores": 9, ...},
  "persona_b": {"comunicacion": 7, "valores": 8, ...}
}
```

### Procesamiento
1. **Diferencias**: comunicacion=1, valores=1, ...
2. **Lógica Difusa**: 
   - comunicacion: 92.5% (diferencia 1 → "muy similar")
   - valores: 95.0% (diferencia 1 → "muy similar")
3. **Score Difuso Global**: 87.3% (ponderado)
4. **Consistencia**: 85% (baja varianza)
5. **Ajuste Bayesiano**: +2.1% (alta consistencia)
6. **Score Final**: 89.4%

### Salida
```json
{
  "compatibilidad_porcentaje": 89.4,
  "analisis": {
    "clasificacion": {"nivel": "Excelente", ...},
    "fortalezas": [...],
    "recomendaciones": [...]
  },
  "visualizacion": {...}
}
```

## 🚀 Ejecución

### Instalación
```bash
cd backend
pip install -r requirements.txt
```

### Iniciar Backend
```bash
uvicorn main:app --reload
```
Servidor en: `http://localhost:8000`

### Abrir Frontend
Doble clic en `frontend/index.html`

### Probar Sistema
```bash
python backend/test_example.py
```

## 📦 Dependencias

### Backend
- **FastAPI**: Framework web moderno
- **Uvicorn**: Servidor ASGI
- **Pydantic**: Validación de datos
- **NumPy**: Cálculos numéricos
- **Pandas**: Análisis de datos

### Frontend
- **Chart.js**: Visualización de gráficos
- **Fetch API**: Comunicación asíncrona
- **CSS Grid**: Layout responsive

## ✨ Características Destacadas

1. **Sin login ni base de datos**: Todo en memoria
2. **Tiempo real**: Resultados instantáneos
3. **Explicable**: Cada paso del cálculo es transparente
4. **Responsive**: Funciona en móviles y desktop
5. **Educativo**: Código comentado y documentado

## 🎓 Conceptos del Pensum IA-Explorador Aplicados

✅ **Lógica Difusa**: Funciones de membresía y reglas difusas  
✅ **Modelos Probabilísticos**: Inferencia Bayesiana  
✅ **Pandas**: Análisis y manipulación de datos  
✅ **Visualización**: Gráficos radar y de barras  
✅ **NumPy**: Cálculos numéricos eficientes  

## 📊 Métricas del Proyecto

- **Líneas de código**: ~800 (backend) + ~200 (frontend)
- **Archivos Python**: 4 módulos principales
- **Endpoints API**: 1 principal + 1 de salud
- **Dimensiones evaluadas**: 8
- **Funciones de membresía**: 4
- **Reglas difusas**: 4
- **Tiempo de respuesta**: <100ms

## 🔮 Extensiones Futuras

1. **Red Neuronal**: Aprender pesos óptimos automáticamente
2. **Más dimensiones**: Finanzas, familia, hobbies
3. **Historial**: Comparar evolución en el tiempo
4. **Clustering**: Comparar con parejas similares
5. **Exportar PDF**: Reporte descargable
6. **Multiidioma**: Soporte para varios idiomas

## 📚 Documentación Incluida

- `README.md`: Descripción general y arquitectura
- `INSTRUCCIONES.md`: Guía paso a paso de ejecución
- `CONCEPTOS_IA.md`: Explicación detallada de técnicas de IA
- `EJEMPLOS_USO.md`: Casos de prueba y ejemplos
- `RESUMEN_PROYECTO.md`: Este documento

## 🎯 Casos de Uso

1. **Educativo**: Aprender IA aplicada
2. **Terapia de pareja**: Herramienta de apoyo
3. **Autoconocimiento**: Reflexión sobre relaciones
4. **Investigación**: Base para estudios de compatibilidad

## ⚠️ Limitaciones

- No es un diagnóstico profesional
- Basado en reglas expertas simplificadas
- No considera contexto cultural
- Requiere honestidad en las respuestas

## 🏆 Logros del Proyecto

✅ Implementación completa de lógica difusa  
✅ Modelo Bayesiano funcional  
✅ Interfaz intuitiva y atractiva  
✅ Código limpio y bien documentado  
✅ Sistema explicable y transparente  
✅ Visualizaciones interactivas  
✅ Sin dependencias externas complejas  
✅ Fácil de ejecutar y modificar  

## 👥 Audiencia

- Estudiantes de IA y Machine Learning
- Desarrolladores interesados en lógica difusa
- Psicólogos y terapeutas de pareja
- Entusiastas de la tecnología

## 📞 Soporte

Para problemas o preguntas:
1. Revisa `INSTRUCCIONES.md`
2. Consulta `EJEMPLOS_USO.md`
3. Ejecuta `test_example.py` para verificar funcionamiento

---

**Desarrollado como proyecto educativo aplicando conceptos avanzados de IA**

Versión: 1.0  
Fecha: 2024  
Tecnologías: Python, FastAPI, JavaScript, Chart.js

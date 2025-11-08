# 💕 Plataforma de Compatibilidad Emocional - Análisis con IA

Plataforma web que evalúa la compatibilidad emocional entre dos personas usando **Lógica Difusa** y **Modelos Probabilísticos Bayesianos**.

## 🎯 Características

- **Sin login ni base de datos**: Todo funciona en memoria
- **8 dimensiones emocionales**: Comunicación, valores, conflictos, estilo emocional, tiempo compartido, intimidad, metas y apoyo mutuo
- **IA avanzada**:
  - Lógica difusa con funciones de membresía triangulares y trapezoidales
  - Ajuste probabilístico Bayesiano
  - Análisis con pandas
- **Visualización interactiva**: Gráficos radar y de barras con Chart.js
- **Reporte completo**: Fortalezas, áreas de mejora y recomendaciones personalizadas

## 🏗️ Arquitectura

```
proyecto/
├── backend/
│   ├── main.py                 # FastAPI server principal
│   ├── requirements.txt        # Dependencias Python
│   └── core/
│       ├── __init__.py
│       ├── fuzzy.py           # Lógica difusa
│       ├── probabilistic.py   # Modelo Bayesiano
│       └── analyzer.py        # Análisis y visualización
└── frontend/
    ├── index.html             # Interfaz web
    ├── styles.css             # Estilos
    └── app.js                 # Lógica frontend
```

## 🚀 Instalación y Ejecución

### Requisitos previos
- Python 3.8+
- pip

### Paso 1: Instalar dependencias del backend

```bash
cd backend
pip install -r requirements.txt
```

### Paso 2: Ejecutar el servidor backend

```bash
uvicorn main:app --reload
```

El servidor estará disponible en `http://localhost:8000`

### Paso 3: Abrir el frontend

Abre el archivo `frontend/index.html` en tu navegador web.

## 📊 Cómo funciona

### 1. Lógica Difusa (`fuzzy.py`)

Implementa funciones de membresía para evaluar similitud entre respuestas:

- **Muy Similar**: Diferencia 0-2 (compatibilidad 100%)
- **Similar**: Diferencia 1.5-4.5 (compatibilidad 75%)
- **Diferente**: Diferencia 3-6 (compatibilidad 40%)
- **Muy Diferente**: Diferencia 5-10 (compatibilidad 10%)

```python
# Ejemplo de función de membresía triangular
def membership_muy_similar(diferencia):
    if diferencia <= 0:
        return 1.0
    elif diferencia <= 2:
        return 1.0 - (diferencia / 2.0)
    else:
        return 0.0
```

### 2. Modelo Bayesiano (`probabilistic.py`)

Ajusta el score difuso usando inferencia Bayesiana:

- **Prior**: Distribución inicial neutral (μ=50, σ=20)
- **Likelihood**: Basado en consistencia entre dimensiones
- **Posterior**: Score ajustado final

```python
# Fórmula de actualización Bayesiana
posterior_mean = (prior_var * observation + obs_var * prior_mean) / (prior_var + obs_var)
```

### 3. Análisis (`analyzer.py`)

Usa pandas para:
- Identificar fortalezas y debilidades
- Generar recomendaciones personalizadas
- Preparar datos para visualización

## 🧪 Ejemplo de Uso

### Request al API:

```json
POST http://localhost:8000/api/compatibilidad

{
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
}
```

### Response:

```json
{
  "compatibilidad_porcentaje": 87.3,
  "compatibilidad_fuzzy": 85.6,
  "dimensiones": {
    "comunicacion": 92.5,
    "valores": 95.0,
    "conflicto": 88.3,
    ...
  },
  "analisis": {
    "clasificacion": {
      "nivel": "Excelente",
      "descripcion": "Compatibilidad muy alta...",
      "color": "#4CAF50"
    },
    "fortalezas": [...],
    "areas_mejora": [...],
    "recomendaciones": [...]
  },
  "visualizacion": {
    "radar": {...},
    "barras": {...}
  }
}
```

## 🎓 Conceptos de IA Aplicados

### Lógica Difusa
- Maneja incertidumbre en respuestas humanas
- Funciones de membresía modelan similitud gradual
- Reglas difusas para inferencia

### Modelo Probabilístico Bayesiano
- Actualiza creencias basándose en evidencia
- Considera consistencia entre dimensiones
- Reduce incertidumbre con más información

### Análisis de Datos con Pandas
- Organización eficiente de respuestas
- Identificación de patrones
- Generación de insights

## 🛠️ Tecnologías

**Backend:**
- FastAPI (framework web)
- NumPy (cálculos numéricos)
- Pandas (análisis de datos)

**Frontend:**
- HTML5/CSS3
- JavaScript (ES6+)
- Chart.js (visualización)

## 📝 Notas

- El sistema no almacena datos; cada análisis es independiente
- Los resultados son orientativos, no diagnósticos profesionales
- La IA usa reglas expertas simplificadas para demostración educativa

## 🔮 Extensiones Futuras (Opcional)

- Red neuronal simple para aprender pesos óptimos de dimensiones
- Más dimensiones emocionales
- Exportar reporte en PDF
- Comparación con parejas similares (clustering)

---

Desarrollado como proyecto educativo aplicando conceptos de IA: Lógica Difusa, Modelos Probabilísticos y Análisis de Datos.

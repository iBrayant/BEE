# Descripción del Programa: LoveLogic - Plataforma de Compatibilidad Emocional

## 1. Introducción
LoveLogic es una plataforma de software diseñada para evaluar y calcular la compatibilidad emocional entre dos personas utilizando técnicas avanzadas de Inteligencia Artificial, específicamente Lógica Difusa (Fuzzy Logic) y Modelos Probabilísticos Bayesianos.

## 2. Objetivo
El objetivo principal del software es proporcionar un análisis detallado y objetivo de la relación entre dos individuos, basándose en 8 dimensiones emocionales clave: Comunicación, Valores, Conflicto, Estilo Emocional, Tiempo Compartido, Intimidad, Metas a Futuro y Apoyo Mutuo.

## 3. Arquitectura del Sistema
El sistema opera bajo una arquitectura Cliente-Servidor:

*   **Frontend (Cliente):** Desarrollado en HTML5, CSS3 y JavaScript. Es la interfaz de usuario donde se ingresan los datos y se visualizan los resultados. Utiliza la librería Chart.js para la generación de gráficos.
*   **Backend (Servidor):** Desarrollado en Python utilizando el framework FastAPI. Es el núcleo de procesamiento que recibe los datos, ejecuta los algoritmos de IA y devuelve el análisis.

## 4. Flujo de Funcionamiento y Procedimientos

### A. Captura de Datos (Frontend)
1.  El usuario accede a la interfaz web.
2.  Se presentan formularios secuenciales para la "Persona 1" y la "Persona 2".
3.  Se recolectan puntuaciones numéricas (0-10) para cada una de las 8 dimensiones emocionales.
4.  Los datos se estructuran en un objeto JSON y se envían al servidor mediante una petición HTTP POST al endpoint `/api/compatibilidad`.

### B. Procesamiento (Backend)
Al recibir la petición, el servidor ejecuta los siguientes pasos secuenciales:

1.  **Normalización:** Los datos recibidos se convierten a estructuras de diccionario para su manipulación.
2.  **Cálculo de Lógica Difusa (Fuzzy Logic):**
    *   Se utiliza la clase `FuzzyCompatibility`.
    *   Para cada dimensión, se evalúa la diferencia entre las puntuaciones de ambas personas.
    *   Se aplican funciones de membresía para determinar el grado de similitud (Bajo, Medio, Alto).
    *   Se genera un "score difuso" preliminar por dimensión y un score global.
3.  **Ajuste Bayesiano (Probabilistic Model):**
    *   Se utiliza la clase `BayesianAdjuster`.
    *   El modelo analiza la consistencia entre las diferentes dimensiones (probabilidad condicional).
    *   Se ajusta el score global difuso basándose en la coherencia de las respuestas, refinando la precisión del resultado final.
4.  **Generación de Análisis:**
    *   La clase `CompatibilityAnalyzer` interpreta los scores finales.
    *   Se generan textos descriptivos para "Fortalezas", "Áreas de Mejora" y "Recomendaciones" basados en reglas predefinidas y los puntajes obtenidos.

### C. Visualización (Frontend)
1.  El backend devuelve un objeto JSON con: Porcentaje de compatibilidad, desglose por dimensiones, y textos de análisis.
2.  El frontend procesa esta respuesta.
3.  Se renderizan dos gráficos interactivos:
    *   **Gráfico de Radar:** Compara visualmente los perfiles de ambas personas.
    *   **Gráfico de Barras:** Muestra el nivel de compatibilidad por cada dimensión.
4.  Se despliega el reporte textual de fortalezas y recomendaciones.

## 5. Tecnologías y Herramientas
*   **Lenguaje de Programación:** Python 3.x (Backend), JavaScript (Frontend).
*   **Frameworks:** FastAPI, Uvicorn.
*   **Librerías:** Pydantic (validación de datos), Chart.js (visualización).

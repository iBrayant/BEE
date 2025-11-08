# 🧠 Conceptos de IA Aplicados en el Proyecto

## 1. Lógica Difusa (Fuzzy Logic)

### ¿Qué es?
La lógica difusa permite manejar incertidumbre y valores graduales en lugar de valores binarios (verdadero/falso). Es ideal para modelar conceptos humanos como "similar" o "diferente".

### Implementación en el Proyecto

#### Funciones de Membresía

**Función Triangular - "Muy Similar":**
```
Grado de membresía
    1.0 |●
        |  ●
        |    ●
    0.5 |      ●
        |        ●
    0.0 |__________●_____
        0    1    2    3  Diferencia
```

Código:
```python
def membership_muy_similar(diferencia):
    if diferencia <= 0:
        return 1.0  # Totalmente similar
    elif diferencia <= 2:
        return 1.0 - (diferencia / 2.0)  # Decae linealmente
    else:
        return 0.0  # No es muy similar
```

**Función Trapezoidal - "Similar":**
```
Grado de membresía
    1.0 |    ●●●●●
        |   ●      ●
    0.5 |  ●        ●
        | ●          ●
    0.0 |●____________●___
        1.5  2.5  3.5  4.5  Diferencia
```

#### Reglas Difusas

El sistema aplica reglas del tipo:
- **SI** diferencia es "muy_similar" **ENTONCES** compatibilidad = 100%
- **SI** diferencia es "similar" **ENTONCES** compatibilidad = 75%
- **SI** diferencia es "diferente" **ENTONCES** compatibilidad = 40%
- **SI** diferencia es "muy_diferente" **ENTONCES** compatibilidad = 10%

#### Defuzzificación

Usamos el método del **centroide ponderado**:

```
Compatibilidad = Σ(membresía_i × valor_i) / Σ(membresía_i)
```

**Ejemplo:**
- Diferencia = 1.5
- Membresías: muy_similar=0.25, similar=0.5, diferente=0, muy_diferente=0
- Cálculo: (0.25×100 + 0.5×75) / (0.25 + 0.5) = 83.3%

### Ventajas en este Contexto
- Modela la ambigüedad natural en respuestas humanas
- Transiciones suaves entre categorías
- Más realista que umbrales rígidos

---

## 2. Modelo Probabilístico Bayesiano

### ¿Qué es?
La inferencia Bayesiana actualiza creencias (probabilidades) basándose en nueva evidencia. Usa el Teorema de Bayes:

```
P(H|E) = P(E|H) × P(H) / P(E)

Donde:
- P(H|E) = Probabilidad posterior (lo que queremos)
- P(E|H) = Likelihood (verosimilitud)
- P(H) = Prior (creencia inicial)
- P(E) = Evidencia
```

### Implementación en el Proyecto

#### Prior (Creencia Inicial)
```python
prior_mean = 50.0  # Neutral
prior_std = 20.0   # Alta incertidumbre inicial
```

Representa nuestra creencia antes de ver los datos: "No sabemos nada, asumimos 50% de compatibilidad con alta incertidumbre".

#### Likelihood (Verosimilitud)
Basado en la **consistencia** entre dimensiones:

```python
consistency = 100 - (std_dev × 2.5)
```

- **Alta consistencia** (baja varianza): Las dimensiones son coherentes → confiamos más en el score
- **Baja consistencia** (alta varianza): Dimensiones contradictorias → más incertidumbre

#### Actualización Bayesiana

Para distribuciones gaussianas:

```python
# Media posterior
posterior_mean = (prior_var × observation + obs_var × prior_mean) / (prior_var + obs_var)

# Varianza posterior
posterior_var = (prior_var × obs_var) / (prior_var + obs_var)
```

**Ejemplo numérico:**
- Prior: μ=50, σ=20 (var=400)
- Observación (score difuso): 85, σ=10 (var=100)
- Posterior: μ = (400×85 + 100×50) / 500 = 78
- El score se ajusta hacia la observación, pero no completamente

#### Ajuste por Consistencia

```python
consistency_bonus = (consistency - 50) × 0.1
final_score = posterior_mean + consistency_bonus
```

Si la consistencia es alta (>50), se añade un bonus. Si es baja (<50), se penaliza.

### Ventajas en este Contexto
- Combina información previa con observaciones
- Maneja incertidumbre de forma principiada
- Ajusta automáticamente según la calidad de los datos

---

## 3. Análisis de Datos con Pandas

### ¿Qué es?
Pandas es una biblioteca de Python para manipulación y análisis de datos estructurados.

### Implementación en el Proyecto

#### Organización de Datos
```python
df = pd.DataFrame({
    'dimension': ['comunicacion', 'valores', ...],
    'score': [92.5, 95.0, ...]
})
```

#### Identificación de Patrones
```python
# Ordenar por score
df = df.sort_values('score', ascending=False)

# Top 3 fortalezas
fortalezas = df.head(3)

# Top 3 debilidades
debilidades = df.tail(3)
```

#### Estadísticas
```python
import numpy as np

# Calcular varianza entre dimensiones
std_dev = np.std(scores)

# Detectar outliers
mean_score = np.mean(scores)
outliers = [s for s in scores if abs(s - mean_score) > 2*std_dev]
```

### Ventajas en este Contexto
- Manipulación eficiente de datos tabulares
- Funciones estadísticas integradas
- Fácil identificación de patrones

---

## 4. Visualización de Datos

### Gráfico Radar
Compara perfiles multidimensionales de ambas personas:

```
        Comunicación
             /\
            /  \
   Apoyo   /    \   Valores
          /      \
         /        \
        /          \
```

**Interpretación:**
- Áreas superpuestas = similitud
- Áreas separadas = diferencias

### Gráfico de Barras
Muestra compatibilidad por dimensión:

```
Comunicación  ████████████ 92%
Valores       ███████████████ 95%
Conflicto     ██████████ 88%
```

**Interpretación:**
- Barras altas = alta compatibilidad en esa dimensión
- Barras bajas = área de mejora

---

## 5. Pesos Ponderados

### Concepto
No todas las dimensiones tienen la misma importancia. Usamos pesos para reflejar esto:

```python
pesos = {
    "comunicacion": 1.5,      # Crítica
    "valores": 1.5,           # Crítica
    "conflicto": 1.2,         # Importante
    "metas_futuro": 1.3,      # Importante
    "estilo_emocional": 1.0,  # Normal
    "tiempo_compartido": 1.0, # Normal
    "intimidad": 1.2,         # Importante
    "apoyo_mutuo": 1.2        # Importante
}
```

### Cálculo Ponderado
```python
score_global = Σ(score_i × peso_i) / Σ(peso_i)
```

**Ejemplo:**
- Comunicación: 90% × 1.5 = 135
- Tiempo: 70% × 1.0 = 70
- Total: (135 + 70) / (1.5 + 1.0) = 82%

---

## 6. Flujo Completo del Sistema

```
┌─────────────────┐
│  Respuestas A,B │
└────────┬────────┘
         │
         ▼
┌─────────────────────────┐
│  1. Lógica Difusa       │
│  - Calcular diferencias │
│  - Fuzzificar           │
│  - Aplicar reglas       │
│  - Defuzzificar         │
└────────┬────────────────┘
         │
         ▼
┌─────────────────────────┐
│  2. Modelo Bayesiano    │
│  - Calcular consistencia│
│  - Determinar likelihood│
│  - Actualizar posterior │
│  - Ajustar score        │
└────────┬────────────────┘
         │
         ▼
┌─────────────────────────┐
│  3. Análisis (Pandas)   │
│  - Identificar patrones │
│  - Generar insights     │
│  - Crear recomendaciones│
└────────┬────────────────┘
         │
         ▼
┌─────────────────────────┐
│  4. Visualización       │
│  - Gráficos radar/barras│
│  - Reporte completo     │
└─────────────────────────┘
```

---

## 7. Extensión: Red Neuronal Simple (Opcional)

### Concepto
Una red neuronal podría aprender los pesos óptimos automáticamente:

```python
import numpy as np

class SimpleNeuralNet:
    def __init__(self, input_size=8):
        # Pesos aleatorios iniciales
        self.weights = np.random.randn(input_size)
        self.bias = 0
    
    def forward(self, X):
        # Combinación lineal + activación sigmoide
        z = np.dot(X, self.weights) + self.bias
        return 1 / (1 + np.exp(-z))  # Sigmoide
    
    def train(self, X, y, epochs=1000, lr=0.01):
        for _ in range(epochs):
            # Forward pass
            pred = self.forward(X)
            
            # Calcular error
            error = y - pred
            
            # Backpropagation (gradiente descendente)
            self.weights += lr * np.dot(X.T, error)
            self.bias += lr * np.sum(error)
```

### Uso
```python
# Datos de entrenamiento (ejemplos de parejas)
X = np.array([
    [8, 9, 7, 6, 8, 7, 9, 8],  # Pareja 1
    [3, 4, 2, 5, 3, 4, 2, 3],  # Pareja 2
    ...
])
y = np.array([0.85, 0.35, ...])  # Compatibilidad real

# Entrenar
nn = SimpleNeuralNet()
nn.train(X, y)

# Predecir
nueva_pareja = [7, 8, 6, 5, 9, 8, 8, 7]
compatibilidad = nn.forward(nueva_pareja)
```

---

## 📚 Referencias y Recursos

### Lógica Difusa
- Zadeh, L.A. (1965). "Fuzzy Sets"
- Mamdani, E.H. (1974). "Application of fuzzy algorithms"

### Inferencia Bayesiana
- Bayes, T. (1763). "An Essay towards solving a Problem"
- Murphy, K. (2012). "Machine Learning: A Probabilistic Perspective"

### Análisis de Datos
- McKinney, W. (2017). "Python for Data Analysis"
- Pandas Documentation: https://pandas.pydata.org/

### Redes Neuronales
- Nielsen, M. (2015). "Neural Networks and Deep Learning"
- Goodfellow, I. et al. (2016). "Deep Learning"

---

## 🎯 Conclusión

Este proyecto integra múltiples técnicas de IA:

1. **Lógica Difusa**: Maneja incertidumbre y valores graduales
2. **Modelo Bayesiano**: Actualiza creencias con evidencia
3. **Análisis de Datos**: Identifica patrones y genera insights
4. **Visualización**: Comunica resultados efectivamente

Cada técnica complementa a las otras, creando un sistema robusto y explicable para evaluar compatibilidad emocional.

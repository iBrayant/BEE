# 📝 Ejemplos de Uso y Casos de Prueba

## Caso 1: Pareja Altamente Compatible

### Respuestas
**Persona A:**
- Comunicación: 9
- Valores: 9
- Conflicto: 8
- Estilo Emocional: 7
- Tiempo Compartido: 8
- Intimidad: 8
- Metas a Futuro: 9
- Apoyo Mutuo: 8

**Persona B:**
- Comunicación: 8
- Valores: 9
- Conflicto: 8
- Estilo Emocional: 7
- Tiempo Compartido: 9
- Intimidad: 7
- Metas a Futuro: 9
- Apoyo Mutuo: 8

### Resultado Esperado
- **Compatibilidad**: ~90-95%
- **Nivel**: Excelente
- **Fortalezas**: Valores, Metas a Futuro, Comunicación
- **Recomendaciones**: Mantener la comunicación abierta

---

## Caso 2: Pareja con Diferencias Moderadas

### Respuestas
**Persona A:**
- Comunicación: 8
- Valores: 7
- Conflicto: 6
- Estilo Emocional: 4
- Tiempo Compartido: 9
- Intimidad: 5
- Metas a Futuro: 7
- Apoyo Mutuo: 6

**Persona B:**
- Comunicación: 5
- Valores: 8
- Conflicto: 4
- Estilo Emocional: 7
- Tiempo Compartido: 5
- Intimidad: 8
- Metas a Futuro: 6
- Apoyo Mutuo: 7

### Resultado Esperado
- **Compatibilidad**: ~60-70%
- **Nivel**: Moderada
- **Áreas de Mejora**: Comunicación, Tiempo Compartido, Estilo Emocional
- **Recomendaciones**: Trabajar en comunicación y negociar tiempo juntos

---

## Caso 3: Pareja con Baja Compatibilidad

### Respuestas
**Persona A:**
- Comunicación: 9
- Valores: 9
- Conflicto: 8
- Estilo Emocional: 8
- Tiempo Compartido: 9
- Intimidad: 8
- Metas a Futuro: 9
- Apoyo Mutuo: 9

**Persona B:**
- Comunicación: 2
- Valores: 3
- Conflicto: 2
- Estilo Emocional: 3
- Tiempo Compartido: 2
- Intimidad: 3
- Metas a Futuro: 2
- Apoyo Mutuo: 2

### Resultado Esperado
- **Compatibilidad**: ~20-35%
- **Nivel**: Muy Baja
- **Áreas de Mejora**: Todas las dimensiones
- **Recomendaciones**: Diferencias fundamentales en múltiples áreas

---

## Caso 4: Pareja con Alta Varianza (Inconsistente)

### Respuestas
**Persona A:**
- Comunicación: 10
- Valores: 2
- Conflicto: 9
- Estilo Emocional: 1
- Tiempo Compartido: 10
- Intimidad: 3
- Metas a Futuro: 9
- Apoyo Mutuo: 2

**Persona B:**
- Comunicación: 9
- Valores: 3
- Conflicto: 8
- Estilo Emocional: 2
- Tiempo Compartido: 9
- Intimidad: 4
- Metas a Futuro: 8
- Apoyo Mutuo: 3

### Resultado Esperado
- **Compatibilidad**: ~70-75% (pero con advertencia)
- **Nivel**: Buena (pero inconsistente)
- **Observación**: El modelo Bayesiano detectará baja consistencia
- **Recomendaciones**: Relación compleja con áreas muy fuertes y muy débiles

---

## Prueba con cURL

### Ejemplo 1: Pareja Compatible
```bash
curl -X POST http://localhost:8000/api/compatibilidad \
  -H "Content-Type: application/json" \
  -d '{
    "persona_a": {
      "comunicacion": 9,
      "valores": 9,
      "conflicto": 8,
      "estilo_emocional": 7,
      "tiempo_compartido": 8,
      "intimidad": 8,
      "metas_futuro": 9,
      "apoyo_mutuo": 8
    },
    "persona_b": {
      "comunicacion": 8,
      "valores": 9,
      "conflicto": 8,
      "estilo_emocional": 7,
      "tiempo_compartido": 9,
      "intimidad": 7,
      "metas_futuro": 9,
      "apoyo_mutuo": 8
    }
  }'
```

### Ejemplo 2: Pareja con Diferencias
```bash
curl -X POST http://localhost:8000/api/compatibilidad \
  -H "Content-Type: application/json" \
  -d '{
    "persona_a": {
      "comunicacion": 8,
      "valores": 7,
      "conflicto": 6,
      "estilo_emocional": 4,
      "tiempo_compartido": 9,
      "intimidad": 5,
      "metas_futuro": 7,
      "apoyo_mutuo": 6
    },
    "persona_b": {
      "comunicacion": 5,
      "valores": 8,
      "conflicto": 4,
      "estilo_emocional": 7,
      "tiempo_compartido": 5,
      "intimidad": 8,
      "metas_futuro": 6,
      "apoyo_mutuo": 7
    }
  }'
```

---

## Prueba con Python

### Script de Prueba Rápida
```python
import requests
import json

# URL del API
url = "http://localhost:8000/api/compatibilidad"

# Datos de prueba
data = {
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

# Enviar petición
response = requests.post(url, json=data)

# Mostrar resultado
if response.status_code == 200:
    resultado = response.json()
    print(f"Compatibilidad: {resultado['compatibilidad_porcentaje']}%")
    print(f"Nivel: {resultado['analisis']['clasificacion']['nivel']}")
    print(f"\nFortalezas:")
    for f in resultado['analisis']['fortalezas']:
        print(f"  - {f['dimension']}: {f['score']:.1f}%")
else:
    print(f"Error: {response.status_code}")
```

---

## Interpretación de Resultados

### Rangos de Compatibilidad

| Rango | Nivel | Interpretación |
|-------|-------|----------------|
| 85-100% | Excelente | Muy alta alineación emocional |
| 70-84% | Buena | Sintonía sólida con diferencias manejables |
| 55-69% | Moderada | Requiere comunicación activa |
| 40-54% | Baja | Diferencias significativas |
| 0-39% | Muy Baja | Perspectivas muy diferentes |

### Dimensiones Críticas

Las dimensiones con mayor peso en el cálculo:
1. **Comunicación** (peso 1.5): Base de toda relación
2. **Valores** (peso 1.5): Principios fundamentales
3. **Metas a Futuro** (peso 1.3): Visión compartida
4. **Conflicto** (peso 1.2): Manejo de desacuerdos
5. **Intimidad** (peso 1.2): Conexión emocional/física
6. **Apoyo Mutuo** (peso 1.2): Red de soporte

### Consistencia

El modelo Bayesiano evalúa la consistencia:
- **Alta consistencia** (>70%): Respuestas uniformes, relación predecible
- **Consistencia media** (40-70%): Algunas contradicciones normales
- **Baja consistencia** (<40%): Relación compleja con extremos

---

## Casos Especiales

### Caso: Respuestas Idénticas
```json
{
  "persona_a": {"comunicacion": 5, "valores": 5, ...},
  "persona_b": {"comunicacion": 5, "valores": 5, ...}
}
```
**Resultado**: 100% de compatibilidad (diferencia = 0 en todas las dimensiones)

### Caso: Respuestas Opuestas
```json
{
  "persona_a": {"comunicacion": 10, "valores": 10, ...},
  "persona_b": {"comunicacion": 0, "valores": 0, ...}
}
```
**Resultado**: ~10-15% de compatibilidad (máxima diferencia)

### Caso: Una Dimensión Muy Diferente
```json
{
  "persona_a": {"comunicacion": 10, "valores": 0, ...},
  "persona_b": {"comunicacion": 9, "valores": 10, ...}
}
```
**Resultado**: El score global se verá afectado, especialmente si es una dimensión crítica (valores tiene peso 1.5)

---

## Validación de Datos

El API valida automáticamente:
- ✅ Todos los valores deben estar entre 0 y 10
- ✅ Todas las 8 dimensiones deben estar presentes
- ✅ Los valores deben ser numéricos

### Ejemplo de Error
```json
{
  "persona_a": {"comunicacion": 15, ...}  // ❌ Fuera de rango
}
```

**Respuesta**:
```json
{
  "detail": "Validation error: values must be between 0 and 10"
}
```

---

## Tips para Pruebas

1. **Prueba extremos**: Valores 0 y 10 en todas las dimensiones
2. **Prueba varianza**: Mezcla valores altos y bajos
3. **Prueba similitud**: Valores muy cercanos entre personas
4. **Prueba diferencias**: Valores muy distantes entre personas
5. **Prueba consistencia**: Todas las dimensiones similares vs. muy variadas

---

## Análisis de Sensibilidad

### ¿Cómo afecta cambiar una dimensión?

**Escenario Base:**
- Todas las dimensiones en 8 para ambas personas
- Compatibilidad: ~100%

**Cambiar Comunicación de B a 4:**
- Diferencia: 4 puntos
- Compatibilidad de comunicación: ~40%
- Compatibilidad global: ~92% (baja por peso 1.5)

**Cambiar Tiempo Compartido de B a 4:**
- Diferencia: 4 puntos
- Compatibilidad de tiempo: ~40%
- Compatibilidad global: ~94% (baja menos por peso 1.0)

**Conclusión**: Las dimensiones críticas (comunicación, valores) tienen mayor impacto en el score final.

---

## Preguntas Frecuentes

### ¿Por qué el score Bayesiano difiere del difuso?
El modelo Bayesiano ajusta según la consistencia. Si las dimensiones son muy variables, añade incertidumbre.

### ¿Qué significa "consistencia"?
Es la uniformidad entre dimensiones. Alta consistencia = respuestas similares en todas las áreas.

### ¿Puedo modificar los pesos?
Sí, edita el diccionario `pesos` en `backend/core/fuzzy.py` línea 95.

### ¿Puedo agregar más dimensiones?
Sí, pero debes:
1. Actualizar el modelo `PersonResponses` en `main.py`
2. Agregar campos en el frontend `index.html`
3. Actualizar `dimension_names` en `analyzer.py`

---

¡Experimenta con diferentes casos y observa cómo la IA evalúa la compatibilidad! 🚀

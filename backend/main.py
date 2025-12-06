"""
Plataforma de Compatibilidad Emocional - Backend Principal
FastAPI server que procesa las respuestas y calcula compatibilidad
"""
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import List, Dict
import json

from core.fuzzy import FuzzyCompatibility
from core.probabilistic import BayesianAdjuster
from core.analyzer import CompatibilityAnalyzer

app = FastAPI(title="Emotional Compatibility API")

# Configurar CORS para permitir peticiones desde el frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class PersonResponses(BaseModel):
    """Modelo de respuestas de una persona (8 dimensiones, escala 0-10)"""
    comunicacion: float
    valores: float
    conflicto: float
    estilo_emocional: float
    tiempo_compartido: float
    intimidad: float
    metas_futuro: float
    apoyo_mutuo: float

class CompatibilityRequest(BaseModel):
    """Modelo de petición con respuestas de ambas personas"""
    persona_a: PersonResponses
    persona_b: PersonResponses

@app.get("/")
def root():
    return {"message": "API de Compatibilidad Emocional activa"}

@app.post("/api/compatibilidad")
def calcular_compatibilidad(request: CompatibilityRequest):
    """
    Endpoint principal que calcula la compatibilidad emocional
    
    Proceso:
    1. Convierte respuestas a diccionarios
    2. Aplica lógica difusa para evaluar similitud
    3. Ajusta con modelo probabilístico Bayesiano
    4. Genera análisis y visualizaciones
    """
    print("\n" + "="*60)
    print("🚀 NUEVA PETICIÓN DE COMPATIBILIDAD")
    print("="*60)
    
    # Convertir a diccionarios
    persona_a = request.persona_a.dict()
    persona_b = request.persona_b.dict()
    
    print("\n📊 DATOS RECIBIDOS:")
    print(f"Persona 1: {persona_a}")
    print(f"Persona 2: {persona_b}")
    
    # Inicializar componentes de IA
    fuzzy = FuzzyCompatibility()
    bayesian = BayesianAdjuster()
    analyzer = CompatibilityAnalyzer()
    
    print("\n🧠 PASO 1: Calculando compatibilidad difusa por dimensión...")
    # 1. Calcular compatibilidad difusa por dimensión
    fuzzy_scores = fuzzy.calculate_dimension_compatibility(persona_a, persona_b)
    print("✅ Scores difusos por dimensión:")
    for dim, score in fuzzy_scores.items():
        print(f"   • {dim}: {score:.2f}%")
    
    print("\n🎯 PASO 2: Calculando score global difuso...")
    # 2. Calcular score global difuso
    fuzzy_global = fuzzy.calculate_global_compatibility(fuzzy_scores)
    print(f"✅ Score global difuso: {fuzzy_global:.2f}%")
    
    print("\n🔮 PASO 3: Ajustando con modelo Bayesiano...")
    # 3. Ajustar con modelo Bayesiano
    final_score = bayesian.adjust_score(fuzzy_global, fuzzy_scores)
    print(f"✅ Score final ajustado: {final_score:.2f}%")
    print(f"   Diferencia: {final_score - fuzzy_global:+.2f}%")
    
    print("\n📝 PASO 4: Generando análisis completo...")
    # 4. Generar análisis completo
    analysis = analyzer.generate_analysis(
        persona_a, 
        persona_b, 
        fuzzy_scores, 
        final_score
    )
    print(f"✅ Clasificación: {analysis['clasificacion']['nivel']}")
    print(f"   Fortalezas encontradas: {len(analysis['fortalezas'])}")
    print(f"   Áreas de mejora: {len(analysis['areas_mejora'])}")
    print(f"   Recomendaciones: {len(analysis['recomendaciones'])}")
    
    print("\n📊 PASO 5: Preparando datos para visualización...")
    # 5. Preparar datos para visualización
    chart_data = analyzer.prepare_chart_data(persona_a, persona_b, fuzzy_scores)
    print("✅ Datos de gráficos preparados")
    
    resultado = {
        "compatibilidad_porcentaje": round(final_score, 1),
        "compatibilidad_fuzzy": round(fuzzy_global, 1),
        "dimensiones": fuzzy_scores,
        "analisis": analysis,
        "visualizacion": chart_data
    }
    
    print("\n" + "="*60)
    print(f"✨ RESULTADO FINAL: {round(final_score, 1)}% de compatibilidad")
    print("="*60 + "\n")
    
    return resultado

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)

"""
Módulo de Análisis y Visualización

Genera reportes textuales y datos para gráficos
Usa pandas para organizar datos
"""
import pandas as pd
from typing import Dict, List

class CompatibilityAnalyzer:
    """
    Analizador que genera insights y prepara datos para visualización
    """
    
    def __init__(self):
        self.dimension_names = {
            "comunicacion": "Comunicación",
            "valores": "Valores Compartidos",
            "conflicto": "Manejo de Conflictos",
            "estilo_emocional": "Estilo Emocional",
            "tiempo_compartido": "Tiempo Compartido",
            "intimidad": "Intimidad",
            "metas_futuro": "Metas a Futuro",
            "apoyo_mutuo": "Apoyo Mutuo"
        }
    
    def classify_compatibility(self, score: float) -> Dict[str, str]:
        """
        Clasifica el nivel de compatibilidad
        """
        if score >= 85:
            return {
                "nivel": "Excelente",
                "descripcion": "Compatibilidad muy alta. Las respuestas muestran gran alineación emocional.",
                "color": "#4CAF50"
            }
        elif score >= 70:
            return {
                "nivel": "Buena",
                "descripcion": "Compatibilidad sólida. Hay buena sintonía con algunas diferencias manejables.",
                "color": "#8BC34A"
            }
        elif score >= 55:
            return {
                "nivel": "Moderada",
                "descripcion": "Compatibilidad media. Existen diferencias que requieren comunicación activa.",
                "color": "#FFC107"
            }
        elif score >= 40:
            return {
                "nivel": "Baja",
                "descripcion": "Compatibilidad limitada. Diferencias significativas en áreas importantes.",
                "color": "#FF9800"
            }
        else:
            return {
                "nivel": "Muy Baja",
                "descripcion": "Compatibilidad baja. Perspectivas muy diferentes en múltiples dimensiones.",
                "color": "#F44336"
            }
    
    def identify_strengths_weaknesses(self, dimension_scores: Dict[str, float]) -> Dict:
        """
        Identifica fortalezas y áreas de mejora
        """
        # Convertir a DataFrame para análisis
        df = pd.DataFrame({
            'dimension': list(dimension_scores.keys()),
            'score': list(dimension_scores.values())
        })
        
        # Ordenar por score
        df = df.sort_values('score', ascending=False)
        
        # Top 3 fortalezas
        fortalezas = df.head(3).to_dict('records')
        fortalezas = [
            {
                "dimension": self.dimension_names[f['dimension']],
                "score": f['score']
            }
            for f in fortalezas
        ]
        
        # Top 3 áreas de mejora
        debilidades = df.tail(3).to_dict('records')
        debilidades = [
            {
                "dimension": self.dimension_names[d['dimension']],
                "score": d['score']
            }
            for d in debilidades
        ]
        
        return {
            "fortalezas": fortalezas,
            "areas_mejora": debilidades
        }
    
    def generate_recommendations(self, dimension_scores: Dict[str, float]) -> List[str]:
        """
        Genera recomendaciones basadas en las dimensiones más débiles
        """
        recommendations = []
        
        # Analizar cada dimensión
        if dimension_scores.get("comunicacion", 100) < 60:
            recommendations.append(
                "Comunicación: Practiquen la escucha activa y expresen sus necesidades claramente."
            )
        
        if dimension_scores.get("valores", 100) < 60:
            recommendations.append(
                "Valores: Dialoguen sobre sus principios fundamentales y busquen puntos en común."
            )
        
        if dimension_scores.get("conflicto", 100) < 60:
            recommendations.append(
                "Conflictos: Establezcan reglas para discusiones constructivas y eviten ataques personales."
            )
        
        if dimension_scores.get("estilo_emocional", 100) < 60:
            recommendations.append(
                "Estilo Emocional: Respeten sus diferencias en expresión emocional y busquen balance."
            )
        
        if dimension_scores.get("tiempo_compartido", 100) < 60:
            recommendations.append(
                "Tiempo: Negocien expectativas sobre tiempo juntos vs. tiempo personal."
            )
        
        if dimension_scores.get("intimidad", 100) < 60:
            recommendations.append(
                "Intimidad: Conversen abiertamente sobre necesidades de cercanía física y emocional."
            )
        
        if dimension_scores.get("metas_futuro", 100) < 60:
            recommendations.append(
                "Metas: Alineen sus visiones de futuro y encuentren objetivos compartidos."
            )
        
        if dimension_scores.get("apoyo_mutuo", 100) < 60:
            recommendations.append(
                "Apoyo: Fortalezcan la red de soporte mutuo en momentos difíciles."
            )
        
        if not recommendations:
            recommendations.append(
                "Excelente compatibilidad. Mantienen una relación equilibrada. Sigan cultivando la comunicación."
            )
        
        return recommendations
    
    def generate_analysis(self, persona_a: Dict, persona_b: Dict, 
                         dimension_scores: Dict[str, float], 
                         final_score: float) -> Dict:
        """
        Genera análisis completo de compatibilidad
        """
        classification = self.classify_compatibility(final_score)
        strengths_weaknesses = self.identify_strengths_weaknesses(dimension_scores)
        recommendations = self.generate_recommendations(dimension_scores)
        
        return {
            "clasificacion": classification,
            "fortalezas": strengths_weaknesses["fortalezas"],
            "areas_mejora": strengths_weaknesses["areas_mejora"],
            "recomendaciones": recommendations
        }
    
    def prepare_chart_data(self, persona_a: Dict, persona_b: Dict, 
                          dimension_scores: Dict[str, float]) -> Dict:
        """
        Prepara datos para visualización en frontend
        """
        # Datos para gráfico radar
        labels = [self.dimension_names[dim] for dim in persona_a.keys()]
        
        radar_data = {
            "labels": labels,
            "persona_a": list(persona_a.values()),
            "persona_b": list(persona_b.values())
        }
        
        # Datos para gráfico de barras (compatibilidad por dimensión)
        bar_data = {
            "labels": labels,
            "scores": [dimension_scores[dim] for dim in persona_a.keys()]
        }
        
        return {
            "radar": radar_data,
            "barras": bar_data
        }

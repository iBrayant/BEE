"""
Módulo de Lógica Difusa para Compatibilidad Emocional

Implementa:
- Funciones de membresía triangulares y trapezoidales
- Reglas difusas para evaluar similitud
- Agregación de dimensiones
"""
import numpy as np
from typing import Dict

class FuzzyCompatibility:
    """
    Sistema de lógica difusa para evaluar compatibilidad emocional
    """
    
    def __init__(self):
        # Definir universo de discurso (diferencias entre respuestas)
        self.diferencia_universo = np.linspace(0, 10, 100)
        
    def membership_muy_similar(self, diferencia: float) -> float:
        """
        Función de membresía triangular para 'muy similar'
        Máximo en diferencia=0, decae linealmente hasta diferencia=2
        """
        if diferencia <= 0:
            return 1.0
        elif diferencia <= 2:
            return 1.0 - (diferencia / 2.0)
        else:
            return 0.0
    
    def membership_similar(self, diferencia: float) -> float:
        """
        Función de membresía trapezoidal para 'similar'
        Activa entre diferencia 1.5 y 4
        """
        if diferencia <= 1.5:
            return 0.0
        elif diferencia <= 2.5:
            return (diferencia - 1.5) / 1.0
        elif diferencia <= 3.5:
            return 1.0
        elif diferencia <= 4.5:
            return 1.0 - (diferencia - 3.5) / 1.0
        else:
            return 0.0
    
    def membership_diferente(self, diferencia: float) -> float:
        """
        Función de membresía para 'diferente'
        Crece linealmente desde diferencia=3
        """
        if diferencia <= 3:
            return 0.0
        elif diferencia <= 6:
            return (diferencia - 3) / 3.0
        else:
            return 1.0
    
    def membership_muy_diferente(self, diferencia: float) -> float:
        """
        Función de membresía para 'muy diferente'
        Activa fuertemente desde diferencia=6
        """
        if diferencia <= 5:
            return 0.0
        elif diferencia <= 7:
            return (diferencia - 5) / 2.0
        else:
            return 1.0
    
    def fuzzify_difference(self, diferencia: float) -> Dict[str, float]:
        """
        Fuzzifica una diferencia en grados de membresía
        """
        return {
            "muy_similar": self.membership_muy_similar(diferencia),
            "similar": self.membership_similar(diferencia),
            "diferente": self.membership_diferente(diferencia),
            "muy_diferente": self.membership_muy_diferente(diferencia)
        }
    
    def apply_fuzzy_rules(self, memberships: Dict[str, float]) -> float:
        """
        Aplica reglas difusas para obtener score de compatibilidad
        
        Reglas:
        - SI muy_similar ENTONCES compatibilidad = 100%
        - SI similar ENTONCES compatibilidad = 75%
        - SI diferente ENTONCES compatibilidad = 40%
        - SI muy_diferente ENTONCES compatibilidad = 10%
        """
        # Valores de salida para cada regla
        outputs = {
            "muy_similar": 100,
            "similar": 75,
            "diferente": 40,
            "muy_diferente": 10
        }
        
        # Defuzzificación usando promedio ponderado (método del centroide simplificado)
        numerador = sum(memberships[key] * outputs[key] for key in memberships)
        denominador = sum(memberships.values())
        
        if denominador == 0:
            return 50.0  # Valor neutral si no hay activación
        
        return numerador / denominador
    
    def calculate_dimension_compatibility(self, persona_a: Dict, persona_b: Dict) -> Dict[str, float]:
        """
        Calcula compatibilidad difusa para cada dimensión
        """
        dimensiones = persona_a.keys()
        resultados = {}
        
        for dim in dimensiones:
            # Calcular diferencia absoluta
            diferencia = abs(persona_a[dim] - persona_b[dim])
            
            # Fuzzificar
            memberships = self.fuzzify_difference(diferencia)
            
            # Aplicar reglas y defuzzificar
            compatibilidad = self.apply_fuzzy_rules(memberships)
            
            resultados[dim] = round(compatibilidad, 2)
        
        return resultados
    
    def calculate_global_compatibility(self, dimension_scores: Dict[str, float]) -> float:
        """
        Calcula compatibilidad global con pesos por dimensión
        
        Dimensiones críticas tienen mayor peso:
        - Valores y comunicación: peso 1.5
        - Resto: peso 1.0
        """
        pesos = {
            "comunicacion": 1.5,
            "valores": 1.5,
            "conflicto": 1.2,
            "estilo_emocional": 1.0,
            "tiempo_compartido": 1.0,
            "intimidad": 1.2,
            "metas_futuro": 1.3,
            "apoyo_mutuo": 1.2
        }
        
        suma_ponderada = sum(dimension_scores[dim] * pesos.get(dim, 1.0) 
                            for dim in dimension_scores)
        suma_pesos = sum(pesos.get(dim, 1.0) for dim in dimension_scores)
        
        return suma_ponderada / suma_pesos

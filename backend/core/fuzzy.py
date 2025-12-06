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
        
        print(f"      Aplicando reglas difusas (defuzzificación):")
        
        # Defuzzificación usando promedio ponderado (método del centroide simplificado)
        calculos = []
        for key in memberships:
            contribucion = memberships[key] * outputs[key]
            calculos.append(f"{memberships[key]:.3f} × {outputs[key]} = {contribucion:.2f}")
            print(f"         {key:15s}: {memberships[key]:.3f} × {outputs[key]:3d}% = {contribucion:.2f}")
        
        numerador = sum(memberships[key] * outputs[key] for key in memberships)
        denominador = sum(memberships.values())
        
        print(f"      Numerador (suma ponderada):   {numerador:.2f}")
        print(f"      Denominador (suma membresías): {denominador:.3f}")
        
        if denominador == 0:
            print(f"      ⚠️  Sin activación, usando valor neutral: 50.0%")
            return 50.0  # Valor neutral si no hay activación
        
        resultado = numerador / denominador
        print(f"      Resultado: {numerador:.2f} ÷ {denominador:.3f} = {resultado:.2f}%")
        
        return resultado
    
    def calculate_dimension_compatibility(self, persona_a: Dict, persona_b: Dict) -> Dict[str, float]:
        """
        Calcula compatibilidad difusa para cada dimensión
        """
        dimensiones = persona_a.keys()
        resultados = {}
        
        print("\n   📐 CÁLCULO DETALLADO POR DIMENSIÓN:")
        print("   " + "-"*70)
        
        for dim in dimensiones:
            # Calcular diferencia absoluta
            diferencia = abs(persona_a[dim] - persona_b[dim])
            
            print(f"\n   🔹 {dim.upper()}:")
            print(f"      Persona 1: {persona_a[dim]:.1f} | Persona 2: {persona_b[dim]:.1f}")
            print(f"      Diferencia absoluta: {diferencia:.2f}")
            
            # Fuzzificar
            memberships = self.fuzzify_difference(diferencia)
            
            print(f"      Grados de membresía (fuzzificación):")
            print(f"         • Muy Similar:    {memberships['muy_similar']:.3f}")
            print(f"         • Similar:        {memberships['similar']:.3f}")
            print(f"         • Diferente:      {memberships['diferente']:.3f}")
            print(f"         • Muy Diferente:  {memberships['muy_diferente']:.3f}")
            
            # Aplicar reglas y defuzzificar
            compatibilidad = self.apply_fuzzy_rules(memberships)
            
            print(f"      ➜ Compatibilidad calculada: {compatibilidad:.2f}%")
            
            resultados[dim] = round(compatibilidad, 2)
        
        print("\n   " + "-"*70)
        
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
        
        print("\n   🎯 AGREGACIÓN GLOBAL CON PESOS:")
        print("   " + "-"*70)
        
        suma_ponderada = 0
        suma_pesos = 0
        
        for dim in dimension_scores:
            peso = pesos.get(dim, 1.0)
            score = dimension_scores[dim]
            contribucion = score * peso
            suma_ponderada += contribucion
            suma_pesos += peso
            
            print(f"   {dim:20s}: {score:6.2f}% × {peso:.1f} = {contribucion:7.2f}")
        
        resultado = suma_ponderada / suma_pesos
        
        print("   " + "-"*70)
        print(f"   Suma ponderada: {suma_ponderada:.2f}")
        print(f"   Suma de pesos:  {suma_pesos:.2f}")
        print(f"   Score global:   {suma_ponderada:.2f} ÷ {suma_pesos:.2f} = {resultado:.2f}%")
        print("   " + "-"*70)
        
        return resultado

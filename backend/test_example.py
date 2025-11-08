"""
Script de prueba para demostrar el funcionamiento del sistema
Ejecutar: python test_example.py
"""
from core.fuzzy import FuzzyCompatibility
from core.probabilistic import BayesianAdjuster
from core.analyzer import CompatibilityAnalyzer
import json

def test_compatibility():
    """
    Ejemplo de cálculo de compatibilidad paso a paso
    """
    print("=" * 60)
    print("EJEMPLO DE CÁLCULO DE COMPATIBILIDAD EMOCIONAL")
    print("=" * 60)
    
    # Datos de ejemplo
    persona_a = {
        "comunicacion": 8.0,
        "valores": 9.0,
        "conflicto": 7.0,
        "estilo_emocional": 6.0,
        "tiempo_compartido": 8.0,
        "intimidad": 7.0,
        "metas_futuro": 9.0,
        "apoyo_mutuo": 8.0
    }
    
    persona_b = {
        "comunicacion": 7.0,
        "valores": 8.0,
        "conflicto": 6.0,
        "estilo_emocional": 5.0,
        "tiempo_compartido": 9.0,
        "intimidad": 8.0,
        "metas_futuro": 8.0,
        "apoyo_mutuo": 7.0
    }
    
    print("\n📋 RESPUESTAS:")
    print("\nPersona A:")
    for dim, val in persona_a.items():
        print(f"  {dim}: {val}")
    
    print("\nPersona B:")
    for dim, val in persona_b.items():
        print(f"  {dim}: {val}")
    
    # Paso 1: Lógica Difusa
    print("\n" + "=" * 60)
    print("PASO 1: LÓGICA DIFUSA")
    print("=" * 60)
    
    fuzzy = FuzzyCompatibility()
    
    # Ejemplo detallado para una dimensión
    dim_ejemplo = "comunicacion"
    diferencia = abs(persona_a[dim_ejemplo] - persona_b[dim_ejemplo])
    
    print(f"\nEjemplo detallado - Dimensión: {dim_ejemplo}")
    print(f"Persona A: {persona_a[dim_ejemplo]}")
    print(f"Persona B: {persona_b[dim_ejemplo]}")
    print(f"Diferencia absoluta: {diferencia}")
    
    memberships = fuzzy.fuzzify_difference(diferencia)
    print(f"\nGrados de membresía:")
    for categoria, grado in memberships.items():
        print(f"  {categoria}: {grado:.3f}")
    
    compatibilidad_dim = fuzzy.apply_fuzzy_rules(memberships)
    print(f"\nCompatibilidad difusa para {dim_ejemplo}: {compatibilidad_dim:.2f}%")
    
    # Calcular todas las dimensiones
    print("\n" + "-" * 60)
    print("Compatibilidad por dimensión:")
    dimension_scores = fuzzy.calculate_dimension_compatibility(persona_a, persona_b)
    
    for dim, score in dimension_scores.items():
        diferencia = abs(persona_a[dim] - persona_b[dim])
        print(f"  {dim:20s}: {score:5.1f}% (diferencia: {diferencia:.1f})")
    
    # Score global difuso
    fuzzy_global = fuzzy.calculate_global_compatibility(dimension_scores)
    print(f"\n✨ Score global difuso (ponderado): {fuzzy_global:.2f}%")
    
    # Paso 2: Ajuste Bayesiano
    print("\n" + "=" * 60)
    print("PASO 2: AJUSTE BAYESIANO")
    print("=" * 60)
    
    bayesian = BayesianAdjuster()
    
    # Calcular consistencia
    consistency = bayesian.calculate_consistency(dimension_scores)
    print(f"\nConsistencia entre dimensiones: {consistency:.2f}%")
    print("(Alta consistencia = respuestas más uniformes)")
    
    # Calcular likelihood
    likelihood_std = bayesian.calculate_likelihood(fuzzy_global, consistency)
    print(f"\nDesviación estándar del likelihood: {likelihood_std:.2f}")
    print("(Menor std = mayor confianza en el score difuso)")
    
    # Ajuste final
    final_score = bayesian.adjust_score(fuzzy_global, dimension_scores)
    print(f"\n✨ Score final ajustado (Bayesiano): {final_score:.2f}%")
    print(f"Diferencia con score difuso: {final_score - fuzzy_global:+.2f}%")
    
    # Paso 3: Análisis
    print("\n" + "=" * 60)
    print("PASO 3: ANÁLISIS Y RECOMENDACIONES")
    print("=" * 60)
    
    analyzer = CompatibilityAnalyzer()
    analysis = analyzer.generate_analysis(persona_a, persona_b, dimension_scores, final_score)
    
    print(f"\n🎯 Clasificación: {analysis['clasificacion']['nivel']}")
    print(f"   {analysis['clasificacion']['descripcion']}")
    
    print("\n💪 Fortalezas:")
    for f in analysis['fortalezas']:
        print(f"   • {f['dimension']}: {f['score']:.1f}%")
    
    print("\n🎯 Áreas de mejora:")
    for a in analysis['areas_mejora']:
        print(f"   • {a['dimension']}: {a['score']:.1f}%")
    
    print("\n💡 Recomendaciones:")
    for r in analysis['recomendaciones']:
        print(f"   {r}")
    
    # Datos de visualización
    print("\n" + "=" * 60)
    print("DATOS PARA VISUALIZACIÓN")
    print("=" * 60)
    
    chart_data = analyzer.prepare_chart_data(persona_a, persona_b, dimension_scores)
    print("\nGráfico Radar - Labels:")
    print(chart_data['radar']['labels'])
    print("\nGráfico Barras - Scores:")
    print(chart_data['barras']['scores'])
    
    print("\n" + "=" * 60)
    print("RESUMEN FINAL")
    print("=" * 60)
    print(f"\n🎯 Compatibilidad Emocional: {final_score:.1f}%")
    print(f"📊 Nivel: {analysis['clasificacion']['nivel']}")
    print(f"💬 {analysis['clasificacion']['descripcion']}")
    print("\n" + "=" * 60)

if __name__ == "__main__":
    test_compatibility()

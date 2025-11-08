"""
Módulo de Ajuste Probabilístico Bayesiano

Implementa un modelo Bayesiano simple que ajusta el score difuso
basándose en la varianza de las dimensiones
"""
import numpy as np
from typing import Dict

class BayesianAdjuster:
    """
    Ajustador Bayesiano que refina el score de compatibilidad
    
    Concepto:
    - Prior: score difuso inicial
    - Likelihood: basado en consistencia entre dimensiones
    - Posterior: score ajustado final
    """
    
    def __init__(self):
        # Prior: distribución inicial (neutral)
        self.prior_mean = 50.0
        self.prior_std = 20.0
    
    def calculate_consistency(self, dimension_scores: Dict[str, float]) -> float:
        """
        Calcula consistencia entre dimensiones
        
        Alta consistencia (baja varianza) = relación más predecible
        Baja consistencia (alta varianza) = relación más compleja
        """
        scores = list(dimension_scores.values())
        std_dev = np.std(scores)
        
        # Normalizar: varianza baja = consistencia alta
        # std_dev puede ir de 0 a ~40
        consistency = max(0, 100 - (std_dev * 2.5))
        return consistency
    
    def calculate_likelihood(self, fuzzy_score: float, consistency: float) -> float:
        """
        Calcula likelihood basado en consistencia
        
        Si la consistencia es alta, confiamos más en el score difuso
        Si es baja, aplicamos más incertidumbre
        """
        # Likelihood es una función gaussiana centrada en fuzzy_score
        # con desviación estándar inversamente proporcional a consistencia
        
        # Consistencia alta (>70) -> std pequeña (confianza alta)
        # Consistencia baja (<30) -> std grande (más incertidumbre)
        likelihood_std = 30 - (consistency * 0.25)
        likelihood_std = max(5, likelihood_std)  # Mínimo 5
        
        return likelihood_std
    
    def bayesian_update(self, prior_mean: float, prior_std: float, 
                       observation: float, obs_std: float) -> tuple:
        """
        Actualización Bayesiana clásica para distribuciones gaussianas
        
        Fórmula:
        posterior_mean = (prior_std² * obs + obs_std² * prior) / (prior_std² + obs_std²)
        posterior_std = sqrt((prior_std² * obs_std²) / (prior_std² + obs_std²))
        """
        prior_var = prior_std ** 2
        obs_var = obs_std ** 2
        
        # Calcular media posterior
        posterior_mean = (prior_var * observation + obs_var * prior_mean) / (prior_var + obs_var)
        
        # Calcular desviación estándar posterior
        posterior_var = (prior_var * obs_var) / (prior_var + obs_var)
        posterior_std = np.sqrt(posterior_var)
        
        return posterior_mean, posterior_std
    
    def adjust_score(self, fuzzy_score: float, dimension_scores: Dict[str, float]) -> float:
        """
        Ajusta el score difuso usando inferencia Bayesiana
        
        Proceso:
        1. Calcular consistencia entre dimensiones
        2. Determinar likelihood basado en consistencia
        3. Aplicar actualización Bayesiana
        4. Retornar score ajustado
        """
        # 1. Calcular consistencia
        consistency = self.calculate_consistency(dimension_scores)
        
        # 2. Calcular likelihood
        obs_std = self.calculate_likelihood(fuzzy_score, consistency)
        
        # 3. Actualización Bayesiana
        posterior_mean, posterior_std = self.bayesian_update(
            self.prior_mean,
            self.prior_std,
            fuzzy_score,
            obs_std
        )
        
        # 4. El score final es la media posterior
        # Aplicamos un pequeño ajuste adicional basado en consistencia
        consistency_bonus = (consistency - 50) * 0.1  # ±5 puntos máximo
        
        final_score = posterior_mean + consistency_bonus
        
        # Asegurar que esté en rango [0, 100]
        final_score = max(0, min(100, final_score))
        
        return final_score

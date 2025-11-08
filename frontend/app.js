// Configuración de la API
const API_URL = 'http://localhost:8000/api/compatibilidad';

// Crear corazones flotantes
function createFloatingHearts() {
    const container = document.getElementById('floatingHearts');
    const heartSymbols = ['♥', '❤', '💕', '💖'];
    
    setInterval(() => {
        const heart = document.createElement('div');
        heart.className = 'floating-heart';
        heart.textContent = heartSymbols[Math.floor(Math.random() * heartSymbols.length)];
        heart.style.left = Math.random() * 100 + '%';
        heart.style.animationDuration = (Math.random() * 10 + 10) + 's';
        heart.style.fontSize = (Math.random() * 20 + 15) + 'px';
        
        container.appendChild(heart);
        
        setTimeout(() => {
            heart.remove();
        }, 15000);
    }, 3000);
}

// Funciones de navegación
function mostrarFormulario() {
    document.getElementById('home-section').style.display = 'none';
    document.getElementById('formulario-section').style.display = 'block';
    window.scrollTo(0, 0);
}

function volverInicio() {
    document.getElementById('home-section').style.display = 'block';
    document.getElementById('formulario-section').style.display = 'none';
    document.getElementById('resultados-section').style.display = 'none';
    window.scrollTo(0, 0);
}

// Actualizar valores de sliders en tiempo real
document.addEventListener('DOMContentLoaded', () => {
    // Iniciar animación de corazones
    createFloatingHearts();
    
    const sliders = document.querySelectorAll('.slider');
    
    sliders.forEach(slider => {
        const valueDisplay = slider.nextElementSibling;
        
        slider.addEventListener('input', (e) => {
            valueDisplay.textContent = e.target.value;
        });
    });
    
    // Manejar envío del formulario
    const form = document.getElementById('compatibility-form');
    form.addEventListener('submit', handleSubmit);
});

async function handleSubmit(e) {
    e.preventDefault();
    
    // Recopilar datos del formulario
    const formData = new FormData(e.target);
    const data = {
        persona_a: {
            comunicacion: parseFloat(formData.get('a_comunicacion')),
            valores: parseFloat(formData.get('a_valores')),
            conflicto: parseFloat(formData.get('a_conflicto')),
            estilo_emocional: parseFloat(formData.get('a_estilo_emocional')),
            tiempo_compartido: parseFloat(formData.get('a_tiempo_compartido')),
            intimidad: parseFloat(formData.get('a_intimidad')),
            metas_futuro: parseFloat(formData.get('a_metas_futuro')),
            apoyo_mutuo: parseFloat(formData.get('a_apoyo_mutuo'))
        },
        persona_b: {
            comunicacion: parseFloat(formData.get('b_comunicacion')),
            valores: parseFloat(formData.get('b_valores')),
            conflicto: parseFloat(formData.get('b_conflicto')),
            estilo_emocional: parseFloat(formData.get('b_estilo_emocional')),
            tiempo_compartido: parseFloat(formData.get('b_tiempo_compartido')),
            intimidad: parseFloat(formData.get('b_intimidad')),
            metas_futuro: parseFloat(formData.get('b_metas_futuro')),
            apoyo_mutuo: parseFloat(formData.get('b_apoyo_mutuo'))
        }
    };
    
    // Mostrar loading
    document.getElementById('formulario-section').style.display = 'none';
    document.getElementById('loading').style.display = 'block';
    
    try {
        // Enviar petición al backend
        const response = await fetch(API_URL, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify(data)
        });
        
        if (!response.ok) {
            throw new Error('Error en la respuesta del servidor');
        }
        
        const resultado = await response.json();
        
        // Mostrar resultados
        mostrarResultados(resultado);
        
    } catch (error) {
        console.error('Error:', error);
        alert('Error al calcular compatibilidad. Asegúrate de que el backend esté ejecutándose.');
        document.getElementById('loading').style.display = 'none';
        document.getElementById('formulario-section').style.display = 'block';
    }
}

function mostrarResultados(resultado) {
    // Ocultar loading y formulario
    document.getElementById('loading').style.display = 'none';
    document.getElementById('formulario-section').style.display = 'none';
    
    // Mostrar sección de resultados
    const resultadosSection = document.getElementById('resultados-section');
    resultadosSection.style.display = 'block';
    window.scrollTo(0, 0);
    
    // Mostrar score principal
    const scorePrincipal = document.getElementById('score-principal');
    const clasificacion = resultado.analisis.clasificacion;
    scorePrincipal.innerHTML = `
        <div style="color: ${clasificacion.color}">
            ${resultado.compatibilidad_porcentaje}%
        </div>
        <div style="font-size: 0.5em; margin-top: 10px;">
            ${clasificacion.nivel} - ${clasificacion.descripcion}
        </div>
    `;
    
    // Crear gráfico radar
    crearGraficoRadar(resultado.visualizacion.radar);
    
    // Crear gráfico de barras
    crearGraficoBarras(resultado.visualizacion.barras);
    
    // Mostrar fortalezas
    const fortalezasContent = document.getElementById('fortalezas-content');
    fortalezasContent.innerHTML = resultado.analisis.fortalezas.map(f => `
        <div>
            <strong>${f.dimension}</strong>
            <span style="float: right; color: #ff6b9d; font-weight: 600;">${f.score.toFixed(1)}%</span>
        </div>
    `).join('');
    
    // Mostrar áreas de mejora
    const mejoraContent = document.getElementById('mejora-content');
    mejoraContent.innerHTML = resultado.analisis.areas_mejora.map(a => `
        <div>
            <strong>${a.dimension}</strong>
            <span style="float: right; color: #ff6b9d; font-weight: 600;">${a.score.toFixed(1)}%</span>
        </div>
    `).join('');
    
    // Mostrar recomendaciones
    const recomendacionesContent = document.getElementById('recomendaciones-content');
    recomendacionesContent.innerHTML = resultado.analisis.recomendaciones.map(r => `
        <div class="recomendacion-item">${r}</div>
    `).join('');
}

function crearGraficoRadar(data) {
    const ctx = document.getElementById('radarChart').getContext('2d');
    
    new Chart(ctx, {
        type: 'radar',
        data: {
            labels: data.labels,
            datasets: [
                {
                    label: 'Persona A',
                    data: data.persona_a,
                    borderColor: 'rgb(255, 107, 157)',
                    backgroundColor: 'rgba(255, 107, 157, 0.15)',
                    pointBackgroundColor: 'rgb(255, 107, 157)',
                    pointBorderColor: '#fff',
                    pointHoverBackgroundColor: '#fff',
                    pointHoverBorderColor: 'rgb(255, 107, 157)',
                    borderWidth: 2
                },
                {
                    label: 'Persona B',
                    data: data.persona_b,
                    borderColor: 'rgb(255, 193, 227)',
                    backgroundColor: 'rgba(255, 193, 227, 0.15)',
                    pointBackgroundColor: 'rgb(255, 193, 227)',
                    pointBorderColor: '#fff',
                    pointHoverBackgroundColor: '#fff',
                    pointHoverBorderColor: 'rgb(255, 193, 227)',
                    borderWidth: 2
                }
            ]
        },
        options: {
            scales: {
                r: {
                    beginAtZero: true,
                    max: 10,
                    ticks: {
                        stepSize: 2,
                        color: '#b8b8d1',
                        backdropColor: 'transparent'
                    },
                    grid: {
                        color: 'rgba(255, 107, 157, 0.1)'
                    },
                    pointLabels: {
                        color: '#ffc1e3',
                        font: {
                            size: 12,
                            family: 'Poppins'
                        }
                    },
                    angleLines: {
                        color: 'rgba(255, 107, 157, 0.1)'
                    }
                }
            },
            plugins: {
                legend: {
                    position: 'top',
                    labels: {
                        color: '#ffc1e3',
                        font: {
                            size: 14,
                            family: 'Poppins'
                        },
                        padding: 15
                    }
                }
            }
        }
    });
}

function crearGraficoBarras(data) {
    const ctx = document.getElementById('barChart').getContext('2d');
    
    new Chart(ctx, {
        type: 'bar',
        data: {
            labels: data.labels,
            datasets: [{
                label: 'Compatibilidad %',
                data: data.scores,
                backgroundColor: 'rgba(255, 107, 157, 0.6)',
                borderColor: 'rgb(255, 107, 157)',
                borderWidth: 0,
                borderRadius: 12,
                hoverBackgroundColor: 'rgba(255, 193, 227, 0.8)',
                hoverBorderColor: 'rgb(255, 193, 227)'
            }]
        },
        options: {
            scales: {
                y: {
                    beginAtZero: true,
                    max: 100,
                    ticks: {
                        color: '#b8b8d1',
                        font: {
                            family: 'Poppins'
                        }
                    },
                    grid: {
                        color: 'rgba(255, 107, 157, 0.08)',
                        drawBorder: false
                    }
                },
                x: {
                    ticks: {
                        color: '#ffc1e3',
                        font: {
                            family: 'Poppins'
                        }
                    },
                    grid: {
                        display: false
                    }
                }
            },
            plugins: {
                legend: {
                    display: false
                }
            }
        }
    });
}

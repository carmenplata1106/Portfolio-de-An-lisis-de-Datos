# Análisis de coste de seguros médicos (pricing/riesgo)

Análisis end-to-end (Python + SQL + Power BI) sobre el [Medical Cost Personal Dataset](https://www.kaggle.com/datasets/mirichoi0218/insurance/data) (1.338 asegurados, EE. UU.), para identificar qué perfiles generan mayor coste médico y cómo traducir eso en segmentación de riesgo y ajuste de primas.

**Hallazgo clave:** los fumadores son el 20,5% de los asegurados pero generan más del 45% del coste total — multiplican el gasto medio por 3-4 respecto a los no fumadores.

## Objetivo del análisis

Identificar qué perfiles generan mayores costes médicos, para:
- Mejorar la segmentación de riesgo.
- Ajustar tarifas y primas de seguro.
- Diseñar estrategias de prevención y programas de salud.
- Entender qué factores influyen económicamente en la aseguradora.

## Dataset

| Columna | Descripción |
|---|---|
| `age` | Edad del beneficiario principal |
| `sex` | Género del asegurado (`female`, `male`) |
| `bmi` | Índice de masa corporal (kg/m²); rango saludable 18.5-24.9 |
| `children` | Número de dependientes cubiertos por la póliza |
| `smoker` | Si el asegurado fuma (`yes`/`no`) |
| `region` | Zona de residencia en EE. UU.: `northeast`, `northwest`, `southeast`, `southwest` |
| `charges` | Coste médico individual facturado por el seguro |

## Metodología y stack técnico

**Python** (`EDA.py`) — Pandas, NumPy, Matplotlib, Seaborn: limpieza, estadísticos descriptivos, detección de outliers, categorización de IMC, análisis de correlaciones, export para Power BI.

**SQL** (`sql_part.py`, `consultas.py`) — segmentación por región, tabaquismo y categoría de IMC.

**Power BI** (`seguros_salud.pbix`) — medidas DAX (Coste Total, Coste Medio, Total de Clientes, % de Fumadores, categorías de edad) y dashboard interactivo: comparativas por sexo/región/IMC, impacto del tabaquismo, dispersión edad-coste, treemap de coste por región e IMC, matriz de riesgo fumador × sexo, slicers demográficos.

## Principales insights

**1. El tabaquismo es el factor que más dispara el coste** — multiplica el gasto medio por 3-4, incluso en jóvenes con IMC saludable. Los fumadores (20,5% de la muestra) generan >45% del coste total.

**2. La obesidad es la categoría de IMC de mayor coste medio**, y la combinación fumador + obeso concentra los costes más altos de todo el dataset — especialmente en las regiones *southeast* y *northeast*.

**3. El sexo por sí solo no es un predictor fuerte**, pero refina la segmentación junto con IMC, tabaquismo y edad (p. ej., entre fumadores los hombres tienen coste algo mayor; entre no fumadores, las mujeres).

**4. Southeast concentra el mayor volumen de asegurados y también el mayor coste medio** — perfil clínico más costoso (más fumadores, más obesidad), candidata a acciones focalizadas.

**5. La edad influye, pero menos que el IMC o el tabaquismo** — a cualquier edad, los fumadores están sistemáticamente por encima de los no fumadores en coste.

![Correlación de variables](images/correlacion_variables_py.png)
![Distribución de costes](images/distrib_costes_py.png)
![Distribución por IMC](images/distrib_prom.coste_IMC_py.png)
![Distribución por edad](images/distrib_edad_py.png)

*(Análisis completo, con la matriz de riesgo fumador × sexo y el resto de detalle por segmento, en [`Insights.txt`](Insights.txt).)*

## Estructura del repositorio

```
├── EDA.py                  # Limpieza + análisis exploratorio (Python)
├── sql_part.py              # Segmentación vía SQL
├── consultas.py              # Consultas adicionales
├── seguros_salud.pbix        # Dashboard Power BI (medidas DAX + visualizaciones)
├── insurance.csv              # Dataset original (Kaggle)
├── insurance_eda.csv          # Dataset limpio, exportado tras el EDA
├── Insights.txt                # Análisis detallado por segmento
├── images/                      # Gráficos exportados del EDA
└── posibles mejoras y ampliación del proyecto.txt
```

## Autora

Carmen Plata — [GitHub](https://github.com/carmenplata1106)

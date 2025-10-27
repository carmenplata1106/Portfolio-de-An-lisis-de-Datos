# Causalidad entre Temperatura Media y Humedad Relativa Media — Análisis con Modelos VAR y Pruebas de Granger

## Descripción general
Este proyecto analiza la relación causal entre la **temperatura media diaria** y la **humedad relativa media** utilizando datos meteorológicos de la estación **Almagro/FAMET (Ciudad Real)**.  
El objetivo es determinar si una de las variables influye causalmente sobre la otra en el sentido de **Granger**, utilizando modelos VAR.

## Objetivos
- Explorar la evolución temporal de ambas variables mediante gráficos y transformaciones.  
- Comprobar la estacionariedad de las series aplicando la transformación Box–Cox y diferenciación.  
- Estimar un modelo VAR óptimo en base a criterios de información (AIC, HQ, SC).  
- Aplicar el test de **Causalidad de Granger** para determinar la dirección de la relación causal.

## Herramientas utilizadas
R · dplyr · ggplot2 · forecast · vars · tseries  

## Principales resultados
- Ambas series muestran tendencias, por lo que se aplicó diferenciación tras la transformación Box–Cox.  
- El modelo VAR con un retardo (p = 1) fue seleccionado como el más adecuado.  
- El test de Granger mostró una relación **unidireccional de causalidad**:  
   - la **humedad relativa media causa la temperatura media** (p-value = 0.009).  
   - no se encontró evidencia de causalidad inversa (p-value = 0.889).  
- Los residuos del modelo no presentaron autocorrelación ni estructura temporal significativa.

## Fuente de datos
Datos meteorológicos de la estación **Almagro/FAMET (AEMET)** — Enero a junio de 2024.  
Archivo original: `datos_AEMET.csv`

## Autora
Carmen Plata Fernández  
Máster en Estadística Aplicada · Universidad de Granada

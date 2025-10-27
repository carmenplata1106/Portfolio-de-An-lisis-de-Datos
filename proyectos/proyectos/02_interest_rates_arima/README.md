# Análisis de la Serie Temporal de Tipos de Interés Hipotecarios en España — Modelos ARIMA

## Descripción general
Este proyecto analiza la evolución mensual del tipo de interés medio al inicio de las hipotecas constituidas sobre viviendas en España, utilizando modelos de Box-Jenkins (ARIMA).  
Los datos fueron obtenidos del Instituto Nacional de Estadística (INE) y abarcan el periodo de **octubre de 2012 a septiembre de 2022**, un total de 120 observaciones.

## Objetivos
- Evaluar la estacionariedad y posibles componentes estacionales de la serie.  
- Identificar y estimar modelos ARIMA adecuados para representar la evolución temporal.  
- Validar los modelos a través del análisis de residuos y criterios de ajuste (BIC, R²).  
- Realizar una predicción a corto plazo del tipo de interés medio.

## Herramientas utilizadas
SPSS · R · Box-Jenkins · ARIMA · Funciones de autocorrelación y autocorrelación parcial  

## Principales resultados
- La serie no era estacionaria inicialmente, por lo que se aplicó una diferenciación.  
- Los modelos ARIMA(0,1,1) y ARIMA(1,1,0) se consideraron válidos tras las pruebas de Ljung–Box.  
- El modelo **ARIMA(0,1,1)** fue seleccionado por su menor BIC y mejor ajuste (R² = 0.076).  
- Los residuos resultaron incorrelados, homocedásticos y con distribución normal.

## Fuente de datos
[INE — Tipo de interés medio de hipotecas constituidas sobre viviendas](https://www.ine.es/jaxiT3/Datos.htm?t=24457)

## Autora
Carmen Plata Fernández  
Grado en Estadística · Universidad de Granada

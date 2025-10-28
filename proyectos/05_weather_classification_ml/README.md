# Clasificación de Datos Meteorológicos — Árboles de Decisión y Naive Bayes

## Descripción general
Este proyecto aplica técnicas clásicas de **minería de datos** para resolver un problema de clasificación basado en variables meteorológicas.  
El objetivo es determinar si, dadas ciertas condiciones del clima (vista, temperatura, humedad y viento), se debería o no realizar una actividad al aire libre.  

Se desarrollaron e interpretaron dos algoritmos:  
 **Árbol de decisión (ID3)**, basado en la ganancia de información.  
 **Clasificador Naive Bayes**, fundamentado en la probabilidad condicional y el teorema de Bayes.

## Objetivos
- Calcular la ganancia de información para seleccionar el mejor atributo en cada división.  
- Construir un árbol de decisión completo con nodos hoja representando decisiones finales.  
- Aplicar el clasificador Naive Bayes para estimar la probabilidad de cada clase.  
- Comparar los resultados obtenidos entre ambos métodos.

## Herramientas utilizadas
R · Python · Teoría de la información · Probabilidad condicional · Árboles de decisión · Naive Bayes  

## Principales resultados
- El atributo **“Vista”** obtuvo la mayor ganancia de información, siendo el nodo raíz del árbol.  
- Se confirmaron clasificaciones puras al dividir por los atributos **“Humedad”** y **“Viento”**, logrando una estructura de árbol completa.  
- El clasificador Naive Bayes arrojó una probabilidad del **72.14 %** de “No jugar” frente a un **27.86 %** de “Sí jugar” para el caso de prueba.  
- Ambos métodos ofrecieron resultados coherentes, mostrando la potencia de las técnicas supervisadas simples.

## Dataset
Conjunto de datos meteorológicos simulados, basados en variables:  
`Vista`, `Temperatura`, `Humedad`, `Viento`, `Jugar`.

## Autora
Carmen Plata Fernández  
Máster en Estadística Aplicada · Universidad de Granada

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

#Leemos el dataset
df = pd.read_csv("insurance.csv")

#Mostramos las primeras filas
print("Primeras filas del DataFrame:")
print(df.head())

#Mostramos información básica del DataFrame
print("\nInformación del DataFrame:")
print(df.info())

#Mostramos estadísticas descriptivas
print("\nEstadísticas descriptivas:")
print(df.describe())

#Comprobamos que no hay NA
print("\nValores nulos por columna:")
print(df.isnull().sum())

#Convertir columnas a tipos adecuados
df['sex'] = df['sex'].astype('category')
df['smoker'] = df['smoker'].astype('category')  
df['region'] = df['region'].astype('category')
print("\nTipos de datos después de la conversión:")
print(df.dtypes)

#Visualización de la distribución de edades
plt.figure(figsize=(8, 5))
plt.hist(df['age'], bins=15, color='skyblue', edgecolor='black')
plt.title('Distribución de Edades')
plt.xlabel('Edad')
plt.ylabel('Frecuencia')
plt.show()

#Visualización de la distribución de costes
plt.figure(figsize=(8, 5))
plt.hist(df['charges'], bins=30, color='salmon', edgecolor='black')
plt.title('Distribución de Costes')
plt.xlabel('Costes')
plt.ylabel('Frecuencia')
plt.show()

#Agrupamos el coste medio por fumador
gb = df.groupby('smoker')['charges'].mean().reset_index()
print("\nCoste medio por fumador:")
print(gb)

#Agrupamos el coste medio por región
gb_region = df.groupby('region')['charges'].mean().reset_index()
print("\nCoste medio por región:")
print(gb_region)

#Creamos la variable IMC
df['bmi_category'] = pd.cut(df['bmi'], bins=[0, 18.5, 24.9, 29.9, 100], labels=['Bajo peso', 'Normal', 'Sobrepeso', 'Obesidad'])
print("\nDataFrame con categoría de IMC:")
print(df[['bmi', 'bmi_category']].head())

#Visualización del coste medio por categoría de IMC
gb_bmi = df.groupby('bmi_category')['charges'].mean().reset_index()
plt.figure(figsize=(8, 5))
plt.bar(gb_bmi['bmi_category'], gb_bmi['charges'], color='lightgreen', edgecolor='black')
plt.title('Coste Medio por Categoría de IMC')
plt.xlabel('Categoría de IMC')
plt.ylabel('Coste Medio')
plt.show()

#Correlación entre variables numéricas
correlation = df[['age', 'bmi', 'children', 'charges']].corr()
print("\nMatriz de correlación entre variables numéricas:")
print(correlation)

#Visualización de la matriz de correlación
plt.figure(figsize=(8, 6))
sns.heatmap(correlation, annot=True, cmap='coolwarm', fmt=".2f")
plt.title('Matriz de Correlación')
plt.show()

#Guardamos el DataFrame modificado
df.to_csv("insurance_eda.csv", index=False)
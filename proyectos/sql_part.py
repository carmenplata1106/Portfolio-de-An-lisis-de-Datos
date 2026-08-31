import pandas as pd
import sqlite3

#Cargamos el dataset
df = pd.read_csv("insurance_eda.csv")
print("Primeras filas del DataFrame:")
print(df.head())

#Conectamos a la base de datos SQLite (o creamos una nueva)
conn = sqlite3.connect('insurance.db')

#exportamos el DataFrame a la tabla "insurance_data" en la base de datos
df.to_sql('insurance_data', conn, if_exists='replace', index=False)
print("\nDatos exportados a la base de datos SQLite 'insurance.db' en la tabla 'insurance_data'.")

#Consultamos algunos datos para verificar
tables = conn.execute("SELECT name FROM sqlite_master WHERE type='table';").fetchall()
print("\nTablas en la base de datos:", tables)

#Cerramos la conexión
conn.close()
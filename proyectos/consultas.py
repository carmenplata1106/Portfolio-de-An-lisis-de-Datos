import sqlite3

# Establecer conexión a la base de datos
conn = sqlite3.connect('insurance.db')

cursor = conn.cursor()
cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
print("Tablas que hay en la base de datos:", cursor.fetchall())

#Función para ejecutar una consulta y devolver resultados
def ejecutar_consulta(query):
    cursor = conn.cursor()
    cursor.execute(query)
    resultados = cursor.fetchall()
    cursor.close()
    return resultados

#1. Coste medio por fumador y no fumador
query1 = """
SELECT smoker, AVG(charges) as avg_cost
FROM insurance_data
GROUP BY smoker;
""" 
result1 = ejecutar_consulta(query1)
print("Coste medio por fumador y no fumador:")
for row in result1:
    print(row)

    #2. Coste medio por región
query2 = """
SELECT region, AVG(charges) as avg_cost
FROM insurance_data
GROUP BY region;
"""
result2 = ejecutar_consulta(query2)
print("\nCoste medio por región:")
for row in result2:
    print(row)

    #3. Coste medio por grupo de edad (categorías)
query3 = """
SELECT 
    CASE 
        WHEN age < 30 THEN 'Joven'
        WHEN age BETWEEN 30 AND 50 THEN 'Adulto'
        ELSE 'Mayor'
    END AS age_group,
    AVG(charges) AS avg_charges,
    COUNT(*) AS n_customers
FROM insurance_data
GROUP BY age_group
ORDER BY avg_charges DESC;
"""


result3 = ejecutar_consulta(query3)
print("\nCoste medio por grupo de edad:")
for row in result3:
    print(row)  

    #4. Coste medio por categoría de IMC
query4 = """
SELECT bmi_category, AVG(charges) as avg_charges, COUNT(*) as n_customers
FROM insurance_data
GROUP BY bmi_category
ORDER BY avg_charges DESC;
"""
result4 = ejecutar_consulta(query4)
print("\nCoste medio por categoría de IMC:")
for row in result4:
    print(row)

    #5. TOP 10 clientes con mayor coste
query5 = """
SELECT *
FROM insurance_data
ORDER BY charges DESC
LIMIT 10;
"""
result5 = ejecutar_consulta(query5)
print("\nTOP 10 clientes con mayor coste:")
for row in result5:
    print(row)
    
# Cerrar la conexión a la base de datos
conn.close()

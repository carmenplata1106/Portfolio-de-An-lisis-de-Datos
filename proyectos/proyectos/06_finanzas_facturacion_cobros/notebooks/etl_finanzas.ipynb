# pandas: para leer y manipular los CSV
# sqlalchemy: para conectarse con SQLite
# datetime: para manejar fechas (hoy, diferencias, etc.)
import pandas as pd
from sqlalchemy import create_engine
from datetime import date

# Esto crea (o abre si ya existe) un archivo finanzas.db.
# "sqlite:///" es la ruta de conexión a una base de datos SQLite.
# Todo lo que hagas aquí se guardará en ese archivo.
engine = create_engine("sqlite:///finanzas.db")

# Usamos pandas.read_csv() para leer cada tabla.
# parse_dates convierte las columnas de fecha en formato de fecha.
clientes = pd.read_csv("data/clientes.csv", parse_dates=["fecha_alta"])
productos = pd.read_csv("data/productos.csv")
facturas = pd.read_csv("data/facturas.csv", parse_dates=["fecha_emision", "fecha_vencimiento"])
lineas = pd.read_csv("data/lineas_factura.csv")
pagos = pd.read_csv("data/pagos.csv", parse_dates=["fecha_pago"])

# Aquí empieza la parte "Transform": creamos nuevos cálculos útiles.

# ---- 4.1 Calcular el total bruto por factura ----
# Multiplicamos cantidad * precio_unitario por cada línea.
lineas["importe_linea"] = lineas["cantidad"] * lineas["precio_unitario"]

# Agrupamos por factura_id para sumar todas las líneas de una factura.
totales = (
    lineas
    .groupby("factura_id", as_index=False)["importe_linea"]
    .sum()
    .rename(columns={"importe_linea": "bruto"})
)

# Unimos la suma al dataframe de facturas.
fact = facturas.merge(totales, on="factura_id", how="left")
fact["bruto"] = fact["bruto"].fillna(0)

# ---- 4.2 Aplicar descuentos e IVA ----
fact["neto_sin_iva"] = fact["bruto"] * (1 - fact["descuento_pct"].fillna(0))
fact["total_con_iva"] = fact["neto_sin_iva"] * (1 + fact["iva_pct"].fillna(0))

# ---- 4.3 Calcular cuánto se ha cobrado de cada factura ----
pagos_factura = (
    pagos
    .groupby("factura_id", as_index=False)["importe_pagado"]
    .sum()
    .rename(columns={"importe_pagado": "cobrado"})
)

# Unimos la información de cobros con las facturas
fact = fact.merge(pagos_factura, on="factura_id", how="left")
fact["cobrado"] = fact["cobrado"].fillna(0)

# Calculamos el saldo pendiente
fact["saldo"] = fact["total_con_iva"] - fact["cobrado"]

# ---- 4.4 Calcular el estado real de la factura ----
# Reglas:
# - saldo <= 0 → cobrada
# - saldo > 0 y hoy > fecha_vencimiento → vencida
# - saldo > 0 y hoy <= fecha_vencimiento → emitida (o parcial si ya cobró algo)
today = pd.to_datetime(date.today())

def calcular_estado(fila):
    if fila["saldo"] <= 1e-6:
        return "cobrada"
    elif fila["cobrado"] > 0 and fila["saldo"] > 0 and fila["fecha_vencimiento"] >= today:
        return "parcial"
    elif fila["saldo"] > 0 and fila["fecha_vencimiento"] < today:
        return "vencida"
    else:
        return "emitida"

fact["estado_calculado"] = fact.apply(calcular_estado, axis=1)

# ---- 4.5 Calcular DSO (Days Sales Outstanding) ----
# DSO = días que pasan desde la fecha de emisión hasta el primer pago.
pagos_ordenados = pagos.sort_values(["factura_id", "fecha_pago"])
primer_pago = (
    pagos_ordenados
    .drop_duplicates("factura_id")[["factura_id", "fecha_pago"]]
    .rename(columns={"fecha_pago": "fecha_primer_pago"})
)

# Unimos la fecha del primer pago a las facturas
fact = fact.merge(primer_pago, on="factura_id", how="left")

# Calculamos la diferencia en días
fact["dso_dias"] = (fact["fecha_primer_pago"] - fact["fecha_emision"]).dt.days

# Esto guarda las tablas en la base SQLite (finanzas.db)
clientes.to_sql("clientes", engine, if_exists="replace", index=False)
productos.to_sql("productos", engine, if_exists="replace", index=False)
lineas.to_sql("lineas_factura", engine, if_exists="replace", index=False)
pagos.to_sql("pagos", engine, if_exists="replace", index=False)
fact.to_sql("facturas", engine, if_exists="replace", index=False)

print("ETL completado. Tablas cargadas en finanzas.db")


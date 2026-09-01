# Facturación, cobros y riesgo de impago

Proyecto propio que simula el trabajo de una analista de datos en el área financiera de una empresa: gestión de facturas, pagos y clientes, con foco en **medir el riesgo de impago y el retraso en el cobro**.

## Esquema de datos
- `clientes` — segmento, país, fecha de alta
- `productos` — categoría, coste unitario
- `facturas` — emisión, vencimiento, IVA, descuento, estado
- `lineas_factura` — detalle de productos por factura
- `pagos` — importe y fecha de cada cobro

## KPIs implementados (SQL)
- **DSO (Days Sales Outstanding)** mensual — tiempo medio real en cobrar una factura
- **Aging de deuda** — clasificación de facturas vencidas en buckets (0-30, 31-60, 61-90, >90 días)
- **Top 20 deudores** — clientes con mayor saldo pendiente
- **Ingresos vs. cobros** por mes
- **Margen por producto** — ingresos menos coste

## Estado
ETL y modelo de datos + KPIs en SQL completos (`sql/schema.sql`, `sql/kpis.sql`, `notebooks/etl_finanzas.ipynb`). Pendiente: extraer insights reales de los datos y, si da tiempo, montar un dashboard en Power BI sobre estas mismas vistas.


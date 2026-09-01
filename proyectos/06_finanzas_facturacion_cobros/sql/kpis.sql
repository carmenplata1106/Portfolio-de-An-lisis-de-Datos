-- ====== VISTAS DE APOYO ======
-- Total por factura (bruto, neto, total con IVA)
CREATE VIEW IF NOT EXISTS v_totales_factura AS
SELECT
  f.factura_id,
  SUM(l.cantidad * l.precio_unitario)                           AS bruto,
  SUM(l.cantidad * l.precio_unitario) * (1 - COALESCE(f.descuento_pct,0))                 AS neto_sin_iva,
  SUM(l.cantidad * l.precio_unitario) * (1 - COALESCE(f.descuento_pct,0)) * (1 + COALESCE(f.iva_pct,0)) AS total_con_iva
FROM facturas f
JOIN lineas_factura l USING (factura_id)
GROUP BY f.factura_id;

-- Cobrado acumulado por factura
CREATE VIEW IF NOT EXISTS v_pagado_factura AS
SELECT
  factura_id,
  COALESCE(SUM(importe_pagado),0) AS cobrado
FROM pagos
GROUP BY factura_id;

-- Facturas con saldo
CREATE VIEW IF NOT EXISTS v_facturas_saldo AS
SELECT
  f.*,
  t.bruto,
  t.neto_sin_iva,
  t.total_con_iva,
  p.cobrado,
  (t.total_con_iva - COALESCE(p.cobrado,0)) AS saldo
FROM facturas f
LEFT JOIN v_totales_factura t USING (factura_id)
LEFT JOIN v_pagado_factura  p USING (factura_id);

-- Primer pago por factura (para DSO)
CREATE VIEW IF NOT EXISTS v_primer_pago AS
SELECT factura_id, MIN(fecha_pago) AS fecha_primer_pago
FROM pagos
GROUP BY factura_id;

-- DSO por factura (solo si existe pago)
CREATE VIEW IF NOT EXISTS v_dso_factura AS
SELECT
  f.factura_id,
  f.fecha_emision,
  pp.fecha_primer_pago,
  CAST(julianday(pp.fecha_primer_pago) - julianday(f.fecha_emision) AS INTEGER) AS dso_dias
FROM facturas f
JOIN v_primer_pago pp USING (factura_id);

-- ====== KPIs PRINCIPALES ======
-- 1) Ingresos y cobros por mes
CREATE VIEW IF NOT EXISTS kpi_ingresos_cobros_mes AS
WITH fact AS (
  SELECT DATE(substr(fecha_emision,1,7) || '-01') AS mes, SUM(total_con_iva) AS ingresos
  FROM v_facturas_saldo
  GROUP BY mes
),
cob AS (
  SELECT DATE(substr(fecha_pago,1,7) || '-01') AS mes, SUM(importe_pagado) AS cobros
  FROM pagos
  GROUP BY mes
)
SELECT
  COALESCE(fact.mes, cob.mes) AS mes,
  COALESCE(fact.ingresos,0)   AS ingresos,
  COALESCE(cob.cobros,0)      AS cobros
FROM fact
FULL OUTER JOIN cob ON fact.mes = cob.mes
-- SQLite no tiene FULL OUTER JOIN; simulamos con UNION ALL:
-- Reemplazo del bloque anterior por UNION ALL:
;

-- (Implementación compatible con SQLite sin FULL OUTER JOIN)
DROP VIEW IF EXISTS kpi_ingresos_cobros_mes;
CREATE VIEW kpi_ingresos_cobros_mes AS
SELECT
  m.mes,
  COALESCE(f.ingresos,0) AS ingresos,
  COALESCE(c.cobros,0)   AS cobros
FROM (
  SELECT DATE(substr(fecha_emision,1,7) || '-01') AS mes FROM facturas
  UNION
  SELECT DATE(substr(fecha_pago,1,7) || '-01') AS mes FROM pagos
) m
LEFT JOIN (
  SELECT DATE(substr(fecha_emision,1,7) || '-01') AS mes, SUM(total_con_iva) AS ingresos
  FROM v_facturas_saldo
  GROUP BY mes
) f ON m.mes = f.mes
LEFT JOIN (
  SELECT DATE(substr(fecha_pago,1,7) || '-01') AS mes, SUM(importe_pagado) AS cobros
  FROM pagos
  GROUP BY mes
) c ON m.mes = c.mes;

-- 2) DSO medio por mes (solo facturas con pago)
CREATE VIEW IF NOT EXISTS kpi_dso_mensual AS
SELECT
  DATE(substr(f.fecha_emision,1,7) || '-01') AS mes_emision,
  AVG(CAST(julianday(pp.fecha_primer_pago) - julianday(f.fecha_emision) AS REAL)) AS dso_medio
FROM facturas f
JOIN v_primer_pago pp USING (factura_id)
GROUP BY mes_emision;

-- 3) Aging (saldo pendiente por bucket)
CREATE VIEW IF NOT EXISTS kpi_aging AS
WITH base AS (
  SELECT
    factura_id,
    fecha_vencimiento,
    saldo,
    MAX(0, CAST(julianday(date('now')) - julianday(fecha_vencimiento) AS INTEGER)) AS dias_vencidos
  FROM v_facturas_saldo
  WHERE saldo > 0
)
SELECT
  CASE
    WHEN dias_vencidos = 0 THEN 'No vencida'
    WHEN dias_vencidos BETWEEN 1 AND 30 THEN '0-30'
    WHEN dias_vencidos BETWEEN 31 AND 60 THEN '31-60'
    WHEN dias_vencidos BETWEEN 61 AND 90 THEN '61-90'
    ELSE '>90'
  END AS bucket,
  SUM(saldo) AS saldo_pendiente
FROM base
GROUP BY bucket
ORDER BY
  CASE bucket
    WHEN 'No vencida' THEN 0
    WHEN '0-30' THEN 1
    WHEN '31-60' THEN 2
    WHEN '61-90' THEN 3
    ELSE 4
  END;

-- 4) Top deudores (clientes con más saldo pendiente)
CREATE VIEW IF NOT EXISTS kpi_top_deudores AS
SELECT
  c.cliente_id,
  c.nombre,
  ROUND(SUM(fs.saldo),2) AS saldo_pendiente
FROM v_facturas_saldo fs
JOIN clientes c USING (cliente_id)
WHERE fs.saldo > 0
GROUP BY c.cliente_id, c.nombre
ORDER BY saldo_pendiente DESC
LIMIT 20;

-- 5) Margen por producto (requiere costo_unitario)
CREATE VIEW IF NOT EXISTS kpi_margen_producto AS
WITH det AS (
  SELECT
    lf.producto_id,
    SUM(lf.cantidad) AS uds,
    SUM(lf.cantidad * lf.precio_unitario) AS ingresos_sin_desc,
    SUM(lf.cantidad * p.costo_unitario)   AS costo_total
  FROM lineas_factura lf
  JOIN productos p USING (producto_id)
  GROUP BY lf.producto_id
)
SELECT
  pr.producto_id,
  pr.nombre,
  pr.categoria,
  det.uds,
  det.ingresos_sin_desc AS ingresos_brutos,
  det.costo_total,
  (det.ingresos_sin_desc - det.costo_total) AS margen
FROM det
JOIN productos pr USING (producto_id)
ORDER BY margen DESC;

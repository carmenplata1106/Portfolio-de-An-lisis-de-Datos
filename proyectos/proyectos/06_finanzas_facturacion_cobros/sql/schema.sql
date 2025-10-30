PRAGMA foreign_keys = ON; -- instrucción específica de SQLite, hace que se activen las claves foráneas (así dará error si intentas buscar una valor inexistente de cierta tabla)

CREATE TABLE clientes (
  cliente_id     INTEGER PRIMARY KEY,
  nombre         TEXT NOT NULL,
  segmento       TEXT,
  pais           TEXT,
  fecha_alta     DATE
);

CREATE TABLE productos (
  producto_id    INTEGER PRIMARY KEY,
  nombre         TEXT NOT NULL,
  categoria      TEXT NOT NULL,
  costo_unitario REAL NOT NULL  -- REAL es número decimal
);

CREATE TABLE facturas (
  factura_id         INTEGER PRIMARY KEY,
  cliente_id         INTEGER NOT NULL,
  fecha_emision      DATE NOT NULL,
  fecha_vencimiento  DATE NOT NULL,
  iva_pct            REAL DEFAULT 0.21,
  descuento_pct      REAL DEFAULT 0.0,
  estado             TEXT,
  FOREIGN KEY (cliente_id) REFERENCES clientes(cliente_id)  -- asegura que solo puedes registrar facturas de clientes existentes.
);

CREATE TABLE lineas_factura (
  linea_id        INTEGER PRIMARY KEY,
  factura_id      INTEGER NOT NULL,
  producto_id     INTEGER NOT NULL,
  cantidad        INTEGER NOT NULL,
  precio_unitario REAL NOT NULL,
  FOREIGN KEY (factura_id) REFERENCES facturas(factura_id),  -- 1 factura -> muchas líneas de factura
  FOREIGN KEY (producto_id) REFERENCES productos(producto_id)
);

CREATE TABLE pagos (
  pago_id        INTEGER PRIMARY KEY,
  factura_id     INTEGER NOT NULL,
  fecha_pago     DATE NOT NULL,
  importe_pagado REAL NOT NULL,
  metodo_pago    TEXT NOT NULL,
  FOREIGN KEY (factura_id) REFERENCES facturas(factura_id) -- 1 factura -> muchos pagos
);

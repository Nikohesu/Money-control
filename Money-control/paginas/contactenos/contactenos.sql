-- Crear la base de datos
CREATE DATABASE IF NOT EXISTS contactenos;

-- Usar la base de datos
USE contactenos;

-- Crear la tabla datos
CREATE TABLE IF NOT EXISTS mensajes (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL,
    correo VARCHAR(100) NOT NULL,
    dispositivo VARCHAR(100) NOT NULL,
    tipo VARCHAR(100) NOT NULL,
    mensaje VARCHAR(255) NOT NULL,
    fecha_creacion TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
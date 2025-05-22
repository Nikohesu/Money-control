CREATE DATABASE IF NOT EXISTS formulario;

USE formulario;

CREATE TABLE IF NOT EXISTS usuarios (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(20) NOT NULL,
    email VARCHAR(20) NOT NULL,
    contrasena VARCHAR(20) NOT NULL,
    fecha_de_creacion TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
);
-- Crear la base de datos
CREATE DATABASE IF NOT EXISTS formulario;

-- Usar la base de datos
USE formulario;

-- Crear la tabla usuarios
CREATE TABLE IF NOT EXISTS registros (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL,
    apellido VARCHAR(100) NOT NULL,
    telefono VARCHAR(100) NOT NULL,
    email VARCHAR(100) NOT NULL,
    contrasena VARCHAR(255) NOT NULL,
    genero VARCHAR(100) NOT NULL,
    fecha_creacion TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
-- Crear la base de datos
CREATE DATABASE GestionDeEstudiantes CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci;
USE GestionDeEstudiantes;

-- Tabla de administradores
CREATE TABLE administradores (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL,
    correo VARCHAR(100) UNIQUE NOT NULL,
    contraseña VARCHAR(255) NOT NULL
);

-- Tabla de profesores
CREATE TABLE profesores (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL,
    correo VARCHAR(100) UNIQUE NOT NULL,
    contraseña VARCHAR(255) NOT NULL
);

-- Tabla de estudiantes
CREATE TABLE estudiantes (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL,
    correo VARCHAR(100) UNIQUE NOT NULL,
    contraseña VARCHAR(255) NOT NULL
);

-- Tabla de padres
CREATE TABLE padres (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL,
    correo VARCHAR(100) UNIQUE NOT NULL,
    contraseña VARCHAR(255) NOT NULL
);

-- Tabla de relación entre padres y estudiantes
CREATE TABLE padres_estudiantes (
    id_padre INT NOT NULL,
    id_estudiante INT NOT NULL,
    PRIMARY KEY (id_padre, id_estudiante),
    FOREIGN KEY (id_padre) REFERENCES padres(id) ON DELETE CASCADE,
    FOREIGN KEY (id_estudiante) REFERENCES estudiantes(id) ON DELETE CASCADE
);

-- Tabla de materias
CREATE TABLE materias (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL UNIQUE,
    descripcion TEXT
);

-- Tabla de asignaciones de profesores a materias
CREATE TABLE asignaciones (
    id_profesor INT NOT NULL,
    id_materia INT NOT NULL,
    PRIMARY KEY (id_profesor, id_materia),
    FOREIGN KEY (id_profesor) REFERENCES profesores(id) ON DELETE CASCADE,
    FOREIGN KEY (id_materia) REFERENCES materias(id) ON DELETE CASCADE
);

-- Tabla de inscripciones de estudiantes a materias
CREATE TABLE inscripciones (
    id_estudiante INT NOT NULL,
    id_materia INT NOT NULL,
    PRIMARY KEY (id_estudiante, id_materia),
    FOREIGN KEY (id_estudiante) REFERENCES estudiantes(id) ON DELETE CASCADE,
    FOREIGN KEY (id_materia) REFERENCES materias(id) ON DELETE CASCADE
);

-- Tabla de notas
CREATE TABLE notas (
    id_estudiante INT NOT NULL,
    id_materia INT NOT NULL,
    calificacion FLOAT NOT NULL,
    fecha TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    PRIMARY KEY (id_estudiante, id_materia),
    FOREIGN KEY (id_estudiante) REFERENCES estudiantes(id) ON DELETE CASCADE,
    FOREIGN KEY (id_materia) REFERENCES materias(id) ON DELETE CASCADE
);

-- Tabla de notificaciones
CREATE TABLE notificaciones (
    id INT AUTO_INCREMENT PRIMARY KEY,
    id_estudiante INT NOT NULL,
    titulo VARCHAR(255) NOT NULL,
    mensaje TEXT NOT NULL,
    fecha TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (id_estudiante) REFERENCES estudiantes(id) ON DELETE CASCADE
);


-- Tabla de usuarios
CREATE TABLE usuarios (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL,
    correo VARCHAR(100) UNIQUE NOT NULL,
    contraseña VARCHAR(255) NOT NULL,
    rol ENUM('admin', 'profesor', 'estudiante', 'padre') NOT NULL
);
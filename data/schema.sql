use astralacademy;

-- Tabla de Usuarios
CREATE TABLE Usuarios (
    IDUsuario INT PRIMARY KEY AUTO_INCREMENT,
    Nombre VARCHAR(50) NOT NULL,
    CorreoElectronico VARCHAR(100) NOT NULL,
    Contraseña VARCHAR(255) NOT NULL,
    Rol ENUM(
        'Organizador',
        'DirectorAcademico',
        'Visitante',
        'Registrado',
        'Ponente'
    ) NOT NULL
);

-- Tabla de Eventos Académicos
CREATE TABLE Eventos (
    IDEvento INT PRIMARY KEY AUTO_INCREMENT,
    Titulo VARCHAR(100) NOT NULL,
    Descripcion TEXT,
    FechaInicio DATE NOT NULL,
    FechaFin DATE NOT NULL,
    Aforo INT NOT NULL,
    Ubicacion VARCHAR(100) NOT NULL,
    Precio DECIMAL(10, 2) NOT NULL,
    DerechosParticipacion TEXT,
    Estado ENUM(
        'Planificacion',
        'Inscripcion',
        'EnCurso',
        'Finalizado'
    ) DEFAULT 'Planificacion',
    IDUsuarioOrganizador INT,
    FOREIGN KEY (IDUsuarioOrganizador) REFERENCES Usuarios(IDUsuario)
);

-- Tabla de Preinscripciones
CREATE TABLE Preinscripciones (
    IDPreinscripcion INT PRIMARY KEY AUTO_INCREMENT,
    IDEvento INT,
    IDUsuarioRegistrado INT,
    FechaPreinscripcion TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    Confirmado BOOLEAN DEFAULT 0,
    FOREIGN KEY (IDUsuarioRegistrado) REFERENCES Usuarios(IDUsuario),
    FOREIGN KEY (IDEvento) REFERENCES Eventos(IDEvento)
);

-- Tabla de Ponentes
CREATE TABLE Ponentes (
    IDPonente INT PRIMARY KEY AUTO_INCREMENT,
    IDEvento INT,
    IDUsuario INT,
    FOREIGN KEY (IDUsuario) REFERENCES Usuarios(IDUsuario),
    FOREIGN KEY (IDEvento) REFERENCES Eventos(IDEvento)
);

-- Tabla de Certificados
CREATE TABLE Certificados (
    IDCertificado INT PRIMARY KEY AUTO_INCREMENT,
    IDPreinscripcion INT,
    Contenido TEXT,
    FOREIGN KEY (IDPreinscripcion) REFERENCES Preinscripciones(IDPreinscripcion)
);

-- Tabla de Correos Electrónicos
CREATE TABLE Correos (
    IDCorreo INT PRIMARY KEY AUTO_INCREMENT,
    IDUsuario INT,
    Asunto VARCHAR(255) NOT NULL,
    Cuerpo TEXT NOT NULL,
    Enviado TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (IDUsuario) REFERENCES Usuarios(IDUsuario)
);
use astralacademy;

CREATE TABLE `usuarios` (
  `IDUsuario` int NOT NULL AUTO_INCREMENT,
  `Nombre` varchar(50) NOT NULL,
  `CorreoElectronico` varchar(100) NOT NULL,
  `Contraseña` varchar(255) NOT NULL,
  `Rol` enum('Organizador','DirectorAcademico','Visitante','Registrado','Ponente') NOT NULL,
  PRIMARY KEY (`IDUsuario`)
)

CREATE TABLE `preinscripciones` (
  `IDPreinscripcion` int NOT NULL AUTO_INCREMENT,
  `IDEvento` int DEFAULT NULL,
  `IDUsuarioRegistrado` int DEFAULT NULL,
  `FechaPreinscripcion` timestamp NULL DEFAULT CURRENT_TIMESTAMP,
  `Confirmado` tinyint(1) DEFAULT '0',
  PRIMARY KEY (`IDPreinscripcion`),
  KEY `IDUsuarioRegistrado` (`IDUsuarioRegistrado`),
  KEY `IDEvento` (`IDEvento`),
  CONSTRAINT `preinscripciones_ibfk_1` FOREIGN KEY (`IDUsuarioRegistrado`) REFERENCES `usuarios` (`IDUsuario`),
  CONSTRAINT `preinscripciones_ibfk_2` FOREIGN KEY (`IDEvento`) REFERENCES `eventos` (`IDEvento`)
)

CREATE TABLE `eventos` (
  `IDEvento` int NOT NULL AUTO_INCREMENT,
  `Titulo` varchar(100) NOT NULL,
  `Descripcion` text,
  `FechaInicio` date DEFAULT NULL,
  `FechaFin` date DEFAULT NULL,
  `Aforo` int DEFAULT NULL,
  `Ubicacion` varchar(100) DEFAULT NULL,
  `Precio` decimal(10,2) DEFAULT NULL,
  `DerechosParticipacion` text,
  `IDUsuarioOrganizador` int DEFAULT NULL,
  PRIMARY KEY (`IDEvento`),
  KEY `IDUsuarioOrganizador` (`IDUsuarioOrganizador`),
  CONSTRAINT `eventos_ibfk_1` FOREIGN KEY (`IDUsuarioOrganizador`) REFERENCES `usuarios` (`IDUsuario`)
)

CREATE TABLE `correos` (
  `IDCorreo` int NOT NULL AUTO_INCREMENT,
  `IDUsuario` int DEFAULT NULL,
  `Asunto` varchar(255) NOT NULL,
  `Cuerpo` text NOT NULL,
  `Enviado` timestamp NULL DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`IDCorreo`),
  KEY `IDUsuario` (`IDUsuario`),
  CONSTRAINT `correos_ibfk_1` FOREIGN KEY (`IDUsuario`) REFERENCES `usuarios` (`IDUsuario`)
)

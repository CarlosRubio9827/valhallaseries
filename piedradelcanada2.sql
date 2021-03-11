-- phpMyAdmin SQL Dump
-- version 4.8.5
-- https://www.phpmyadmin.net/
--
-- Servidor: 127.0.0.1:3307
-- Tiempo de generación: 06-03-2021 a las 14:08:40
-- Versión del servidor: 10.3.14-MariaDB
-- Versión de PHP: 7.3.5

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Base de datos: `piedradelcanada2`
--

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `categorias`
--

DROP TABLE IF EXISTS `categorias`;
CREATE TABLE IF NOT EXISTS `categorias` (
  `idcategorias` int(11) NOT NULL AUTO_INCREMENT,
  `nombreCategoría` varchar(45) DEFAULT NULL,
  `rangoMin` int(11) DEFAULT NULL,
  `rangoMax` int(11) DEFAULT NULL,
  `descripcionCategoria` varchar(45) DEFAULT NULL,
  `sexo` varchar(32) NOT NULL,
  `distancia` varchar(32) NOT NULL,
  PRIMARY KEY (`idcategorias`)
) ENGINE=InnoDB AUTO_INCREMENT=44 DEFAULT CHARSET=utf8mb4;

--
-- Volcado de datos para la tabla `categorias`
--

INSERT INTO `categorias` (`idcategorias`, `nombreCategoría`, `rangoMin`, `rangoMax`, `descripcionCategoria`, `sexo`, `distancia`) VALUES
(3, 'PreInfantil-Masculino-10K', 0, 15, 'Pre-Infantil masculino', 'Masculino', '10K'),
(4, 'PreInfantil-Femenino-10K', 0, 15, 'Pre-Infantil femenino', 'Femenino', '10K'),
(5, 'PreInfantil-Masculino-21K', 0, 15, 'Pre-Infantil masculino', 'Masculino', '21K'),
(6, 'PreInfantil-Femenino-21K', 0, 15, 'Pre-Infantil femenino', 'Femenino', '21K'),
(7, 'PreInfantil-Masculino-30K', 0, 15, 'Pre-Infantil masculino', 'Masculino', '30K'),
(8, 'PreInfantil-Femenino-30K', 0, 15, 'Pre-Infantil femenino', 'Femenino', '30K'),
(9, 'PreJuvenil-Masculino-10K', 15, 18, 'Pre-Juvenil masculino', 'Masculino', '10K'),
(10, 'PreJuvenil-Femenino-10K', 15, 18, 'Pre-Juvenil femenino', 'Femenino', '10K'),
(11, 'PreJuvenil-Masculino-21K', 15, 18, 'Pre-Juvenil masculino', 'Masculino', '21K'),
(12, 'PreJuvenil-Femenino-21K', 15, 18, 'Pre-Juvenil femenino', 'Femenino', '21K'),
(13, 'PreJuvenil-Masculino-30K', 15, 18, 'Pre-Juvenil masculino', 'Masculino', '30K'),
(14, 'PreJuvenil-Femenino-30K', 15, 18, 'Pre-Juvenil femenino', 'Femenino', '30K'),
(15, 'General-Masculino-10K', 18, 40, 'General masculino', 'Masculino', '10K'),
(16, 'General-Femenino-10K', 18, 40, 'General femenino', 'Femenino', '10K'),
(17, 'General-Masculino-21K', 18, 40, 'General masculino', 'Masculino', '21K'),
(18, 'General-Femenino-21K', 18, 40, 'General femenino', 'Femenino', '21K'),
(19, 'General-Masculino-30K', 18, 40, 'General masculino', 'Masculino', '30K'),
(20, 'General-Femenino-30K', 18, 40, 'General femenino', 'Femenino', '30K'),
(21, 'MasterA-Masculino-10K', 40, 50, 'Master-A masculino', 'Masculino', '10K'),
(22, 'MasterA-Femenino-10K', 40, 50, 'Master-A femenino', 'Femenino', '10K'),
(23, 'MasterA-Masculino-21K', 40, 50, 'Master-A masculino', 'Masculino', '21K'),
(24, 'MasterA-Femenino-21K', 40, 50, 'Master-A femenino', 'Femenino', '21K'),
(25, 'MasterA-Masculino-30K', 40, 50, 'Master-A masculino', 'Masculino', '30K'),
(26, 'MasterA-Femenino-30K', 40, 50, 'Master-A femenino', 'Femenino', '30K'),
(27, 'MasterB-Masculino-10K', 50, 100, 'Master-B masculino', 'Masculino', '10K'),
(28, 'MasterB-Femenino-10K', 50, 100, 'Master-B femenino', 'Femenino', '10K'),
(29, 'MasterB-Masculino-21K', 50, 100, 'Master-B masculino', 'Masculino', '21K'),
(30, 'MasterB-Femenino-21K', 50, 100, 'Master-B femenino', 'Femenino', '21K'),
(31, 'MasterB-Masculino-30K', 50, 100, 'Master-B masculino', 'Masculino', '30K'),
(32, 'MasterB-Femenino-30K', 50, 100, 'Master-B femenino', 'Femenino', '30K'),
(33, 'No aplica', NULL, NULL, NULL, '', ''),
(34, 'PreInfantil-Femenino-42K', 0, 15, 'Pre-Infantil femenino', 'Femenino', '42K'),
(35, 'MasterB-Femenino-42K', 50, 100, 'Master-B femenino', 'Femenino', '42K'),
(36, 'MasterB-Masculino-42K', 50, 100, 'Master-B masculino', 'Masculino', '42K'),
(37, 'General-Femenino-42K', 18, 40, 'General femenino', 'Femenino', '42K'),
(38, 'PreJuvenil-Masculino-42K', 15, 18, 'Pre-Juvenil masculino', 'Masculino', '42K'),
(39, 'PreJuvenil-Femenino-42K', 15, 18, 'Pre-Juvenil femenino', 'Femenino', '42K'),
(40, 'General-Masculino-42K', 18, 40, 'General masculino', 'Masculino', '42K'),
(41, 'MasterA-Femenino-42K', 40, 50, 'Master-A femenino', 'Femenino', '42K'),
(42, 'MasterA-Masculino-42K', 40, 50, 'Master-A masculino', 'Masculino', '42K'),
(43, 'PreInfantil-Masculino-42K', 0, 15, 'Pre-Infantil masculino', 'Masculino', '42K');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `distancias`
--

DROP TABLE IF EXISTS `distancias`;
CREATE TABLE IF NOT EXISTS `distancias` (
  `iddistancias` int(11) NOT NULL AUTO_INCREMENT,
  `nombreDistancia` varchar(45) DEFAULT NULL,
  `precioDistancia` int(11) DEFAULT NULL,
  PRIMARY KEY (`iddistancias`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8mb4;

--
-- Volcado de datos para la tabla `distancias`
--

INSERT INTO `distancias` (`iddistancias`, `nombreDistancia`, `precioDistancia`) VALUES
(1, '10K', 50000),
(2, '21K', 65000),
(3, '30K', 70000),
(4, '42K', 85000);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `equipos`
--

DROP TABLE IF EXISTS `equipos`;
CREATE TABLE IF NOT EXISTS `equipos` (
  `idequipos` int(11) NOT NULL AUTO_INCREMENT,
  `nombreEquipo` varchar(45) DEFAULT NULL,
  `codigoEquipo` varchar(45) DEFAULT NULL,
  PRIMARY KEY (`idequipos`)
) ENGINE=InnoDB AUTO_INCREMENT=54 DEFAULT CHARSET=utf8mb4;

--
-- Volcado de datos para la tabla `equipos`
--

INSERT INTO `equipos` (`idequipos`, `nombreEquipo`, `codigoEquipo`) VALUES
(1, 'Fuerte Forest', 'H43A46MM'),
(2, 'Buitrera Vertical', 'S33I42KL'),
(3, 'Pradera Trail', 'X38W14XZ'),
(4, 'Pantera del Bosque', 'L40I45CP'),
(5, 'Vida Corrida', 'M20Q30RI'),
(6, 'Pegasus Team', 'O35W22IN'),
(7, 'Team Mao', 'G46X16KV'),
(8, 'Maja de Hierro', 'F30I31KV'),
(9, 'Coyotes Trail', 'Q45F3BB'),
(10, 'The Wolf', 'J29M11XZ'),
(11, 'The Fastest Runner', 'D22O20GR'),
(12, 'The Warriors', 'O20X28CV'),
(13, 'Bikila', 'K31R21AG'),
(14, 'Coomeva', 'Z21F23IL'),
(15, 'United Runners Team', 'L33P47KG'),
(16, 'Mi Gente Runner', 'R16Y41XJ'),
(17, 'Sanchocho Runner', 'W9E20VD'),
(18, 'Pachamama Trail', 'T12G43VM'),
(19, 'Crazy Runners', 'B15D24VG'),
(20, 'Valedalen Club editado', 'V413dada'),
(21, 'Ultra Trail Delta', 'L47O45EN'),
(22, 'Colibrí Trail Running', 'E18N17KK'),
(23, 'Mercenario Trail Running', 'B2C34SY'),
(24, 'The Mountain Runners', 'W32I49RY'),
(25, 'Cali Ultra Trail', 'Z3F43ZP'),
(26, 'Sin Equipo', ''),
(27, 'Jose Sanchez Team', 'J053S4CJ'),
(28, 'Senderos', 'S3ND3R05'),
(29, 'Forest Runners', 'F0735JKS'),
(30, 'Hard Runners', 'H4R9R8JN'),
(31, 'Aguiluchos', 'A42DCH0s'),
(32, 'Warrior Team', 'W4RR105D'),
(33, 'Zarihuellas', 'Z4R1HU3L'),
(34, 'Ultra trail delta', 'U1T749KJ'),
(35, 'La roka', 'L4R0544J'),
(36, 'Trail runnig ciudad blanca', 'T7417JSJ'),
(37, 'Trail runnig costa rica', 'TRC0574R'),
(38, 'Road Runners Andalucía', 'R047R4ND'),
(39, 'G\'LATINOS ANDALUCIA', 'G3L4T7I0'),
(40, 'CORREDORES DE TENERIFE', 'C077T3N3'),
(41, 'BENGALA RUNNERS', 'B3N641AR'),
(42, 'Trail Runnig Manizales', 'TR41LR49'),
(43, 'Trotadores Tuluá', 'T7074TUL'),
(44, 'Betomania de Andalucía', 'B3704N1A'),
(45, 'wings runners de zarzal', 'W1N5RRU3'),
(46, '360fit', 'DASDASDA'),
(47, 'Titan runners', 'T1T4N7UN'),
(48, 'Equipo de prueba', 'sssdsdsd'),
(49, 'Amrica', 'G46X16Kp'),
(50, 'jjjjjjjjjj', 'jjjjjjjj'),
(51, 'HHH', 'GVBGFFGB'),
(52, 'sasasa', 'F30I31Kl'),
(53, 'jjjjj', 'hhhjjjjj');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `estadoinscripcion`
--

DROP TABLE IF EXISTS `estadoinscripcion`;
CREATE TABLE IF NOT EXISTS `estadoinscripcion` (
  `idestadoInscripcion` int(11) NOT NULL AUTO_INCREMENT,
  `estadoActualInscripcion` varchar(45) DEFAULT NULL,
  PRIMARY KEY (`idestadoInscripcion`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4;

--
-- Volcado de datos para la tabla `estadoinscripcion`
--

INSERT INTO `estadoinscripcion` (`idestadoInscripcion`, `estadoActualInscripcion`) VALUES
(1, 'Pendiente de Pago'),
(2, 'Registrado');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `estadokit`
--

DROP TABLE IF EXISTS `estadokit`;
CREATE TABLE IF NOT EXISTS `estadokit` (
  `idestadoKit` int(11) NOT NULL AUTO_INCREMENT,
  `estadoActualKit` varchar(45) DEFAULT NULL,
  PRIMARY KEY (`idestadoKit`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4;

--
-- Volcado de datos para la tabla `estadokit`
--

INSERT INTO `estadokit` (`idestadoKit`, `estadoActualKit`) VALUES
(1, 'Sin entregar'),
(2, 'Entregado');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `eventos`
--

DROP TABLE IF EXISTS `eventos`;
CREATE TABLE IF NOT EXISTS `eventos` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `nombre` varchar(64) CHARACTER SET utf8 COLLATE utf8_spanish2_ci NOT NULL,
  `estado` varchar(64) CHARACTER SET utf8 COLLATE utf8_spanish2_ci NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=MyISAM AUTO_INCREMENT=4 DEFAULT CHARSET=utf8mb4;

--
-- Volcado de datos para la tabla `eventos`
--

INSERT INTO `eventos` (`id`, `nombre`, `estado`) VALUES
(1, 'entreno', 'Disponible'),
(2, 'Km Vertical', 'Disponible'),
(3, 'Carrera', 'Disponible');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `sexo`
--

DROP TABLE IF EXISTS `sexo`;
CREATE TABLE IF NOT EXISTS `sexo` (
  `idsexo` int(11) NOT NULL AUTO_INCREMENT,
  `nombreSexo` varchar(45) DEFAULT NULL,
  PRIMARY KEY (`idsexo`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4;

--
-- Volcado de datos para la tabla `sexo`
--

INSERT INTO `sexo` (`idsexo`, `nombreSexo`) VALUES
(1, 'Femenino'),
(2, 'Masculino');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `tallacamisa`
--

DROP TABLE IF EXISTS `tallacamisa`;
CREATE TABLE IF NOT EXISTS `tallacamisa` (
  `idtallaCamisa` int(11) NOT NULL AUTO_INCREMENT,
  `tamañoTalla` varchar(45) DEFAULT NULL,
  PRIMARY KEY (`idtallaCamisa`)
) ENGINE=InnoDB AUTO_INCREMENT=14 DEFAULT CHARSET=utf8mb4;

--
-- Volcado de datos para la tabla `tallacamisa`
--

INSERT INTO `tallacamisa` (`idtallaCamisa`, `tamañoTalla`) VALUES
(1, 'XS'),
(2, 'S'),
(3, 'M'),
(4, 'L'),
(5, 'XL'),
(6, 'XXL'),
(13, 'No aplica');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `tipoidentificacion`
--

DROP TABLE IF EXISTS `tipoidentificacion`;
CREATE TABLE IF NOT EXISTS `tipoidentificacion` (
  `idtipoIdentificacion` int(11) NOT NULL AUTO_INCREMENT,
  `nombreTipoIdentificacion` varchar(45) DEFAULT NULL,
  `inicialesTipoIdentificacion` varchar(45) DEFAULT NULL,
  PRIMARY KEY (`idtipoIdentificacion`)
) ENGINE=InnoDB AUTO_INCREMENT=8 DEFAULT CHARSET=utf8mb4;

--
-- Volcado de datos para la tabla `tipoidentificacion`
--

INSERT INTO `tipoidentificacion` (`idtipoIdentificacion`, `nombreTipoIdentificacion`, `inicialesTipoIdentificacion`) VALUES
(1, 'Registro Civil', 'RC'),
(2, 'Tarjeta de identidad', 'TI'),
(3, 'Cédula de ciudadanía', 'CC'),
(4, 'Cédula de extranjería', 'CE'),
(5, 'Pasaporte', 'PA');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `tiposangre`
--

DROP TABLE IF EXISTS `tiposangre`;
CREATE TABLE IF NOT EXISTS `tiposangre` (
  `idtipoSangre` int(11) NOT NULL AUTO_INCREMENT,
  `nombreTipoSangre` varchar(45) DEFAULT NULL,
  PRIMARY KEY (`idtipoSangre`)
) ENGINE=InnoDB AUTO_INCREMENT=10 DEFAULT CHARSET=utf8mb4;

--
-- Volcado de datos para la tabla `tiposangre`
--

INSERT INTO `tiposangre` (`idtipoSangre`, `nombreTipoSangre`) VALUES
(1, 'A+'),
(2, 'A-'),
(3, 'B+'),
(4, 'B-'),
(5, 'AB+'),
(6, 'AB-'),
(7, 'O+'),
(8, 'O-'),
(9, 'No Aplica');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `usuarioadministrador`
--

DROP TABLE IF EXISTS `usuarioadministrador`;
CREATE TABLE IF NOT EXISTS `usuarioadministrador` (
  `idusuarioAdministrador` int(11) NOT NULL AUTO_INCREMENT,
  `correoElectronico` varchar(45) DEFAULT NULL,
  `contraseña` varchar(45) DEFAULT NULL,
  PRIMARY KEY (`idusuarioAdministrador`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4;

--
-- Volcado de datos para la tabla `usuarioadministrador`
--

INSERT INTO `usuarioadministrador` (`idusuarioAdministrador`, `correoElectronico`, `contraseña`) VALUES
(1, 'ejemplo@ejemplo.com', '1234');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `usuarios`
--

DROP TABLE IF EXISTS `usuarios`;
CREATE TABLE IF NOT EXISTS `usuarios` (
  `idusuarios` int(11) NOT NULL AUTO_INCREMENT,
  `nombreUsuario` varchar(45) DEFAULT NULL,
  `apellidosUsuario` varchar(45) DEFAULT NULL,
  `distancias_iddistancias` int(11) NOT NULL,
  `categorias_idcategorias` int(11) NOT NULL,
  `correoElectronico` varchar(45) DEFAULT NULL,
  `tipoIdentificacion_idtipoIdentificacion` int(11) NOT NULL,
  `numeroIdentificacion` varchar(45) DEFAULT NULL,
  `fechaNacimiento` date DEFAULT NULL,
  `sexo_idsexo` int(11) NOT NULL,
  `telefono` varchar(45) DEFAULT NULL,
  `pais` varchar(45) DEFAULT NULL,
  `departamento` varchar(45) DEFAULT NULL,
  `ciudad` varchar(45) DEFAULT NULL,
  `tipoSangre_idtipoSangre` int(11) NOT NULL,
  `entidadSalud` varchar(45) DEFAULT NULL,
  `tallaCamisa_idtallaCamisa` int(11) NOT NULL,
  `contactoEmergenciaNombre` varchar(45) DEFAULT NULL,
  `contactoEmergenciaApellido` varchar(45) DEFAULT NULL,
  `estadoInscripcion_idestadoInscripcion` int(11) NOT NULL,
  `estadoKit_idestadoKit` int(11) NOT NULL,
  `equipos_idequipos` int(11) NOT NULL,
  `fechaRegistro` timestamp(2) NULL DEFAULT current_timestamp(2),
  PRIMARY KEY (`idusuarios`,`distancias_iddistancias`,`categorias_idcategorias`,`tipoIdentificacion_idtipoIdentificacion`,`sexo_idsexo`,`tipoSangre_idtipoSangre`,`tallaCamisa_idtallaCamisa`,`estadoInscripcion_idestadoInscripcion`,`estadoKit_idestadoKit`,`equipos_idequipos`),
  KEY `fk_usuarios_tipoIdentificacion_idx` (`tipoIdentificacion_idtipoIdentificacion`),
  KEY `fk_usuarios_categorias1_idx` (`categorias_idcategorias`),
  KEY `fk_usuarios_equipos1_idx` (`equipos_idequipos`),
  KEY `fk_usuarios_tipoSangre1_idx` (`tipoSangre_idtipoSangre`),
  KEY `fk_usuarios_distancias1_idx` (`distancias_iddistancias`),
  KEY `fk_usuarios_estadoInscripcion1_idx` (`estadoInscripcion_idestadoInscripcion`),
  KEY `fk_usuarios_tallaCamisa1_idx` (`tallaCamisa_idtallaCamisa`),
  KEY `fk_usuarios_sexo1_idx` (`sexo_idsexo`),
  KEY `fk_usuarios_estadoKit1_idx` (`estadoKit_idestadoKit`)
) ENGINE=InnoDB AUTO_INCREMENT=14 DEFAULT CHARSET=utf8mb4;

--
-- Volcado de datos para la tabla `usuarios`
--

INSERT INTO `usuarios` (`idusuarios`, `nombreUsuario`, `apellidosUsuario`, `distancias_iddistancias`, `categorias_idcategorias`, `correoElectronico`, `tipoIdentificacion_idtipoIdentificacion`, `numeroIdentificacion`, `fechaNacimiento`, `sexo_idsexo`, `telefono`, `pais`, `departamento`, `ciudad`, `tipoSangre_idtipoSangre`, `entidadSalud`, `tallaCamisa_idtallaCamisa`, `contactoEmergenciaNombre`, `contactoEmergenciaApellido`, `estadoInscripcion_idestadoInscripcion`, `estadoKit_idestadoKit`, `equipos_idequipos`, `fechaRegistro`) VALUES
(5, 'CArlos', 'Rubio', 2, 17, 'ejemplo@ejemplo.com', 2, '1234', '1998-02-05', 2, '3157873181', 'Colombia', 'Valle del cauca', 'Palmira', 2, 'Coomeva', 3, '', '', 1, 1, 26, '2021-02-05 19:38:05.08'),
(6, 'CArlos', 'Rubio', 3, 7, 'rubiogallegoc@gmail.com', 1, '12345', '2021-02-03', 2, '21212', 'Colombia', 'Valle del Cauca', 'Palmira', 2, 'Coomeva', 4, '', '', 1, 1, 26, '2021-02-10 00:46:02.79'),
(7, 'CArlos', 'Rubio', 3, 7, 'mairita_1313_@hotmail.com', 2, '21212', '2021-02-02', 2, '3157873181', 'Colombia', 'Valle del Cauca', 'Palmira', 2, 'Coomeva', 3, '', '', 1, 1, 3, '2021-02-10 02:18:50.74'),
(8, 'CArlos', 'rodrigeuz', 2, 5, 'ejemplo@ejemplo.com', 1, '4321', '2021-02-03', 2, '21212', 'Colombia', 'Valle del Cauca', 'Palmira', 1, 'Coomeva', 3, '', '', 1, 1, 26, '2021-02-10 18:44:09.50'),
(11, 'CArlos', 'Rubio', 4, 43, 'carlos.rubio@correounivalle.edu.co', 4, '123456789', '2021-02-02', 2, '3157873181', 'Colombia', 'Valle del Cauca', 'Palmira', 5, 'Coomeva', 4, '', '', 1, 1, 26, '2021-02-24 16:36:19.31'),
(12, 'CArlos', 'Rubio', 4, 43, 'carlos.rubio@correounivalle.edu.co', 4, '123456789', '2021-02-02', 2, '3157873181', 'Colombia', 'Valle del Cauca', 'Palmira', 5, 'Coomeva', 4, '', '', 1, 1, 26, '2021-02-24 16:37:43.24'),
(13, 'Estefania', 'Gallego', 3, 19, 'carlos.rubio@correounivalle.edu.cos', 3, '3496', '1996-03-03', 2, '3157873181', 'Colombia', 'Valle del Cauca', 'Palmira', 4, 'Coomeva', 4, '', '', 2, 1, 26, '2021-03-04 04:01:55.45');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `usuariosentreno`
--

DROP TABLE IF EXISTS `usuariosentreno`;
CREATE TABLE IF NOT EXISTS `usuariosentreno` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `nombre` varchar(64) NOT NULL,
  `apellidos` varchar(64) NOT NULL,
  `email` varchar(64) NOT NULL,
  `telefono` varchar(24) NOT NULL,
  `fecharegistro` datetime NOT NULL DEFAULT current_timestamp(),
  `estado` varchar(24) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=MyISAM AUTO_INCREMENT=17 DEFAULT CHARSET=utf8mb4;

--
-- Volcado de datos para la tabla `usuariosentreno`
--

INSERT INTO `usuariosentreno` (`id`, `nombre`, `apellidos`, `email`, `telefono`, `fecharegistro`, `estado`) VALUES
(1, 'CArlos', 'Rubio', 'ejemplo@ejemplo.com', '3157873181', '2021-02-16 00:00:00', 'Pendiente'),
(2, 'CArlos', 'Rubio', 'ejemplo@ejemplo.com', '3157873181', '2021-02-16 12:59:49', 'Pendiente'),
(3, 'CArlos', 'Rubio', 'ejemplo@ejemplo.com', '3157873181', '2021-02-16 13:00:10', 'Pendiente'),
(4, 'CArlos', 'Gonzaes', 'ejemplo@ejemplo.com', '3121212', '2021-02-16 13:00:27', 'Registrado'),
(5, 'CArlos', 'rodrigeuz', 'juan3.4@hotmail.com', '3157873181', '2021-02-16 13:02:29', 'Registrado'),
(6, 'CArlos', 'Rubio', 'ejemplo@ejemplo.com', '3157873181', '2021-02-17 10:28:20', 'Pendiente'),
(7, 'CArlos', 'Rubio', 'ejemplo@ejemplo.com', '3157873181', '2021-02-17 11:32:36', 'Registrado'),
(8, 'CArlos', 'Rubio', 'rubiogallegoc@gmail.com', '3157873181', '2021-03-02 09:43:09', 'Pendiente'),
(9, 'Jose', 'Lleras', 'juan3.4@hotmail.com', '3157873181', '2021-03-02 10:43:37', 'Registrado'),
(10, 'Jose', 'Lleras', 'juan3.4@hotmail.com', '3157873181', '2021-03-02 10:44:07', 'Registrado'),
(11, 'LAura', 'Peña', 'root@example.com', '3157873181', '2021-03-02 10:44:42', 'Pendiente'),
(12, 'Juan Manuel', 'Rubio Gallego ', 'juan3.4@hotmail.com', '3158293271', '2021-03-02 16:34:06', 'Registrado'),
(13, 'Jorge', 'Cardenas', 'uribe@paraco.com', '21212', '2021-03-02 22:39:53', 'Registrado'),
(14, 'Raul', 'Hernandez', 'raul@corre.com', '21212', '2021-03-03 12:21:19', 'Registrado'),
(15, 'Juan Manuel', 'Gonzaes', 'root@example.com', '3131', '2021-03-03 12:58:11', 'Pendiente'),
(16, 'edilia', 'Camacho', 'edilia@ejemplo.com', '3123131', '2021-03-03 22:58:42', 'Pendiente');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `usuarioskmvertical`
--

DROP TABLE IF EXISTS `usuarioskmvertical`;
CREATE TABLE IF NOT EXISTS `usuarioskmvertical` (
  `idusuarios` int(11) NOT NULL AUTO_INCREMENT,
  `nombreUsuario` varchar(45) DEFAULT NULL,
  `apellidosUsuario` varchar(45) DEFAULT NULL,
  `valorKmvertical` varchar(11) NOT NULL,
  `categorias_idcategorias` int(11) NOT NULL,
  `correoElectronico` varchar(45) DEFAULT NULL,
  `tipoIdentificacion_idtipoIdentificacion` int(11) NOT NULL,
  `numeroIdentificacion` varchar(45) DEFAULT NULL,
  `fechaNacimiento` date DEFAULT NULL,
  `sexo_idsexo` int(11) NOT NULL,
  `telefono` varchar(45) DEFAULT NULL,
  `ciudad` varchar(45) DEFAULT NULL,
  `tipoSangre_idtipoSangre` int(11) NOT NULL,
  `entidadSalud` varchar(45) DEFAULT NULL,
  `tallaCamisa_idtallaCamisa` int(11) NOT NULL,
  `contactoEmergenciaNombre` varchar(45) DEFAULT NULL,
  `contactoEmergenciaApellido` varchar(45) DEFAULT NULL,
  `estadoInscripcion_idestadoInscripcion` int(11) NOT NULL,
  `estadoKit_idestadoKit` int(11) NOT NULL,
  `equipos_idequipos` int(11) NOT NULL,
  `fechaRegistro` timestamp(2) NULL DEFAULT current_timestamp(2),
  PRIMARY KEY (`idusuarios`,`categorias_idcategorias`,`tipoIdentificacion_idtipoIdentificacion`,`sexo_idsexo`,`tipoSangre_idtipoSangre`,`tallaCamisa_idtallaCamisa`,`estadoInscripcion_idestadoInscripcion`,`estadoKit_idestadoKit`,`equipos_idequipos`) USING BTREE,
  KEY `fk_usuarios_tipoIdentificacion_idx` (`tipoIdentificacion_idtipoIdentificacion`),
  KEY `fk_usuarios_categorias1_idx` (`categorias_idcategorias`),
  KEY `fk_usuarios_equipos1_idx` (`equipos_idequipos`),
  KEY `fk_usuarios_tipoSangre1_idx` (`tipoSangre_idtipoSangre`),
  KEY `fk_usuarios_estadoInscripcion1_idx` (`estadoInscripcion_idestadoInscripcion`),
  KEY `fk_usuarios_tallaCamisa1_idx` (`tallaCamisa_idtallaCamisa`),
  KEY `fk_usuarios_sexo1_idx` (`sexo_idsexo`),
  KEY `fk_usuarios_estadoKit1_idx` (`estadoKit_idestadoKit`)
) ENGINE=InnoDB AUTO_INCREMENT=23 DEFAULT CHARSET=utf8mb4;

--
-- Volcado de datos para la tabla `usuarioskmvertical`
--

INSERT INTO `usuarioskmvertical` (`idusuarios`, `nombreUsuario`, `apellidosUsuario`, `valorKmvertical`, `categorias_idcategorias`, `correoElectronico`, `tipoIdentificacion_idtipoIdentificacion`, `numeroIdentificacion`, `fechaNacimiento`, `sexo_idsexo`, `telefono`, `ciudad`, `tipoSangre_idtipoSangre`, `entidadSalud`, `tallaCamisa_idtallaCamisa`, `contactoEmergenciaNombre`, `contactoEmergenciaApellido`, `estadoInscripcion_idestadoInscripcion`, `estadoKit_idestadoKit`, `equipos_idequipos`, `fechaRegistro`) VALUES
(5, 'CArlos', 'Rubio', '2', 17, 'ejemplo@ejemplo.com', 2, '1234', '1998-02-05', 2, '3157873181', 'Palmira', 2, 'Coomeva', 3, '', '', 1, 1, 26, '2021-02-05 19:38:05.08'),
(6, 'CArlos', 'Rubio', '3', 7, 'rubiogallegoc@gmail.com', 1, '12345', '2021-02-03', 2, '21212', 'Palmira', 2, 'Coomeva', 4, '', '', 1, 1, 26, '2021-02-10 00:46:02.79'),
(7, 'CArlos', 'Rubio', '3', 7, 'mairita_1313_@hotmail.com', 2, '21212', '2021-02-02', 2, '3157873181', 'Palmira', 2, 'Coomeva', 3, '', '', 1, 1, 3, '2021-02-10 02:18:50.74'),
(8, 'CArlos', 'rodrigeuz', '2', 5, 'ejemplo@ejemplo.com', 1, '4321', '2021-02-03', 2, '21212', 'Palmira', 1, 'Coomeva', 3, '', '', 1, 1, 26, '2021-02-10 18:44:09.50'),
(9, 'CArlos', 'Rubio', '5', 33, 'ejemplo@ejemplo.com', 1, '3496', '2021-02-02', 2, '3157873181', 'Palmira', 9, 'Coomeva', 13, '', '', 1, 1, 26, '2021-02-14 04:17:41.41'),
(10, 'CArlos', 'Rubio', '5', 33, 'ejemplo@ejemplo.com', 1, '3496', '2021-02-02', 2, '3157873181', 'Palmira', 9, 'Coomeva', 13, '', '', 1, 1, 26, '2021-02-14 04:19:19.80'),
(11, 'CArlos', 'Rubio', '5', 33, 'ejemplo@ejemplo.com', 2, '123456', '2021-02-09', 1, '3157873181', 'Palmira', 1, 'Coomeva', 13, '', '', 1, 1, 26, '2021-02-20 00:21:23.01'),
(12, 'CArlos', 'Rubio', '5', 33, 'ejemplo@ejemplo.com', 2, '123456', '2021-02-09', 1, '3157873181', 'Palmira', 1, 'Coomeva', 13, '', '', 1, 1, 26, '2021-02-20 00:23:10.42'),
(13, 'CArlos', 'Rubio', '5', 33, 'ejemplo@ejemplo.com', 2, '123456', '2021-02-09', 1, '3157873181', 'Palmira', 1, 'Coomeva', 13, '', '', 1, 1, 26, '2021-02-20 00:23:48.20'),
(14, 'CArlos', 'Rubio', '5', 33, 'rubiogallegoc@gmail.com', 2, '54321', '2021-02-04', 2, '3157873181', 'Palmira', 3, 'Coomeva', 13, '', '', 1, 1, 26, '2021-02-22 16:20:46.91'),
(15, 'Jose', 'Peña', '5', 33, 'carlos.rubio@correounivalle.edu.co', 2, '1234321', '2021-02-04', 1, '3157873181', 'Palmira', 4, 'Coomeva', 13, 'Carlos', '31212', 1, 1, 26, '2021-02-22 19:38:54.70'),
(16, 'LAura', 'San', '60000', 33, 'rubiogallegoc@gmail.com', 3, '1212', '2021-02-02', 1, '3157873181', 'Palmira', 3, 'Coomeva', 13, '', '', 1, 1, 26, '2021-02-22 20:05:32.99'),
(17, 'Carlos', 'Lleras', '60000', 33, 'carlos.rubio@correounivalle.edu.co', 3, '98765', '2021-02-01', 2, '212121', 'Cali', 3, 'Coomeva', 13, '', '', 1, 1, 26, '2021-02-22 20:42:25.14'),
(18, 'Jorge', 'CArdenas', '60000', 33, 'jorge@40.com', 3, '1233112', '2006-03-02', 2, '3157873181', 'Palmira', 3, 'Coomeva', 13, '', '', 1, 1, 26, '2021-03-03 17:56:57.88'),
(19, 'CArlos', 'Rubio', '60000', 33, 'ejemplo@ejemplo.com', 2, '123454321', '2021-03-01', 2, '3157873181', 'Palmira', 2, 'Coomeva', 13, '', '', 1, 1, 26, '2021-03-03 18:08:18.49'),
(20, 'CArlos', 'Peña', '60000', 33, 'rubiogallegoc@gmail.com', 2, '2233', '2009-03-03', 2, '3157873181', 'Palmira', 3, 'Coomeva', 13, '', '', 1, 1, 26, '2021-03-03 18:11:55.47'),
(21, 'LAura', 'Peña', '60000', 33, 'carlos.rubio@correounivalle.edu.co', 3, '123456', '2015-03-02', 1, '3157873181', 'Palmira', 5, 'Coomeva', 13, '', '', 1, 1, 26, '2021-03-03 19:35:23.76'),
(22, 'Carolina', 'Cepeda', '60000', 33, 'carol@gmail.com', 3, '9827', '2014-03-03', 2, '3157873181', 'Palmira', 7, 'Coomeva', 13, 'Carlos', '232323', 1, 1, 26, '2021-03-04 04:00:15.72');

--
-- Restricciones para tablas volcadas
--

--
-- Filtros para la tabla `usuarios`
--
ALTER TABLE `usuarios`
  ADD CONSTRAINT `fk_usuarios_categorias1` FOREIGN KEY (`categorias_idcategorias`) REFERENCES `categorias` (`idcategorias`) ON DELETE NO ACTION ON UPDATE NO ACTION,
  ADD CONSTRAINT `fk_usuarios_distancias1` FOREIGN KEY (`distancias_iddistancias`) REFERENCES `distancias` (`iddistancias`) ON DELETE NO ACTION ON UPDATE NO ACTION,
  ADD CONSTRAINT `fk_usuarios_equipos1` FOREIGN KEY (`equipos_idequipos`) REFERENCES `equipos` (`idequipos`) ON DELETE NO ACTION ON UPDATE NO ACTION,
  ADD CONSTRAINT `fk_usuarios_estadoInscripcion1` FOREIGN KEY (`estadoInscripcion_idestadoInscripcion`) REFERENCES `estadoinscripcion` (`idestadoInscripcion`) ON DELETE NO ACTION ON UPDATE NO ACTION,
  ADD CONSTRAINT `fk_usuarios_estadoKit1` FOREIGN KEY (`estadoKit_idestadoKit`) REFERENCES `estadokit` (`idestadoKit`) ON DELETE NO ACTION ON UPDATE NO ACTION,
  ADD CONSTRAINT `fk_usuarios_sexo1` FOREIGN KEY (`sexo_idsexo`) REFERENCES `sexo` (`idsexo`) ON DELETE NO ACTION ON UPDATE NO ACTION,
  ADD CONSTRAINT `fk_usuarios_tallaCamisa1` FOREIGN KEY (`tallaCamisa_idtallaCamisa`) REFERENCES `tallacamisa` (`idtallaCamisa`) ON DELETE NO ACTION ON UPDATE NO ACTION,
  ADD CONSTRAINT `fk_usuarios_tipoIdentificacion` FOREIGN KEY (`tipoIdentificacion_idtipoIdentificacion`) REFERENCES `tipoidentificacion` (`idtipoIdentificacion`) ON DELETE NO ACTION ON UPDATE NO ACTION,
  ADD CONSTRAINT `fk_usuarios_tipoSangre1` FOREIGN KEY (`tipoSangre_idtipoSangre`) REFERENCES `tiposangre` (`idtipoSangre`) ON DELETE NO ACTION ON UPDATE NO ACTION;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;

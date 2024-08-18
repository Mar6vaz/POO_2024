-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Servidor: 127.0.0.1
-- Tiempo de generación: 18-08-2024 a las 05:15:52
-- Versión del servidor: 10.4.32-MariaDB
-- Versión de PHP: 8.1.25

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Base de datos: `agencia_service`
--

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `agencias`
--

CREATE TABLE `agencias` (
  `id` int(11) NOT NULL,
  `nombre` varchar(100) NOT NULL,
  `direccion` varchar(100) DEFAULT NULL,
  `telefono` varchar(30) DEFAULT NULL,
  `descripcion` varchar(500) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `agencias`
--

INSERT INTO `agencias` (`id`, `nombre`, `direccion`, `telefono`, `descripcion`) VALUES
(1, 'Agencia Bienestar y Salud', 'Av. Principal 123, Ciudad', '555-0001', 'Atención médica gratuita, prótesis dentales.'),
(2, 'Fundación Futuro Brillante', 'Calle Secundaria 456, Ciudad', '555-0002', 'Becas para estudiantes, orientación y apoyo educativo.'),
(3, 'Centro de Apoyo Comunitario', 'Plaza Central 789, Ciudad', '555-0003', 'Despensas de comida, apoyo para necesidades básicas.'),
(4, 'Red de Construcción Solidaria', 'Avenida Norte 101, Ciudad', '555-0004', 'Préstamos económicos para la construcción de casas, asesoría en proyectos habitacionales.'),
(5, 'Centro Infantil \"Manitas Felices\"', 'Calle Este 202, Ciudad', '555-0005', 'Guardería gratuita, actividades educativas, cuidado infantil, desarrollo social y emocional, apoyo a padres trabajadores.');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `citas`
--

CREATE TABLE `citas` (
  `id` int(11) NOT NULL,
  `cliente_id` int(11) DEFAULT NULL,
  `solicitud_id` int(11) DEFAULT NULL,
  `empleado_id` int(11) DEFAULT NULL,
  `fecha_cita` datetime DEFAULT NULL,
  `estado` enum('Pendiente','Confirmada','Cancelada') DEFAULT 'Pendiente'
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `clientes`
--

CREATE TABLE `clientes` (
  `id` int(11) NOT NULL,
  `nombre` varchar(100) NOT NULL,
  `apellidos` varchar(100) DEFAULT NULL,
  `edad` int(11) DEFAULT NULL,
  `tel` varchar(15) DEFAULT NULL,
  `direccion` text DEFAULT NULL,
  `email` varchar(100) DEFAULT NULL,
  `password` varchar(64) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `clientes`
--

INSERT INTO `clientes` (`id`, `nombre`, `apellidos`, `edad`, `tel`, `direccion`, `email`, `password`) VALUES
(1, 'Mahori', 'Ontiveros Reyes', 18, '346575685', 'Calle Las Puchainas #678', 'mahori@gmail.com', '994f13cca57f1fe96183c1acbc2f0c19fd8180b43ee8a91c676985aadda25ad0'),
(7, 'mangarito', 'firulais', 45, '324\'9834\'2', 'Colonia', 'firu@gmaill.com', '854bec665eedf95f3972fe589fbc5d070f00870a45b2c73e296c8d47f88642eb'),
(13, 'Ami ', 'Ontiveros', 23, '5645', 'Jorge Rivero', 'ami@gmail.com', '7796d0a5eba5978b880f6c8362fe031cae224b20e917c44e70772ea522ee3ea5'),
(14, 'Guffy', 'Carre Anjir', 34, '65745835', 'Por las orillas del mar', 'guffy@gmail.com', 'a1bf67aab0100316f0698d36943999dc22a5608ccf72f7fa11aa6d52828dc3fb');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `empleados`
--

CREATE TABLE `empleados` (
  `id` int(11) NOT NULL,
  `nombre` varchar(100) NOT NULL,
  `apellidos` varchar(100) DEFAULT NULL,
  `edad` int(11) DEFAULT NULL,
  `fecha_nacimiento` date DEFAULT NULL,
  `telefono` varchar(30) DEFAULT NULL,
  `email` varchar(100) DEFAULT NULL,
  `password` varchar(64) DEFAULT NULL,
  `puesto` varchar(50) DEFAULT NULL,
  `titulo` varchar(200) DEFAULT NULL,
  `salario` decimal(10,2) DEFAULT NULL,
  `agencia_id` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `empleados`
--

INSERT INTO `empleados` (`id`, `nombre`, `apellidos`, `edad`, `fecha_nacimiento`, `telefono`, `email`, `password`, `puesto`, `titulo`, `salario`, `agencia_id`) VALUES
(1, 'Laura', 'Gómez Martiínez', 35, '1988-07-15', '55-1234', 'laura@gmail.com', '5a797e04dd084f9e9502d0e0e54d0a0996bc9d13e14fbf1613425a8bb4b448ce', 'Dentista', 'Licenciada en Odontología', 3000.00, 1),
(2, 'Pedro', 'Fernández Ruiz', 40, '1983-11-22', '55-5678', 'pedro@gmail.com', '2702cb34ee041711b9df0c67a8d5c9de02110c80e3fc966ba8341456dbc9ef2b', 'Higienista Dental', 'Técnico en Higiene Dental', 2500.00, 1),
(3, 'Ana', 'López García', 30, '1993-05-03', '555-8765', 'ana@gmail.com', 'e82827b00b2ca8620beb37f879778c082b292a52270390cff35b6fe3157f4e8b', 'Coordinadora de Despensas', 'Licenciada en Trabajo Social', 2800.00, 2),
(4, 'Luis', 'Hernandez Flores', 16, '2024-12-06', '555-8987', 'luis@gmail.com', 'ec7908dc8241f0e4340266990dfe6001b1757084d891c6758bfaac826750009a', 'Auxiliar en Logistica', 'Licenciado en Logistica', 2000000.00, 2),
(5, 'Mariana', 'Reyes Silva', 32, '1991-08-25', '555-1122', 'mariana@gmail.com', 'daf6669f00f3e4a88c264cf0de5928f81b42bcd292e3ca6737757ed32d996f98', 'Coordinadora de Becas', 'Licenciada en Educación', 2900.00, 3),
(6, 'Javier', 'Morales Soto', 36, '1987-09-10', '555-3344', 'javier@gmail.com', '26ce13833bf9b1a34904d0b8ff10bc035178931c4ac6d8d02cc2274c6d20a09c', 'Asistente Administrativo', 'Técnico en Adminictración', 2400.00, 3),
(7, 'Beatriz', 'Sánchez López', 38, '1985-04-20', '555-5566', 'beatriz@gmail.com', '8499726e178ed90033984cf18145e1f554095358fe52b305139fbcad1ce11492', 'Supervisor de Proyectos Habitacionales', 'Civil Especialista en Vivienda Social', 3400.00, 4),
(8, 'Dagoberto', 'Diaz Mendoza', 45, '1978-06-30', '555-3049', 'dago@gmail.com', 'a3e61c7c850e42866314b5375825742cfd5dcd0d87fb6f8e671f2c1ab8a2737f', 'Coordinador de Asesoría ', 'Arquitecto Asesor en Construcción', 2700.00, 4),
(9, 'Carla', 'Morales Ruiz', 35, '1995-07-22', '555-44499', 'carla@gmail.com', 'e408145e7fc3f031d5aa3b08710d0eddabf61cb11864822af9b16b92c0c9c576', 'Educadora Infantil', 'Licenciada en Educación Infantil', 2300.00, 5),
(10, 'Fernando', 'Ortega Perez', 33, '1990-11-10', '555-5566', 'fernando@gmail.com', '873278545c8226be2de9b3b53e593cb8c3ab4eaf6e2615d77fec6d5d9d53dc48', 'Asistente en Cuidado Infantil', 'Técnico en Educación Infantil', 2000.00, 5);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `servicios`
--

CREATE TABLE `servicios` (
  `id` int(11) NOT NULL,
  `nombre` varchar(100) NOT NULL,
  `descripcion` varchar(255) DEFAULT NULL,
  `empleado_id` int(11) DEFAULT NULL,
  `agencia_id` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `servicios`
--

INSERT INTO `servicios` (`id`, `nombre`, `descripcion`, `empleado_id`, `agencia_id`) VALUES
(23, 'Consulta Dental Gratuita', 'Evaluación y diagnóstico dental sin costo para pacientes.', 1, 1),
(24, 'Asesoría Nutricional Gratuita', 'Consultas sobre dieta y nutrición para mejorar la salud.', 2, 1),
(25, 'Programa de Vacunas Infantiles', 'Vacunación gratuita para niños en edad escolar.', 1, 1),
(26, 'Despensa de Alimentos', 'Entrega gratuita de despensas a familias necesitadas.', 3, 2),
(27, 'Programa de Becas Universitarias', 'Becas completas para estudiantes de bajos recursos.', 4, 2),
(28, 'Apoyo Escolar Gratuito', 'Tutores y materiales educativos sin costo para estudiantes.', 3, 2),
(29, 'Préstamos para Construcción', 'Préstamos sin interés para la construcción de vivienda.', 6, 3),
(30, 'Evaluación de Propiedades', 'Evaluación gratuita de propiedades para determinar su valor', 5, 3),
(31, 'Guardería para hijos de Trabajadores', 'Atención y cuidado de padres que trabajan en la maquila.', 7, 5),
(32, 'Actividades Educativas y Recreativas', 'Actividades dirigidas para el desarrollo educativo y recreativo de los niños.', 7, 5),
(33, 'Apoyo Psicológico Infantil', 'Sesiones gratuitas de apoyo psicológico para niños.', 7, 5);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `solicitudes`
--

CREATE TABLE `solicitudes` (
  `id` int(11) NOT NULL,
  `servicio_id` int(11) DEFAULT NULL,
  `empleado_id` int(11) DEFAULT NULL,
  `cliente_id` int(11) DEFAULT NULL,
  `agencia_id` int(11) DEFAULT NULL,
  `fecha_solicitud` datetime DEFAULT NULL,
  `estado` enum('Pendiente','Aprobada','Rechazada') DEFAULT 'Pendiente',
  `documentos` text DEFAULT NULL,
  `comentarios` text DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `solicitudes`
--

INSERT INTO `solicitudes` (`id`, `servicio_id`, `empleado_id`, `cliente_id`, `agencia_id`, `fecha_solicitud`, `estado`, `documentos`, `comentarios`) VALUES
(2, 23, 1, 13, 1, '2024-08-17 18:56:13', 'Pendiente', 'kesote.pdf', 'AYUDA YA ME CANSÉ'),
(3, 23, 1, 1, 1, '2024-08-17 21:05:24', 'Pendiente', 'zoro.pdf', 'SE LOGRO GENTEEEE, ANIMO QUE SI SE PUEDE'),
(4, 28, 3, 13, 2, '2024-08-17 21:14:49', 'Pendiente', 'michelada.pdf', 'LOGRÉ HACERLOOOO, ME SIENTO HAPPY');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `usuarios`
--

CREATE TABLE `usuarios` (
  `id` int(11) NOT NULL,
  `username` varchar(50) NOT NULL,
  `password` varchar(50) NOT NULL,
  `tipo` enum('cliente','empleado') NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1 COLLATE=latin1_swedish_ci;

--
-- Índices para tablas volcadas
--

--
-- Indices de la tabla `agencias`
--
ALTER TABLE `agencias`
  ADD PRIMARY KEY (`id`);

--
-- Indices de la tabla `citas`
--
ALTER TABLE `citas`
  ADD PRIMARY KEY (`id`),
  ADD KEY `cliente_id` (`cliente_id`),
  ADD KEY `solicitud_id` (`solicitud_id`),
  ADD KEY `empleado_id` (`empleado_id`);

--
-- Indices de la tabla `clientes`
--
ALTER TABLE `clientes`
  ADD PRIMARY KEY (`id`);

--
-- Indices de la tabla `empleados`
--
ALTER TABLE `empleados`
  ADD PRIMARY KEY (`id`),
  ADD KEY `agencia_id` (`agencia_id`);

--
-- Indices de la tabla `servicios`
--
ALTER TABLE `servicios`
  ADD PRIMARY KEY (`id`),
  ADD KEY `empleado_id` (`empleado_id`),
  ADD KEY `agencia_id` (`agencia_id`);

--
-- Indices de la tabla `solicitudes`
--
ALTER TABLE `solicitudes`
  ADD PRIMARY KEY (`id`),
  ADD KEY `servicio_id` (`servicio_id`),
  ADD KEY `empleado_id` (`empleado_id`),
  ADD KEY `cliente_id` (`cliente_id`),
  ADD KEY `agencia_id` (`agencia_id`);

--
-- Indices de la tabla `usuarios`
--
ALTER TABLE `usuarios`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `username` (`username`);

--
-- AUTO_INCREMENT de las tablas volcadas
--

--
-- AUTO_INCREMENT de la tabla `agencias`
--
ALTER TABLE `agencias`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=6;

--
-- AUTO_INCREMENT de la tabla `citas`
--
ALTER TABLE `citas`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de la tabla `clientes`
--
ALTER TABLE `clientes`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=15;

--
-- AUTO_INCREMENT de la tabla `empleados`
--
ALTER TABLE `empleados`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=11;

--
-- AUTO_INCREMENT de la tabla `servicios`
--
ALTER TABLE `servicios`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=34;

--
-- AUTO_INCREMENT de la tabla `solicitudes`
--
ALTER TABLE `solicitudes`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;

--
-- AUTO_INCREMENT de la tabla `usuarios`
--
ALTER TABLE `usuarios`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- Restricciones para tablas volcadas
--

--
-- Filtros para la tabla `citas`
--
ALTER TABLE `citas`
  ADD CONSTRAINT `citas_ibfk_1` FOREIGN KEY (`cliente_id`) REFERENCES `clientes` (`id`),
  ADD CONSTRAINT `citas_ibfk_2` FOREIGN KEY (`solicitud_id`) REFERENCES `solicitudes` (`id`),
  ADD CONSTRAINT `citas_ibfk_3` FOREIGN KEY (`empleado_id`) REFERENCES `empleados` (`id`);

--
-- Filtros para la tabla `empleados`
--
ALTER TABLE `empleados`
  ADD CONSTRAINT `empleados_ibfk_1` FOREIGN KEY (`agencia_id`) REFERENCES `agencias` (`id`);

--
-- Filtros para la tabla `servicios`
--
ALTER TABLE `servicios`
  ADD CONSTRAINT `servicios_ibfk_1` FOREIGN KEY (`empleado_id`) REFERENCES `empleados` (`id`),
  ADD CONSTRAINT `servicios_ibfk_2` FOREIGN KEY (`agencia_id`) REFERENCES `agencias` (`id`);

--
-- Filtros para la tabla `solicitudes`
--
ALTER TABLE `solicitudes`
  ADD CONSTRAINT `solicitudes_ibfk_1` FOREIGN KEY (`servicio_id`) REFERENCES `servicios` (`id`),
  ADD CONSTRAINT `solicitudes_ibfk_2` FOREIGN KEY (`empleado_id`) REFERENCES `empleados` (`id`),
  ADD CONSTRAINT `solicitudes_ibfk_3` FOREIGN KEY (`cliente_id`) REFERENCES `clientes` (`id`),
  ADD CONSTRAINT `solicitudes_ibfk_4` FOREIGN KEY (`agencia_id`) REFERENCES `agencias` (`id`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;

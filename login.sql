-- MySQL dump 10.13  Distrib 8.0.25, for Linux (x86_64)
--
-- Host: localhost    Database: lifechoices_login
-- ------------------------------------------------------
-- Server version	8.0.25-0ubuntu0.20.04.1

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8mb4 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `kin`
--

DROP TABLE IF EXISTS `kin`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `kin` (
  `position` int NOT NULL AUTO_INCREMENT,
  `username` varchar(30) DEFAULT NULL,
  `kin_name` varchar(30) NOT NULL,
  `phone_number` varchar(30) NOT NULL,
  PRIMARY KEY (`position`),
  KEY `username` (`username`),
  CONSTRAINT `kin_ibfk_1` FOREIGN KEY (`username`) REFERENCES `users` (`id_number`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `kin`
--

LOCK TABLES `kin` WRITE;
/*!40000 ALTER TABLE `kin` DISABLE KEYS */;
INSERT INTO `kin` VALUES (1,'9856321478965','Julias','25896478523');
/*!40000 ALTER TABLE `kin` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `log_times`
--

DROP TABLE IF EXISTS `log_times`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `log_times` (
  `id` int NOT NULL AUTO_INCREMENT,
  `id_number` varchar(13) NOT NULL,
  `sign_in_time` varchar(40) NOT NULL,
  `sign_in_date` varchar(30) NOT NULL,
  `sign_out_time` varchar(30) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `id_number` (`id_number`),
  CONSTRAINT `log_times_ibfk_1` FOREIGN KEY (`id_number`) REFERENCES `users` (`id_number`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `log_times`
--

LOCK TABLES `log_times` WRITE;
/*!40000 ALTER TABLE `log_times` DISABLE KEYS */;
INSERT INTO `log_times` VALUES (1,'9903105047084','18:19:35','21-07-10',NULL),(2,'9856324789541','18:20:02','21-07-10','18:20:04'),(3,'9903105478805','18:22:08','21-07-10',NULL),(4,'9856321478965','18:22:31','21-07-10','18:22:32');
/*!40000 ALTER TABLE `log_times` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `users`
--

DROP TABLE IF EXISTS `users`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `users` (
  `id_number` varchar(13) NOT NULL,
  `username` varchar(30) NOT NULL,
  `surname` varchar(30) NOT NULL,
  `phone` varchar(11) NOT NULL,
  `password` varchar(30) NOT NULL,
  `privilege` varchar(30) NOT NULL,
  PRIMARY KEY (`id_number`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `users`
--

LOCK TABLES `users` WRITE;
/*!40000 ALTER TABLE `users` DISABLE KEYS */;
INSERT INTO `users` VALUES ('9856321478965','Jaco','Zuma','27856984236','heyhey','Visitor'),('9856324789541','Adele','Carmac','27756897412','hrrep','Staff'),('9903105047084','Tashwill','Andries','2772158689','goku','Student'),('9903105478805','Jason','Wandrag','27785671235','firebender','Lecturer');
/*!40000 ALTER TABLE `users` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2021-07-10 18:23:33

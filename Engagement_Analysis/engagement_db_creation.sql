-- MySQL dump 10.13  Distrib 8.0.34, for Win64 (x86_64)
--
-- Host: localhost    Database: engagement
-- ------------------------------------------------------
-- Server version	8.0.34

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `posts`
--

DROP TABLE IF EXISTS `posts`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `posts` (
  `post_id` int NOT NULL,
  `post_content` text,
  `post_date` datetime DEFAULT NULL,
  PRIMARY KEY (`post_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `posts`
--

LOCK TABLES `posts` WRITE;
/*!40000 ALTER TABLE `posts` DISABLE KEYS */;
INSERT INTO `posts` VALUES (1,'Current growth of Data Science','2023-08-25 10:00:00'),(2,'Exploring the beauty of nature...','2023-08-26 15:30:00'),(3,'Unveiling the latest tech trends...','2023-08-27 12:00:00'),(4,'Journey into the world of literature...','2023-08-28 09:45:00'),(5,'Capturing the essence of city life...','2023-08-29 16:20:00');
/*!40000 ALTER TABLE `posts` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `userreactions`
--

DROP TABLE IF EXISTS `userreactions`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `userreactions` (
  `reaction_id` int NOT NULL,
  `user_id` int DEFAULT NULL,
  `post_id` int DEFAULT NULL,
  `reaction_type` enum('like','comment','share') DEFAULT NULL,
  `reaction_date` datetime DEFAULT NULL,
  PRIMARY KEY (`reaction_id`),
  KEY `post_id` (`post_id`),
  CONSTRAINT `userreactions_ibfk_1` FOREIGN KEY (`post_id`) REFERENCES `posts` (`post_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `userreactions`
--

LOCK TABLES `userreactions` WRITE;
/*!40000 ALTER TABLE `userreactions` DISABLE KEYS */;
INSERT INTO `userreactions` VALUES (1,101,1,'like','2023-08-25 10:15:00'),(2,102,1,'comment','2023-08-25 11:30:00'),(3,103,1,'share','2023-08-26 12:45:00'),(4,101,2,'like','2023-08-26 15:45:00'),(5,102,2,'comment','2023-08-27 09:20:00'),(6,104,2,'like','2023-08-27 10:00:00'),(7,105,3,'comment','2023-08-27 14:30:00'),(8,101,3,'like','2023-08-28 08:15:00'),(9,103,4,'like','2023-08-28 10:30:00'),(10,105,4,'share','2023-08-29 11:15:00'),(11,104,5,'like','2023-08-29 16:30:00'),(12,101,5,'comment','2023-08-30 09:45:00');
/*!40000 ALTER TABLE `userreactions` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Dumping events for database 'engagement'
--

--
-- Dumping routines for database 'engagement'
--
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2023-09-24 20:45:47

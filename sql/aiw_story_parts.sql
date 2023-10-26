-- MySQL dump 10.13  Distrib 8.0.34, for Win64 (x86_64)
--
-- Host: localhost    Database: aiw
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
-- Table structure for table `story_parts`
--

DROP TABLE IF EXISTS `story_parts`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `story_parts` (
  `id` int NOT NULL AUTO_INCREMENT,
  `writing_project_id` int NOT NULL,
  `parent_id` int DEFAULT NULL,
  `part_type` enum('TEXT','COLLECTION','IMAGE','IMAGEREF') NOT NULL,
  `title` varchar(120) NOT NULL,
  `summary` text,
  `content` text,
  `created` timestamp NULL DEFAULT NULL,
  `created_by_id` int DEFAULT NULL,
  `modified` timestamp NULL DEFAULT NULL,
  `modified_by_id` int DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `created_by_id` (`created_by_id`),
  KEY `modified_by_id` (`modified_by_id`),
  KEY `parent_id` (`parent_id`),
  KEY `writing_project_id` (`writing_project_id`),
  CONSTRAINT `story_parts_ibfk_1` FOREIGN KEY (`created_by_id`) REFERENCES `users` (`id`),
  CONSTRAINT `story_parts_ibfk_2` FOREIGN KEY (`modified_by_id`) REFERENCES `users` (`id`),
  CONSTRAINT `story_parts_ibfk_3` FOREIGN KEY (`parent_id`) REFERENCES `story_parts` (`id`),
  CONSTRAINT `story_parts_ibfk_4` FOREIGN KEY (`writing_project_id`) REFERENCES `writing_projects` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `story_parts`
--

LOCK TABLES `story_parts` WRITE;
/*!40000 ALTER TABLE `story_parts` DISABLE KEYS */;
/*!40000 ALTER TABLE `story_parts` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2023-10-26  7:35:29

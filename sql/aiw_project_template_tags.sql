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
-- Table structure for table `project_template_tags`
--

DROP TABLE IF EXISTS `project_template_tags`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `project_template_tags` (
  `project_template_id` int NOT NULL,
  `tag_id` int NOT NULL,
  PRIMARY KEY (`project_template_id`,`tag_id`),
  KEY `tag_id` (`tag_id`),
  CONSTRAINT `project_template_tags_ibfk_1` FOREIGN KEY (`project_template_id`) REFERENCES `project_template` (`id`),
  CONSTRAINT `project_template_tags_ibfk_2` FOREIGN KEY (`tag_id`) REFERENCES `tag` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `project_template_tags`
--

LOCK TABLES `project_template_tags` WRITE;
/*!40000 ALTER TABLE `project_template_tags` DISABLE KEYS */;
INSERT INTO `project_template_tags` VALUES (5,1),(6,1),(7,1),(8,1),(9,1),(21,1),(22,1),(10,2),(11,2),(12,2),(13,2),(14,2),(15,2),(16,2),(17,2),(45,2),(10,3),(11,3),(12,3),(13,3),(14,3),(15,3),(16,3),(17,3),(18,4),(19,4),(20,4),(18,5),(19,5),(20,5),(20,6),(20,7),(21,8),(22,8),(23,8),(24,8),(27,8),(32,8),(33,8),(21,9),(22,9),(25,9),(26,9),(27,9),(23,10),(42,10),(44,10),(24,11),(25,11),(26,11),(27,11),(28,11),(29,11),(30,11),(31,11),(32,11),(33,11),(34,11),(35,11),(36,11),(37,11),(38,11),(39,11),(40,11),(41,11),(43,11),(25,12),(26,12),(25,13),(26,13),(27,13),(28,13),(28,14),(34,14),(35,14),(36,14),(33,15),(37,15),(37,16),(38,17),(39,17),(40,17),(41,17);
/*!40000 ALTER TABLE `project_template_tags` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2023-10-24 17:38:53
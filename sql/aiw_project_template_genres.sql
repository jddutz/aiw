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
-- Table structure for table `project_template_genres`
--

DROP TABLE IF EXISTS `project_template_genres`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `project_template_genres` (
  `project_template_id` int NOT NULL,
  `genre_id` int NOT NULL,
  PRIMARY KEY (`project_template_id`,`genre_id`),
  KEY `genre_id` (`genre_id`),
  CONSTRAINT `project_template_genres_ibfk_1` FOREIGN KEY (`genre_id`) REFERENCES `genre` (`id`),
  CONSTRAINT `project_template_genres_ibfk_2` FOREIGN KEY (`project_template_id`) REFERENCES `project_template` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `project_template_genres`
--

LOCK TABLES `project_template_genres` WRITE;
/*!40000 ALTER TABLE `project_template_genres` DISABLE KEYS */;
INSERT INTO `project_template_genres` VALUES (5,1),(6,1),(7,1),(21,1),(5,2),(6,2),(9,2),(19,2),(20,2),(21,2),(5,3),(6,3),(7,3),(9,3),(12,3),(15,3),(18,3),(19,3),(20,3),(21,3),(5,4),(6,4),(7,4),(8,4),(9,4),(10,4),(11,4),(13,4),(14,4),(15,4),(18,4),(20,4),(21,4),(5,5),(7,5),(9,5),(18,5),(19,5),(21,5),(5,6),(6,6),(19,6),(21,6),(5,7),(6,7),(7,7),(9,7),(10,7),(11,7),(12,7),(15,7),(18,7),(19,7),(20,7),(21,7),(5,8),(6,8),(7,8),(9,8),(21,8),(5,9),(6,9),(7,9),(9,9),(10,9),(11,9),(12,9),(13,9),(14,9),(21,9),(5,10),(7,10),(9,10),(10,10),(11,10),(12,10),(13,10),(14,10),(21,10),(6,11),(6,12),(8,12),(9,12),(12,12),(18,12),(19,12),(21,12),(6,13),(22,13),(6,14),(11,14),(6,15),(6,16),(6,17),(7,18),(10,18),(11,18),(12,18),(13,18),(14,18),(15,18),(18,18),(7,19),(8,19),(9,19),(10,19),(11,19),(13,19),(14,19),(15,19),(16,19),(18,19),(20,19),(8,20),(19,20),(8,21),(8,22),(8,23),(8,24),(8,25),(8,26),(8,27),(10,28),(10,29),(11,29),(10,30),(11,30),(10,31),(11,31),(12,32),(12,33),(13,33),(14,33),(12,34),(45,34),(12,35),(13,36),(14,36),(13,37),(14,37),(17,37),(13,38),(13,39),(14,40),(14,41),(15,42),(15,43),(15,44),(15,45),(15,46),(16,47),(16,48),(16,49),(16,50),(16,51),(16,52),(16,53),(17,53),(45,53),(16,54),(26,54),(16,55),(17,56),(17,57),(17,58),(17,59),(17,60),(17,61),(17,62),(17,63),(18,64),(20,64),(18,65),(18,66),(21,66),(19,67),(22,67),(19,68),(19,69),(43,69),(20,70),(22,70),(20,71),(22,71),(20,72),(22,72),(20,73),(21,74),(22,75),(22,76),(22,77),(22,78),(22,79),(22,80),(22,81),(23,82),(23,83),(43,83),(23,84),(23,85),(23,86),(23,87),(23,88),(23,89),(23,90),(23,91),(24,92),(25,93),(25,94),(25,95),(25,96),(25,97),(25,98),(25,99),(25,100),(25,101),(25,102),(26,103),(26,104),(26,105),(26,106),(26,107),(26,108),(26,109),(26,110),(26,111),(27,112),(27,113),(27,114),(27,115),(27,116),(27,117),(27,118),(27,119),(27,120),(27,121),(28,122),(28,123),(28,124),(28,125),(28,126),(28,127),(28,128),(28,129),(28,130),(28,131),(29,132),(29,133),(29,134),(29,135),(29,136),(29,137),(29,138),(29,139),(29,140),(29,141),(30,142),(30,143),(30,144),(30,145),(30,146),(30,147),(30,148),(30,149),(30,150),(30,151),(31,152),(31,153),(31,154),(31,155),(31,156),(31,157),(31,158),(31,159),(31,160),(31,161),(32,162),(32,163),(32,164),(32,165),(32,166),(32,167),(32,168),(32,169),(32,170),(32,171),(33,172),(33,173),(33,174),(33,175),(33,176),(33,177),(33,178),(33,179),(33,180),(33,181),(34,182),(34,183),(34,184),(34,185),(34,186),(36,186),(34,187),(34,188),(34,189),(34,190),(34,191),(35,192),(35,193),(35,194),(35,195),(35,196),(35,197),(35,198),(35,199),(35,200),(35,201),(36,202),(36,203),(36,204),(36,205),(36,206),(36,207),(36,208),(36,209),(36,210),(37,211),(37,212),(39,212),(37,213),(37,214),(37,215),(37,216),(39,216),(37,217),(37,218),(37,219),(37,220),(38,221),(38,222),(38,223),(38,224),(38,225),(38,226),(38,227),(38,228),(38,229),(38,230),(39,231),(39,232),(39,233),(39,234),(39,235),(39,236),(39,237),(39,238),(40,239),(40,240),(40,241),(40,242),(40,243),(40,244),(40,245),(40,246),(40,247),(40,248),(41,249),(41,250),(41,251),(41,252),(41,253),(41,254),(41,255),(41,256),(41,257),(41,258),(42,259),(42,260),(42,261),(42,262),(42,263),(42,264),(42,265),(42,266),(42,267),(42,268),(43,269),(43,270),(43,271),(43,272),(43,273),(43,274),(43,275),(43,276),(44,277),(44,278),(44,279),(44,280),(44,281),(44,282),(44,283),(44,284),(44,285),(44,286),(45,287),(45,288),(45,289),(45,290),(45,291),(45,292),(45,293),(45,294);
/*!40000 ALTER TABLE `project_template_genres` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2023-10-24 17:38:52

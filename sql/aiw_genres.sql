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
-- Table structure for table `genres`
--

DROP TABLE IF EXISTS `genres`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `genres` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  `description` text NOT NULL,
  `imageref` varchar(255) DEFAULT NULL,
  `created` timestamp NULL DEFAULT NULL,
  `created_by_id` int DEFAULT NULL,
  `modified` timestamp NULL DEFAULT NULL,
  `modified_by_id` int DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `ix_genres_name` (`name`),
  KEY `created_by_id` (`created_by_id`),
  KEY `modified_by_id` (`modified_by_id`),
  CONSTRAINT `genres_ibfk_1` FOREIGN KEY (`created_by_id`) REFERENCES `users` (`id`),
  CONSTRAINT `genres_ibfk_2` FOREIGN KEY (`modified_by_id`) REFERENCES `users` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=295 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `genres`
--

LOCK TABLES `genres` WRITE;
/*!40000 ALTER TABLE `genres` DISABLE KEYS */;
INSERT INTO `genres` VALUES (1,'Literary Fiction','Literary Fiction',NULL,'2023-10-26 13:04:50',NULL,'2023-10-26 13:05:30',NULL),(2,'Mystery/Thriller','Mystery/Thriller',NULL,'2023-10-26 13:04:50',NULL,'2023-10-26 13:05:30',NULL),(3,'Science Fiction','Science Fiction',NULL,'2023-10-26 13:04:50',NULL,'2023-10-26 13:05:30',NULL),(4,'Fantasy','Fantasy',NULL,'2023-10-26 13:04:50',NULL,'2023-10-26 13:05:30',NULL),(5,'Romance','Romance',NULL,'2023-10-26 13:04:50',NULL,'2023-10-26 13:05:30',NULL),(6,'Historical Fiction','Historical Fiction',NULL,'2023-10-26 13:04:50',NULL,'2023-10-26 13:05:30',NULL),(7,'Horror','Horror',NULL,'2023-10-26 13:04:50',NULL,'2023-10-26 13:05:30',NULL),(8,'Speculative Fiction','Speculative Fiction',NULL,'2023-10-26 13:04:50',NULL,'2023-10-26 13:05:30',NULL),(9,'Drama','Drama',NULL,'2023-10-26 13:04:50',NULL,'2023-10-26 13:05:30',NULL),(10,'Comedy','Comedy',NULL,'2023-10-26 13:04:50',NULL,'2023-10-26 13:05:30',NULL),(11,'Romantic Fiction','Romantic Fiction',NULL,'2023-10-26 13:04:50',NULL,'2023-10-26 13:05:30',NULL),(12,'Adventure','Adventure',NULL,'2023-10-26 13:04:50',NULL,'2023-10-26 13:05:30',NULL),(13,'Dystopian','Dystopian',NULL,'2023-10-26 13:04:50',NULL,'2023-10-26 13:05:30',NULL),(14,'Crime','Crime',NULL,'2023-10-26 13:04:50',NULL,'2023-10-26 13:05:30',NULL),(15,'Young Adult','Young Adult',NULL,'2023-10-26 13:04:50',NULL,'2023-10-26 13:05:30',NULL),(16,'Paranormal','Paranormal',NULL,'2023-10-26 13:04:50',NULL,'2023-10-26 13:05:30',NULL),(17,'Erotica','Erotica',NULL,'2023-10-26 13:04:50',NULL,'2023-10-26 13:05:30',NULL),(18,'Mystery','Mystery',NULL,'2023-10-26 13:04:50',NULL,'2023-10-26 13:05:30',NULL),(19,'Historical','Historical',NULL,'2023-10-26 13:04:50',NULL,'2023-10-26 13:05:30',NULL),(20,'Realistic Fiction','Realistic Fiction',NULL,'2023-10-26 13:04:50',NULL,'2023-10-26 13:05:30',NULL),(21,'Non-Fiction','Non-Fiction',NULL,'2023-10-26 13:04:50',NULL,'2023-10-26 13:05:30',NULL),(22,'Folktales','Folktales',NULL,'2023-10-26 13:04:50',NULL,'2023-10-26 13:05:30',NULL),(23,'Fairy Tales','Fairy Tales',NULL,'2023-10-26 13:04:50',NULL,'2023-10-26 13:05:30',NULL),(24,'Learn to Read','Learn to Read',NULL,'2023-10-26 13:04:50',NULL,'2023-10-26 13:05:30',NULL),(25,'Concept Books','Concept Books',NULL,'2023-10-26 13:04:50',NULL,'2023-10-26 13:05:30',NULL),(26,'Rhyming','Rhyming',NULL,'2023-10-26 13:04:50',NULL,'2023-10-26 13:05:30',NULL),(27,'Cultural Stories','Cultural Stories',NULL,'2023-10-26 13:04:50',NULL,'2023-10-26 13:05:30',NULL),(28,'Action','Action',NULL,'2023-10-26 13:04:50',NULL,'2023-10-26 13:05:30',NULL),(29,'Sci-Fi','Sci-Fi',NULL,'2023-10-26 13:04:50',NULL,'2023-10-26 13:05:30',NULL),(30,'Romantic Comedy','Romantic Comedy',NULL,'2023-10-26 13:04:50',NULL,'2023-10-26 13:05:30',NULL),(31,'Thriller','Thriller',NULL,'2023-10-26 13:04:50',NULL,'2023-10-26 13:05:30',NULL),(32,'Historical Retelling','Historical Retelling',NULL,'2023-10-26 13:04:50',NULL,'2023-10-26 13:05:30',NULL),(33,'Romantic','Romantic',NULL,'2023-10-26 13:04:50',NULL,'2023-10-26 13:05:30',NULL),(34,'Educational','Educational',NULL,'2023-10-26 13:04:50',NULL,'2023-10-26 13:05:30',NULL),(35,'Documentary','Documentary',NULL,'2023-10-26 13:04:50',NULL,'2023-10-26 13:05:30',NULL),(36,'Tragedy','Tragedy',NULL,'2023-10-26 13:04:50',NULL,'2023-10-26 13:05:30',NULL),(37,'Satire','Satire',NULL,'2023-10-26 13:04:50',NULL,'2023-10-26 13:05:30',NULL),(38,'Farce','Farce',NULL,'2023-10-26 13:04:50',NULL,'2023-10-26 13:05:30',NULL),(39,'Melodrama','Melodrama',NULL,'2023-10-26 13:04:50',NULL,'2023-10-26 13:05:30',NULL),(40,'Adaptation','Adaptation',NULL,'2023-10-26 13:04:50',NULL,'2023-10-26 13:05:30',NULL),(41,'Contemporary','Contemporary',NULL,'2023-10-26 13:04:50',NULL,'2023-10-26 13:05:30',NULL),(42,'Action/Adventure','Action/Adventure',NULL,'2023-10-26 13:04:50',NULL,'2023-10-26 13:05:30',NULL),(43,'Role-Playing Game (RPG)','Role-Playing Game (RPG)',NULL,'2023-10-26 13:04:50',NULL,'2023-10-26 13:05:30',NULL),(44,'Simulation','Simulation',NULL,'2023-10-26 13:04:50',NULL,'2023-10-26 13:05:30',NULL),(45,'Survival','Survival',NULL,'2023-10-26 13:04:50',NULL,'2023-10-26 13:05:30',NULL),(46,'Strategy','Strategy',NULL,'2023-10-26 13:04:50',NULL,'2023-10-26 13:05:30',NULL),(47,'Investigative','Investigative',NULL,'2023-10-26 13:04:50',NULL,'2023-10-26 13:05:30',NULL),(48,'Nature and Wildlife','Nature and Wildlife',NULL,'2023-10-26 13:04:50',NULL,'2023-10-26 13:05:30',NULL),(49,'Biographical','Biographical',NULL,'2023-10-26 13:04:50',NULL,'2023-10-26 13:05:30',NULL),(50,'Cultural/Social Commentary','Cultural/Social Commentary',NULL,'2023-10-26 13:04:50',NULL,'2023-10-26 13:05:30',NULL),(51,'Science and Technology','Science and Technology',NULL,'2023-10-26 13:04:50',NULL,'2023-10-26 13:05:30',NULL),(52,'Travel and Exploration','Travel and Exploration',NULL,'2023-10-26 13:04:50',NULL,'2023-10-26 13:05:30',NULL),(53,'Political','Political',NULL,'2023-10-26 13:04:50',NULL,'2023-10-26 13:05:30',NULL),(54,'Health and Wellness','Health and Wellness',NULL,'2023-10-26 13:04:50',NULL,'2023-10-26 13:05:30',NULL),(55,'Personal Narrative','Personal Narrative',NULL,'2023-10-26 13:04:50',NULL,'2023-10-26 13:05:30',NULL),(56,'Observational','Observational',NULL,'2023-10-26 13:04:50',NULL,'2023-10-26 13:05:30',NULL),(57,'Dark Humor','Dark Humor',NULL,'2023-10-26 13:04:50',NULL,'2023-10-26 13:05:30',NULL),(58,'Slapstick','Slapstick',NULL,'2023-10-26 13:04:50',NULL,'2023-10-26 13:05:30',NULL),(59,'Anecdotal','Anecdotal',NULL,'2023-10-26 13:04:50',NULL,'2023-10-26 13:05:30',NULL),(60,'Deadpan','Deadpan',NULL,'2023-10-26 13:04:50',NULL,'2023-10-26 13:05:30',NULL),(61,'Cringe Comedy','Cringe Comedy',NULL,'2023-10-26 13:04:50',NULL,'2023-10-26 13:05:30',NULL),(62,'Prop Comedy','Prop Comedy',NULL,'2023-10-26 13:04:50',NULL,'2023-10-26 13:05:30',NULL),(63,'Blue Comedy','Blue Comedy',NULL,'2023-10-26 13:04:50',NULL,'2023-10-26 13:05:30',NULL),(64,'Superhero','Superhero',NULL,'2023-10-26 13:04:50',NULL,'2023-10-26 13:05:30',NULL),(65,'Noir','Noir',NULL,'2023-10-26 13:04:50',NULL,'2023-10-26 13:05:30',NULL),(66,'Slice of Life','Slice of Life',NULL,'2023-10-26 13:04:50',NULL,'2023-10-26 13:05:30',NULL),(67,'Epic Fantasy','Epic Fantasy',NULL,'2023-10-26 13:04:50',NULL,'2023-10-26 13:05:30',NULL),(68,'Memoir/Biography','Memoir/Biography',NULL,'2023-10-26 13:04:50',NULL,'2023-10-26 13:05:30',NULL),(69,'Philosophical','Philosophical',NULL,'2023-10-26 13:04:50',NULL,'2023-10-26 13:05:30',NULL),(70,'Post-Apocalyptic','Post-Apocalyptic',NULL,'2023-10-26 13:04:50',NULL,'2023-10-26 13:05:30',NULL),(71,'Steampunk','Steampunk',NULL,'2023-10-26 13:04:50',NULL,'2023-10-26 13:05:30',NULL),(72,'Urban Fantasy','Urban Fantasy',NULL,'2023-10-26 13:04:50',NULL,'2023-10-26 13:05:30',NULL),(73,'Western','Western',NULL,'2023-10-26 13:04:50',NULL,'2023-10-26 13:05:30',NULL),(74,'Magical Realism','Magical Realism',NULL,'2023-10-26 13:04:50',NULL,'2023-10-26 13:05:30',NULL),(75,'High Fantasy','High Fantasy',NULL,'2023-10-26 13:04:50',NULL,'2023-10-26 13:05:30',NULL),(76,'Dark Fantasy','Dark Fantasy',NULL,'2023-10-26 13:04:50',NULL,'2023-10-26 13:05:30',NULL),(77,'Space Opera','Space Opera',NULL,'2023-10-26 13:04:50',NULL,'2023-10-26 13:05:30',NULL),(78,'Cyberpunk','Cyberpunk',NULL,'2023-10-26 13:04:50',NULL,'2023-10-26 13:05:30',NULL),(79,'Military Science Fiction','Military Science Fiction',NULL,'2023-10-26 13:04:50',NULL,'2023-10-26 13:05:30',NULL),(80,'Time Travel','Time Travel',NULL,'2023-10-26 13:04:50',NULL,'2023-10-26 13:05:30',NULL),(81,'Parallel Universes','Parallel Universes',NULL,'2023-10-26 13:04:50',NULL,'2023-10-26 13:05:30',NULL),(82,'Lyric','Lyric',NULL,'2023-10-26 13:04:50',NULL,'2023-10-26 13:05:30',NULL),(83,'Narrative','Narrative',NULL,'2023-10-26 13:04:50',NULL,'2023-10-26 13:05:30',NULL),(84,'Epic','Epic',NULL,'2023-10-26 13:04:50',NULL,'2023-10-26 13:05:30',NULL),(85,'Satirical','Satirical',NULL,'2023-10-26 13:04:50',NULL,'2023-10-26 13:05:30',NULL),(86,'Haiku','Haiku',NULL,'2023-10-26 13:04:50',NULL,'2023-10-26 13:05:30',NULL),(87,'Sonnet','Sonnet',NULL,'2023-10-26 13:04:50',NULL,'2023-10-26 13:05:30',NULL),(88,'Free Verse','Free Verse',NULL,'2023-10-26 13:04:50',NULL,'2023-10-26 13:05:30',NULL),(89,'Acrostic','Acrostic',NULL,'2023-10-26 13:04:50',NULL,'2023-10-26 13:05:30',NULL),(90,'Limerick','Limerick',NULL,'2023-10-26 13:04:50',NULL,'2023-10-26 13:05:30',NULL),(91,'Ballad','Ballad',NULL,'2023-10-26 13:04:50',NULL,'2023-10-26 13:05:30',NULL),(92,'','',NULL,'2023-10-26 13:04:50',NULL,'2023-10-26 13:05:30',NULL),(93,'Investigative Journalism','Investigative Journalism',NULL,'2023-10-26 13:04:50',NULL,'2023-10-26 13:05:30',NULL),(94,'News Report','News Report',NULL,'2023-10-26 13:04:50',NULL,'2023-10-26 13:05:30',NULL),(95,'Feature Stories','Feature Stories',NULL,'2023-10-26 13:04:50',NULL,'2023-10-26 13:05:30',NULL),(96,'Opinion/Editorial','Opinion/Editorial',NULL,'2023-10-26 13:04:50',NULL,'2023-10-26 13:05:30',NULL),(97,'Profile','Profile',NULL,'2023-10-26 13:04:50',NULL,'2023-10-26 13:05:30',NULL),(98,'Review','Review',NULL,'2023-10-26 13:04:50',NULL,'2023-10-26 13:05:30',NULL),(99,'Explanatory Journalism','Explanatory Journalism',NULL,'2023-10-26 13:04:50',NULL,'2023-10-26 13:05:30',NULL),(100,'Data Journalism','Data Journalism',NULL,'2023-10-26 13:04:50',NULL,'2023-10-26 13:05:30',NULL),(101,'Photojournalism','Photojournalism',NULL,'2023-10-26 13:04:50',NULL,'2023-10-26 13:05:30',NULL),(102,'Narrative Journalism','Narrative Journalism',NULL,'2023-10-26 13:04:50',NULL,'2023-10-26 13:05:30',NULL),(103,'Profile Feature','Profile Feature',NULL,'2023-10-26 13:04:50',NULL,'2023-10-26 13:05:30',NULL),(104,'Human Interest','Human Interest',NULL,'2023-10-26 13:04:50',NULL,'2023-10-26 13:05:30',NULL),(105,'Investigative Feature','Investigative Feature',NULL,'2023-10-26 13:04:50',NULL,'2023-10-26 13:05:30',NULL),(106,'Historical Retrospective','Historical Retrospective',NULL,'2023-10-26 13:04:50',NULL,'2023-10-26 13:05:30',NULL),(107,'Travel and Lifestyle','Travel and Lifestyle',NULL,'2023-10-26 13:04:50',NULL,'2023-10-26 13:05:30',NULL),(108,'Tech and Innovation','Tech and Innovation',NULL,'2023-10-26 13:04:50',NULL,'2023-10-26 13:05:30',NULL),(109,'Culture and Art','Culture and Art',NULL,'2023-10-26 13:04:50',NULL,'2023-10-26 13:05:30',NULL),(110,'Opinion and Commentary','Opinion and Commentary',NULL,'2023-10-26 13:04:50',NULL,'2023-10-26 13:05:30',NULL),(111,'Fashion and Beauty','Fashion and Beauty',NULL,'2023-10-26 13:04:50',NULL,'2023-10-26 13:05:30',NULL),(112,'Book Reviews','Book Reviews',NULL,'2023-10-26 13:04:50',NULL,'2023-10-26 13:05:30',NULL),(113,'Film and TV Reviews','Film and TV Reviews',NULL,'2023-10-26 13:04:50',NULL,'2023-10-26 13:05:30',NULL),(114,'Music Album Reviews','Music Album Reviews',NULL,'2023-10-26 13:04:50',NULL,'2023-10-26 13:05:30',NULL),(115,'Tech Product Reviews','Tech Product Reviews',NULL,'2023-10-26 13:04:50',NULL,'2023-10-26 13:05:30',NULL),(116,'Restaurant and Food Reviews','Restaurant and Food Reviews',NULL,'2023-10-26 13:04:50',NULL,'2023-10-26 13:05:30',NULL),(117,'Theater and Performance Reviews','Theater and Performance Reviews',NULL,'2023-10-26 13:04:50',NULL,'2023-10-26 13:05:30',NULL),(118,'Video Game Reviews','Video Game Reviews',NULL,'2023-10-26 13:04:50',NULL,'2023-10-26 13:05:30',NULL),(119,'Travel Destination Reviews','Travel Destination Reviews',NULL,'2023-10-26 13:04:50',NULL,'2023-10-26 13:05:30',NULL),(120,'Fashion and Beauty Product Reviews','Fashion and Beauty Product Reviews',NULL,'2023-10-26 13:04:50',NULL,'2023-10-26 13:05:30',NULL),(121,'Service Reviews','Service Reviews',NULL,'2023-10-26 13:04:50',NULL,'2023-10-26 13:05:30',NULL),(122,'Scientific Research Report','Scientific Research Report',NULL,'2023-10-26 13:04:50',NULL,'2023-10-26 13:05:30',NULL),(123,'Market Research Report','Market Research Report',NULL,'2023-10-26 13:04:50',NULL,'2023-10-26 13:05:30',NULL),(124,'Social Science Research Report','Social Science Research Report',NULL,'2023-10-26 13:04:50',NULL,'2023-10-26 13:05:30',NULL),(125,'Medical and Clinical Research Report','Medical and Clinical Research Report',NULL,'2023-10-26 13:04:50',NULL,'2023-10-26 13:05:30',NULL),(126,'Educational Research Report','Educational Research Report',NULL,'2023-10-26 13:04:50',NULL,'2023-10-26 13:05:30',NULL),(127,'Technical Research Report','Technical Research Report',NULL,'2023-10-26 13:04:50',NULL,'2023-10-26 13:05:30',NULL),(128,'Economic Research Report','Economic Research Report',NULL,'2023-10-26 13:04:50',NULL,'2023-10-26 13:05:30',NULL),(129,'Environmental Research Report','Environmental Research Report',NULL,'2023-10-26 13:04:50',NULL,'2023-10-26 13:05:30',NULL),(130,'Psychological Research Report','Psychological Research Report',NULL,'2023-10-26 13:04:50',NULL,'2023-10-26 13:05:30',NULL),(131,'Historical Research Report','Historical Research Report',NULL,'2023-10-26 13:04:50',NULL,'2023-10-26 13:05:30',NULL),(132,'Coming-of-Age Memoir','Coming-of-Age Memoir',NULL,'2023-10-26 13:04:50',NULL,'2023-10-26 13:05:30',NULL),(133,'Travel Memoir','Travel Memoir',NULL,'2023-10-26 13:04:50',NULL,'2023-10-26 13:05:30',NULL),(134,'Grief Memoir','Grief Memoir',NULL,'2023-10-26 13:04:50',NULL,'2023-10-26 13:05:30',NULL),(135,'Addiction and Recovery Memoir','Addiction and Recovery Memoir',NULL,'2023-10-26 13:04:50',NULL,'2023-10-26 13:05:30',NULL),(136,'Family Memoir','Family Memoir',NULL,'2023-10-26 13:04:50',NULL,'2023-10-26 13:05:30',NULL),(137,'Historical Memoir','Historical Memoir',NULL,'2023-10-26 13:04:50',NULL,'2023-10-26 13:05:30',NULL),(138,'Celebrity Memoir','Celebrity Memoir',NULL,'2023-10-26 13:04:50',NULL,'2023-10-26 13:05:30',NULL),(139,'Adventure Memoir','Adventure Memoir',NULL,'2023-10-26 13:04:50',NULL,'2023-10-26 13:05:30',NULL),(140,'Relationship Memoir','Relationship Memoir',NULL,'2023-10-26 13:04:50',NULL,'2023-10-26 13:05:30',NULL),(141,'Inspirational Memoir','Inspirational Memoir',NULL,'2023-10-26 13:04:50',NULL,'2023-10-26 13:05:30',NULL),(142,'Historical Autobiography','Historical Autobiography',NULL,'2023-10-26 13:04:50',NULL,'2023-10-26 13:05:30',NULL),(143,'Celebrity Autobiography','Celebrity Autobiography',NULL,'2023-10-26 13:04:50',NULL,'2023-10-26 13:05:30',NULL),(144,'Political Autobiography','Political Autobiography',NULL,'2023-10-26 13:04:50',NULL,'2023-10-26 13:05:30',NULL),(145,'Adventure Autobiography','Adventure Autobiography',NULL,'2023-10-26 13:04:50',NULL,'2023-10-26 13:05:30',NULL),(146,'Spiritual Autobiography','Spiritual Autobiography',NULL,'2023-10-26 13:04:50',NULL,'2023-10-26 13:05:30',NULL),(147,'Scientific Autobiography','Scientific Autobiography',NULL,'2023-10-26 13:04:50',NULL,'2023-10-26 13:05:30',NULL),(148,'Business Autobiography','Business Autobiography',NULL,'2023-10-26 13:04:50',NULL,'2023-10-26 13:05:30',NULL),(149,'Sports Autobiography','Sports Autobiography',NULL,'2023-10-26 13:04:50',NULL,'2023-10-26 13:05:30',NULL),(150,'Artistic Autobiography','Artistic Autobiography',NULL,'2023-10-26 13:04:50',NULL,'2023-10-26 13:05:30',NULL),(151,'Philosophical Autobiography','Philosophical Autobiography',NULL,'2023-10-26 13:04:50',NULL,'2023-10-26 13:05:30',NULL),(152,'Historical Biography','Historical Biography',NULL,'2023-10-26 13:04:50',NULL,'2023-10-26 13:05:30',NULL),(153,'Celebrity Biography','Celebrity Biography',NULL,'2023-10-26 13:04:50',NULL,'2023-10-26 13:05:30',NULL),(154,'Political Biography','Political Biography',NULL,'2023-10-26 13:04:50',NULL,'2023-10-26 13:05:30',NULL),(155,'Adventure Biography','Adventure Biography',NULL,'2023-10-26 13:04:50',NULL,'2023-10-26 13:05:30',NULL),(156,'Literary Biography','Literary Biography',NULL,'2023-10-26 13:04:50',NULL,'2023-10-26 13:05:30',NULL),(157,'Scientific Biography','Scientific Biography',NULL,'2023-10-26 13:04:50',NULL,'2023-10-26 13:05:30',NULL),(158,'Business Biography','Business Biography',NULL,'2023-10-26 13:04:50',NULL,'2023-10-26 13:05:30',NULL),(159,'Sports Biography','Sports Biography',NULL,'2023-10-26 13:04:50',NULL,'2023-10-26 13:05:30',NULL),(160,'Artistic Biography','Artistic Biography',NULL,'2023-10-26 13:04:50',NULL,'2023-10-26 13:05:30',NULL),(161,'Philosophical Biography','Philosophical Biography',NULL,'2023-10-26 13:04:50',NULL,'2023-10-26 13:05:30',NULL),(162,'City Guide','City Guide',NULL,'2023-10-26 13:04:50',NULL,'2023-10-26 13:05:30',NULL),(163,'Country Guide','Country Guide',NULL,'2023-10-26 13:04:50',NULL,'2023-10-26 13:05:30',NULL),(164,'Adventure Travel Guide','Adventure Travel Guide',NULL,'2023-10-26 13:04:50',NULL,'2023-10-26 13:05:30',NULL),(165,'Cultural Travel Guide','Cultural Travel Guide',NULL,'2023-10-26 13:04:50',NULL,'2023-10-26 13:05:30',NULL),(166,'Historical Travel Guide','Historical Travel Guide',NULL,'2023-10-26 13:04:50',NULL,'2023-10-26 13:05:30',NULL),(167,'Nature & Wildlife Guide','Nature & Wildlife Guide',NULL,'2023-10-26 13:04:50',NULL,'2023-10-26 13:05:30',NULL),(168,'Road Trip Guide','Road Trip Guide',NULL,'2023-10-26 13:04:50',NULL,'2023-10-26 13:05:30',NULL),(169,'Beach & Island Guide','Beach & Island Guide',NULL,'2023-10-26 13:04:50',NULL,'2023-10-26 13:05:30',NULL),(170,'Culinary Travel Guide','Culinary Travel Guide',NULL,'2023-10-26 13:04:50',NULL,'2023-10-26 13:05:30',NULL),(171,'Budget Travel Guide','Budget Travel Guide',NULL,'2023-10-26 13:04:50',NULL,'2023-10-26 13:05:30',NULL),(172,'Solo Travel Journal','Solo Travel Journal',NULL,'2023-10-26 13:04:50',NULL,'2023-10-26 13:05:30',NULL),(173,'Adventure Travel Journal','Adventure Travel Journal',NULL,'2023-10-26 13:04:50',NULL,'2023-10-26 13:05:30',NULL),(174,'Cultural Immersion Journal','Cultural Immersion Journal',NULL,'2023-10-26 13:04:50',NULL,'2023-10-26 13:05:30',NULL),(175,'Road Trip Journal','Road Trip Journal',NULL,'2023-10-26 13:04:50',NULL,'2023-10-26 13:05:30',NULL),(176,'Backpacking Journal','Backpacking Journal',NULL,'2023-10-26 13:04:50',NULL,'2023-10-26 13:05:30',NULL),(177,'Nature Exploration Journal','Nature Exploration Journal',NULL,'2023-10-26 13:04:50',NULL,'2023-10-26 13:05:30',NULL),(178,'Spiritual Journey Journal','Spiritual Journey Journal',NULL,'2023-10-26 13:04:50',NULL,'2023-10-26 13:05:30',NULL),(179,'Family Vacation Journal','Family Vacation Journal',NULL,'2023-10-26 13:04:50',NULL,'2023-10-26 13:05:30',NULL),(180,'Gap Year Journal','Gap Year Journal',NULL,'2023-10-26 13:04:50',NULL,'2023-10-26 13:05:30',NULL),(181,'Expat Diary','Expat Diary',NULL,'2023-10-26 13:04:50',NULL,'2023-10-26 13:05:30',NULL),(182,'Business Strategy','Business Strategy',NULL,'2023-10-26 13:04:50',NULL,'2023-10-26 13:05:30',NULL),(183,'Medical/Healthcare','Medical/Healthcare',NULL,'2023-10-26 13:04:50',NULL,'2023-10-26 13:05:30',NULL),(184,'Psychological Analysis','Psychological Analysis',NULL,'2023-10-26 13:04:50',NULL,'2023-10-26 13:05:30',NULL),(185,'Social Research','Social Research',NULL,'2023-10-26 13:04:50',NULL,'2023-10-26 13:05:30',NULL),(186,'Environmental Studies','Environmental Studies',NULL,'2023-10-26 13:04:50',NULL,'2023-10-26 13:05:30',NULL),(187,'Technology Implementation','Technology Implementation',NULL,'2023-10-26 13:04:50',NULL,'2023-10-26 13:05:30',NULL),(188,'Marketing Effectiveness','Marketing Effectiveness',NULL,'2023-10-26 13:04:50',NULL,'2023-10-26 13:05:30',NULL),(189,'Educational Practices','Educational Practices',NULL,'2023-10-26 13:04:50',NULL,'2023-10-26 13:05:30',NULL),(190,'Economic Analysis','Economic Analysis',NULL,'2023-10-26 13:04:50',NULL,'2023-10-26 13:05:30',NULL),(191,'Legal Precedent','Legal Precedent',NULL,'2023-10-26 13:04:50',NULL,'2023-10-26 13:05:30',NULL),(192,'Technology Solutions','Technology Solutions',NULL,'2023-10-26 13:04:50',NULL,'2023-10-26 13:05:30',NULL),(193,'Government Policy','Government Policy',NULL,'2023-10-26 13:04:50',NULL,'2023-10-26 13:05:30',NULL),(194,'Business Strategies','Business Strategies',NULL,'2023-10-26 13:04:50',NULL,'2023-10-26 13:05:30',NULL),(195,'Medical Advancements','Medical Advancements',NULL,'2023-10-26 13:04:50',NULL,'2023-10-26 13:05:30',NULL),(196,'Financial Models','Financial Models',NULL,'2023-10-26 13:04:50',NULL,'2023-10-26 13:05:30',NULL),(197,'Legal Analysis','Legal Analysis',NULL,'2023-10-26 13:04:50',NULL,'2023-10-26 13:05:30',NULL),(198,'Environmental Concerns','Environmental Concerns',NULL,'2023-10-26 13:04:50',NULL,'2023-10-26 13:05:30',NULL),(199,'Educational Reform','Educational Reform',NULL,'2023-10-26 13:04:50',NULL,'2023-10-26 13:05:30',NULL),(200,'Market Analysis','Market Analysis',NULL,'2023-10-26 13:04:50',NULL,'2023-10-26 13:05:30',NULL),(201,'Product Launch','Product Launch',NULL,'2023-10-26 13:04:50',NULL,'2023-10-26 13:05:30',NULL),(202,'Natural Sciences','Natural Sciences',NULL,'2023-10-26 13:04:50',NULL,'2023-10-26 13:05:30',NULL),(203,'Social Sciences','Social Sciences',NULL,'2023-10-26 13:04:50',NULL,'2023-10-26 13:05:30',NULL),(204,'Humanities','Humanities',NULL,'2023-10-26 13:04:50',NULL,'2023-10-26 13:05:30',NULL),(205,'Engineering','Engineering',NULL,'2023-10-26 13:04:50',NULL,'2023-10-26 13:05:30',NULL),(206,'Medical Studies','Medical Studies',NULL,'2023-10-26 13:04:50',NULL,'2023-10-26 13:05:30',NULL),(207,'Business and Economics','Business and Economics',NULL,'2023-10-26 13:04:50',NULL,'2023-10-26 13:05:30',NULL),(208,'Law Studies','Law Studies',NULL,'2023-10-26 13:04:50',NULL,'2023-10-26 13:05:30',NULL),(209,'Arts and Design','Arts and Design',NULL,'2023-10-26 13:04:50',NULL,'2023-10-26 13:05:30',NULL),(210,'Educational Research','Educational Research',NULL,'2023-10-26 13:04:50',NULL,'2023-10-26 13:05:30',NULL),(211,'Personal/Lifestyle','Personal/Lifestyle',NULL,'2023-10-26 13:04:50',NULL,'2023-10-26 13:05:30',NULL),(212,'Travel','Travel',NULL,'2023-10-26 13:04:50',NULL,'2023-10-26 13:05:30',NULL),(213,'Food & Cooking','Food & Cooking',NULL,'2023-10-26 13:04:50',NULL,'2023-10-26 13:05:30',NULL),(214,'Tech & Gadgets','Tech & Gadgets',NULL,'2023-10-26 13:04:50',NULL,'2023-10-26 13:05:30',NULL),(215,'Health & Wellness','Health & Wellness',NULL,'2023-10-26 13:04:50',NULL,'2023-10-26 13:05:30',NULL),(216,'Business & Marketing','Business & Marketing',NULL,'2023-10-26 13:04:50',NULL,'2023-10-26 13:05:30',NULL),(217,'DIY & Crafts','DIY & Crafts',NULL,'2023-10-26 13:04:50',NULL,'2023-10-26 13:05:30',NULL),(218,'Fashion & Beauty','Fashion & Beauty',NULL,'2023-10-26 13:04:50',NULL,'2023-10-26 13:05:30',NULL),(219,'Entertainment & Pop Culture','Entertainment & Pop Culture',NULL,'2023-10-26 13:04:50',NULL,'2023-10-26 13:05:30',NULL),(220,'News & Current Events','News & Current Events',NULL,'2023-10-26 13:04:50',NULL,'2023-10-26 13:05:30',NULL),(221,'Electronics & Gadgets','Electronics & Gadgets',NULL,'2023-10-26 13:04:50',NULL,'2023-10-26 13:05:30',NULL),(222,'Software & Applications','Software & Applications',NULL,'2023-10-26 13:04:50',NULL,'2023-10-26 13:05:30',NULL),(223,'Machinery & Heavy Equipment','Machinery & Heavy Equipment',NULL,'2023-10-26 13:04:50',NULL,'2023-10-26 13:05:30',NULL),(224,'Automobiles & Vehicles','Automobiles & Vehicles',NULL,'2023-10-26 13:04:50',NULL,'2023-10-26 13:05:30',NULL),(225,'Medical Devices','Medical Devices',NULL,'2023-10-26 13:04:50',NULL,'2023-10-26 13:05:30',NULL),(226,'Household Appliances','Household Appliances',NULL,'2023-10-26 13:04:50',NULL,'2023-10-26 13:05:30',NULL),(227,'Computer Hardware','Computer Hardware',NULL,'2023-10-26 13:04:50',NULL,'2023-10-26 13:05:30',NULL),(228,'Networking Equipment','Networking Equipment',NULL,'2023-10-26 13:04:50',NULL,'2023-10-26 13:05:30',NULL),(229,'Construction Tools','Construction Tools',NULL,'2023-10-26 13:04:50',NULL,'2023-10-26 13:05:30',NULL),(230,'Aerospace & Aviation','Aerospace & Aviation',NULL,'2023-10-26 13:04:50',NULL,'2023-10-26 13:05:30',NULL),(231,'Home & Garden','Home & Garden',NULL,'2023-10-26 13:04:50',NULL,'2023-10-26 13:05:30',NULL),(232,'Technology & Gadgets','Technology & Gadgets',NULL,'2023-10-26 13:04:50',NULL,'2023-10-26 13:05:30',NULL),(233,'Cooking & Baking','Cooking & Baking',NULL,'2023-10-26 13:04:50',NULL,'2023-10-26 13:05:30',NULL),(234,'Crafts & DIY Projects','Crafts & DIY Projects',NULL,'2023-10-26 13:04:50',NULL,'2023-10-26 13:05:30',NULL),(235,'Health & Fitness','Health & Fitness',NULL,'2023-10-26 13:04:50',NULL,'2023-10-26 13:05:30',NULL),(236,'Automotive','Automotive',NULL,'2023-10-26 13:04:50',NULL,'2023-10-26 13:05:30',NULL),(237,'Beauty & Fashion','Beauty & Fashion',NULL,'2023-10-26 13:04:50',NULL,'2023-10-26 13:05:30',NULL),(238,'Finance & Budgeting','Finance & Budgeting',NULL,'2023-10-26 13:04:50',NULL,'2023-10-26 13:05:30',NULL),(239,'Startup','Startup',NULL,'2023-10-26 13:04:50',NULL,'2023-10-26 13:05:30',NULL),(240,'Retail','Retail',NULL,'2023-10-26 13:04:50',NULL,'2023-10-26 13:05:30',NULL),(241,'E-commerce','E-commerce',NULL,'2023-10-26 13:04:50',NULL,'2023-10-26 13:05:30',NULL),(242,'Tech & Software','Tech & Software',NULL,'2023-10-26 13:04:50',NULL,'2023-10-26 13:05:30',NULL),(243,'Healthcare','Healthcare',NULL,'2023-10-26 13:04:50',NULL,'2023-10-26 13:05:30',NULL),(244,'Agriculture','Agriculture',NULL,'2023-10-26 13:04:50',NULL,'2023-10-26 13:05:30',NULL),(245,'Manufacturing','Manufacturing',NULL,'2023-10-26 13:04:50',NULL,'2023-10-26 13:05:30',NULL),(246,'Hospitality','Hospitality',NULL,'2023-10-26 13:04:50',NULL,'2023-10-26 13:05:30',NULL),(247,'Finance & Fintech','Finance & Fintech',NULL,'2023-10-26 13:04:50',NULL,'2023-10-26 13:05:30',NULL),(248,'Education','Education',NULL,'2023-10-26 13:04:50',NULL,'2023-10-26 13:05:30',NULL),(249,'Software & IT','Software & IT',NULL,'2023-10-26 13:04:50',NULL,'2023-10-26 13:05:30',NULL),(250,'Machinery & Equipment Operation','Machinery & Equipment Operation',NULL,'2023-10-26 13:04:50',NULL,'2023-10-26 13:05:30',NULL),(251,'Human Resources & Onboarding','Human Resources & Onboarding',NULL,'2023-10-26 13:04:50',NULL,'2023-10-26 13:05:30',NULL),(252,'Sales & Customer Service','Sales & Customer Service',NULL,'2023-10-26 13:04:50',NULL,'2023-10-26 13:05:30',NULL),(253,'Leadership & Management','Leadership & Management',NULL,'2023-10-26 13:04:50',NULL,'2023-10-26 13:05:30',NULL),(254,'Health & Safety','Health & Safety',NULL,'2023-10-26 13:04:50',NULL,'2023-10-26 13:05:30',NULL),(255,'Product Knowledge','Product Knowledge',NULL,'2023-10-26 13:04:50',NULL,'2023-10-26 13:05:30',NULL),(256,'Language & Communication','Language & Communication',NULL,'2023-10-26 13:04:50',NULL,'2023-10-26 13:05:30',NULL),(257,'Financial Processes','Financial Processes',NULL,'2023-10-26 13:04:50',NULL,'2023-10-26 13:05:30',NULL),(258,'Professional Development','Professional Development',NULL,'2023-10-26 13:04:50',NULL,'2023-10-26 13:05:30',NULL),(259,'Heroic Adventure','Heroic Adventure',NULL,'2023-10-26 13:04:50',NULL,'2023-10-26 13:05:30',NULL),(260,'Historical Recount','Historical Recount',NULL,'2023-10-26 13:04:50',NULL,'2023-10-26 13:05:30',NULL),(261,'Mythological','Mythological',NULL,'2023-10-26 13:04:50',NULL,'2023-10-26 13:05:30',NULL),(262,'Allegory','Allegory',NULL,'2023-10-26 13:04:50',NULL,'2023-10-26 13:05:30',NULL),(263,'Tragic Romance','Tragic Romance',NULL,'2023-10-26 13:04:50',NULL,'2023-10-26 13:05:30',NULL),(264,'Moral & Philosophical Reflections','Moral & Philosophical Reflections',NULL,'2023-10-26 13:04:50',NULL,'2023-10-26 13:05:30',NULL),(265,'War & Battles','War & Battles',NULL,'2023-10-26 13:04:50',NULL,'2023-10-26 13:05:30',NULL),(266,'Quest & Exploration','Quest & Exploration',NULL,'2023-10-26 13:04:50',NULL,'2023-10-26 13:05:30',NULL),(267,'Divine & Supernatural','Divine & Supernatural',NULL,'2023-10-26 13:04:50',NULL,'2023-10-26 13:05:30',NULL),(268,'Cultural & Nationalistic','Cultural & Nationalistic',NULL,'2023-10-26 13:04:50',NULL,'2023-10-26 13:05:30',NULL),(269,'Personal Reflection','Personal Reflection',NULL,'2023-10-26 13:04:50',NULL,'2023-10-26 13:05:30',NULL),(270,'Argumentative/Persuasive','Argumentative/Persuasive',NULL,'2023-10-26 13:04:50',NULL,'2023-10-26 13:05:30',NULL),(271,'Descriptive','Descriptive',NULL,'2023-10-26 13:04:50',NULL,'2023-10-26 13:05:30',NULL),(272,'Expository','Expository',NULL,'2023-10-26 13:04:50',NULL,'2023-10-26 13:05:30',NULL),(273,'Analytical','Analytical',NULL,'2023-10-26 13:04:50',NULL,'2023-10-26 13:05:30',NULL),(274,'Cause and Effect','Cause and Effect',NULL,'2023-10-26 13:04:50',NULL,'2023-10-26 13:05:30',NULL),(275,'Compare and Contrast','Compare and Contrast',NULL,'2023-10-26 13:04:50',NULL,'2023-10-26 13:05:30',NULL),(276,'Problem-Solution','Problem-Solution',NULL,'2023-10-26 13:04:50',NULL,'2023-10-26 13:05:30',NULL),(277,'Pop','Pop',NULL,'2023-10-26 13:04:50',NULL,'2023-10-26 13:05:30',NULL),(278,'Rock','Rock',NULL,'2023-10-26 13:04:50',NULL,'2023-10-26 13:05:30',NULL),(279,'R&B/Soul','R&B/Soul',NULL,'2023-10-26 13:04:50',NULL,'2023-10-26 13:05:30',NULL),(280,'Hip-Hop/Rap','Hip-Hop/Rap',NULL,'2023-10-26 13:04:50',NULL,'2023-10-26 13:05:30',NULL),(281,'Country','Country',NULL,'2023-10-26 13:04:50',NULL,'2023-10-26 13:05:30',NULL),(282,'Jazz','Jazz',NULL,'2023-10-26 13:04:50',NULL,'2023-10-26 13:05:30',NULL),(283,'Blues','Blues',NULL,'2023-10-26 13:04:50',NULL,'2023-10-26 13:05:30',NULL),(284,'Electronic/Dance','Electronic/Dance',NULL,'2023-10-26 13:04:50',NULL,'2023-10-26 13:05:30',NULL),(285,'Folk','Folk',NULL,'2023-10-26 13:04:50',NULL,'2023-10-26 13:05:30',NULL),(286,'Classical/Crossover','Classical/Crossover',NULL,'2023-10-26 13:04:50',NULL,'2023-10-26 13:05:30',NULL),(287,'Inspirational/Motivational','Inspirational/Motivational',NULL,'2023-10-26 13:04:50',NULL,'2023-10-26 13:05:30',NULL),(288,'Ceremonial (e.g., weddings, graduations)','Ceremonial (e.g., weddings, graduations)',NULL,'2023-10-26 13:04:50',NULL,'2023-10-26 13:05:30',NULL),(289,'Persuasive','Persuasive',NULL,'2023-10-26 13:04:50',NULL,'2023-10-26 13:05:30',NULL),(290,'Informative','Informative',NULL,'2023-10-26 13:04:50',NULL,'2023-10-26 13:05:30',NULL),(291,'Commemorative','Commemorative',NULL,'2023-10-26 13:04:50',NULL,'2023-10-26 13:05:30',NULL),(292,'Entertainment','Entertainment',NULL,'2023-10-26 13:04:50',NULL,'2023-10-26 13:05:30',NULL),(293,'Business/Corporate','Business/Corporate',NULL,'2023-10-26 13:04:50',NULL,'2023-10-26 13:05:30',NULL),(294,'Technical','Technical',NULL,'2023-10-26 13:04:50',NULL,'2023-10-26 13:05:30',NULL);
/*!40000 ALTER TABLE `genres` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2023-10-26  7:35:30
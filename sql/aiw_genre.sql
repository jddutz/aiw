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
-- Table structure for table `genre`
--

DROP TABLE IF EXISTS `genre`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `genre` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  `description` text NOT NULL,
  `imageref` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `ix_genre_name` (`name`)
) ENGINE=InnoDB AUTO_INCREMENT=295 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `genre`
--

LOCK TABLES `genre` WRITE;
/*!40000 ALTER TABLE `genre` DISABLE KEYS */;
INSERT INTO `genre` VALUES (1,'Literary Fiction','Literary Fiction',NULL),(2,'Mystery/Thriller','Mystery/Thriller',NULL),(3,'Science Fiction','Science Fiction',NULL),(4,'Fantasy','Fantasy',NULL),(5,'Romance','Romance',NULL),(6,'Historical Fiction','Historical Fiction',NULL),(7,'Horror','Horror',NULL),(8,'Speculative Fiction','Speculative Fiction',NULL),(9,'Drama','Drama',NULL),(10,'Comedy','Comedy',NULL),(11,'Romantic Fiction','Romantic Fiction',NULL),(12,'Adventure','Adventure',NULL),(13,'Dystopian','Dystopian',NULL),(14,'Crime','Crime',NULL),(15,'Young Adult','Young Adult',NULL),(16,'Paranormal','Paranormal',NULL),(17,'Erotica','Erotica',NULL),(18,'Mystery','Mystery',NULL),(19,'Historical','Historical',NULL),(20,'Realistic Fiction','Realistic Fiction',NULL),(21,'Non-Fiction','Non-Fiction',NULL),(22,'Folktales','Folktales',NULL),(23,'Fairy Tales','Fairy Tales',NULL),(24,'Learn to Read','Learn to Read',NULL),(25,'Concept Books','Concept Books',NULL),(26,'Rhyming','Rhyming',NULL),(27,'Cultural Stories','Cultural Stories',NULL),(28,'Action','Action',NULL),(29,'Sci-Fi','Sci-Fi',NULL),(30,'Romantic Comedy','Romantic Comedy',NULL),(31,'Thriller','Thriller',NULL),(32,'Historical Retelling','Historical Retelling',NULL),(33,'Romantic','Romantic',NULL),(34,'Educational','Educational',NULL),(35,'Documentary','Documentary',NULL),(36,'Tragedy','Tragedy',NULL),(37,'Satire','Satire',NULL),(38,'Farce','Farce',NULL),(39,'Melodrama','Melodrama',NULL),(40,'Adaptation','Adaptation',NULL),(41,'Contemporary','Contemporary',NULL),(42,'Action/Adventure','Action/Adventure',NULL),(43,'Role-Playing Game (RPG)','Role-Playing Game (RPG)',NULL),(44,'Simulation','Simulation',NULL),(45,'Survival','Survival',NULL),(46,'Strategy','Strategy',NULL),(47,'Investigative','Investigative',NULL),(48,'Nature and Wildlife','Nature and Wildlife',NULL),(49,'Biographical','Biographical',NULL),(50,'Cultural/Social Commentary','Cultural/Social Commentary',NULL),(51,'Science and Technology','Science and Technology',NULL),(52,'Travel and Exploration','Travel and Exploration',NULL),(53,'Political','Political',NULL),(54,'Health and Wellness','Health and Wellness',NULL),(55,'Personal Narrative','Personal Narrative',NULL),(56,'Observational','Observational',NULL),(57,'Dark Humor','Dark Humor',NULL),(58,'Slapstick','Slapstick',NULL),(59,'Anecdotal','Anecdotal',NULL),(60,'Deadpan','Deadpan',NULL),(61,'Cringe Comedy','Cringe Comedy',NULL),(62,'Prop Comedy','Prop Comedy',NULL),(63,'Blue Comedy','Blue Comedy',NULL),(64,'Superhero','Superhero',NULL),(65,'Noir','Noir',NULL),(66,'Slice of Life','Slice of Life',NULL),(67,'Epic Fantasy','Epic Fantasy',NULL),(68,'Memoir/Biography','Memoir/Biography',NULL),(69,'Philosophical','Philosophical',NULL),(70,'Post-Apocalyptic','Post-Apocalyptic',NULL),(71,'Steampunk','Steampunk',NULL),(72,'Urban Fantasy','Urban Fantasy',NULL),(73,'Western','Western',NULL),(74,'Magical Realism','Magical Realism',NULL),(75,'High Fantasy','High Fantasy',NULL),(76,'Dark Fantasy','Dark Fantasy',NULL),(77,'Space Opera','Space Opera',NULL),(78,'Cyberpunk','Cyberpunk',NULL),(79,'Military Science Fiction','Military Science Fiction',NULL),(80,'Time Travel','Time Travel',NULL),(81,'Parallel Universes','Parallel Universes',NULL),(82,'Lyric','Lyric',NULL),(83,'Narrative','Narrative',NULL),(84,'Epic','Epic',NULL),(85,'Satirical','Satirical',NULL),(86,'Haiku','Haiku',NULL),(87,'Sonnet','Sonnet',NULL),(88,'Free Verse','Free Verse',NULL),(89,'Acrostic','Acrostic',NULL),(90,'Limerick','Limerick',NULL),(91,'Ballad','Ballad',NULL),(92,'','',NULL),(93,'Investigative Journalism','Investigative Journalism',NULL),(94,'News Report','News Report',NULL),(95,'Feature Stories','Feature Stories',NULL),(96,'Opinion/Editorial','Opinion/Editorial',NULL),(97,'Profile','Profile',NULL),(98,'Review','Review',NULL),(99,'Explanatory Journalism','Explanatory Journalism',NULL),(100,'Data Journalism','Data Journalism',NULL),(101,'Photojournalism','Photojournalism',NULL),(102,'Narrative Journalism','Narrative Journalism',NULL),(103,'Profile Feature','Profile Feature',NULL),(104,'Human Interest','Human Interest',NULL),(105,'Investigative Feature','Investigative Feature',NULL),(106,'Historical Retrospective','Historical Retrospective',NULL),(107,'Travel and Lifestyle','Travel and Lifestyle',NULL),(108,'Tech and Innovation','Tech and Innovation',NULL),(109,'Culture and Art','Culture and Art',NULL),(110,'Opinion and Commentary','Opinion and Commentary',NULL),(111,'Fashion and Beauty','Fashion and Beauty',NULL),(112,'Book Reviews','Book Reviews',NULL),(113,'Film and TV Reviews','Film and TV Reviews',NULL),(114,'Music Album Reviews','Music Album Reviews',NULL),(115,'Tech Product Reviews','Tech Product Reviews',NULL),(116,'Restaurant and Food Reviews','Restaurant and Food Reviews',NULL),(117,'Theater and Performance Reviews','Theater and Performance Reviews',NULL),(118,'Video Game Reviews','Video Game Reviews',NULL),(119,'Travel Destination Reviews','Travel Destination Reviews',NULL),(120,'Fashion and Beauty Product Reviews','Fashion and Beauty Product Reviews',NULL),(121,'Service Reviews','Service Reviews',NULL),(122,'Scientific Research Report','Scientific Research Report',NULL),(123,'Market Research Report','Market Research Report',NULL),(124,'Social Science Research Report','Social Science Research Report',NULL),(125,'Medical and Clinical Research Report','Medical and Clinical Research Report',NULL),(126,'Educational Research Report','Educational Research Report',NULL),(127,'Technical Research Report','Technical Research Report',NULL),(128,'Economic Research Report','Economic Research Report',NULL),(129,'Environmental Research Report','Environmental Research Report',NULL),(130,'Psychological Research Report','Psychological Research Report',NULL),(131,'Historical Research Report','Historical Research Report',NULL),(132,'Coming-of-Age Memoir','Coming-of-Age Memoir',NULL),(133,'Travel Memoir','Travel Memoir',NULL),(134,'Grief Memoir','Grief Memoir',NULL),(135,'Addiction and Recovery Memoir','Addiction and Recovery Memoir',NULL),(136,'Family Memoir','Family Memoir',NULL),(137,'Historical Memoir','Historical Memoir',NULL),(138,'Celebrity Memoir','Celebrity Memoir',NULL),(139,'Adventure Memoir','Adventure Memoir',NULL),(140,'Relationship Memoir','Relationship Memoir',NULL),(141,'Inspirational Memoir','Inspirational Memoir',NULL),(142,'Historical Autobiography','Historical Autobiography',NULL),(143,'Celebrity Autobiography','Celebrity Autobiography',NULL),(144,'Political Autobiography','Political Autobiography',NULL),(145,'Adventure Autobiography','Adventure Autobiography',NULL),(146,'Spiritual Autobiography','Spiritual Autobiography',NULL),(147,'Scientific Autobiography','Scientific Autobiography',NULL),(148,'Business Autobiography','Business Autobiography',NULL),(149,'Sports Autobiography','Sports Autobiography',NULL),(150,'Artistic Autobiography','Artistic Autobiography',NULL),(151,'Philosophical Autobiography','Philosophical Autobiography',NULL),(152,'Historical Biography','Historical Biography',NULL),(153,'Celebrity Biography','Celebrity Biography',NULL),(154,'Political Biography','Political Biography',NULL),(155,'Adventure Biography','Adventure Biography',NULL),(156,'Literary Biography','Literary Biography',NULL),(157,'Scientific Biography','Scientific Biography',NULL),(158,'Business Biography','Business Biography',NULL),(159,'Sports Biography','Sports Biography',NULL),(160,'Artistic Biography','Artistic Biography',NULL),(161,'Philosophical Biography','Philosophical Biography',NULL),(162,'City Guide','City Guide',NULL),(163,'Country Guide','Country Guide',NULL),(164,'Adventure Travel Guide','Adventure Travel Guide',NULL),(165,'Cultural Travel Guide','Cultural Travel Guide',NULL),(166,'Historical Travel Guide','Historical Travel Guide',NULL),(167,'Nature & Wildlife Guide','Nature & Wildlife Guide',NULL),(168,'Road Trip Guide','Road Trip Guide',NULL),(169,'Beach & Island Guide','Beach & Island Guide',NULL),(170,'Culinary Travel Guide','Culinary Travel Guide',NULL),(171,'Budget Travel Guide','Budget Travel Guide',NULL),(172,'Solo Travel Journal','Solo Travel Journal',NULL),(173,'Adventure Travel Journal','Adventure Travel Journal',NULL),(174,'Cultural Immersion Journal','Cultural Immersion Journal',NULL),(175,'Road Trip Journal','Road Trip Journal',NULL),(176,'Backpacking Journal','Backpacking Journal',NULL),(177,'Nature Exploration Journal','Nature Exploration Journal',NULL),(178,'Spiritual Journey Journal','Spiritual Journey Journal',NULL),(179,'Family Vacation Journal','Family Vacation Journal',NULL),(180,'Gap Year Journal','Gap Year Journal',NULL),(181,'Expat Diary','Expat Diary',NULL),(182,'Business Strategy','Business Strategy',NULL),(183,'Medical/Healthcare','Medical/Healthcare',NULL),(184,'Psychological Analysis','Psychological Analysis',NULL),(185,'Social Research','Social Research',NULL),(186,'Environmental Studies','Environmental Studies',NULL),(187,'Technology Implementation','Technology Implementation',NULL),(188,'Marketing Effectiveness','Marketing Effectiveness',NULL),(189,'Educational Practices','Educational Practices',NULL),(190,'Economic Analysis','Economic Analysis',NULL),(191,'Legal Precedent','Legal Precedent',NULL),(192,'Technology Solutions','Technology Solutions',NULL),(193,'Government Policy','Government Policy',NULL),(194,'Business Strategies','Business Strategies',NULL),(195,'Medical Advancements','Medical Advancements',NULL),(196,'Financial Models','Financial Models',NULL),(197,'Legal Analysis','Legal Analysis',NULL),(198,'Environmental Concerns','Environmental Concerns',NULL),(199,'Educational Reform','Educational Reform',NULL),(200,'Market Analysis','Market Analysis',NULL),(201,'Product Launch','Product Launch',NULL),(202,'Natural Sciences','Natural Sciences',NULL),(203,'Social Sciences','Social Sciences',NULL),(204,'Humanities','Humanities',NULL),(205,'Engineering','Engineering',NULL),(206,'Medical Studies','Medical Studies',NULL),(207,'Business and Economics','Business and Economics',NULL),(208,'Law Studies','Law Studies',NULL),(209,'Arts and Design','Arts and Design',NULL),(210,'Educational Research','Educational Research',NULL),(211,'Personal/Lifestyle','Personal/Lifestyle',NULL),(212,'Travel','Travel',NULL),(213,'Food & Cooking','Food & Cooking',NULL),(214,'Tech & Gadgets','Tech & Gadgets',NULL),(215,'Health & Wellness','Health & Wellness',NULL),(216,'Business & Marketing','Business & Marketing',NULL),(217,'DIY & Crafts','DIY & Crafts',NULL),(218,'Fashion & Beauty','Fashion & Beauty',NULL),(219,'Entertainment & Pop Culture','Entertainment & Pop Culture',NULL),(220,'News & Current Events','News & Current Events',NULL),(221,'Electronics & Gadgets','Electronics & Gadgets',NULL),(222,'Software & Applications','Software & Applications',NULL),(223,'Machinery & Heavy Equipment','Machinery & Heavy Equipment',NULL),(224,'Automobiles & Vehicles','Automobiles & Vehicles',NULL),(225,'Medical Devices','Medical Devices',NULL),(226,'Household Appliances','Household Appliances',NULL),(227,'Computer Hardware','Computer Hardware',NULL),(228,'Networking Equipment','Networking Equipment',NULL),(229,'Construction Tools','Construction Tools',NULL),(230,'Aerospace & Aviation','Aerospace & Aviation',NULL),(231,'Home & Garden','Home & Garden',NULL),(232,'Technology & Gadgets','Technology & Gadgets',NULL),(233,'Cooking & Baking','Cooking & Baking',NULL),(234,'Crafts & DIY Projects','Crafts & DIY Projects',NULL),(235,'Health & Fitness','Health & Fitness',NULL),(236,'Automotive','Automotive',NULL),(237,'Beauty & Fashion','Beauty & Fashion',NULL),(238,'Finance & Budgeting','Finance & Budgeting',NULL),(239,'Startup','Startup',NULL),(240,'Retail','Retail',NULL),(241,'E-commerce','E-commerce',NULL),(242,'Tech & Software','Tech & Software',NULL),(243,'Healthcare','Healthcare',NULL),(244,'Agriculture','Agriculture',NULL),(245,'Manufacturing','Manufacturing',NULL),(246,'Hospitality','Hospitality',NULL),(247,'Finance & Fintech','Finance & Fintech',NULL),(248,'Education','Education',NULL),(249,'Software & IT','Software & IT',NULL),(250,'Machinery & Equipment Operation','Machinery & Equipment Operation',NULL),(251,'Human Resources & Onboarding','Human Resources & Onboarding',NULL),(252,'Sales & Customer Service','Sales & Customer Service',NULL),(253,'Leadership & Management','Leadership & Management',NULL),(254,'Health & Safety','Health & Safety',NULL),(255,'Product Knowledge','Product Knowledge',NULL),(256,'Language & Communication','Language & Communication',NULL),(257,'Financial Processes','Financial Processes',NULL),(258,'Professional Development','Professional Development',NULL),(259,'Heroic Adventure','Heroic Adventure',NULL),(260,'Historical Recount','Historical Recount',NULL),(261,'Mythological','Mythological',NULL),(262,'Allegory','Allegory',NULL),(263,'Tragic Romance','Tragic Romance',NULL),(264,'Moral & Philosophical Reflections','Moral & Philosophical Reflections',NULL),(265,'War & Battles','War & Battles',NULL),(266,'Quest & Exploration','Quest & Exploration',NULL),(267,'Divine & Supernatural','Divine & Supernatural',NULL),(268,'Cultural & Nationalistic','Cultural & Nationalistic',NULL),(269,'Personal Reflection','Personal Reflection',NULL),(270,'Argumentative/Persuasive','Argumentative/Persuasive',NULL),(271,'Descriptive','Descriptive',NULL),(272,'Expository','Expository',NULL),(273,'Analytical','Analytical',NULL),(274,'Cause and Effect','Cause and Effect',NULL),(275,'Compare and Contrast','Compare and Contrast',NULL),(276,'Problem-Solution','Problem-Solution',NULL),(277,'Pop','Pop',NULL),(278,'Rock','Rock',NULL),(279,'R&B/Soul','R&B/Soul',NULL),(280,'Hip-Hop/Rap','Hip-Hop/Rap',NULL),(281,'Country','Country',NULL),(282,'Jazz','Jazz',NULL),(283,'Blues','Blues',NULL),(284,'Electronic/Dance','Electronic/Dance',NULL),(285,'Folk','Folk',NULL),(286,'Classical/Crossover','Classical/Crossover',NULL),(287,'Inspirational/Motivational','Inspirational/Motivational',NULL),(288,'Ceremonial (e.g., weddings, graduations)','Ceremonial (e.g., weddings, graduations)',NULL),(289,'Persuasive','Persuasive',NULL),(290,'Informative','Informative',NULL),(291,'Commemorative','Commemorative',NULL),(292,'Entertainment','Entertainment',NULL),(293,'Business/Corporate','Business/Corporate',NULL),(294,'Technical','Technical',NULL);
/*!40000 ALTER TABLE `genre` ENABLE KEYS */;
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

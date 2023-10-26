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
-- Table structure for table `chat_system_messages`
--

DROP TABLE IF EXISTS `chat_system_messages`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `chat_system_messages` (
  `title` varchar(255) NOT NULL,
  `content` text NOT NULL,
  `message_type` varchar(50) DEFAULT NULL,
  `associated_module` varchar(50) DEFAULT NULL,
  `tags` varchar(255) DEFAULT NULL,
  `version` varchar(50) DEFAULT NULL,
  `is_active` tinyint(1) DEFAULT NULL,
  `id` int NOT NULL AUTO_INCREMENT,
  `created` timestamp NULL DEFAULT NULL,
  `created_by_id` int DEFAULT NULL,
  `modified` timestamp NULL DEFAULT NULL,
  `modified_by_id` int DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `created_by_id` (`created_by_id`),
  KEY `modified_by_id` (`modified_by_id`),
  CONSTRAINT `chat_system_messages_ibfk_1` FOREIGN KEY (`created_by_id`) REFERENCES `users` (`id`),
  CONSTRAINT `chat_system_messages_ibfk_2` FOREIGN KEY (`modified_by_id`) REFERENCES `users` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=11 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `chat_system_messages`
--

LOCK TABLES `chat_system_messages` WRITE;
/*!40000 ALTER TABLE `chat_system_messages` DISABLE KEYS */;
INSERT INTO `chat_system_messages` VALUES ('Initialization','As a virtual assistant who helps authors with their writing projects, your mission is to facilitate a harmonious, productive collaboration, enhancing the writer\'s creative journey without intrusion.\r\nTo this end, you may:\r\n   Offer content suggestions during creative droughts,\r\n   Provide proofreading, pacing analysis, and linguistic enhancement,\r\n   Suggest scenarios, character archetypes, themes, and conflicts in line with the story\'s direction,\r\n   Assist in world-building, character depth, and narrative continuity,\r\n   Ensure factual accuracy, cultural sensitivity, and tone consistency, or\r\n   Help craft synopses, evaluate tension, or review submittal letters post-completion.\r\nYou shall:\r\n   Maintain a responsive, supportive posture and allow the author to craft the narrative unless explicitly asked to contribute,\r\n   Deliver concise, context-aware solutions without straying beyond the scope of the request,\r\n   While your expertise is valuable, the writer\'s vision remains paramount,\r\n   Provide guidance, do not try to force the narrative in a particular direction,\r\n   Retain the context of ongoing narratives, ensuring alignment and relevance in all interactions, and\r\n   Prioritize continuity and coherence in feedback and suggestions.\r\nYour primary purpose is to serve as a supportive, collaborative assistant in the creative writing journey, accelerating the writing process and elevating the quality of the author\'s writing without superseding their creativity.','instruction','2','','',1,2,'2023-10-24 11:05:21',NULL,'2023-10-24 12:09:54',NULL),('Help Context Message','The following explains intended use of the page that is currently loaded','instruction','2','','',1,3,'2023-10-24 11:34:10',NULL,'2023-10-24 12:10:35',NULL),('Page Content Message','The following content was extracted from the page the user is currently working on','instruction','2','','',1,4,'2023-10-24 11:35:08',NULL,'2023-10-24 22:00:17',NULL),('System Greeting Message','You are starting a new conversation. Come up with a greeting that demonstrates your understanding of what the user is working on while offering some appropriate support.','instruction','2','','',1,5,'2023-10-24 11:37:35',NULL,'2023-10-24 12:11:22',NULL),('Update System Message','Based on the current page content, update the Content of the system message.','instruction','2','','',1,6,'2023-10-24 22:40:59',NULL,'2023-10-24 22:59:49',NULL),('Update Help Context','Based on the information included in the current page, update the content of this system message to concisely explain the page described.','instruction','2','','',1,7,'2023-10-24 23:02:23',NULL,'2023-10-24 23:02:23',NULL),('Update Project Template Description','Based on the content extracted from this page, describe the outputs from this type of writing project. Stick to the outputs and not the process or components of the project itself. Your response should be concise and authoritative. You do not need to provide any justification for the result. It should be a single paragraph consisting of two to five sentences.','instruction','2','','',1,8,'2023-10-24 23:03:58',NULL,'2023-10-24 23:06:53',NULL),('Update Project Template Methodology','Based on the content extracted from this page, describe the process for this type of writing project. Each step in the process should be on a separate line, and concisely describe what is required at that step. For example:\r\n1) Plan: Write a plan for how to complete the project\r\n2) Gather Ideas: Gather some ideas to write about\r\n3) Write It Down: Just write. Don\'t worry about the technical aspects or details of your writing.\r\n4) Review and Review: Read it through, revising the narrative as you go.\r\n5) Proofread: Once again, read it through and correct any spelling, grammar, punctuation and other technical errors.\r\n6) Peer Review: Share it with someone who will provide constructive criticism and advice.\r\n7) Finalize: Incorporate comments and revise accordingly.\r\n8) Publish: Get it published. Be tenacious and persistent and be prepared to be rejected. That is just part of the process.','instruction','2','','',1,9,'2023-10-24 23:14:29',NULL,'2023-10-24 23:14:29',NULL),('Update Project Template Structure','In the current context, Structure refers to the organization of Collections and StoryParts in the project. A StoryPart is an element of the story: a chapter, a character, a setting, etc. A StoryPart has a title, description, text content, images, and other properties that allow it to be rendered into the final output as needed.\r\nCollections contain many StoryParts. A writing project may contain many StoryParts, and it may contain many Collections. StoryParts may also contain many Collections. This nested tree forms the framework in which the project is developed.\r\nFor example, the structure of a project template for short stories might look like this:\r\n{\r\n  \"Manuscript\": {\r\n    \"Description\": \"A manuscript is the complete text of a short story and may be made up of multiple scenes.\"\r\n    \"Scenes\": []\r\n  },\r\n  \"Characters\": [],\r\n  \"Locations\": []\r\n}\r\nThis template structure contains one story part (Manuscript) and two collections (Characters and Locations). The Characters and Locations Collections are currently empty. The Manuscript contains a Collection called Scenes which is also currently empty.\r\nBased on the description and methodology of the current project template, determine what components are likely to be produced and provide a general structure that can be applied to as broad a range of projects of the given type as possible.','instruction','2','','',1,10,'2023-10-24 23:52:36',NULL,'2023-10-25 00:21:02',NULL);
/*!40000 ALTER TABLE `chat_system_messages` ENABLE KEYS */;
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

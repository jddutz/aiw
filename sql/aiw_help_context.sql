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
-- Table structure for table `help_context`
--

DROP TABLE IF EXISTS `help_context`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `help_context` (
  `context_id` varchar(128) NOT NULL,
  `title` varchar(128) NOT NULL,
  `content` text NOT NULL,
  `id` int NOT NULL AUTO_INCREMENT,
  `created` timestamp NULL DEFAULT NULL,
  `created_by_id` int DEFAULT NULL,
  `modified` timestamp NULL DEFAULT NULL,
  `modified_by_id` int DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `ix_help_context_context_id` (`context_id`),
  UNIQUE KEY `ix_help_context_title` (`title`),
  KEY `created_by_id` (`created_by_id`),
  KEY `modified_by_id` (`modified_by_id`),
  CONSTRAINT `help_context_ibfk_1` FOREIGN KEY (`created_by_id`) REFERENCES `users` (`id`),
  CONSTRAINT `help_context_ibfk_2` FOREIGN KEY (`modified_by_id`) REFERENCES `users` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=14 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `help_context`
--

LOCK TABLES `help_context` WRITE;
/*!40000 ALTER TABLE `help_context` DISABLE KEYS */;
INSERT INTO `help_context` VALUES ('help_context.list','Help Context List','The \"Help Context List\" page allows an administrator to search the available help context entries used to provide additional information about the intended use of various pages. From this page, the administrator can choose to view the details of a particular help context entry.',2,'2023-10-24 18:04:22',NULL,'2023-10-24 18:57:35',NULL),('help_context.create','Create Help Context','The \"Create Help Context\" page allows an administrator to specify the details when creating a new help context entry. Help context entries are used to provide the AI assistant with clues about the intended use of a particular page. Help Context ID is a unique identifier that is derived from the routing of the page. Title is a readable identifier that provides a brief description of the help context entry. Content is a detailed explanation of the intended use of the page including form fields and the various elements that can be found on the page. ',3,'2023-10-24 18:18:55',NULL,'2023-10-24 18:57:14',NULL),('help_context.edit','Edit Help Context','The \"Edit Help Context\" page allows administrators to specify the details when creating a new help context entry. Help context entries are used to provide the AI assistant with clues about the intended use of a particular page.\r\nThis page includes the following fields:\r\nHelp Context ID: Enter a unique identifier for the help context. The help context ID is derived from the routing of the page and is used to associate the help context entry with the specific page.\r\nTitle: Provide a brief, readable identifier for the help context entry. This title should succinctly describe the purpose or functionality of the page.\r\nContent: In this section, provide a detailed explanation of the intended use of the page, including the various form fields and elements that can be found on the page. Be sure to include any specific instructions or guidelines for administrators when creating a help context entry for this page.\r\nCreate: Clicking this button will create the help context entry with the specified details. Once created, the help context entry will be associated with the corresponding page and will be used to guide the AI assistant in providing context-aware suggestions and assistance.\r\nBack to Index: This link will take you back to the index page of the help context management system, allowing you to view and manage all existing help context entries.\r\nRemember that providing accurate and comprehensive help context entries helps the AI assistant better understand and assist users in their tasks. It is important to ensure that the help context entry accurately reflects the intended use and functionality of the page.',4,'2023-10-24 18:23:20',NULL,'2023-10-24 18:23:20',NULL),('help_context.detail','Help Context Details','The \"Help Context Details\" page provides a detailed view of a specific help context entry, which is a foundational part of the AI Writer app. Each entry assists in guiding users on a particular page or component of the app. This detailed view allows Administrators and potentially other users to view, edit, or delete the entry, ensuring that the app\'s help documentation remains up-to-date and relevant.\r\n\r\nFields:\r\n- Context ID: Displayed at the top, this field represents a unique identifier for the help context entry. It provides a quick reference for users and developers alike to understand the context and its associated page or component.\r\n- Title: This field displays the title of the help context entry. It gives a quick overview of the purpose or subject of the help content.\r\n- Content: This is the main body of the help context entry. Displayed paragraph-by-paragraph, it provides detailed instructions, guidance, or explanations about the associated page or component. Content is structured for easy reading and understanding.\r\n\r\nActions:\r\n- Edit: The pencil icon near the context ID is an actionable button that directs users to an edit page, allowing them to modify the title, content, or other details of the help context entry.\r\n- Delete: Clicking on this button triggers a modal dialog prompting the user to confirm the deletion of the help context entry. If confirmed, the entry will be removed from the system. Deleting a help context is irreversible, so users should be cautious and ensure they have backup or documentation before proceeding with this action. \r\n- Back to Index: This link will take users back to the list of all available help context entries, allowing them to view and manage the entire collection.\r\n',5,'2023-10-24 18:27:17',NULL,'2023-10-25 03:34:14',NULL),('system_message.list','System Messages','The \"System Messages\" page is where administrators can view and manage system messages. System messages are used to provide important information or instructions to users and AI assistants. On this page, administrators can create new system messages, search for existing messages, and view a list of all system messages.\r\nTo create a new system message, click on the \"Create\" button. This will redirect you to the page where you can enter the details of the message.\r\nTo search for a specific system message, use the search form located at the top right corner of the page. Enter the keywords related to the message you are looking for and click on the search button. The list of system messages will be filtered based on your search query.\r\nBelow the search form, you will find a list of all system messages. Each system message is displayed as a clickable item with its title and a brief description. Clicking on a system message will take you to the page where you can view and edit the message details.',6,'2023-10-24 18:30:57',NULL,'2023-10-24 18:30:57',NULL),('system_message.create','Create System Message','The \"Create System Message\" page allows an administrator to create a new system message. Here are the details of the form:\r\n\r\n- Title: The administrator can enter the title of the system message. It is a required field.\r\n- Content: The administrator can enter the content of the system message. It is a required field and accepts multiple lines of text.\r\n- Type: The administrator can select the type of the system message from a dropdown list. The available option is \"Instructional\".\r\n- Associated Module: The administrator can select the associated module for the system message from a dropdown list. The available option is \"2\".\r\n- Tags: The administrator can enter tags for the system message. It is an optional field.\r\n- Version: The administrator can enter the version for the system message. It is an optional field.\r\n- Active: The administrator can check a checkbox to indicate if the system message is active.\r\n\r\nThe administrator can click the \"Create\" button to submit the form and create the system message. There is also a \"Back to Index\" button to go back to the index page.',7,'2023-10-24 18:34:54',NULL,'2023-10-24 18:34:54',NULL),('system_message.edit','Edit System Message','The \"Edit System Message\" page allows an administrator to edit a system message. System messages are used to provide important information or instructions to users and AI assistants.\r\n\r\nForm Fields:\r\n- Title: The title of the system message. This field is required and has a maximum length of 255 characters.\r\n- Content: The content of the system message. This field is required and allows for multi-line text with a maximum of 10 rows.\r\n- Type: The type of the system message. There are currently only two types of system messages:\r\n  1) Instructional: This type of system message is sent to an AI assistant as instructions to perform a specific task\r\n  2) User: Messages used to convey information to the user such as error messages, or system status notifications\r\n- Associated Module: The module associated with the system message. This field is pre-selected as \"2\" from a dropdown menu.\r\n- Tags: Tags associated with the system message. This field is optional and allows for multiple tags separated by commas.\r\n- Version: The version of the system message. This field is optional and has a maximum length of 50 characters.\r\n- Active: A checkbox to indicate whether the system message is active or not. This field is pre-selected as checked.\r\n\r\nActions:\r\n- Save Changes: Clicking this button will save the changes made to the system message.\r\n- Back to Index: Clicking this button will take the user back to the index page for system messages.\r\n',8,'2023-10-24 18:38:50',NULL,'2023-10-25 04:57:12',NULL),('system_message.detail','System Message Details','The \"System Message Details\" page displays the details of a system message and its content in a read-only format. It does not allow for editing or updating of the system message\'s content. The page provides the following information:\r\n\r\n- Title: The title of the system message.\r\n- Content: The content of the system message.\r\n- Type: The type of the system message, which is typically \"Instructional\".\r\n- Associated Module: The module associated with the system message.\r\n- Tags: Any tags associated with the system message.\r\n- Version: The version of the system message.\r\n- Active: Indicates if the system message is currently active.\r\n\r\nIf you need to update the content of a system message, you would need to go to the edit page for that specific system message.',9,'2023-10-24 18:41:18',NULL,'2023-10-24 18:41:18',NULL),('project_template.list','Project Templates','The Project Templates page displays a list of project templates. Project templates are pre-designed frameworks that authors can use as a starting point for their writing projects. Each project template represents a specific type of writing project, such as a short story, novel, screenplay, or podcast.\r\n\r\nForm Fields:\r\n- \"Create a new Project Template\" button: Clicking this button will navigate the user to the page for creating a new project template.\r\n- Search Form: This form allows users to search for specific project templates by entering keywords in the search input field and clicking the search button.\r\n- Project Template List: This list displays the available project templates. Each project template is represented as a list item with a clickable link. The list items contain the following elements:\r\n- Project Template Title: The title of the project template.\r\n- Last Modified Date: The date when the project template was last modified.\r\n- Project Template Description: A brief description of the project template.\r\n',10,'2023-10-24 18:44:29',NULL,'2023-10-24 18:44:29',NULL),('project_template.detail','Project Template Details','The \"Project Template Details\" page shows the details of a project template, which are used to define the structure of a new writing project. This page provides administrators with the necessary information to understand and work with different project templates effectively.\r\n\r\nFields:\r\n- Description: This field provides a description of the project template. Administrators can use this field to provide a brief overview of the project template\'s purpose, theme, or any specific characteristics that distinguish it from other templates.\r\n- Methodology: This field describes the typical methodology or approach to this type of project. Administrators can use this field to outline the recommended steps, techniques, or processes for executing a project based on this template. This information can help writers understand the creative and technical aspects involved in using the template.\r\n- Length: This field describes the typical length of the project in terms of word count, page count, or other relevant measures. Administrators can use this field to provide an estimate or range of the project\'s size, helping writers gauge the scope and expectations associated with the template.\r\n- Genres: This field lists the genres typically associated with the type of project. Administrators can use this field to specify the genres that align with the template, such as romance, science fiction, mystery, fantasy, etc. This information helps writers choose a template based on their preferred genre or explore templates within specific genres.\r\n- Tags: This field includes identifiers and search terms that may be affiliated with this type of project. Administrators can use this field to add relevant keywords, phrases, or categories that can help users discover or filter project templates. Tags can cover a wide range of considerations, such as target audience, setting, tone, or any other relevant thematic or stylistic aspects.\r\n\r\nActions:\r\n- Save Changes: Clicking this button will save any changes made to the project template details.\r\n- Back to Index: This link will take administrators back to the project template list, allowing them to view and manage all existing project templates.\r\n',11,'2023-10-24 18:51:25',NULL,'2023-10-24 18:53:37',NULL),('project_template.edit','Edit Project Template','The \"Edit Project Template\" page is designed to edit existing project templates. Administrators or designated users can define the core attributes of a project template, such as category, template name, description, and others. This makes it easier for authors to select a template that fits their project\'s requirements.\r\nA project template is made up of StoryParts and Collections of StoryParts. These components may represent any element in the writing: chapters, scenes, characters, settings, etc.\r\n\r\nFields:\r\n- Category: This dropdown field allows users to select a category for the project template. The category helps in classifying templates based on their type or use case.\r\n- Template Name: A descriptive name for the project template. It helps users identify and differentiate between various templates.\r\n- Description: A description of the type of writing output that is expected. This field should be a single paragraph with just a few sentences.\r\n- Methodology: A deeper insight into the preferred approach or steps related to this template. This field provides generalized step-by-step instructions to complete this type of project from developing the concept to sharing with others.\r\n- Length: An estimate or range of the project\'s size in terms of word count, page count, or other relevant measures.\r\n- Links: Additional references or resources related to the template. Users can provide multiple links separated by semicolons.\r\n- Structure (JSON format): The underlying structure of the project in a serialized JSON format. This structure will be used to establish the initial Collections and StoryParts when a project is created.\r\n- Image Reference: A link or identifier for a visual representation or thumbnail associated with the project template. This image can provide a quick visual cue about the template\'s theme or content.\r\n\r\nActions:\r\n- Save Changes: This button will save the changes to the project template and update the database.\r\n- Back to Templates: This link will take users back to the list of all project templates, allowing them to view or manage other templates.',12,'2023-10-24 18:56:19',NULL,'2023-10-25 03:50:32',NULL),('project_template.create','Create Project Template','The \"Create Project Template\" page is used by administrators to create a new project template, which is used to define the structure and organization of a new writing project. This page contains the following form fields:\r\n- Category: This is a dropdown list that allows you to select the category of the project template. The current value is \"Fiction,\" but you can choose from other options such as \"Academic/Research,\" \"Comics,\" \"Non-Fiction,\" \"Poetry,\" \"Script,\" \"Specialty Writing,\" or \"Technical.\"\r\n- Template Name: This is a text input field where you can enter the name of the project template. The current value is \"Short Story,\" but you can modify it according to your needs.\r\n- Description: This is a text area where you can provide a description of the project template. The current description explains what a short story is and its characteristics. You can edit this description to suit your project template.\r\n- Methodology: This is a text area where you can describe the methodology or steps involved in creating a project based on this template. The current methodology includes steps like Idea Generation, Research, Outlining, Drafting, Revising, Editing, and Finalizing. You can customize the methodology to align with your specific project needs.\r\n- Length: This is a text input field where you can specify the length of the project created using this template, in terms of page and word count, or any other relevant measure. You can modify this information as required.\r\n- Links: This is a text area where you can include any relevant links related to the project template. Simply separate each link with a semicolon. You can provide links that offer additional resources or references useful for the project.\r\n- Structure: This is a text area where you can provide a serialized JSON structure for the project template. This allows you to define the structure or format in which the project should be organized. The structure consists of StoryParts and Collections of StoryParts. A StoryPart is an element of the story: an act, chapter, scene, character, location, plot feature, map or any other element that could make up part of the finished writing project.\r\n- Image Reference: This is a text input field where you can enter an image reference related to the project template. This can be a URL, file path, or any other reference that helps visualize or represent the project template.\r\n- Create: A button to submit the form and create the project template.\r\n- Back to Templates: A link to navigate back to the list of project templates.',13,'2023-10-24 19:02:30',NULL,'2023-10-24 19:10:02',NULL);
/*!40000 ALTER TABLE `help_context` ENABLE KEYS */;
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

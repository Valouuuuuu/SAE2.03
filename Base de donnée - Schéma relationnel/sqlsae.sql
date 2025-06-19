-- MySQL dump 10.13  Distrib 8.0.42, for Win64 (x86_64)
--
-- Host: localhost    Database: sql_sae203
-- ------------------------------------------------------
-- Server version	8.0.42

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
-- Table structure for table `enseignant`
--

DROP TABLE IF EXISTS `enseignant`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `enseignant` (
  `ID_Enseignant` int NOT NULL AUTO_INCREMENT,
  `Prenom` varchar(255) NOT NULL,
  `Nom` varchar(255) NOT NULL,
  `Email` varchar(255) NOT NULL,
  PRIMARY KEY (`ID_Enseignant`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `enseignant`
--

LOCK TABLES `enseignant` WRITE;
/*!40000 ALTER TABLE `enseignant` DISABLE KEYS */;
/*!40000 ALTER TABLE `enseignant` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `etudiant`
--

DROP TABLE IF EXISTS `etudiant`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `etudiant` (
  `ID_Etudiant` int NOT NULL AUTO_INCREMENT,
  `Prenom` varchar(255) NOT NULL,
  `Nom` varchar(255) NOT NULL,
  `Email` varchar(255) NOT NULL,
  `Groupe` varchar(20) NOT NULL,
  `Photo` blob,
  PRIMARY KEY (`ID_Etudiant`),
  UNIQUE KEY `Email` (`Email`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `etudiant`
--

LOCK TABLES `etudiant` WRITE;
/*!40000 ALTER TABLE `etudiant` DISABLE KEYS */;
/*!40000 ALTER TABLE `etudiant` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `examen`
--

DROP TABLE IF EXISTS `examen`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `examen` (
  `ID_Examen` int NOT NULL AUTO_INCREMENT,
  `Nom` varchar(255) NOT NULL,
  `Date` date NOT NULL,
  `Coefficient` float NOT NULL,
  `ID_Ressource` int NOT NULL,
  `ID_Enseignant` int DEFAULT NULL,
  PRIMARY KEY (`ID_Examen`),
  KEY `fk_examen_ressource` (`ID_Ressource`),
  KEY `fk_examen_enseignant` (`ID_Enseignant`),
  CONSTRAINT `fk_examen_enseignant` FOREIGN KEY (`ID_Enseignant`) REFERENCES `enseignant` (`ID_Enseignant`) ON DELETE SET NULL ON UPDATE CASCADE,
  CONSTRAINT `fk_examen_ressource` FOREIGN KEY (`ID_Ressource`) REFERENCES `ressource` (`ID_Ressource`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `examen`
--

LOCK TABLES `examen` WRITE;
/*!40000 ALTER TABLE `examen` DISABLE KEYS */;
/*!40000 ALTER TABLE `examen` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `note`
--

DROP TABLE IF EXISTS `note`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `note` (
  `ID_Note` int NOT NULL AUTO_INCREMENT,
  `Note` float NOT NULL,
  `Appreciation` text NOT NULL,
  `ID_Etudiant` int NOT NULL,
  `ID_Examen` int NOT NULL,
  PRIMARY KEY (`ID_Note`),
  UNIQUE KEY `uq_note_etudiant_examen` (`ID_Etudiant`,`ID_Examen`),
  KEY `fk_note_examen` (`ID_Examen`),
  CONSTRAINT `fk_note_etudiant` FOREIGN KEY (`ID_Etudiant`) REFERENCES `etudiant` (`ID_Etudiant`) ON DELETE CASCADE ON UPDATE CASCADE,
  CONSTRAINT `fk_note_examen` FOREIGN KEY (`ID_Examen`) REFERENCES `examen` (`ID_Examen`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `note`
--

LOCK TABLES `note` WRITE;
/*!40000 ALTER TABLE `note` DISABLE KEYS */;
/*!40000 ALTER TABLE `note` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `ressource`
--

DROP TABLE IF EXISTS `ressource`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `ressource` (
  `ID_Ressource` int NOT NULL AUTO_INCREMENT,
  `UE_ID` int NOT NULL,
  `Nom` varchar(255) NOT NULL,
  `Description` text NOT NULL,
  PRIMARY KEY (`ID_Ressource`),
  KEY `fk_ressource_ue` (`UE_ID`),
  CONSTRAINT `fk_ressource_ue` FOREIGN KEY (`UE_ID`) REFERENCES `ue` (`ID_UE`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `ressource`
--

LOCK TABLES `ressource` WRITE;
/*!40000 ALTER TABLE `ressource` DISABLE KEYS */;
/*!40000 ALTER TABLE `ressource` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `ue`
--

DROP TABLE IF EXISTS `ue`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `ue` (
  `ID_UE` int NOT NULL AUTO_INCREMENT,
  `Nom` varchar(255) NOT NULL,
  `Semestre` int NOT NULL,
  `Credits` int NOT NULL,
  PRIMARY KEY (`ID_UE`),
  UNIQUE KEY `uq_ue_nom_semestre` (`Nom`,`Semestre`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `ue`
--

LOCK TABLES `ue` WRITE;
/*!40000 ALTER TABLE `ue` DISABLE KEYS */;
/*!40000 ALTER TABLE `ue` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2025-06-10 16:08:55

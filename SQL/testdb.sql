-- MySQL dump 10.13  Distrib 8.0.21, for Win64 (x86_64)
--
-- Host: localhost    Database: testdb
-- ------------------------------------------------------
-- Server version	8.0.21

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
-- Dumping data for table `students`
--

LOCK TABLES `students` WRITE;
/*!40000 ALTER TABLE `students` DISABLE KEYS */;
INSERT INTO `students` (`ID`, `name`, `mark`) VALUES (100000,'Paul Breitner',87),(100001,'Jessica Jones',77),(100002,'Luke Cage',66),(100003,'Alen Jones',66),(100004,'Ron Dex',45),(100005,'Amy Dentz',50),(100006,'Lucy Lam',80),(100007,'Adam Berts',90),(100008,'David Suiter',35),(100009,'Jess Jones',72),(100010,'Alex Carter',88),(100011,'Rony Dolton',48),(100012,'Alice Denis',52),(100013,'Lara Lin',81),(100014,'Aden Banner',92),(100015,'Dania Sutler',39),(100016,'Jessy James',74),(100017,'Alia Camil',87),(100018,'Ortega Gomez',76),(100019,'Lian Lyn',89),(100020,'Adonis Bas',93),(100021,'Daneka Semens',32),(100022,'Jasper James',73),(100023,'Amos Cahan',86),(100024,'Oliver Gotez',77),(100025,'Amir Baber',93),(100026,'Daisy Suns',40),(100027,'Jaime Julz',71),(100028,'Axel Castor',86),(100029,'Orelia Gomez',76),(100030,'Lena Lin',90),(100031,'Apolo Creed',92),(100032,'Damia Semar',33),(100033,'Jamal Jones',72),(100034,'Aria Calian',85),(100035,'Olena Golez',77),(100036,'Adolf Baits',90),(100037,'Dona Stone',37),(100038,'Julie Jaan',71),(100039,'Aster Cruz',86),(100040,'Lama Lyn',89);
/*!40000 ALTER TABLE `students` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2023-11-03 14:45:30

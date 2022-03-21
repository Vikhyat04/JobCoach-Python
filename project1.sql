-- MySQL dump 10.10
--
-- Host: localhost    Database: project
-- ------------------------------------------------------
-- Server version	5.0.17-nt

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `construction`
--

DROP TABLE IF EXISTS `construction`;
CREATE TABLE `construction` (
  `Jobs` varchar(100) default NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `construction`
--


/*!40000 ALTER TABLE `construction` DISABLE KEYS */;
LOCK TABLES `construction` WRITE;
INSERT INTO `construction` VALUES ('Plumber'),('Electrician'),('Carpenter'),('Mason'),('Sheet metal worker'),('Equipment operator'),('Glazier'),('Construction Laboreres and Helpers'),('Hazardous Material Removers'),('Ironworkers'),('Solar PV Installers'),('AC Installers'),('Elevator Mechanic'),('Crane Operator'),('Equipment Operator'),('Signal Worker'),('Heavy Equipment Operator'),('Roofer'),('Concrete Laborers'),('Plumber'),('Pipe Fitter'),('Boilermaker'),('Siding Contractor'),('Apprentice'),('Painter'),('General Laborer'),('Ceiling Tile Installer'),('Plasterer'),('Joiner'),('Dry Wall Installer'),('Framing Carpenter'),('Dry wall Finisher'),('Construction Inspector'),('Technician'),('Quantity Surveyor');
UNLOCK TABLES;
/*!40000 ALTER TABLE `construction` ENABLE KEYS */;

--
-- Table structure for table `manufacture`
--

DROP TABLE IF EXISTS `manufacture`;
CREATE TABLE `manufacture` (
  `Jobs` varchar(100) default NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `manufacture`
--


/*!40000 ALTER TABLE `manufacture` DISABLE KEYS */;
LOCK TABLES `manufacture` WRITE;
INSERT INTO `manufacture` VALUES ('Assembler'),('Boiler Operator'),('Boilermaker'),('Bookbinder and Bindery worker'),('Electronic Assembler'),('Expediter'),('Fabricator'),('Fiberglass Laminator'),('Floor Assembler'),('General Laborer'),('Material Handler'),('Packaging Engineer'),('Painting and Coating Worker'),('Photographic Processor'),('Precision Assembler'),('Processing Worker'),('Production Painter'),('Production Worker'),('Semiconductor Processor'),('Tool and Die Maker'),('Tool Crib attendent'),('Warehouse Worker'),('Woodworker'),('Brazer'),('Cutter'),('Metal Worker'),('Solderer'),('Structural Metal Fabricator'),('Weldor'),('Assemble Supervisor'),('Machinist'),('Operator'),('Plastic Machine Worker'),('Process Operator'),('Electrician'),('Vehicle Parts repairer'),('Food Mill Worker'),('Garment Worker'),('Textile Worker'),('Apparel Worker');
UNLOCK TABLES;
/*!40000 ALTER TABLE `manufacture` ENABLE KEYS */;

--
-- Table structure for table `personal_details`
--

DROP TABLE IF EXISTS `personal_details`;
CREATE TABLE `personal_details` (
  `Sno` int(11) NOT NULL,
  `Questions` varchar(200) default NULL,
  PRIMARY KEY  (`Sno`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `personal_details`
--


/*!40000 ALTER TABLE `personal_details` DISABLE KEYS */;
LOCK TABLES `personal_details` WRITE;
INSERT INTO `personal_details` VALUES (1,'Full Name'),(2,'Age'),(3,'Highest Level of Education'),(4,'Phone Number'),(5,'Gender'),(6,'Region of Origin'),(7,'Number of Languages known'),(8,'Highest Level of Expertise in Language'),(9,'Maritial Status'),(10,'Drivers License');
UNLOCK TABLES;
/*!40000 ALTER TABLE `personal_details` ENABLE KEYS */;

--
-- Table structure for table `service`
--

DROP TABLE IF EXISTS `service`;
CREATE TABLE `service` (
  `Jobs` varchar(100) default NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `service`
--


/*!40000 ALTER TABLE `service` DISABLE KEYS */;
LOCK TABLES `service` WRITE;
INSERT INTO `service` VALUES ('tailor'),('gardener'),('security gaurd'),('janitor'),('delivery person'),('driver'),('cook'),('caregivers'),('military'),('coastguard'),('police'),('firefighter'),('beautician'),('hairstylist'),('server'),('call center representative'),('baker worker'),('bangle seller'),('blacksmithy'),('boat/ferry occupation'),('book binding'),('bicycle repair'),('butchery'),('cable TV operation'),('carpentary'),('catering'),('carpet weaving'),('clubs and canteen services'),('domestic work'),('embroidery work'),('fisherman'),('honey gathering'),('Newspaper and Magazine distributor'),('Plantation'),('Pottery'),('Powerloom weaving'),('Rag picking'),('Rickshaw pulling'),('service station work'),('tanning'),('telephone booth service'),('toy making'),('laundry work'),('sweeping'),('shoe shinning work');
UNLOCK TABLES;
/*!40000 ALTER TABLE `service` ENABLE KEYS */;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;


-- --------------------------------------------------------
-- Host:                         C:\Users\2087\Desktop\REPO\pw-z.github.io\code\trivial\java-web-fundamentals\sqliteDB.db
-- Server version:               3.38.0
-- Server OS:                    
-- HeidiSQL Version:             12.0.0.6468
-- --------------------------------------------------------

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET NAMES  */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;


-- Dumping database structure for sqliteDB
CREATE DATABASE IF NOT EXISTS "sqliteDB";
;

-- Dumping structure for table sqliteDB.GUITAR
CREATE TABLE IF NOT EXISTS GUITAR(id VARCHAR(50) PRIMARY KEY, brand VARCHAR(10), type VARCHAR(10));

-- Dumping data for table sqliteDB.GUITAR: 5 rows
/*!40000 ALTER TABLE "GUITAR" DISABLE KEYS */;
INSERT INTO "GUITAR" ("id", "brand", "type") VALUES
	('1', 'Fender', 'Stratocaster'),
	('2', 'Fender', 'Telecaster'),
	('3', 'Gibson', 'Les Paul'),
	('4', 'Epiphone', 'Les Paul'),
	('5', 'TEMPFender', 'TEMPStratocaster');
/*!40000 ALTER TABLE "GUITAR" ENABLE KEYS */;

/*!40103 SET TIME_ZONE=IFNULL(@OLD_TIME_ZONE, 'system') */;
/*!40101 SET SQL_MODE=IFNULL(@OLD_SQL_MODE, '') */;
/*!40014 SET FOREIGN_KEY_CHECKS=IFNULL(@OLD_FOREIGN_KEY_CHECKS, 1) */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40111 SET SQL_NOTES=IFNULL(@OLD_SQL_NOTES, 1) */;

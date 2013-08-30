DROP TABLE IF EXISTS `ajaxj`.`movcat`;
CREATE TABLE  `ajaxj`.`movcat` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `ename` varchar(45) DEFAULT NULL,
  `name` varchar(45) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=1 DEFAULT CHARSET=utf8;

DROP TABLE IF EXISTS `ajaxj`.`mov`;
CREATE TABLE  `ajaxj`.`mov` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `title` varchar(200) DEFAULT NULL,
  `banben` varchar(50) DEFAULT NULL,
  `arts` varchar(200) DEFAULT NULL,
  `dc` varchar(100) DEFAULT NULL,
  `lang` varchar(50) DEFAULT NULL,
  `location` varchar(50) DEFAULT NULL,
  `pubdate` varchar(50) DEFAULT NULL,
  `status` varchar(50) DEFAULT NULL,
  `year` varchar(50) DEFAULT NULL,
  `contents` varchar(10000) DEFAULT NULL,
  `img` varchar(200) DEFAULT NULL,
  `fromto` varchar(20) DEFAULT NULL,
  `category_id` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `category_id` (`category_id`),
  CONSTRAINT `mov_ibfk_1` FOREIGN KEY (`category_id`) REFERENCES `movcat` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=1 DEFAULT CHARSET=utf8;

DROP TABLE IF EXISTS `ajaxj`.`movdetail`;
CREATE TABLE  `ajaxj`.`movdetail` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `tp` int(11) DEFAULT NULL,
  `url` varchar(255) DEFAULT NULL,
  `mov_id` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `mov_id` (`mov_id`),
  CONSTRAINT `movdetail_ibfk_1` FOREIGN KEY (`mov_id`) REFERENCES `mov` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
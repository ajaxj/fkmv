DROP TABLE IF EXISTS `ajaxj`.`mv_movie_hakuzycat`;
CREATE TABLE  `ajaxj`.`mv_movie_hakuzycat` (
  `id` int(10) unsigned NOT NULL AUTO_INCREMENT,
  `name` varchar(45) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=MyISAM AUTO_INCREMENT=17 DEFAULT CHARSET=utf8;



DROP TABLE IF EXISTS `ajaxj`.`mv_movie_hakuzy`;
CREATE TABLE  `ajaxj`.`mv_movie_hakuzy` (
  `id` int(10) unsigned NOT NULL AUTO_INCREMENT,
  `title` varchar(200) DEFAULT NULL,
  `url` varchar(200) DEFAULT NULL,
  `img` varchar(200) DEFAULT NULL,
  `category` varchar(50) DEFAULT NULL,
  `location` varchar(50) DEFAULT NULL,
  `banben` varchar(50) DEFAULT NULL,
  `pubdate` varchar(50) DEFAULT '0000-00-00 00:00:00',
  `lang` varchar(50) DEFAULT NULL,
  `arts` varchar(50) DEFAULT NULL,
  `year` varchar(50) DEFAULT NULL,
  `contents` text,
  `lists` text,
  `tp` varchar(50) DEFAULT NULL,
  `dc` varchar(100) DEFAULT NULL,
  `status` varchar(50) DEFAULT NULL,
  `urltxt` text,
  PRIMARY KEY (`id`)
) ENGINE=MyISAM AUTO_INCREMENT=55971 DEFAULT CHARSET=utf8 COMMENT='hakuzy';



DROP TABLE IF EXISTS `ajaxj`.`mv_hakyzy`;
CREATE TABLE  `ajaxj`.`mv_hakuzy` (
  `id` int(10) unsigned NOT NULL AUTO_INCREMENT,
  `title` varchar(200) DEFAULT NULL,
  `banben` varchar(50) DEFAULT NULL,
  `arts` varchar(200) DEFAULT NULL,
  `dc` varchar(100) DEFAULT NULL,
  `category` varchar(50) DEFAULT NULL,
  `cid` varchar(50) DEFAULT NULL,
  `lang` varchar(50) DEFAULT NULL,
  `location` varchar(50) DEFAULT NULL,
  `pubdate` varchar(50) DEFAULT '0000-00-00 00:00:00',
  `status` varchar(50) DEFAULT NULL,
  `year` varchar(50) DEFAULT NULL,
  `contents` text,
  `img` varchar(200) DEFAULT NULL,
  `urltxt` text,
  `ck` int(10) unsigned DEFAULT '0',
  PRIMARY KEY (`id`)
) ENGINE=MyISAM AUTO_INCREMENT=1 DEFAULT CHARSET=utf8 COMMENT='hakuzy';





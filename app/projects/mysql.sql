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
  PRIMARY KEY (`id`)
) ENGINE=MyISAM AUTO_INCREMENT=52578 DEFAULT CHARSET=utf8 COMMENT='hakuzy';



DROP TABLE IF EXISTS `ajaxj`.`mv_movie_zhuzhu`;
CREATE TABLE  `ajaxj`.`mv_movie_zhuzhu` (
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
  PRIMARY KEY (`id`)
) ENGINE=MyISAM AUTO_INCREMENT=29117 DEFAULT CHARSET=utf8 COMMENT='zhuzhu';


DROP TABLE IF EXISTS `ajaxj`.`mv_movie_dyzy`;
CREATE TABLE  `ajaxj`.`mv_movie_dyzy` (
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
  PRIMARY KEY (`id`)
) ENGINE=MyISAM AUTO_INCREMENT=51910 DEFAULT CHARSET=utf8 COMMENT='dyzy';


DROP TABLE IF EXISTS `ajaxj`.`mv_movie_3444`;
CREATE TABLE  `ajaxj`.`mv_movie_3444` (
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
  PRIMARY KEY (`id`)
) ENGINE=MyISAM AUTO_INCREMENT=33430 DEFAULT CHARSET=utf8 COMMENT='3444';
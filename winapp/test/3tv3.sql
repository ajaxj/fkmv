DROP TABLE IF EXISTS `3tv3`.`zhuzhu_page`;
CREATE TABLE  `3tv3`.`zhuzhu_page` (
  `id` int(10) unsigned NOT NULL AUTO_INCREMENT,
  `pagenum` int(10) unsigned DEFAULT NULL,
  `category` varchar(45) DEFAULT NULL,
  `status` tinyint(1) unsigned DEFAULT '0',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=1 DEFAULT CHARSET=utf8 COMMENT='zhuzhu分类下面的页号';

DROP TABLE IF EXISTS `3tv3`.`zhuzhu_mv`;
CREATE TABLE  `3tv3`.`zhuzhu_mv` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `cateen` varchar(45) DEFAULT NULL COMMENT '分类英文',
  `catecn` varchar(45) DEFAULT NULL COMMENT '分类中文',
  `url` varchar(200) DEFAULT NULL COMMENT '远程地址',
  `title` varchar(100) DEFAULT NULL COMMENT '片名',
  `banben` varchar(45) DEFAULT NULL COMMENT '版本',
  `arts` varchar(200) DEFAULT NULL COMMENT '演员',
  `lang` varchar(45) DEFAULT NULL COMMENT '语言',
  `location` varchar(45) DEFAULT NULL COMMENT '地区',
  `pubdate` varchar(45) DEFAULT NULL COMMENT '发布时间',
  `content` text COMMENT '介绍',
  `list` text COMMENT '地址列表',
  `status` tinyint(3) unsigned DEFAULT '0' COMMENT '状态0初始1抓取补全2修正',
  `img` varchar(255) DEFAULT NULL COMMENT '图片地址',
  `pubyear` varchar(45) DEFAULT NULL COMMENT '出品年',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=1 DEFAULT CHARSET=utf8 ROW_FORMAT=DYNAMIC COMMENT='zhuzhu mv';


DROP TABLE IF EXISTS `3tv3`.`zhuzhu_ls`;
CREATE TABLE  `3tv3`.`zhuzhu_ls` (
  `id` int(10) unsigned NOT NULL AUTO_INCREMENT,
  `mvid` int(10) unsigned DEFAULT NULL,
  `txt` varchar(45) DEFAULT NULL,
  `res` text DEFAULT NULL,
  `url` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

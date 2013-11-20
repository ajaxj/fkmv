-- 3tv3
CREATE DATABASE `3tv3` /*!40100 DEFAULT CHARACTER SET utf8 */;

DROP TABLE IF EXISTS `3tv3`.`suku_page`;
CREATE TABLE  `3tv3`.`suku_page` (
  `id` int(10) unsigned NOT NULL AUTO_INCREMENT,
  `pagenum` int(10) unsigned DEFAULT NULL,
  `category` varchar(45) DEFAULT NULL,
  `status` tinyint(1) unsigned DEFAULT '0',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=1 DEFAULT CHARSET=utf8 COMMENT='suku分类下面的页号';

DROP TABLE IF EXISTS `3tv3`.`suku_mv`;
CREATE TABLE  `3tv3`.`suku_mv` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `cateen` varchar(45) DEFAULT NULL COMMENT '分类英文',
  `catecn` varchar(45) DEFAULT NULL COMMENT '分类中文',
  `url` varchar(200) DEFAULT NULL COMMENT '远程地址',
  `title` varchar(100) DEFAULT NULL COMMENT '片名',
  `banben` varchar(45) DEFAULT NULL COMMENT '版本',
  `arts` varchar(200) DEFAULT NULL COMMENT '演员',
  `location` varchar(45) DEFAULT NULL COMMENT '地区',
  `pubdate` varchar(45) DEFAULT NULL COMMENT '发布时间',
  `content` text COMMENT '介绍',
  `list` text COMMENT '地址列表',
  `status` tinyint(3) unsigned DEFAULT '0' COMMENT '状态0初始1抓取补全2修正',
  `img` varchar(100) DEFAULT NULL COMMENT '图片地址',
  `pubyear` varchar(45) DEFAULT NULL COMMENT '出品年',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=1 DEFAULT CHARSET=utf8 ROW_FORMAT=DYNAMIC COMMENT='suku mv';



DROP TABLE IF EXISTS `3tv3`.`suku_ls`;
CREATE TABLE  `3tv3`.`suku_ls` (
  `id` int(10) unsigned NOT NULL AUTO_INCREMENT,
  `mvid` int(10) unsigned DEFAULT NULL,
  `txt` varchar(45) DEFAULT NULL,
  `res` varchar(500) DEFAULT NULL,
  `url` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

安德的游戏DVD中字

主要演员：阿沙·巴特菲尔德 / 阿比盖尔·布蕾斯琳

最新推荐 ：

影视类别：动作片

拍摄地区：欧美

上映年份：2013

更新时间：2013-11-16 16:40:42




DROP TABLE IF EXISTS `ajaxj1`.`hakuzy`;
CREATE TABLE  `ajaxj1`.`hakuzy` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `catename` varchar(45) DEFAULT NULL COMMENT '分类英文',
  `url` varchar(200) DEFAULT NULL COMMENT '远程地址',
  `status` tinyint(3) unsigned DEFAULT '0' COMMENT '状态0初始1抓取补全2修正',
  `title` varchar(100) DEFAULT NULL COMMENT '片名',
  `banben` varchar(45) DEFAULT NULL COMMENT '版本',
  `arts` varchar(200) DEFAULT NULL COMMENT '演员',
  `dc` varchar(100) DEFAULT NULL COMMENT '导演',
  `lang` varchar(45) DEFAULT NULL COMMENT '语言',
  `location` varchar(45) DEFAULT NULL COMMENT '地区',
  `year` varchar(45) DEFAULT NULL COMMENT '出品年',
  `state` varchar(45) DEFAULT NULL COMMENT '状态',
  `catecn` varchar(45) DEFAULT NULL COMMENT '分类中文',
  `content` text COMMENT '介绍',
  `list` text COMMENT '地址列表',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=7466 DEFAULT CHARSET=utf8 ROW_FORMAT=DYNAMIC;


DROP TABLE IF EXISTS `ajaxj1`.`mv_movie`;
CREATE TABLE  `ajaxj1`.`mv_movie` (
  `id` int(11) NOT NULL,
  `catename` varchar(45) DEFAULT NULL COMMENT '分类英文',
  `title` varchar(100) DEFAULT NULL,
  `banben` varchar(45) DEFAULT NULL,
  `arts` varchar(200) DEFAULT NULL,
  `dc` varchar(100) DEFAULT NULL,
  `lang` varchar(45) DEFAULT NULL,
  `location` varchar(45) DEFAULT NULL,
  `year` varchar(45) DEFAULT NULL,
  `catecn` varchar(45) DEFAULT NULL,
  `content` text,
  `lists` text,
  `img` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 ROW_FORMAT=DYNAMIC;



DROP TABLE IF EXISTS `ajaxj1`.`mv_movie_hakuzy`;
CREATE TABLE  `ajaxj1`.`mv_movie_hakuzy` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `title` varchar(200) DEFAULT NULL,
  `url` varchar(200) DEFAULT NULL,
  `category` varchar(200) DEFAULT NULL,
  `title1` varchar(45) DEFAULT NULL,
  `title2` varchar(45) DEFAULT NULL,
  `pubdate` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  `location` varchar(45) DEFAULT NULL,
  `banben` varchar(45) DEFAULT NULL,
  `arts` varchar(100) DEFAULT NULL,
  `dc` varchar(100) DEFAULT NULL,
  `lang` varchar(45) DEFAULT NULL,
  `status` varchar(50) DEFAULT NULL,
  `year` varchar(45) DEFAULT NULL,
  `content` text,
  `img` varchar(200) DEFAULT NULL,
  `lists` text,
  `ck` tinyint(3) unsigned DEFAULT '0',
  PRIMARY KEY (`id`)
) ENGINE=MyISAM AUTO_INCREMENT=49769 DEFAULT CHARSET=utf8 ROW_FORMAT=DYNAMIC;

DROP TABLE IF EXISTS `ajaxj1`.`mv_qvodzi`;
CREATE TABLE  `ajaxj1`.`mv_qvodzi` (
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
  `content` text,
  `lists` text,
  `tp` varchar(50) DEFAULT NULL,
  `dc` varchar(100) DEFAULT NULL,
  `status` varchar(50) DEFAULT NULL,
  `oldcontent` text,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=23946 DEFAULT CHARSET=utf8 ROW_FORMAT=DYNAMIC COMMENT='qvodzi';


update mv_qvodzi set category = 'dongzuo' where tp = '动作片'

update mv_qvodzi set category = 'aiqing' where tp = '爱情片'

update mv_qvodzi set category = 'kehuan' where tp = '科幻片'

update mv_qvodzi set category = 'kongbu' where tp = '恐怖片'
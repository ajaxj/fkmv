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
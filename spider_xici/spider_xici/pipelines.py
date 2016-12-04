# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

import MySQLdb  


class SpiderXiciPipeline(object):
    def process_item(self, item, spider):

    	DBKWARGS = spider.settings.get('DBKWARGS')

    	con = MySQLdb.connect(**DBKWARGS)
    	cur = con.cursor()

    	sql  = ("INSERT INTO xici_ip(IP,PORT, TYPE, POSITION, SPEED, LAST_CHECK_TIME) "
    		"VALUES(%s, %s, %s, %s, %s, %s)")

    	lis = (item['IP'], item['PORT'], item['TYPE'], item['POSITION'], item['SPEED'], 
    		item['LAST_CHECK_TIME']) 

    	try:
    		cur.execute(sql, lis)
    	except Exception,e:
    		print "Insert error:", e  
    		con.rollback()
    	else:
    		con.commit()

    	cur.close()
    	con.close()
    	

        return item

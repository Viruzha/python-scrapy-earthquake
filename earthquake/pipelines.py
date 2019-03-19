# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import MySQLdb


class EarthquakePipeline(object):
    CONN=MySQLdb.connect(host='localhost',port=3306,user='root',passwd='1234',db='data',charset='utf8')
    conn =  CONN.cursor()

    def process_item(self, item, spider):
        self.conn.execute(f'''
        INSERT INTO data1 VALUES('{item['name']}','{item['level']}','{item['time']}');
        commit;
        ''')
        return item

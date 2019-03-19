import scrapy
from earthquake.items import EarthquakeItem
import json
from random import randint


class ext_data(scrapy.Spider):
    name='EA'
    UserAgent = [
        'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36',
        'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Mobile Safari/537.36',
        'Mozilla/5.0 (iPad; CPU OS 11_0 like Mac OS X) AppleWebKit/604.1.34 (KHTML, like Gecko) Version/11.0 Mobile/15A5341f Safari/604.1',
        'Mozilla/5.0 (iPhone; CPU iPhone OS 11_0 like Mac OS X) AppleWebKit/604.1.38 (KHTML, like Gecko) Version/11.0 Mobile/15A372 Safari/604.1'
    ]
    def start_requests(self):
        for i in range(1,328):
            yield scrapy.Request(f'http://www.ceic.ac.cn/ajax/search?page={i}&&start=2007-01-01&&end=2019-03-06&&jingdu1=&&jingdu2=&&weidu1=&&weidu2=&&height1=&&height2=&&zhenji1=&&zhenji2=&&callback=jQuery18007183313762912973_1551851155694&_=1551851208104',headers={'user-agent':self.UserAgent[randint(0,3)]})

    def parse(self,response):        
        for i in json.loads((response.text)[41:-1])['shuju']:
            item=EarthquakeItem()
            item['name']=i['LOCATION_C']
            item['level']=i['M']
            item['time']=i['O_TIME']
            yield item

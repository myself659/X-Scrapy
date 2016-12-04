# -*- coding: utf-8  -*- 
import scrapy 
 
from  spider_xici.items import SpiderXiciItem  

class SPIDERXICI(scrapy.Spider): 
	name = "xici"
	allowed_domains = ["xicidaili.com"]
	start_urls = (
		'http://www.xicidaili.com',
	)


	def start_requests(self):
		reqs=[]
		for i in range (1, 1000): 
			req = scrapy.Request("http://www.xicidaili.com/nn/%s"%i)
			reqs.append(req)
    
		return reqs 


	def parse(self, response):
		ip_list=response.xpath('//table[@id="ip_list"]')

		trs = ip_list[0].xpath('tr')

		items = [] 

		for ip in trs[1:]: 
			pre_item = SpiderXiciItem()
			"""
			 ¾ø¶ÔÂ·¾¶ /html/body/div[1]/div[2]/table/tbody/tr[3]/td[2]

			"""
			pre_item['IP'] = ip.xpath('td[2]/text()')[0].extract()
			pre_item['PORT'] = ip.xpath('td[3]/text()')[0].extract()
			"""
			<a href="/2016-10-31/fujian">¸£½¨</a>
			"""
			pre_item["POSITION"]=ip.xpath('string(td[4])')[0].extract().strip()
			#pre_item["POSITION"]=ip.xpath('td[4]/a/text()')[0].extract()
			pre_item['TYPE'] = ip.xpath('td[6]/text()')[0].extract()
			pre_item["SPEED"] = (ip.xpath(
				'td[7]/div[@class="bar"]/@title').re('\d+\.\d{0,}'))[0]
			
			pre_item['LAST_CHECK_TIME'] = ip.xpath('td[10]/text()')[0].extract()

			items.append(pre_item)

		return  items 



# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy

class AdsyscrawlItem(scrapy.Item):
	
	'''
	Custom Scrapy item specific to the adsys requirements
	Records the page url as link
	and the page text in the text field
	'''
	
	link = scrapy.Field()
	text = scrapy.Field()

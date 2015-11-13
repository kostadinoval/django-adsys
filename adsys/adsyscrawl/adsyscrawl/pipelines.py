# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

from django.contrib.auth.models import User
from advert.models import Advert
from stopwords.models import StopWord
from domain.models import Domain
from page.models import Page
from content.models import Keyword, Content
from string import translate, digits
from collections import Counter

class AdsyscrawlPipeline(object):
	def process_item(self, item, spider):
		
		'''
		Function that processes each item
		after it has been scraped.
		Its purpose is to create content
		objects for each keyword on the page.		
		'''
		
		stop_words = []
		
		stop_words_obj_list = StopWord.objects.all()
		
		for stop_word_obj in stop_words_obj_list:
			stop_words.append(stop_word_obj.stopword.strip())
		
		stop_words.append("")
		
		temp_word_list = []
		
		
		text = item["text"].encode("ascii","ignore")
		text = text.lower().translate(None,"\r\"!\\/?,:|][*&£^`¬;()").translate(None,digits)
		
		temp_word_list = text.split(" ")
		
		word_list = [word.strip(" \'").rstrip("-.") for word in temp_word_list if word.rstrip("-.") not in stop_words and word.strip("\n \t") != ""]
		
		page_text = ' '.join(word_list)
		
		domains = Domain.objects.all()
		domain_obj = None
		for domain in domains:
			temp_domain = domain.domain.replace("http://","").replace("www.","").rstrip("/")
			if  temp_domain in item["link"]:
				domain_obj = domain
		
		try:
			page = Page.objects.get(domain = domain_obj, pageURL=item["link"])
		except Page.DoesNotExist:
			page = None
		
		if page:
			if page.text == page_text:
				return item
			else:
				page.text = page_text
				page.has_adscore = False
				page.save()
		else:	
			page = Page(domain=domain_obj, pageURL=item["link"], text=page_text)
			page.save()
		
		counter_list = Counter(word_list)
		
		for k,v in counter_list.items():
			if k.strip() == "" or k is None:
				continue
			
			try:
				keyword = Keyword.objects.get(keyword=k)
			except Keyword.DoesNotExist:
				keyword = None
			
			if keyword:
				temp_content = Content(page=page, keyword=keyword, occurrence=v)
				temp_content.save()
			
			else:
				temp_keyword = Keyword(keyword=k)
				temp_keyword.save()
				temp_content = Content(page=page, keyword=temp_keyword, occurrence=v)
				temp_content.save()
		
		return item
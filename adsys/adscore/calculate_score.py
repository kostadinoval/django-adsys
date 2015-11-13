#from __future__ import division
import sys,os
sys.path.append("PATH TO ROOT OF PROJECT")
os.environ["DJANGO_SETTINGS_MODULE"] = "adsys.settings"
import django
django.setup()

from adscore.models import AdScore
from advert.models import Advert, AdvertKeyword
from page.models import Page
from content.models import Content, Keyword
from adtopage.models import AdToPage

def calculate_score():
	
	'''
	
	calculate_score function runs periodically
	and checks the database for any pages that
	have recently been added by the web crawler
	and do not have an an advert score. It calculates
	an advert score for any retrieved pages.
	
	'''
	
	adverts = Advert.objects.all()
	pages = Page.objects.filter(has_adscore = False)
	
	for page in pages:
		
		for advert in adverts:
			
			advert_keywords = AdvertKeyword.objects.filter(advert = advert)
			
			ad_kw_list = [kw.keyword.lower() for kw in advert_keywords]
			
			page_keywords = Content.objects.filter(page = page)
			page_kw_list = []
			total_occ = 0
			page_occ = 0
			
			'''
			Loop through the page keywords objects,
			to extract the string keyword,
			add the number of occurrences for that keyword
			to the total number of occurrences
			'''
			for page_kw in page_keywords:
				keyword = Keyword.objects.get(pk = page_kw.keyword.pk)
				page_kw_list.append(keyword.keyword)
				total_occ += page_kw.occurrence
				
				# For each keyword that is both on the page and associated with an advert, keep a separate counter for occurrences 
				if keyword.keyword in ad_kw_list:
					page_occ += page_kw.occurrence
			
			try:
				# Use of sets to get the intersection and so the number of keywords that appear both on the page and are associated with the advert
				count = len(list(set(page_kw_list) & set(ad_kw_list)))
				
				# ad_prop - proportion of advert keywords that appear on the page divided by the total number of advert keywords
				ad_prop = count / float(len(ad_kw_list))
				
				# page_prop - proportion of advert keywords that appear on the page divided by the total number of keywords on the page
				page_prop = count / float(len(page_kw_list))
				
				# occ_prop - total number of advert keyword occurrences divided by total number of page keyword occurrences
				occ_prop = page_occ / float(total_occ)
				
				adscore = ad_prop * page_prop * occ_prop
				
			except ZeroDivisionError:
				adscore = 0
			
			AdScore(page = page, advert = advert, score = adscore).save()
		
		page.has_adscore = True
		page.save()
	return pages

def ads_to_pages(pages):
	
	'''
	Updates the AdToPage table by creating a record for each page
	and a reference to the advert with the highest advert score
	'''
	
	for page in pages:
		adscore = AdScore.objects.filter(page = page).order_by("-score")[0]
		AdToPage(page = page, advert = adscore.advert, active = True).save()

if __name__ == "__main__":
	pages = calculate_score()
	ads_to_pages(pages)
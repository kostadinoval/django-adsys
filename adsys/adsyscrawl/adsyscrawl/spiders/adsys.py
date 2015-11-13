from domain.models import Domain
from scrapy.contrib.linkextractors.lxmlhtml import LxmlLinkExtractor
from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.selector import Selector
#from scrapy.item import Item, Field
from adsyscrawl.items import AdsyscrawlItem

class AdsysSpider(CrawlSpider):
	
	'''
	Custom spider class sub-classing CrawlSpider in order to
	add rules end extend its functionality
	'''
	
	name = "adsys"
	allowed_domains = []
	start_urls = []
	rules = (Rule(LxmlLinkExtractor(), callback='parse_url', follow=True),)
	
	def __init__(self, *args, **kwargs):
		
		'''
		Override the default constructor in order
		to populate the allowed_domains and start_urls
		lists
		'''
		
		CrawlSpider.__init__(self, *args, **kwargs)
		domains = Domain.objects.all()
		for domain in domains:
			self.allowed_domains.append(str(domain.domain).replace("http://","").rstrip("/"))
			self.start_urls.append(str(domain.domain).rstrip("/"))
	
	def parse_url(self, response):
		
		'''
		Callback function for each crawled page.
		Creates a new Item to store the page URL
		and text within <p> tags.
		
		returns item which is processed in the pipelines
		'''
		
		item = AdsyscrawlItem()
		item["link"] = response.url
		selector = Selector(response)
		item["text"] = ' '.join(response.selector.xpath("//body//p/text()").extract())
		return item

# -*- coding: utf-8 -*-

# Scrapy settings for adsyscrawl project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#

BOT_NAME = 'adsyscrawl'

SPIDER_MODULES = ['adsyscrawl.spiders']
NEWSPIDER_MODULE = 'adsyscrawl.spiders'
ITEM_PIPELINES = { 'adsyscrawl.pipelines.AdsyscrawlPipeline' : 1 }
ROBOTSTXT_OBEY = True

# Crawl responsibly by identifying yourself (and your website) on the user-agent
USER_AGENT = 'adsyscrawl'

import sys,os
sys.path.append("PATH TO ROOT OF PROJECT")
sys.path.append("PATH TO ROOT OF SCRAPY PROJECT")
os.environ["DJANGO_SETTINGS_MODULE"] = "adsys.settings"
import django
django.setup()
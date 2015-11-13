import sys,os
sys.path.append("PATH TO ROOT OF PROJECT")
os.environ["DJANGO_SETTINGS_MODULE"] = "adsys.settings"
import django
django.setup()
from stopwords.models import StopWord

"""
Script which has been executed once,
Used to populate the database stopwords table with
a list of stop words.

The words used in this words.txt file can be found
at: http://www.ranks.nl/stopwords
"""

stop_words = []
stop_words_file = open("words.txt","r")
stop_words = stop_words_file.read().split("\n")
for word in stop_words:
	stopword = StopWord(stopword=word)
	stopword.save()

import scrapy
import pandas as pd
from ..items import FacultyextracterItem

class faculty_spider(scrapy.Spider):
	# name='stanfordfacultyinfo'
	name='mitfacultyinfo'
	# df=pd.read_csv('stanfordurls.csv')
	# df=pd.read_csv('stanfordurls1.csv')
	df=pd.read_csv('miturls.csv')
	start_urls=list(df['faculty_url'])

	def parse(self,response):
		# content=response.css('div#content-wrapper *:not(style)::text').extract()
		# content=response.css('div.su-person-content *:not(style)::text').extract()
		content=response.css('div.primary-info *::text').extract()
		contents=[]
		for s in content:
			s=s.strip()
			if ('\n' not in s) and (s!=',') and (len(s)!=0):
				contents.append(s)
		yield {'content':contents}
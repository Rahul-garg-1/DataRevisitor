import scrapy
import pandas as pd
from ..items import FacultyextracterItem

class faculty_spider(scrapy.Spider):
	name='facultyinfo'
	df=pd.read_csv('urls.csv')
	start_urls=list(df['faculty_url'])

	def parse(self,response):
		content=response.css('div#content div.fusion-row *:not(style)::text').extract()
		contents=[]
		for s in content:
			s=s.strip()
			if ('\n' not in s) and (s!=',') and (len(s)!=0):
				contents.append(s)
		yield {'content':contents}
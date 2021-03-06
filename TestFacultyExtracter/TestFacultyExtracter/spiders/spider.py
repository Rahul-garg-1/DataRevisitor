import scrapy
import pandas as pd
from ..items import TestfacultyextracterItem

class faculty_spider(scrapy.Spider):
	name='facultyinfo'
	df=pd.read_excel('1 california institute of technology.xlsx')

	def __init__(self):
		self.start_urls=self.get_urls(self.df)

	def parse(self,response):
		items=TestfacultyextracterItem()
		# content=response.css('body *:not(script):not(style):not(nav):not(footer)::text').extract()
		content=response.css('p::text').extract()
		contents=[]
		for s in content:
			s=s.strip()
			if ('\n' not in s) and (s!=',') and (s!='.') and (len(s)!=0):
				contents.append(s)
		items['content']=contents
		items['imageUrl']=response.css('img::attr(src)').extract()
		url=str(response)
		url=url[5:]
		items['url']=url[:-1]
		yield items

	def get_urls(self,df):
		urls=list(df['URL'])
		faculty_urls=set()
		for url in urls:
			url_list=url.split(',')

			for url1 in url_list:
				url1=url1.strip()

				if '.edu/' in url1:
					faculty_urls.add(url1)

		return list(faculty_urls)
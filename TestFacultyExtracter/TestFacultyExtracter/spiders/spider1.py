import scrapy
import pandas as pd
from ..items import TestfacultyextracterItem2

class faculty_spider(scrapy.Spider):
	name='newfacultyinfo'
	url_dict=dict()
	visited_urls=set()
	df=pd.read_excel('new_named_urls.xlsx')

	def __init__(self):
		self.start_urls=self.get_urls(self.df)

	def parse(self,response):
		url=str(response.request.url)
		if url in self.visited_urls:
			return
		items=TestfacultyextracterItem2()
		content=response.css('body *:not(script):not(style):not(nav):not(footer)::text').extract()
		# content=response.css('p::text').extract()
		contents=[]
		for s in content:
			s=s.strip()
			if ('\n' not in s) and (s!=',') and (s!='.') and (len(s)>1):
				contents.append(s)
		items['content']=contents
		items['url']=url
		self.visited_urls.add(url)
		# if items['url'] not in self.url_dict.keys():
			# print(items['url']+' not found in dictionary')
		items['name']=self.url_dict[items['url']]
		yield items

	def get_urls(self,df):
		urls=list(df['URL'])
		names=list(df['Name'])
		for i in range(len(urls)):
			self.url_dict[urls[i]]=names[i]
			url=urls[i]
			if 'https' in url:
				url=url.replace('https','http')
			else:
				url=url.replace('http','https')
			self.url_dict[url]=names[i]
		# print(self.url_dict)
		urls=set(urls)
		return list(urls)
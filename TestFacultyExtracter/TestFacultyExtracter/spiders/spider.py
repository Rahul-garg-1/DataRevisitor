import scrapy
import pandas as pd

class faculty_spider(scrapy.Spider):
	name='facultyinfo'
	df=pd.read_excel('1 california institute of technology.xlsx')

	def __init__(self):
		self.start_urls=self.get_urls(self.df)

	def parse(self,response):
		content=response.css('*:not(script) :not(style) ::text').extract()
		contents=[]
		for s in content:
			s=s.strip()
			if ('\n' not in s) and (s!=',') and (s!='.') and (len(s)!=0):
				contents.append(s)
		yield {'content':contents}

	def get_urls(self,df):
		urls=list(df['URL'])
		faculty_urls=[]
		for url in urls:
			url_list=url.split(',')

			for url1 in url_list:
				url1=url1.strip()

				if '.edu/' in url1:
					faculty_urls.append(url1)

		return faculty_urls
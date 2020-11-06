import scrapy
from ..items import FacultyextracterItem

class faculty_spider(scrapy.Spider):
	# name='stanfordfaculty'
	name='mitfaculty'
	# start_urls=['https://aa.stanford.edu/people/faculty/grid']
	# start_urls=['https://mse.stanford.edu/people/faculty']
	start_urls=['https://dmse.mit.edu/people/faculty']

	def parse(self,response):
		items=FacultyextracterItem()
		links=response.css('h3 a')
		# links=response.css('div.field-content a')
		# base_url='https://aa.stanford.edu'
		# base_url='https://mse.stanford.edu'
		base_url='https://dmse.mit.edu'
		for link in links:
			relative_url=link.css('::attr(href)').extract()
			if 'http' not in relative_url:
				items['faculty_url']=base_url+relative_url[0]
			else:
				items['faculty_url']=relative_url
			yield items
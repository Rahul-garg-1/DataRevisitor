import scrapy
from ..items import FacultyextracterItem

class faculty_spider(scrapy.Spider):
	name='stanfordfaculty'
	start_urls=['https://aa.stanford.edu/people/faculty/grid']

	def parse(self,response):
		items=FacultyextracterItem()
		links=response.css('h3 a')
		base_url='https://aa.stanford.edu'
		for link in links:
			relative_url=link.css('::attr(href)').extract()
			items['faculty_url']=base_url+relative_url[0]
			yield items
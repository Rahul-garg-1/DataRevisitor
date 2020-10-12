import scrapy
from ..items import FacultyextracterItem

class faculty_spider(scrapy.Spider):
	name='faculty'
	start_urls=['https://iqim.caltech.edu/people/iqim-postdoctoral-scholars/','https://iqim.caltech.edu/people/faculty/']

	def parse(self,response):
		items=FacultyextracterItem()
		links=response.css('h2 a')
		for link in links:
			items['faculty_url']=link.css('::attr(href)').extract()
			yield items
import scrapy
from ..items import CityextracterItem

class city_spider(scrapy.Spider):
	name='cities'
	start_urls=['https://en.wikipedia.org/wiki/List_of_cities_in_Brazil_by_population']

	def parse(self,response):
		items=CityextracterItem()
		cities=response.css('table.sortable tbody td a:nth-child(1)')
		for city in cities:
			items['city']=city.css('::text').extract()
			yield items
		# 	print(city)
		# yield {'cities':cities}
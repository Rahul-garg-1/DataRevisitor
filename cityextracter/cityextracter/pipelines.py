# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter

class CityextracterPipeline:

	# def __init__(self):
	# 	self.file=open('Brazil_cities.csv',mode='w',encoding='utf-8')


    def process_item(self, item, spider):
        return item

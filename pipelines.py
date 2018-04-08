# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
from scrapy.utils.project import get_project_settings
from scrapy.pipelines.images import ImagesPipeline
import scrapy,os
from scrapy.exceptions import DropItem

class BizhiPipeline(ImagesPipeline):
    IMAGES_STORE = get_project_settings().get("IMAGES_STORE")

    def get_media_requests(self, item, info):
        for image in item['image_url']:
            yield scrapy.Request(image)

    def item_completed(self, results, item, info):
        image_path = [x['path'] for ok, x in results if ok]
        if not image_path:
            raise DropItem('item contatins no images')

        # item['imagePath'] = image_path
        os.rename(self.IMAGES_STORE + '/' + image_path[0], self.IMAGES_STORE + '/' + str(item['name']) +str(item['num'])+ '.jpg')
        item['imagePath'] = self.IMAGES_STORE + '/' + str(item['name'])+str(item['num'])
        return item


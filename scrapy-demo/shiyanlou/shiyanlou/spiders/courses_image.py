# -*- coding: utf-8 -*-
import scrapy
from shiyanlou.items import CourseImageItem


class CoursesImageSpider(scrapy.Spider):
    name = 'courses_image'
    #allowed_domains = ['shiyanlou.com/courses']
    start_urls = ['https://shiyanlou.com/courses/']

    def parse(self, response):
        item=CourseImageItem()
        item['image_urls']=response.xpath('//div[@class="course-img"]/img/@src').extract()
        yield item

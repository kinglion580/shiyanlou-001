# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class CourseItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()

    name=scrapy.Field()
    description=scrapy.Field()
    type=scrapy.Field()
    students=scrapy.Field()

class UserItem(scrapy.Item):
    name = scrapy.Field()
    type = scrapy.Field()
    status = scrapy.Field()
    job = scrapy.Field()
    school = scrapy.Field()
    level = scrapy.Field()
    join_date = scrapy.Field()
    learn_courses_num = scrapy.Field()

class CourseImageItem(scrapy.Item):
    image_urls=scrapy.Field()
    images=scrapy.Field()

class MultipageCourseItem(scrapy.Item):
    name=scrapy.Field()
    image=scrapy.Field()
    author=scrapy.Field()

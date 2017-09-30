#-*- coding:utf-8 -*-
import scrapy

class LoginSpiderSpider(scrapy.Spider):
    name='login_spider'
    start_urls=['https://www.shiyanlou.com/login']

    def parse(self,response):
        csrf_token=response.xpath('//div[@class="login-body"]//input[@id="csrf_token"]/@value').extract_first()
        self.logger.info(csrf_token)
        return scrapy.FormRequest.from_response(
                response,
                formdata={
                    'csrf_token':csrf_token,
                    'login':'1609019405@qq.com',
                    'password':'033181995212ydp',
                    },
                callback=self.after_login
                )

    def after_login(self,response):
        return [scrapy.Request(
            url='https://www.shiyanlou.com/user/8797/',
            callback=self.parse_after_login
            )]

    def parse_after_login(self,response):
        return {
                'lab_count':response.xpath('(//span[@class="info-text"])[2]/text()').re_first('[^\d]*(\d*)[^\d*]'),
                'lab_minutes':response.xpath('(//span[@class="info-text"])[3]/text()').re_first('[^\d]*(\d*)[^\d*]')
                }

import scrapy


class CoursesFollowSpider(scrapy.Spider):
    name = 'courses_follow'
    start_urls = ['https://shiyanlou.com/courses/63']
    
    def parse(self, response):
        yield {
            'name': response.xpath('//h4[@class="course-infobox-title"]/span/text()').extract_first(),
            'author': response.xpath('//div[@class="mooc-info"]/div[@class="name"]/strong/text()').extract_first()
        }

        for url in response.xpath('//div[@class="sidebox-body course-content"]/a/@href'):
            yield response.follow(url, callback=self.parse)

import scrapy
import json

class TestSpider(scrapy.Spider):
    name = "testspider"
    start_url = 'https://www3.nhk.or.jp/news/html/20180822/k10011585581000.html'

    def start_requests(self):
        yield scrapy.Request(url=self.start_url, callback=self.parse_test)

    def parse_test(self, response):
        # print('\nLEN:: ', response.css('section.detail-no-js').extract_first(), '\n')
        title = response.css('section.detail-no-js p.title span.contentTitle::text').extract_first()
        time = response.css('section.detail-no-js p.title span#news_date::text').extract_first() + response.css('section.detail-no-js p.title span#news_time::text').extract_first()
        content = response.css('section.detail-no-js div#news_textbody::text').extract_first()
        yield {
            'title': title,
            'time': time,
            'content': content,
        }
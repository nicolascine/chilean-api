# -*- coding: utf-8 -*-
import scrapy

class SenateSpider(scrapy.Spider):
    name = "senate"
    allowed_domains = ["senado.cl"]
    start_urls = (
        'http://www.senado.cl/appsenado/index.php?mo=senadores&ac=listado',
    )

    def parse(self, response):
            for photo in response.xpath('//td//img/@src').extract():
                yield {"photo": photo}
            for name in response.xpath('//td//a[1]/text()').extract():
                yield {"name": name}
            for email in response.xpath('//td//a[2]/text()').extract():
                yield {"email": email}
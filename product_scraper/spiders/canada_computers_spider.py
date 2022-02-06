import scrapy
from product_scraper.items import ProductItem


class CanadaComputersSpider(scrapy.Spider):
    name = 'canada_computers_spider'
    allowed_domains = ['canadacomputers.com/']
    start_urls = ['https://canadacomputers.com//']

    def parse(self, response):
        containers = response.xpath('//div[contains(@class, "product-tiles")]')
        for container in containers:
            name = container.xpath(
                '//div[contains(@class, "product-description")]/text()').get()
            link = container.xpath(
                '//a[contains(@href,"product")]/@href').get()
            image = container.xpath(
                '//div[contains(@class, "img-container")]//img/@src').get()

            price = container.xpath(
                '//*[contains(@class, "price-tag")]//*[contains(@class," price") or contains(@class,"finalprice")]//*/text()').get()

            before_price = container.xpath(
                '//*[contains(@class, "price-tag")]//*[contains(@class,"before-price")]//*/text()').get()

            item = ProductItem(
                Name=name,
                Url=link,
                Image=image,
                Price=price,
                Before_price=before_price
            )
            yield item

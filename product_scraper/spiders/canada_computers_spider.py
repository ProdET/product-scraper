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
                '//div[contains(@class, "product-description")]/text()')
            link = container.xpath(
                '//div[contains(@class, "stretched-link")]').attr('href')
            image = container.xpath(
                '//div[contains(@class, "img-container")]//img').attr('src')

            price = container.xpath(
                '//p[contains(@class, "price-tag")]//*[contains(@class," price")]//label/text()')

            before_price = container.xpath(
                '//p[contains(@class, "price-tag")]//*[contains(@class,"before-price")]//label/text()')

            item = ProductItem(
                Name=name,
                Url=link,
                Image=image,
                Price=price,
                Before_price=before_price
            )
            yield item

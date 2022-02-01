import scrapy
from scrapy import Request
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from product_scraper.items import ProductItem


class AmazonSpider(scrapy.Spider):
    name = 'amazon'
    allowed_domains = ['amazon.ca', 'amazon.com']
    start_urls = [
        'https://www.amazon.ca/Electronics-Accessories/b/?ie=UTF8&node=667823011&ref_=nav_cs_electronics'
        'https://www.amazon.ca/Computers-Accessories/b/?ie=UTF8&node=2404990011&ref_=nav_cs_pc',
        'https://www.amazon.ca/gp/bestsellers/',
    ]

    def parse(self, response):
        item_container = '//div[@class="a-section a-spacing-none octopus-pc-item-block octopus-pc-asin-block"]'
        containers = response.xpath(item_container)
        for container in containers:
            item = ProductItem()

            title = container.xpath(
                '//div[contains(@class,"title")]/span/text()').get()

            price = container.xpath(
                '//span[@class="a-price-whole"]/text()').get()
            # , response.xpath(item_container + '//span[@class="a-price-fraction"]/text()').get()])
            sale_price = container.xpath(
                '//div[@class="a-section octopus-pc-asin-strike-price"]//text()').get()

            product_url = container.xpath(
                '//a[@class="a-link-normal octopus-pc-item-link"]/@href').get()
            image_url = container.xpath('//img/@src').get()

            # todo: find a better way to grab category
            # category = response.xpath(
            #    '//a[@class="a-link-normal a-color-tertiary"]/text()').get()
            # if(category.contains('Back to results')):
            #    category = response.xpath(
            #        '//span[@class="cat-name"]/text()').get()

            yield {'Name': title,
                   'price': price,
                   'sale_price': sale_price,
                   'product_url': product_url,
                   'image_url': image_url}

            """ yield ProductItem(
                product_name=title,
                #product_category = category,
                product_price=price,
                product_sale_price=sale_price,
                product_url=product_url,
                product_image=image_url) """

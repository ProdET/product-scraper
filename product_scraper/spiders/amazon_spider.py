import scrapy
from scrapy import Request
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from product_scraper.items import ProductItem

carouselPath = '//ol[@class="a-carousel" and @role="list"]'
carouselItemPath = carouselPath + \
    '//li[@class="a-carousel-card" and not(@aria-hidden="true")]'
carouselLinkPath = carouselItemPath + '//a[@class="a-link-normal"][2]'
carouselItemNamePath = carouselLinkPath + '//span//div'
carouselPricePath = carouselItemPath + \
    '//span[@class="a-size-base a-color-price"]//span'

gridPath = '//div[contains(@class,"desktop-grid")]'
gridItemPath = gridPath + '//div[@id="gridItemRoot"]'
gridLinkPath = gridItemPath + '//a[@class="a-link-normal"][2]'
gridItemNamePath = gridLinkPath + '//span//div'
gridPricePath = gridItemPath + \
    '//span[@class="a-size-base a-color-price"]//span'


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

        for container in response.xpath(item_container):
            item = ProductItem()

            title = container.xpath('//div[contains(@class,"title")]/span/text()').get()

            price = container.xpath('//span[@class="a-price-whole"]/text()').get()
            # , response.xpath(item_container + '//span[@class="a-price-fraction"]/text()').get()])
            sale_price = container.xpath('//div[@class="a-section octopus-pc-asin-strike-price"]//text()').get()

            # todo: find a better way to grab category
            # category = response.xpath(
            #    '//a[@class="a-link-normal a-color-tertiary"]/text()').get()
            # if(category.contains('Back to results')):
            #    category = response.xpath(
            #        '//span[@class="cat-name"]/text()').get()

            # availability = response.xpath(
            #    '//div[@id="availability"]//text()').get()
            product_url = container.xpath('//a[@class="a-link-normal octopus-pc-item-link"]/@href').get()
            image_url = container.xpath('//img/@src').get()

            item['product_name'] = title
            # item['product_category'] = ','.join(
            #    map(lambda x: x.strip(), category)).strip()
            item['product_price'] = price
            item['product_sale_price'] = sale_price
            #item['product_availability'] = ''.join(availability).strip()
            item['product_url'] = product_url
            item['product_image'] = image_url
            yield item


class AmazonCarouselSpider(scrapy.Spider):
    name = 'amazonCarousel'
    allowed_domains = ['amazon.ca', 'amazon.com']
    start_urls = [
        'https://www.amazon.ca/',
        'https://www.amazon.com/',
        'https://www.amazon.ca/gp/bestsellers/',
    ]

    def parse(self, response):
        for item in response.xpath(carouselItemPath):
            yield {
                'itemName': item.xpath(carouselItemNamePath).get(),
                'price': item.xpath(carouselPricePath).get(),
                'link': item.xpath(carouselLinkPath).attr('href'),
            }

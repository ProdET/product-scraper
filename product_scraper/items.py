# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy

# Generic product


class ProductItem(scrapy.Item):
    # product name
    Name = scrapy.Field()
    # product url
    Url = scrapy.Field()
    # product category
    Category = scrapy.Field()
    # base price
    Price = scrapy.Field()
    # optional: sale price (if applicable)
    Before_price = scrapy.Field()
    # optional: number of items available
    Availability = scrapy.Field()
    # optional: image url
    Image = scrapy.Field()

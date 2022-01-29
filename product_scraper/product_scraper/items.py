# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy

# Generic product


class ProductItem(scrapy.Item):
    # product name
    product_name = scrapy.Field()
    # product url
    product_url = scrapy.Field()
    # product category
    product_category = scrapy.Field()
    # base price
    product_price = scrapy.Field()
    # optional: sale price (if applicable)
    product_sale_price = scrapy.Field()
    # optional: number of items available
    product_availability = scrapy.Field()
    # optional: image url
    product_image = scrapy.Field()

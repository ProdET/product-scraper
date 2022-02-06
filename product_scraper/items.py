# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy
from dataclasses import dataclass, field
from typing import Optional
# Generic product

@dataclass
class ProductItem:
    # product name
    name: Optional[str] = field(default=None)
    # product url
    Url: Optional[str] = field(default=None)
    # product category
    Category: Optional[str] = field(default=None)
    # base price
    Price: Optional[float] = field(default=None)
    # optional: sale price (if applicable)
    Before_price: Optional[float] = field(default=None)
    # optional: number of items available
    Availability: Optional[int] = field(default=None)
    # optional: image url
    Image: Optional[str] = field(default=None)

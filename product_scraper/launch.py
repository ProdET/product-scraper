from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings
from product_scraper.spiders.amazon_spider import AmazonSpider
 
 
process = CrawlerProcess(get_project_settings())
process.crawl(AmazonSpider)
process.start()
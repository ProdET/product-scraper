from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings
from product_scraper.spiders.amazon_spider import AmazonSpider
from product_scraper.spiders.canada_computers_spider import CanadaComputersSpider

process = CrawlerProcess(get_project_settings())
process.crawl(CanadaComputersSpider)
process.start()

import scrapy


class Spider(scrapy.Spider):
    name = "go_and_see_aus"
    allowed_domains = ["goseeaustralia.com.au"]
    start_urls = [
        "http://www.goseeaustralia.com.au/caravan_parks/vic"]

    def __init__(self):
        self.update_settings = []
        pass

    def parse(self, response):
        pass

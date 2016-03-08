from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings

from crawler.spiders import go_and_see_aus_spider


def main():
    settings = get_project_settings()
    process = CrawlerProcess(settings)

    process.crawl(go_and_see_aus_spider)
    process.start()


if __name__ == '__main__':
    main()

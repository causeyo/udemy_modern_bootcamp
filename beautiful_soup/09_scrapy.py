import scrapy


class BookSpider(scrapy.Spider):
    name = 'bookspider'
    start_urls = ['http://books.toscrape.com']

    def parse(self, response):
        for article in response.css('article.product_pod'):
            yield {
                'price': article.css(".price_color::text").extract_first(),
                'title': article.css("h3 > a::attr(title)").extract_first()
            }

            next = response.css('.next > a::attr(href)').extract_first()
            if next:
                yield response.follow(next, self.parse)

# to execute this script type:
# scrapy runspider -o book.csv 09_scrapy.py
# scrapy runspider -o book1.json 09_scrapy.py

# http://books.toscrape.com/

import scrapy

class BookSpider(scrapy.Spider):
	name = "bookspider"
	start_urls = ['http://books.toscrape.com']

	def parse(self, respone):
		for article in respone.css('article.product_pod'):
			yield {
			'price': article.css(".price_color::text ").extract_first(),
			'title': article.css("h3 > a::attr(title)").extract_first()
			}
			next = respone.css('.next > a::attr(href)').extract_first()
			if next:
				yield respone.follow(next, self.parse)
import scrapy

class MySpider(scrapy.Spider):
    name = 'my_spider'
    start_urls = ['https://fr.wikipedia.org/wiki/Wikipédia:Accueil_principal']

    def parse(self, response):
        # Extraire le contenu de la page actuelle
        page_title = response.xpath('//title/text()').get()
        page_content = response.xpath('//body//text()').getall()
        yield {
            'url': response.url,
            'title': page_title,
            'content': ' '.join(page_content)
        }

        # Suivre tous les liens sur la page
        for href in response.css('a::attr(href)').getall():
            if href.startswith('/wiki/'):
                yield response.follow(href, self.parse)

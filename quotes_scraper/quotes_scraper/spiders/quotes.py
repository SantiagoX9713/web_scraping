import scrapy
# Título = //h1/a/text()
# Citas = //span[@class="text" and @itemprop="text"]/text()
# Top Ten tags = //div[contains(@class, "tags-box")]//span[@class="tag-item"]/a/text()

# Los spider que necesite deben de heredar de scrapy.Spider, así la el framework y la shel podrán reconocerlo


class QuotesScraper(scrapy.Spider):
    # El atributo nombre es importante para que la shell lo renonozca, debe de ser único
    name = 'quotes'
    # Las urls que vamos a consultar
    start_urls = [
        'http://quotes.toscrape.com/page/1/'
    ]

    # Esta función es la que obtiene lo datos de las urls de arriba
    def parse(self, response):

        # Y aquí abajo vamos a jugar con el contenido de texto de response con XPath
        title = response.xpath('//h1/a/text()').get()
        quotes = response.xpath('//span[@class="text" and @itemprop="text"]/text()').getall()
        top_ten_tags = response.xpath('//div[contains(@class, "tags-box")]//span[@class="tag-item"]/a/text()').getall()
        

        yield {
            'title': title,
            'quotes': quotes,
            'top_ten_tags': top_ten_tags
        }

        # Para guardar en consola es:
        # scrapy crawl quotes -o quotes.json Para guardar en JSON
        # scrapy crawl quotes -o quotes.csv Para guardar en CSV
import scrapy

class GoogleSpider(scrapy.Spider):
    name = 'example_google'
    start_urls = ['https://www.google.com']

    def parse(self, response):
        # extraer el titulo de la pagina
        title = response.css('title::text').get()

        dict_item = {
            'title': title,
            'url': response.url
        }

        lst_items = []
        lst_items.append(dict_item)

        # devolver una lista con el item
        return lst_items


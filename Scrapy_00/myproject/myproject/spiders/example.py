import scrapy

class ExampleSpider(scrapy.Spider):
    name = 'example_00'
    start_urls = ['https://weather.com/es-UY/tiempo/hoy/l/UYXX0006:1:UY?Goto=Redirected']

    def parse(self, response):
        # extraer el titulo con xpath
        degrees = response.xpath('//div/div[2]/div[1]/div[1]/span/text()').get()
        city = response.xpath('//div/section/div/div/div[1]/h1/text()').get()

        dict_item = {
            'url': response.url,
            'degrees': degrees,
            'city': city
        }

        lst_items = []
        lst_items.append(dict_item)

        # devolver una lista con el item
        return lst_items

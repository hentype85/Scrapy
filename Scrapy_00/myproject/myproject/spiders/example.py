import scrapy

class ExampleSpider(scrapy.Spider):
    name = 'example_00'
    start_urls = ['https://weather.com/es-UY/tiempo/hoy/l/UYXX0006:1:UY?Goto=Redirected']

    def parse(self, response):
        # extraer datos
        temp_max = response.xpath('//div[@id="todayDetails"]/section/div/div[2]/div[1]/div[2]/span[1]/text()').get()
        temp_min = response.xpath('//div[@id="todayDetails"]/section/div/div[2]/div[1]/div[2]/span[2]/text()').get()
        city = response.xpath('//div/section/div/div/div[1]/h1/text()').get()

        dict_item = {
            'url': response.url,
            'city': city,
            'temp_max': temp_max,
            'temp_min': temp_min,
        }

        lst_items = []
        lst_items.append(dict_item)

        # devolver una lista con el item
        return lst_items

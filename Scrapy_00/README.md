# Scrapy

https://scrapy.org/

instalar scrapy:
```
pip install scrapy
scrapy --version
```

crear proyecto scrapy:
```
scrapy startproject myproject
cd myproject/myproject/spiders
```  
crear "example_google.py" en myproject/spiders  
ejecutar el Spider:
```
scrapy crawl example_google
```
guardar los resultados en un archivo:
```
scrapy crawl example_google -o output.json
```
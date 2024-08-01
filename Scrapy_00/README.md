# Scrapy 2.11.2

https://scrapy.org/  

instalar scrapy:
```
pip install scrapy
scrapy --version
```  
(posiblemente necesite agregar `..\Local-Packages\Python..\Scripts` a variables de entorno)
  
crear proyecto scrapy `scrapy startproject myproject`:
```
scrapy startproject myproject
cd myproject/myproject/spiders
```  
crear "example.py" en myproject/spiders  
ejecutar el Spider `scrapy crawl example_00`:
```
C:\...\Scrapy\Scrapy_00\myproject> scrapy crawl example_00 -o output.json
```
guardar los resultados en un archivo `scrapy crawl example_00 -o output.json`:
```
C:\...\Scrapy\Scrapy_00\myproject> scrapy crawl example_00 -o output.json
```
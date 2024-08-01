# Scrapy

https://scrapy.org/  

instalar scrapy:
```
pip install scrapy
scrapy --version


**(posiblemente necesite agregar ..\Local-Packages\Python..\Scripts a variables de entorno)**


Scrapy 2.11.2 - active project: myproject

Usage:
  scrapy <command> [options] [args]

Available commands:
  bench         Run quick benchmark test
  check         Check spider contracts
  crawl         Run a spider
  edit          Edit spider
  fetch         Fetch a URL using the Scrapy downloader
  genspider     Generate new spider using pre-defined templates
  list          List available spiders
  parse         Parse URL (using its spider) and print the results
  runspider     Run a self-contained spider (without creating a project)
  settings      Get settings values
  shell         Interactive scraping console
  startproject  Create new project
  version       Print Scrapy version
  view          Open URL in browser, as seen by Scrapy

Use "scrapy <command> -h" to see more info about a command
```

crear proyecto scrapy:
```
scrapy startproject myproject
cd myproject/myproject/spiders
```  
crear "example.py" en myproject/spiders  
ejecutar el Spider:
```
scrapy crawl example_00
```
guardar los resultados en un archivo:
```
scrapy crawl example_00 -o output.json
```
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from scrapy.selector import Selector
import time

# Setup Chrome for headless browser
options = Options()
options.add_argument("--headless")
options.add_argument("--disable-gpu")
options.add_argument("--no-sandbox")

# Start Chrome browser
driver = webdriver.Chrome(service=Service(), options=options)

# Target product URL
url = "https://www.dafiti.com.co/Reloj-Tommy-Hilfiger-Modelo-1710680-Negro-Hombre-2642741.html"
driver.get(url)

# Wait for JavaScript to render
time.sleep(5)

# Extract rendered HTML
html = driver.page_source
sel = Selector(text=html)

# Extract product details
brand = sel.xpath("//h2[@class='prd-brand mbs']/text()").get()
# title = sel.xpath("//h1[@class='prd-name mbs']/text()").get()

# Look for specs in key-value layout (like Modelo, Color, etc.)

model_number = sel.xpath("//td[contains(text(), 'Código Artículo')]/following-sibling::td[1]//text()").get()

color = sel.xpath("//body//table[@class='prd-attributes mbl prm']//td[@class='name']//following-sibling::td[1]//text()").get()

# Price (discounted)
current_price = sel.xpath("//body//span[@class='prd-price special-price']//text()").get()

# Original price (MRP before discount)
original_price = sel.xpath("//body//span[@class='prd-price']//text()").get()

# Output results
print("lklExtracted Product Details:")
print(f"Brand: {brand.strip() if brand else 'Not Found'}")
print(f"Model Number: {model_number.strip() if model_number else 'Not Found'}")
print(f"Color: {color.strip() if color else 'Not Found'}")
print(f"Current Price: {current_price.strip() if current_price else 'Not Found'}")
print(f"Original Price: {original_price.strip() if original_price else 'Not Found'}")

# Close browser
driver.quit()

# import scrapy
# from scrapy.crawler import CrawlerProcess

# class DafitiSpider(scrapy.Spider):
#     name = 'dafiti'
#     start_urls = ['https://www.dafiti.com.co/Reloj-Tommy-Hilfiger-Modelo-1710680-Negro-Hombre-2642741.html']

#     def parse(self, response):
#         brand = response.xpath("//h2[@class='prd-brand mbs']/text()").get()
#         model_number = response.xpath("//td[contains(text(), 'Código Artículo')]/following-sibling::td[1]//text()").get()
#         color = response.xpath("//body//table[@class='prd-attributes mbl prm']//td[@class='name']//following-sibling::td[1]//text()").get()
#         current_price = response.xpath("//body//span[@class='prd-price special-price']//text()").get()
#         original_price = response.xpath("//span[@class='prd-price']/text()").get()

#         print("Extracted Product Details:")
#         print(f"Brand: {brand.strip() if brand else 'Not Found'}")
#         print(f"Model Number: {model_number.strip() if model_number else 'Not Found'}")
#         print(f"Color: {color.strip() if color else 'Not Found'}")
#         print(f"Current Price: {current_price.strip() if current_price else 'Not Found'}")
#         print(f"Original Price: {original_price.strip() if original_price else 'Not Found'}")

# # Run the spider
# process = CrawlerProcess()
# process.crawl(DafitiSpider)
# process.start() 

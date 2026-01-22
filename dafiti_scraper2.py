from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from scrapy.selector import Selector
import pandas as pd
import time

# Setup headless Chrome
options = Options()
options.add_argument("--headless")

# Create Chrome driver instance
driver = webdriver.Chrome(service=Service(), options=options)

# List of product URLs (add more as needed)
urls = [
    "https://www.dafiti.com.co/Reloj-Inteligente-Smart-F12-Pro-6-Negro-2509860.html",
    "https://www.dafiti.com.co/Reloj-Hombre-Sven-3002-Diesel---Negro-1510459.html",
    "https://www.dafiti.com.co/Reloj-Tommy-Hilfiger-Modelo-1710680-Negro-Hombre-2642741.html",
    "https://www.dafiti.com.co/Reloj-Tissot-Hombre-T1418073705100-2708781.html",
    "https://www.dafiti.com.co/Reloj-Casio-Negro-Hombre-MTP-V004D-1C-2492971.html",
    "https://www.dafiti.com.co/Reloj-Curren-8314-Cronografo---Cafe-Oscuro-2688595.html",
    "https://www.dafiti.com.co/Reloj-Tommy-Hilfiger-Modelo-1710680-Negro-Hombre-2642741.html",
    "https://www.dafiti.com.co/Reloj-Tissot-Hombre-T1204171705102-2708603.html",
    "https://www.dafiti.com.co/Reloj-Tommy-Hilfiger-Modelo-1710680-Negro-Hombre-2642741.html",
    "https://www.dafiti.com.co/Reloj-Curren-8314-Cronografo---Cafe-Oscuro-2688595.html",
    "https://www.dafiti.com.co/Reloj-Curren-8314-Cronografo---Blanco-2688599.html",
    "https://www.dafiti.com.co/Reloj-Curren-8402-Cronografo---Verde-2151876.html",
    "https://www.dafiti.com.co/Reloj-Curren-8402-Cronografo---Azul-2634828.html",
    "https://www.dafiti.com.co/Reloj-Casio-Negro-Hombre-MTP-V004D-1C-2492971.html",
    "https://www.dafiti.com.co/Reloj-Tissot-Hombre-T1204103309100-2717030.html",
    "https://www.dafiti.com.co/Reloj-Tissot-Hombre-T1144171705700-2708645.html",
    "https://www.dafiti.com.co/Reloj-Diesel-DZ4676-Para-Hombre-2709675.html",
    "https://www.dafiti.com.co/Reloj-Diesel-DZ2213-Para-Hombre-2709643.html",
    "https://www.dafiti.com.co/Reloj-Diesel-DZ2175-Para-Hombre-2709658.html",
    "https://www.dafiti.com.co/Reloj-Diesel-DZ1799-Para-Hombre-2709595.html",
    "https://www.dafiti.com.co/Reloj-Diesel-DZ4678-Para-Unisex-2709683.html"

]

product_data = []

for url in urls:
    try:
        driver.get(url)
        time.sleep(5)  
        html = driver.page_source
        sel = Selector(text=html)

        brand = sel.xpath("//h2[@class='prd-brand mbs']/text()").get()
        model_number = sel.xpath("//td[contains(text(), 'Código Artículo')]/following-sibling::td[1]//text()").get()
        color = sel.xpath("//body//table[@class='prd-attributes mbl prm']//td[@class='name']//following-sibling::td[1]//text()").get()
        current_price = sel.xpath("//span[@class='prd-price special-price']//text()").get()
        original_price = sel.xpath("//span[@class='prd-price']//text()").get()

        product_data.append({
            "URL": url,
            "Brand": brand.strip() if brand else "Not Found",
            "Model Number": model_number.strip() if model_number else "Not Found",
            "Color": color.strip() if color else "Not Found",
            "Current Price": current_price.strip() if current_price else "Not Found",
            "Original Price": original_price.strip() if original_price else "Not Found"
        })

        print(f"Scraped: {url}")
    except Exception as e:
        print(f"Error scraping {url}: {e}")

df = pd.DataFrame(product_data)
df.to_csv("dafiti_products.csv", index=False, encoding='utf-8-sig')

print("\n✅ Data saved to 'dafiti_products.csv'.")

driver.quit()

# Note: The above code is a complete script that scrapes product details from Dafiti using Selenium and saves the data to a CSV file.
# Ensure you have the required libraries installed:
# # pip install selenium scrapy pandas
# # Also, make sure to have the appropriate WebDriver for your browser (e.g., ChromeDriver for Chrome).
# # You can run this script in a Python environment where you have access to the internet and the necessary permissions to scrape the website.
# # The script uses Selenium to handle JavaScript-rendered content, extracts product details using XPath, and saves the results in a structured format.
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from scrapy.selector import Selector
import pandas as pd
import time

options = Options()
options.add_argument("--headless")
options.add_argument("--disable-gpu")
options.add_argument("--no-sandbox")

driver = webdriver.Chrome(service=Service(), options=options)

urls = [
    "https://www.falabella.com/falabella-cl/product/134036874/BALANZA-DIGITAL-ELECTRONICA-30-KG/134036875",
    "https://www.falabella.com/falabella-cl/product/115974898/Electron-Termo-Hervidor-Electrico-Inox-2.8-Litros./115974899",
    "https://sodimac.falabella.com/sodimac-cl/product/110395700/Balanza-electronica-30-kg-blanco/110395701",
    "https://www.falabella.com/falabella-cl/product/113146957/Cocedor-de-Huevos-Electron-BA-1400./113146958",
    "https://www.falabella.com/falabella-cl/product/135862642/Pesa-Balanza-Digital-Electronica-40Kg-Bascula-De-Precios/135862643",
    "https://sodimac.falabella.com/sodimac-cl/product/110372876/Balanza-electronica-30-kg-azul-blanco/110372881",
    "https://www.falabella.com/falabella-cl/product/113751290/Balanza-Digital-para-Cocina-1G-10kg/113751291",
    "https://www.falabella.com/falabella-cl/product/143108990/Auto-Electrico-Deportivo/143108991",
    "https://www.falabella.com/falabella-cl/product/138734709/Tablet-Iconia-P11-Teclado-+-Stylus-Android-14-MT8781N-8GB-256GB-QLED-11'-2K-GPS-./138734710",
    "https://www.falabella.com/falabella-cl/product/140763897/CD-Electrodomesticos-Publico/140763898",
    "https://www.falabella.com/falabella-cl/product/118332235/Teclado-Musical-Electronico-Infantil-Con-Microfono-32-Teclas/118332236",
    "https://www.falabella.com/falabella-cl/product/124390507/Piano-Teclado-Electronico-Digital-61-Teclas-con-Microfono./124390510",
    "https://www.falabella.com/falabella-cl/product/140155857/Ukelele-Electroacustico-OV/140155858",
    "https://www.falabella.com/falabella-cl/product/136586677/Single-Expression-Pedal/136586678",
    "https://www.falabella.com/falabella-cl/product/127614649/Teclado-Piano-Electronico-Microfono-37-Teclas./127614650",
    "https://www.falabella.com/falabella-cl/product/prod76727856/Celular-Samsung-Galaxy-S23-Ultra-256GB/16689936",
    "https://www.falabella.com/falabella-cl/product/prod43139229/Apple-iPhone-13-128Gb/15643401",
    "https://www.falabella.com/falabella-cl/product/136026316/Samsung-Galaxy-A06-LTE-128GB-Verde/136026317",
    "https://www.falabella.com/falabella-cl/product/140922738/Galaxy-A06-128-GB-Negro/140922739",
    "https://www.falabella.com/falabella-cl/product/140148617/Xiaomi-Redmi-Note-14-Midnight-Black-8GB-RAM+-256GB-Memoria-Nuevo/140148618"
]

product_data = []

for url in urls:
    try:
        driver.get(url)
        time.sleep(5)
        html = driver.page_source
        sel = Selector(text=html)

        title = sel.xpath("//h1/text()").get()

       
        product_code_full = sel.xpath("//*[contains(text(), 'Product code')]/text()").get()
        if not product_code_full:
            alt_code = sel.xpath("//*[contains(text(), 'Product code')]/parent::*//text()").getall()
            for txt in alt_code:
                if 'Product code' in txt:
                    product_code_full = txt
                    break

        product_code = product_code_full.split(':')[1].strip() if product_code_full else "Not Found"
        if product_code == "Not Found":
            print(f"  Product code not found at: {url}")

        
        price_spans = sel.xpath("//span[contains(@class,'copy10') or contains(@class,'main-price')]/text()").getall()
        current_price = price_spans[0] if price_spans else "Not Found"

        original_price = sel.xpath("//span[contains(@class,'list-price')]/text()").get()
        if not original_price or original_price.strip() == current_price.strip():
            original_price = "Not Available"

        product_data.append({
            "URL": url,
            "Brand/Title": title.strip() if title else "Not Found",
            "Product Code": product_code,
            "Current Price": current_price.strip() if current_price else "Not Found",
            "Original Price": original_price.strip() if original_price else "Not Found"
        })

        print(f" Scraped: {url}")                         
    except Exception as e:
        print(f"❌ Error scraping {url}: {e}")


df = pd.DataFrame(product_data)
df.to_csv("falabella_products2.csv", index=False, encoding='utf-8-sig')

print("\n Data saved to 'falabella_products2.csv'.")


driver.quit()
        
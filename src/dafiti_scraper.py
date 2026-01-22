import requests
import scrapy
from scrapy.selector import Selector
import pandas as pd 

# Step 1: Store the request data as a dictionary
request_data = {
    "referer": "https://www.dafiti.com.co/Reloj-Tommy-Hilfiger-Modelo-1710680-Negro-Hombre-2642741.html",
    "request_url": "https://analytics.google.com/g/collect",
    "method": "POST",
    "status_code": "204 No Content",
    "remote_address": "[2001:4860:4802:36::181]:443",
    "referrer_policy": "strict-origin-when-cross-origin",
    "headers": {
        "access-control-allow-credentials": "true",
        "access-control-allow-origin": "https://www.dafiti.com.co",
        "alt-svc": 'h3=":443"; ma=2592000,h3-29=":443"; ma=2592000',
        "cache-control": "no-cache, no-store, must-revalidate",
        "content-length": "0",
        "content-security-policy-report-only": (
            "script-src 'none'; form-action 'none'; frame-src 'none'; "
            "report-uri https://csp.withgoogle.com/csp/scaffolding/ascnsrsggc:158:0"
        ),
        "content-type": "text/plain",
        "cross-origin-opener-policy-report-only": "same-origin; report-to=ascnsrsggc:158:0",
        "cross-origin-resource-policy": "cross-origin",
        "date": "Tue, 24 Jun 2025 17:01:54 GMT",
        "expires": "Fri, 01 Jan 1990 00:00:00 GMT",
        "pragma": "no-cache",
        "report-to": {
            "group": "ascnsrsggc:158:0",
            "max_age": 2592000,
            "endpoints": [{
                "url": "https://csp.withgoogle.com/csp/report-to/scaffolding/ascnsrsggc:158:0"
            }]
        },
        "server": "Golfe2"
    },
    "query_parameters": {
        "v": "2",
        "tid": "G-2MJMQ15YLT",
        "gtm": "45je56n0v9162041016z86125902za200zb6125902",
        "_p": "1750784506040",
        "gcd": "13l3l3l3l1l1",
        "npa": "0",
        "dma": "0",
        "tag_exp": (
            "101509157~103116026~103200004~103233427~103351869~103351871~"
            "104684204~104684207~104718208"
        ),
        "tt": "internal",
        "cid": "2068936903.1750582463",
        "ul": "en-gb",
        "sr": "1536x864",
        "uaa": "x86",
        "uab": "64",
        "uafvl": (
            "Google%2520Chrome%3B137.0.7151.120%7CChromium%3B137.0.7151.120"
            "%7CNot%252FA)Brand%3B24.0.0.0"
        ),
        "uamb": "0",
        "uam": "",
        "uap": "Windows",
        "uapv": "19.0.0",
        "uaw": "0",
        "are": "1",
        "frm": "0",
        "pscdl": "noapi",
        "_prs": "ok",
        "_eu": "AAAAAAQ",
        "_s": "6",
        "dl": "https://www.dafiti.com.co/Reloj-Tommy-Hilfiger-Modelo-1710680-Negro-Hombre-2642741.html",
        "dp": "/reloj-tommy-hilfiger-modelo-1710680-negro-hombre-2642741.html",
        "dt": "ecommerce - product detail",
        "sid": "1750784507",
        "sct": "3",
        "seg": "1",
        "_tu": "Dg",
        "tfd": "17850"
    }
}

request_list = [request_data]


df = pd.DataFrame(request_list)

df.head()

url = request_data["referer"]

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/137.0.0.0 Safari/537.36"
}

response = requests.get(url, headers=headers)
html = response.text

sel = Selector(text=html)

product_name = sel.xpath("//h2[@class='prd-brand mbs']/text()").get()
color = sel.xpath("//body//table[@class='prd-attributes mbl prm']//td[@class='name']//following-sibling::td[1]//text()").get()
original_price = sel.xpath("//body//span[@class='prd-price']//text()").get()
current_price = sel.xpath("//body//span[@class='prd-price special-price']//text()").get()
model_number = sel.xpath("//td[contains(text(), 'Código Artículo')]/following-sibling::td[1]//text()").get()

print(f"Product Name: {product_name}")
print(f"Model Number: {model_number}")
print(f"Color: {color}")
print(f"MRP: {original_price}")
print(f"Price: {current_price}")
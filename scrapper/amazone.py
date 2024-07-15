import pandas as pd
from bs4 import BeautifulSoup

with open('amazone.html', 'r', encoding='utf-8') as file:
    soup = BeautifulSoup(file, 'html.parser')

products = []

for item in soup.select('.s-main-slot .s-result-item'):
    product = {}
    
    title_tag = item.select_one('h2 a span')
    price_whole_tag = item.select_one('.a-price-whole')
    price_fraction_tag = item.select_one('.a-price-fraction')
    rating_tag = item.select_one('.a-row.a-size-small span[aria-label]')
    
    if title_tag:
        product['Title'] = title_tag.get_text()
    if price_whole_tag and price_fraction_tag:
        product['Price'] = f"{price_whole_tag.get_text()}{price_fraction_tag.get_text()}"
    if rating_tag:
        product['Rating'] = rating_tag['aria-label']
    
    if product:
        products.append(product)

df = pd.DataFrame(products)

df.to_excel('amazonProducts.xlsx', index=False)

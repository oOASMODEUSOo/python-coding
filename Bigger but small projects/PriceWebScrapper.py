import requests
from bs4 import BeautifulSoup

URL="https://www.amazon.in/gp/product/B079S811J3/ref=ox_sc_act_image_1?smid=A14CZOWI0VEHLG&psc=1"

headers = {"User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36 OPR/73.0.3856.427'}

def price_check():
    page = requests.get(URL, headers=headers)

    soup = BeautifulSoup(page.content, 'html.parser')

    title = soup.find(id='productTitle').get_text()
    print(title.strip())
    price = soup.find(id='priceblock_ourprice').get_text()

    badchar = ['₹', ',', ' ']
    for i in badchar:
        price=price.replace(i,'')

    converted_price = int(price[1:5])
    print(converted_price)
import requests
from bs4 import BeautifulSoup

url = 'https://www.nike.com/launch/?s=in-stock'
req = requests.get(url)

soup = BeautifulSoup(req.content, 'html.parser')

print(soup)
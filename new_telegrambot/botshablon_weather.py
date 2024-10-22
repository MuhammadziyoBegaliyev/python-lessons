from bs4 import BeautifulSoup
import requests

url = 'https://obhavo.uz/'

page = requests.get(url)
soup = BeautifulSoup(page.text, 'html')


soup.find('div')
soup.find_all('div')
print(soup.prettify())
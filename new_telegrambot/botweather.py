import requests
from bs4 import BeautifulSoup as BS

t = requests.get('https://obhavo.uz')
html_t = BS(t.content , 'html.parser')

for el in html_t.select('#main'):
    min = el.select('.current-forecast.min')[0].text
    max = el.select('.current-forecast.max')[0].text
    print(min, max)

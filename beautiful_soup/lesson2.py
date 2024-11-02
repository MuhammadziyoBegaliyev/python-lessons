from bs4 import BeautifulSoup
import requests

source = requests.get('file:///home/muhammadziyo/apps/python-lessons/beautiful_soup/project.html').text

soup = BeautifulSoup(source ,'lxml')
print(soup)
# container = soup.find('container')

# headline = container.h2.a.text
# print(headline)   
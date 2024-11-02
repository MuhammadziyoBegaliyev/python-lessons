import requests
from bs4 import BeautifulSoup

page = requests.get('https://obhavo.uz/tashkent')
soup = BeautifulSoup(page.content, 'html.parser') # parser orqali html malumotlari chaqiramiz
# print(soup.find_all('a'))   # bu kod orqali a classni chaqiramiz
week = soup.find(id='main') # asosiy class 'main ' orqali hamma malumotlarni chaqirib olamiz 
# print(week)

items = week.find_all(class_='grid-1 cont-block')
# print(items) 

print(items[0].find(class_='padd-block').get_text())
print(items[0].find(class_='current-day').get_text())
print(items[0].find(class_='current-forecast').get_text())

period_names = [item.find(class_='padd-block').get_text() for item in items ]
print(period_names)

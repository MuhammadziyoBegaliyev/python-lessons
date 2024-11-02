from bs4 import BeautifulSoup as soup
from urllib.request import urlopen as uReq


my_url = 'https://www.flipkart.com/apple-iphone-15-blue-128-gb/p/itmbf14ef54f645d?pid=MOBGTAGPAQNVFZZY&lid=LSTMOBGTAGPAQNVFZZY7RHDU7&marketplace=FLIPKART&q=iphone&store=tyy%2F4io&spotlightTagId=BestsellerId_tyy%2F4io&srno=s_1_1&otracker=search&otracker1=search&fm=Search&iid=fc46472f-0eb0-44ae-af6b-a3f0d864e0e4.MOBGTAGPAQNVFZZY.SEARCH&ppt=sp&ppn=sp&ssid=auxfzmei4wu8kpvk1729943402774&qH=0b3f45b266a97d70'

uClient = uReq(my_url)
page_html = uClient.read()
uClient.close()
page_soup = soup(page_html, 'html.parser')

containers = page_soup.findAll("div", {"class": "DOjaWF gdgoEp col-8-12"})
# print(len(containers))
# print(soup.prettify(containers[0])) 
container = containers[0]
price = container.findAll('div', {'class': 'cPHDOP col-12-12'})
print(price[0].text)



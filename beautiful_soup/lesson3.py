from urllib.request import urlopen as uReq 
from bs4 import BeautifulSoup as soup 


my_url = 'https://www.newegg.com/p/pl?d=graphic'

uClient = uReq(my_url)
page_html = uClient.read()
uClient.close()
page_soup = soup(page_html, "html.perser")

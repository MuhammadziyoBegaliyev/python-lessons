from bs4 import BeautifulSoup
import requests


with open("project.html") as html_file:
    soup = BeautifulSoup(html_file, 'lxml')

for experience in soup.find_all('div', class_='experience'):
    # headline = experience.h2.a.text
    # print(headline)
    summary = experience.p.text
    print(summary)



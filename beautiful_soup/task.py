import requests
from bs4 import BeautifulSoup 


wiki_link = "https://en.wikipedia.org/wiki/List_of_Asian_countries_by_area"
link = requests.get(wiki_link).text
soup = BeautifulSoup(link)
right_table = soup.find('table', class_='sortable wikitable sticky-header col2left jquery-tablesorter')
table_link = right_table.findAll('a')
table_link  


#
# right_table
 



# all_link = soup.find_all('a') 
# for link in all_link:
#     print(link.get('href'))


# all_tables = soup.find_all('table')
# print(all_tables)

# soup.find_all('a')
# soup.title.string
# print(soup.prettify())
# print(link)
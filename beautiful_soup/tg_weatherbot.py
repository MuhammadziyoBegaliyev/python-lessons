import requests
from bs4 import BeautifulSoup

# URL for the page
url = "https://obhavo.uz/tashkent"

# Get the HTML content of the page
response = requests.get(url)
soup = BeautifulSoup(response.content, 'html.parser')

# Find the section for "Ertaga" forecast
forecast_table = soup.find("table", class_="weather-table")

# Locate the "Ertaga" row (first row in the table)
ertaga_row = forecast_table.find("tr", class_="weather-row-day")

# Extract the necessary details
day = soup.ertaga_row.find("strong").text  # Day (Ertaga)
date = soup.ertaga_row.find("div").text  # Date (8 noyabr)
day_temp = soup.ertaga_row.find("span", class_="forecast-day").text  # Day temperature
night_temp = soup.ertaga_row.find("span", class_="forecast-night").text  # Night temperature
description = soup.ertaga_row.find("td", class_="weather-row-desc").text.strip()  # Weather description
precipitation = soup.ertaga_row.find("td", class_="weather-row-pop").text.strip()  # Precipitation

# Display the results
print(f"{day}\n{date}\n{description}\t{day_temp} {night_temp}\t{description}\t{precipitation}")

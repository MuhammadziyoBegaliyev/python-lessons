import requests
from bs4 import BeautifulSoup

# URL for the page
url = "https://obhavo.uz/tashkent"

# Get the HTML content of the page
response = requests.get(url)
soup = BeautifulSoup(response.content, 'html.parser')

# Find the section for the weather forecast table
forecast_table = soup.find("table", class_="weather-table")

if forecast_table:
    # Search for rows in the forecast table
    rows = forecast_table.find_all("tr")
        
    ertaga_row = None
    for row in rows:
        # Look for "Ertaga" keyword in the row text
        if "Ertaga" in row.text:
            ertaga_row = row
            break

    if ertaga_row:
        # Extract the necessary details with error handling
        try:
            day = ertaga_row.find("strong").text.strip()  # Day (Ertaga)
            date = ertaga_row.find("div").text.strip()  # Date (e.g., 8 noyabr)
            day_temp = ertaga_row.find("span", class_="forecast-day").text.strip()  # Day temperature
            night_temp = ertaga_row.find("span", class_="forecast-night").text.strip()  # Night temperature
            description = ertaga_row.find("td", class_="weather-row-desc").text.strip()  # Weather description
            precipitation = ertaga_row.find("td", class_="weather-row-pop").text.strip()  # Precipitation

            # Display the results
            print(f"{day}\n{date}\n{description}\t{day_temp} / {night_temp}\t{precipitation}")
        
        except AttributeError:
            print("Some data could not be retrieved. The structure may have changed.")
    else:
        print("Ertaga row not found in the forecast table.")
else:
    print("Weather forecast table not found on the page.")

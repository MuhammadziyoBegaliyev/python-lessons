# exchangerate-api.com 
import requests
from pprint import pprint as print

API_KEY = 'a392d547edf80bf6fb439e01'

currency = 'USD'

url = f"https://v6.exchangerate-api.com/v6/a392d547edf80bf6fb439e01/latest/USD"
r = requests.get(url)
print(r.status_code)
print(r.json())
print(r.json()['conversion_rates']['UZS'])
# res = r.json()
# print(res)
# print(res['conversion_rate'])


import requests
from bs4 import BeautifulSoup

url = 'https://www.meteoprog.pl/pl/weather/Olsztyn/'

response = requests.get(url)

soup = BeautifulSoup(response.content, features='html.parser')

todays_temp = soup.find("div", class_="today-temperature").find("span")
todays_next_temp = soup.find("ul", class_="today-hourly-weather hide-scroll")

print(todays_next_temp)


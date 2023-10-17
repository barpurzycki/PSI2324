import requests
from bs4 import BeautifulSoup
import matplotlib.pyplot as plt

url = 'https://www.meteoprog.pl/pl/weather/Olsztyn/'

response = requests.get(url)
soup = BeautifulSoup(response.content, features='html.parser')

temp_hourly = []
plotlabel = []

next_temp_ul = soup.find("div", class_="current-temperature").findAll("ul", class_ = "today-hourly-weather hide-scroll")
next_temp_ul_name = soup.find("ul", class_="today-hourly-weather hide-scroll")

for next_temp_li in next_temp_ul:
    next_temp = next_temp_li.findAll("span", class_="today-hourly-weather__temp")
    for temp in next_temp:
            temp_hourly.append(temp.text.strip())

for temp_name in next_temp_ul_name.findAll('span', class_="today-hourly-weather__name"):
    plotlabel.append(temp_name.text)

temp_hourly_value = [int(temp_value.replace('+', '').replace('°', '')) for temp_value in temp_hourly]

plt.plot(plotlabel, temp_hourly_value)
plt.ylabel('°C', rotation=0)
plt.xticks(rotation=45)
plt.title('Wykres temperatury w Olsztynie')
plt.show()


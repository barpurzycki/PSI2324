import requests
import matplotlib.pyplot as plt
import json

id = 400

url = f"https://api.gios.gov.pl/pjp-api/rest/data/getData/{id}"

response = requests.get(url)
if response.status_code != 200:
  assert False

values = []
date = []

data = json.loads(response.content.decode('utf-8'))
for item in range(min(len(data["values"]), 5)):
    values.append(data['values'][item]['value'])
    date.append(data['values'][item]['date'])

plt.plot(values, date)
plt.ylabel('Data pomiaru')
plt.xlabel('Wartość czujnika')
plt.title('Wartość czujnika dla ostatnich 5 godzin') #Jeśli nie pokazuje dla x godziny, to znaczy, że value jest null
plt.show()

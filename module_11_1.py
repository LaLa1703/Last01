import requests
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

print("\nРабота с requests")
response = requests.get("http://api.openweathermap.org/data/2.5/weather?q=Saint+Petersburg&appid=af078918f740218cbabdbce8dcb41426")
if response.status_code == 200:
    data = response.json()
    print(data)
else:
    print("Ошибка:", response.status_code, response.text)


print("\nРабота с pandas")
data_dict = {
    "Имя": ["Даниил", "Алина", "Илья", "Андрей"],
    "Возраст": [21, 33, 38, 44],
    "Город": ["Москва", "Хабаровск", "Казань", "Санкт-Петрбург"],
}
df = pd.DataFrame(data_dict)
print("Данные:")
print(df)
print("\nСредний возраст:", df["Возраст"].mean())


print("\nРабота с matplotlib")
x = np.linspace(0, 100, 500)
y = np.sin(x)

plt.plot(x, y, label="sin(x)", color="blue")
plt.title("График синуса")
plt.xlabel("x")
plt.ylabel("y")
plt.legend()
plt.grid()
plt.show()

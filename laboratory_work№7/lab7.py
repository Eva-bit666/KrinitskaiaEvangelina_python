#Вариант 9
import json
import requests
import io
import tkinter as tk
from PIL import Image, ImageTk

city_name = 'Saint Petersburg'
key = '2f44ab8d94825710392977b37c24d3ac'
response = requests.get(f'https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={key}')
result = json.loads(response.text)
print('Город:', result['name'])
print('Погода:', result['weather'][0]['main'])
print('Влажность:', result['main']['humidity'])
print('Давление:', result['main']['pressure'])

response = requests.get('https://rickandmortyapi.com/api/character?name=rick&status=alive')
result = json.loads(response.text)
character = result['results'][0]
print('Имя:', character['name'])
print('Статус:', character['status'])
print('Вид:', character['species'])
print('Пол:', character['gender'])
print('Родина:', character['origin']['name'])
print('Локация:', character['location']['name'])


def next_image():
    response = requests.get('https://cataas.com/cat?width=500&height=500')
    photo = ImageTk.PhotoImage(Image.open(io.BytesIO(response.content)))
    label.config(image=photo)
    label.image = photo


root = tk.Tk()
label = tk.Label(root)
label.pack()
button = tk.Button(root, text = 'Следующая картинка', command = next_image)
button.pack()
next_image()
root.mainloop()


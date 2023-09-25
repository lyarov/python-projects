import base64
import requests

# Замените "Your Api Key Here" на ваш ключ API
api_key = "d3c3ec10-1b10-4494-a2d4-6acf297441e7"

# Откройте файл с изображением
with open('image.png', 'rb') as image_file:
    image_data = image_file.read()

# Параметры запроса
url = 'https://api.benzin.io/v1/removeBackground'
headers = {
    'X-API-Key': api_key,
}
data = {
    'size': 'full',  # Установите размер "full"
    'output_format': 'json'
}

# Выполнение POST-запроса с данными формата "multipart/form-data"
response = requests.post(url, headers=headers, data=data, files={'image_file': ('image.jpg', image_data)})

# Проверка успешности запроса
if response.status_code == 200:
    # Получение данных в формате JSON
    result_data = response.json()
    
    # Извлечение бинарных данных изображения
    image_base64 = result_data.get('image_raw', '')

    if image_base64:
            with open('result_image.png', 'wb') as result_file:
                result_file.write(base64.b64decode(image_base64))
            print("Изображение успешно сохранено.")
    else:
        print("Нет данных изображения в ответе.")
else:
    print(f"Ошибка {response.status_code}: {response.text}")

# Создаем "курьера" который будет отправляь данные на сервер

import requests # это библиотека python
import configuration # это информация из папки конфигурации
import data # это информация из папки дата

# Пишем самого "курьера"
def post_new_user(body): #Создаем ф-ию которая применяет данные пользователя
    return requests.post( # говорим курьеру сделать пост запроос
        configuration.URL_SERVICE + configuration.CREATE_USER_PATH, #склеиаваем адрес + путь к ручке
        json=body, # передае данные тела в формате джсон
        headers=data.headers # прикрепляю на коробку наклейку "я отправил джсон"
    )

# Теперь пишем вспомогательную ф-ию которая вытащит токен
def get_new_user_token(): # это ф-ия просто добывает токен
    user_response = post_new_user(data.user_body) # вызов функции и передаем туда данные из даты
    return user_response.json()["authToken"] # залезаем в ответ, находим токен и возвращаем его значение

def post_new_kit(kit_body, auth_token): # создание ф-ии которая принимает 2 аргумента
    headers = data.headers.copy() # берем наши заготовки и делаем копию
    headers["Authorization"] = f"Bearer {auth_token}" # добавляем в копию заголовка новый ключ авторизации

    return requests.post( # отправляем запрос на сервер, передаем туда путь создания набора, тело и заголовоки
        configuration.URL_SERVICE + configuration.CREATE_KIT_PATH,
        json=kit_body,
        headers=headers
    )

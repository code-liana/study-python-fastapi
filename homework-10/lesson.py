import requests_test
# # python3 -m venv venv -------------- source venv/bin/activate ---------------- pip install requests
site = "https://jsonplaceholder.typicode.com"
# # response = requests.get(url=site)
# # print(response)

# Завдання 2: Клієнт та Сервер
#
# 2.1. Опишіть різницю між клієнтом і сервером у контексті веб-розробки.
#
# 2.2. Поясніть, як клієнт та сервер взаємодіють за допомогою HTTP-запитів та відповідей.
#
# Блок бібліотеки requests:
#
# Завдання 1: Виконання GET-запиту
#
# Створіть Python-сценарій, який використовує бібліотеку requests для виконання GET-запиту до веб-ресурсу та виведення вмісту веб-сторінки на екран. Використовуйте функцію requests.get() для виконання запиту.
# response_get = requests.get(url=site)
# for header, value in response_get.headers.items():
#     print(f"Header: {header} --> Value: {value}")
# # print(response_get.text)
# print("------------")

# Завдання 2: Параметри запиту
#
# Розширте попереднє завдання, додаючи можливість вказати параметри запиту. Виконайте GET-запит до веб-ресурсу, передаючи параметри запиту, такі як параметри запиту у URL або параметри через словник.
params = {"userId": 1}  # Приклад параметрів запиту
response_get_users = requests.get(url=site +"/posts/", params=params)
#
# print(response_get_users.status_code)
# print(response_get_users.reason)
# print(response_get_users.text)
# print(response_get_users.encoding)

# for header, value in response_get_users.headers.items():
#     print(f"Header: {header} --> Value: {value}")
# Завдання 3: POST-запит
#
# Створіть Python-сценарій для виконання POST-запиту до веб-ресурсу. Відправте дані на сервер, наприклад, форму з ім'ям користувача і паролем.
# params={
#     "username": "PrettyCool123",
#     'password': "pass"
# }
# response_post_users = requests.post(url=site +"/users/", params=params)
# print(response_post_users.status_code)
# print(response_post_users.reason)
# print(response_post_users.text)
# Завдання 4: Обробка відповіді
#
# Після виконання запиту, розпарсьте вміст HTTP-відповіді та виведіть потрібну інформацію. Наприклад, виведіть заголовки відповіді або вміст сторінки.
# def make_post_request(base_url, data=None):
#     """
#     Виконує POST-запит до веб-ресурсу з можливістю передачі даних.
#
#     :param base_url: Базова URL-адреса ресурсу
#     :param data: Словник із даними для запиту (опціонально)
#     :return: Заголовки та вміст відповіді сервера
#     """
#     try:
#         # Виконуємо POST-запит із даними
#         response = requests.post(base_url, json=data)
#         # Перевірка статусу відповіді
#         response.raise_for_status()
#
#         # Отримання заголовків і вмісту сторінки
#         headers = response.headers
#         content = response.text
#
#         return headers, content  # Повертаємо заголовки та вміст сторінки
#     except requests.exceptions.RequestException as e:
#         return f"Помилка запиту: {e}", None


# Приклад використання
# if __name__ == "__main__":
#     base_url = "https://jsonplaceholder.typicode.com/posts"
#     data = {
#         "title": "foo",
#         "body": "bar",
#         "userId": 1
#     }  # Приклад даних для запиту
#
#     headers, content = make_post_request(base_url, data=data)
#
#     if headers and content:
#         print("Заголовки відповіді:")
#         for key, value in headers.items():
#             print(f"{key}: {value}")
#
#         print("\nВміст сторінки:")
#         print(content)
#     else:
#         print("Не вдалося виконати запит.")

# Завдання 5: Обробка помилок
#
# Додайте обробку помилок до вашого коду. Обробляйте можливі винятки, такі як requests.exceptions.RequestException, та виводьте відповідні повідомлення про помилку.
def make_post_request(base_url, data=None):
    """
    Виконує POST-запит до веб-ресурсу з можливістю передачі даних.

    :param base_url: Базова URL-адреса ресурсу
    :param data: Словник із даними для запиту (опціонально)
    :return: Заголовки та вміст відповіді сервера
    """
    try:
        # Виконуємо POST-запит із даними
        response = requests.post(base_url, json=data)
        # Перевірка статусу відповіді
        response.raise_for_status()

        # Отримання заголовків і вмісту сторінки
        headers = response.headers
        content = response.text

        return headers, content  # Повертаємо заголовки та вміст сторінки

    except requests.exceptions.HTTPError as http_err:
        return f"HTTP помилка: {http_err}", None
    except requests.exceptions.ConnectionError as conn_err:
        return f"Помилка з'єднання: {conn_err}", None
    except requests.exceptions.Timeout as timeout_err:
        return f"Помилка тайм-ауту: {timeout_err}", None
    except requests.exceptions.RequestException as req_err:
        return f"Невідома помилка запиту: {req_err}", None


# Приклад використання
if __name__ == "__main__":
    base_url = "https://jsonplaceholder.typicode.com/posts"
    data = {
        "title": "foo",
        "body": "bar",
        "userId": 1
    }  # Приклад даних для запиту

    headers, content = make_post_request(base_url, data=data)

    if headers and content:
        print("Заголовки відповіді:")
        for key, value in headers.items():
            print(f"{key}: {value}")

        print("\nВміст сторінки:")
        print(content)
        # Збереження вмісту у файл
        with open("response_content.txt", "w", encoding="utf-8") as file:
            file.write(content)
        print("\nВміст відповіді збережено у файл 'response_content.txt'.")
    else:
        print("Не вдалося виконати запит.")
# Завдання 6: Збереження вмісту в файл
#
# Розширте ваш код, щоб зберегти отриманий вміст веб-сторінки у файл. Використайте функціонал Python для роботи з файлами для збереження вмісту.
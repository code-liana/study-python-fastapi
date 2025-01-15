# ### Списки:
#
# 1. **Робота із списками:**
#    Завдання: Створіть список чисел. Додайте до списку числа 10 і 20, видаліть число 10 і виведіть отриманий список.
# numbers_list = [ 1, 2, 8, 9, 10, 11, 12, 18, 19, 20]
# numbers_list.insert(2, 10)
# print(numbers_list)
# numbers_list.extend([20, 21])
# print(numbers_list)
# numbers_list.pop(10)
# numbers_list.remove(10)
# print(numbers_list)
from faker.utils.decorators import lowercase

# 2. **Знаходження суми:**
#    Завдання: Створіть список чисел. Знайдіть та виведіть суму всіх чисел у списку.
# numbers_list = [ 1, 2, 8, 9, 10, 11, 12, 18, 19, 20]
# result=0
# for i in numbers_list:
#     result +=i
# print(f"Result ==== ", result)

# 3. **Подвійні значення:**
#    Завдання: Створіть список чисел. Подвойте кожне число у списку та виведіть результат.
# numbers_list = [1, 2, 8, 9, 10, 11, 12, 18, 19, 20]
# duplicate_numbers = numbers_list * 2
# duplicate_numbers.sort()
# print(duplicate_numbers)


# ### Кортежі:
#
# 1. **Робота із кортежами:**
#    Завдання: Створіть кортеж з трьох різних предметів, таких як ("яблуко", "банан", "апельсин"). Виведіть кожен елемент кортежу окремо.
# veggies = ("яблуко", "банан", "апельсин")
# for i in veggies:
#     print(i)

# 2. **Об'єднання кортежів:**
#    Завдання: Створіть два кортежі з числами і об'єднайте їх у новий кортеж. Виведіть отриманий кортеж.
# tuple_1 = (1, 5, "Test", True)
# tuple_2 = ("Weather", 5, False, 1, 2)
# print(tuple_1[:], tuple_2[:])
# tuple_3 = tuple_1 + tuple_2
# print(tuple_3)
# ### Словники:
#
# 1. **Робота із словниками:**
#    Завдання: Створіть словник, що містить інформацію про вашого улюбленого спортсмена (ім'я, вік, спорт, команда тощо). Виведіть цю інформацію на екран.
favorite_athlete = {
    "ім'я": "Олександр Усик",
    "вік": 37,
    "спорт": "бокс",
    "країна": "Україна",
    "вагова категорія": "важка вага",
    "титули": ["WBA", "WBO", "IBF", "The Ring"],
    "досягнення": "Олімпійський чемпіон 2012 року",
    "поточний статус": "Діючий чемпіон світу",
}
# print(favorite_athlete)
# print(len(favorite_athlete))
# print(type(favorite_athlete))
# print(favorite_athlete["вік"])
# print(favorite_athlete.keys())
# print(favorite_athlete.values())
# print(favorite_athlete.items())

# 2. **Оновлення словника:**
#    Завдання: Створіть словник, що містить ваші улюблені книги (назва книги та рік видання). Додайте до словника нову улюблену книгу та виведіть оновлений словник.
favorite_books = {
    "451° за Фаренгейтом": 1953,
    "Майстер і Маргарита": 1967,
    "Гаррі Поттер і філософський камінь": 1997,
    "Аліса в Країні Див": 1865,
    "Тіні забутих предків": 1911
}

print(favorite_books)
favorite_books['Володар перснів: Хранителі Персня'] = 1954
print(favorite_books)

# 3. **Пошук значення:**
#    Завдання: Створіть словник, що містить інформацію про країни та їх столиці. Запитайте користувача про назву країни і виведіть столицю цієї країни (якщо така країна є у словнику).
countries_capitals = {
    "United States": "Washington, D.C.",
    "Ukraine": "Kyiv",
    "Canada": "Ottawa",
    "Mexico": "Mexico City",
    "Brazil": "Brasília",
    "United Kingdom": "London",
    "France": "Paris",
    "Germany": "Berlin",
    "Italy": "Rome",
    "Spain": "Madrid",
    "Australia": "Canberra",
    "Japan": "Tokyo",
    "China": "Beijing",
    "India": "New Delhi",
    "russia": "PARASHA",
    "South Africa": "Pretoria",
    "Egypt": "Cairo",
    "Argentina": "Buenos Aires",
    "Sweden": "Stockholm",
    "Norway": "Oslo",
    "Netherlands": "Amsterdam"
}

countries_capitals = {
    "United States": "Washington, D.C.",
    "Ukraine": "Kyiv",
    "Canada": "Ottawa",
    "Mexico": "Mexico City",
    "Brazil": "Brasília",
    "United Kingdom": "London",
    "France": "Paris",
    "Germany": "Berlin",
    "Italy": "Rome",
    "Spain": "Madrid",
    "Australia": "Canberra",
    "Japan": "Tokyo",
    "China": "Beijing",
    "India": "New Delhi",
    "Russia": "Moscow",
    "South Africa": "Pretoria",
    "Egypt": "Cairo",
    "Argentina": "Buenos Aires",
    "Sweden": "Stockholm",
    "Norway": "Oslo",
    "Netherlands": "Amsterdam"
}

def what_capital():
    user_input = input("Provide a country: ").strip().title()
    capital = countries_capitals.get(user_input)
    if capital:
        print(f"The capital of {user_input} is {capital}.")
    else:
        print("Country not found. Please try another country.")

what_capital()


# Завершіть кожне завдання, використовуючи вбудовані методи для списків, кортежів та словників. Бажаю успіхів у виконанні цих завдань!
#

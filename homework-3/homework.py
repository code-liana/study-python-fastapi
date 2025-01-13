# 1. **Перевірка паролю:**
#    Завдання: Напишіть програму, яка встановлює початковий пароль і перевіряє, чи введений користувачем пароль співпадає з ним. Якщо пароль дорівнює "password123", виведіть повідомлення "Ви увійшли в систему". В іншому випадку виведіть повідомлення "Неправильний пароль".
from operator import index

from faker.utils.decorators import lowercase

user_1 = {
    "name": "James",
    "username": "james246",
    "password": "password123",
    "age": 30,
    "status": "active",
    "visibility": True
}

user_2 = {
    "name": "Liz",
    "username": "liz",
    "password": "123",
    "age": 20,
    "status": "disabled",
    "visibility": True
}

user_3 = {
    "name": "Bob",
    "username": "BobSponge",
    "password": "SpongeMeDirty",
    "age": 21,
    "status": "active",
    "visibility": True
}

users = [user_1, user_2, user_3]

def credentials_validator(username, password):
    # username = input("What is your username?")

    for user in users:
        if username == user["username"]:
            # password = input("What is your password?")
            if password == user["password"]:
                print("You are successfully logged into the system")
                return
            else:
                print("Wrong password")
                return
    print("Username not found.")

# credentials_validator()
credentials_validator(users[0]["username"], users[0]["password"])
# credentials_validator("james", users[0]["password"])
# credentials_validator(users[0]["username"], "pass")


# 2. **Визначення днів тижня:**
#    Завдання: Створіть програму, яка встановлює номер дня тижня і виводить назву відповідного дня тижня. Якщо номер дня недійсний (менше 1 або більше 7), виведіть повідомлення про помилку.
days_of_the_week = {
    1: "Monday",
    2: "Tuesday",
    3: "Wednesday",
    4: "Thursday",
    5: "Friday",
    6: "Saturday",
    7: "Sunday"
}

def what_day_is_it_today():
    while True:  # Keeps asking until a valid input or exit condition
        print('------------->To exit, type "0" or any letter.<---------------')
        week_day = input("What day of the week are you looking for? ")

        # Break the loop if the input is empty or contains any non-digit character
        if not week_day.isdigit() or week_day == "":
            print("Have a great day!")
            break

        week_day = int(week_day)  # Convert input to an integer after validation

        if 1 <= week_day <= 5:
            print(f"Day {week_day} is {days_of_the_week[week_day]} and it's a weekday. Hope you have an amazing day!")
        elif 6 <= week_day <= 7:
            print(f"Day {week_day} is {days_of_the_week[week_day]} and it's the weekend. Hope you have a great rest!")
        else:
            print("Week has only 7 days, so please choose a number between 1 and 7.")

# what_day_is_it_today()
# ### Цикли:
#
# 1. **Таблиця множення:**
#    Завдання: Виведіть таблицю множення для заданого числа від 1 до 10.
# number = input("Provide a number from 1 to 10 to get a number multiplications: ")
# count = 0
# while count < 10:
#     for i in range(11):
#         print(f"{number} x {i} = {i*int(number)}")
#         count+=1
# 2. **Сума чисел:**
#    Завдання: Визначте список чисел і обчисліть їх суму.
# list_numbers = [1,2,3,4,5]
# storage = 0
# for number in list_numbers:
#     summary = storage+number
#     storage = summary
#     print(summary)
# 3. **Факторіал числа:**
#    Завдання: Обчисліть факторіал заданого числа.
#iterative approach
# def factorial(number):
#     factorial_num = 1
#     for i in range(1, number + 1):
#         factorial_num *= i
#     return factorial_num
#
# print(factorial(10))

#recursive approach
# def factorial_recursive(n):
#     if n == 0 or n == 1:
#         return 1
#     return n * factorial_recursive(n - 1)
#
# print(factorial_recursive(5))

# 4. **Парні числа:**
#    Завдання: Виведіть всі парні числа від 1 до 50.
# for i in range(1,51):
#     if not i%2:
#         print(i)

# 5. **Пошук простих чисел:**
#    Завдання: Знайдіть всі прості числа в заданому діапазоні.
# for i in range(1, 100):
#     if (i%2) and (i%3) and (i%5):
#         print("prime number -------->", i)

def is_prime(n):
    # Prime numbers must be greater than 1
    if n <= 1:
        return False

    # Check for factors from 2 to n-1
    for i in range(2, n):
        if n % i == 0:  # If n is divisible by any number, it's not prime
            return False
    return True

# Print prime numbers from 2 to 99
for i in range(2, 100):
    if is_prime(i):
        print("Prime number:", i)

# Створіть власні змінні або встановіть початкові значення, щоб виконати ці завдання без використання `input`. Використовуйте умовні конструкції і цикли для розв'язання кожного завдання. Бажаю успіхів у виконанні цих завдань!
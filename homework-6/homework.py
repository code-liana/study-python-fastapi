import turtle
# **Завдання 1: Створення класу і об'єктів**
#
# Створіть клас `Animal`, який представляє тварину. Кожний об'єкт класу `Animal` повинен мати наступні атрибути:
#
# - `name` (ім'я тварини)
# - `species` (вид тварини)
# - `age` (вік тварини)
#
# Створіть конструктор класу, який ініціалізує ці атрибути при створенні об'єкта. Напишіть метод `make_sound()`, який буде виводити звук, який виділяє тварина.
#
# Створіть два об'єкта класу `Animal` з різними характеристиками та викличте їхні методи `make_sound()`.
class Animal:
    def __init__(self, name, species, age):
        self.name = name
        self.species = species.lower()  # Convert to lowercase
        self.age = age
        self.animals = {
            "dog": "Bark",
            "cat": "Meow",
            "cow": "Moo",
            "duck": "Quack",
            "sheep": "Baa"
        }
        self.name_sound()

    def name_sound(self):
        if self.species in self.animals:
            print(f"{self.name} is a {self.species.capitalize()} that makes \"{self.animals[self.species]}\" sound")
        else:
            print("Please try another animal!")

animal = Animal("Script", "at", 7)

# **Завдання 2: Робота з об'єктами**
#
# Створіть клас `Rectangle`, який представляє прямокутник. Кожен об'єкт класу `Rectangle` повинен мати наступні атрибути:
#
# - `width` (ширина прямокутника)
# - `height` (висота прямокутника)
#
# Створіть конструктор класу, який ініціалізує ці атрибути при створенні об'єкта. Напишіть метод `calculate_area()`, який розраховує площу прямокутника (площа = ширина * висота).
#
# Створіть два об'єкта класу `Rectangle` з різними розмірами та викличте їхні методи `calculate_area()`, виведіть площу прямокутників на екран.
import turtle


class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.calculate_area()

    def calculate_area(self):
        return print("Area:", self.width * self.height)

    def draw_rectangle(self, start_x=0, start_y=0):
        turtle.penup()
        turtle.goto(start_x, start_y)
        turtle.pendown()
        turtle.speed(1)
        turtle.begin_fill()

        for _ in range(2):
            turtle.forward(self.width)
            turtle.left(90)
            turtle.forward(self.height)
            turtle.left(90)

        turtle.end_fill()

rectangle_1 = Rectangle(200, 100)
rectangle_1.draw_rectangle()

rectangle_2 = Rectangle(50, 120)
rectangle_2.draw_rectangle(200, 200)

turtle.done()




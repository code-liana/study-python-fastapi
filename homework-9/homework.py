# Завдання 1: Принцип єдиного обов'язку (Single Responsibility Principle - SRP)
#
# Спроектуйте і реалізуйте клас "Користувач" (User), який відповідає принципу SRP. В цьому класі повинні бути методи для створення користувача, оновлення даних користувача та видалення користувача. Переконайтеся, що кожен метод відповідає за одну конкретну функцію.
import math
import uuid
from abc import abstractmethod, ABC


class User:
    def __init__(self):
        """
        Ініціалізує новий об'єкт користувача.
        """
        self.user = []
        self.count = 0

    def add_user(self, name, email):
        self.count += 1
        user_id = uuid.uuid4()
        self.user.append({"id": user_id, "name": name, "email": email})

    def update_name(self, user_id, new_name):
        for u in self.user:
            if u["id"] == user_id:
                u["name"] = new_name
                print(f"Ім'я користувача оновлено на: {new_name}")
                return
        print("Користувача не знайдено.")

    def update_email(self, user_id, new_email):
        for u in self.user:
            if u["id"] == user_id:
                u["email"] = new_email
                print(f"Електронна адреса користувача оновлена на: {new_email}")
                return
        print("Користувача не знайдено.")

    def delete_user(self, user_id):
        self.user = [u for u in self.user if u["id"] != user_id]
        print(f"Користувач з ID {user_id} видалений.")

    def print_users(self):
        for u in self.user:
            print(u)

# Приклад використання
user = User()
user.add_user(name="Олександр", email="alex@example.com")
user.add_user(name="Tim", email="tim@example.com")
user.add_user(name="Olia", email="olia@example.com")
user.print_users()

# Оновлення даних користувача
first_user_id = user.user[0]["id"]
user.update_name(first_user_id, "Андрій")
user.update_email(first_user_id, "andriy@example.com")

# Видалення користувача
user.delete_user(first_user_id)
user.print_users()



# Завдання 2: Принцип відкритості/закритості (Open/Closed Principle - OCP)
#
# Створіть інтерфейс "Фігура" (Shape) та два класи, які реалізують цей інтерфейс, наприклад, "Коло" (Circle) та "Прямокутник" (Rectangle). Потім додайте новий клас, який розраховує площу будь-якої фігури, не модифікуючи існуючі класи. Використовуйте принцип OCP для розширення функціональності.
class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

# Клас "Коло"
class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14159 * self.radius * self.radius

# Клас "Прямокутник"
class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

# Клас для розрахунку площі будь-якої фігури
class AreaCalculator:
    @staticmethod
    def calculate(shape: Shape):
        return shape.area()

# Приклад використання
circle = Circle(5)
rectangle = Rectangle(4, 6)

print("Площа кола:", AreaCalculator.calculate(circle))
print("Площа прямокутника:", AreaCalculator.calculate(rectangle))


# Завдання 3: Принцип підстановки Лісков (Liskov Substitution Principle - LSP)
#
# Створіть ієрархію класів для геометричних фігур, де кожен підклас (наприклад, "Квадрат" і "Круг") може замінити базовий клас "Фігура" без порушення функціональності. Переконайтеся, що ці підкласи можуть використовуватися замість базового класу у всіх контекстах без проблем.
#
# Завдання 4: Принцип інтерфейсу користувача (Interface Segregation Principle - ISP)
#
# Розробіть інтерфейс "Мережевий принтер" (NetworkPrinter), який включає методи для друку, сканування та копіювання. Потім створіть два класи: "Принтер" (Printer) та "Сканер" (Scanner), які реалізують цей інтерфейс та використовують лише ті методи, які їм потрібні. Переконайтеся, що жоден з класів не має пустого методу.
#
# Завдання 5: Принцип залежностей (Dependency Inversion Principle - DIP)
#
# Використовуючи принцип DIP, переробіть код залежностей у вашому проекті так, щоб він використовував абстракції та інтерфейси замість конкретних реалізацій. Переконайтеся, що класи залежностей не знають про конкретну реалізацію інших класів.
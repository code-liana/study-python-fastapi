# Завдання 1: Інкапсуляція
#
# Створіть клас "Користувач" (User), який має такі приватні поля (інкапсульовані дані):
#
# Ім'я (name)
# Електронна пошта (email)
# Пароль (password)
# Напишіть публічні методи для установки і отримання значень цих полів (геттери і сеттери). Потім створіть об'єкт класу "Користувач" і встановіть значення полів, а також виведіть їх на екран.
import math
from abc import abstractmethod
from curses.textpad import rectangle


class User:
    def __init__(self, name, email, password):
        self.__name = name
        self.__email = email
        self.__password = password

    def get_name(self):
        return self.__name

    def set_name(self, name):
        self.__name = name

    def get_email(self):
        return self.__email

    def set_email(self, email):
        self.__email = email

    def get_password(self):
        return self.__password

    def set_password(self, password):
        self.__password = password

user = User("Yuliana", "test_email@ail.com", "password123")
print(f"Username: {user.get_name()}, \nEmail address: {user.get_email()}, \nYour password: {user.get_password()} ")
user.set_name("James")
user.set_email("test123@ttest.co")
user.set_password("123")
print(f"Username: {user.get_name()}, \nEmail address: {user.get_email()}, \nYour password: {user.get_password()} ")

# Завдання 2: Абстракція
#
# Створіть клас "Фігура" (Shape), який буде абстрактним класом. У цьому класі визначіть абстрактний метод "обчислити_площу" (calculate_area).
#
# Створіть підкласи цього класу для різних геометричних фігур, наприклад, "Коло" (Circle), "Прямокутник" (Rectangle) і "Трикутник" (Triangle). У кожному з підкласів реалізуйте метод "обчислити_площу" відповідно до формули для обчислення площі кожної фігури.
#
# Створіть об'єкти кожного з підкласів і використайте метод "обчислити_площу", щоб вивести площу кожної фігури на екран.
class Shape:
    @abstractmethod
    def calculate_area(self):
        pass

class Circle(Shape):
    def __init__(self, area):
        self.area = area

    def calculate_area(self):
        result = math.pi * self.area ** 2
        return result

class Rectangle(Shape):

    def __init__(self, width, height):
        self.width = width
        self.height = height

    def calculate_area(self):
        return self.width * self.height


class Triangle(Shape):

    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def calculate_area(self):
        s = (self.a + self.b + self.c) / 2
        # Calculate the area
        area = math.sqrt(s * (s - self.a) * (s - self.b) * (s - self.c))
        return area


circle = Circle(5)
print(circle.calculate_area())

rectan = Rectangle(34, 30)
print(rectan.calculate_area())

triangle = Triangle(10, 10,15)
print(triangle.calculate_area())


# Завдання 3: Користування інкапсуляцією та абстракцією у реальному коді
#
# Розгляньте фрагмент коду з існуючого проекту або бібліотеки та ідентифікуйте в ньому використання інкапсуляції та абстракції. Поясніть, як вони застосовуються і як це допомагає поліпшити читабельність та підтримку коду.
#
class BankAccount:
    def __init__(self, owner, balance=0):
        self.__owner = owner  # Інкапсуляція: приховуємо деталі реалізації
        self.__balance = balance  # Приватний атрибут

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            return f"Deposited {amount}. New balance: {self.__balance}"
        return "Invalid deposit amount"

    def withdraw(self, amount):
        if 0 < amount <= self.__balance:
            self.__balance -= amount
            return f"Withdrew {amount}. Remaining balance: {self.__balance}"
        return "Invalid withdrawal amount or insufficient funds"

    def get_balance(self):
        return self.__balance  # Абстракція: надає доступ лише до необхідних деталей


from abc import ABC, abstractmethod


# Abstract class for accounts - showcasing abstraction
class BankAccount(ABC):
    def __init__(self, account_number, owner, balance=0.0):
        self._account_number = account_number  # Protected attribute
        self._owner = owner  # Protected attribute
        self._balance = balance  # Protected attribute for encapsulation

    @abstractmethod
    def deposit(self, amount):
        pass

    @abstractmethod
    def withdraw(self, amount):
        pass

    def get_balance(self):
        return self._balance

    def __str__(self):
        return f"Account[{self._account_number}] - Owner: {self._owner}, Balance: ${self._balance:.2f}"


# Concrete class for savings account - applying abstraction and encapsulation
class SavingsAccount(BankAccount):
    INTEREST_RATE = 0.02  # Class attribute representing a constant interest rate

    def deposit(self, amount):
        if amount > 0:
            self._balance += amount
            return f"Deposited ${amount}. New balance: ${self._balance:.2f}"
        return "Deposit amount must be positive"

    def withdraw(self, amount):
        if 0 < amount <= self._balance:
            self._balance -= amount
            return f"Withdrew ${amount}. Remaining balance: ${self._balance:.2f}"
        return "Invalid withdrawal amount or insufficient funds"

    def apply_interest(self):
        self._balance += self._balance * self.INTEREST_RATE
        return f"Interest applied. New balance: ${self._balance:.2f}"


# Another concrete class for checking account
class CheckingAccount(BankAccount):
    OVERDRAFT_LIMIT = 500  # Allow overdraft up to a certain limit

    def deposit(self, amount):
        if amount > 0:
            self._balance += amount
            return f"Deposited ${amount}. New balance: ${self._balance:.2f}"
        return "Deposit amount must be positive"

    def withdraw(self, amount):
        if 0 < amount <= self._balance + self.OVERDRAFT_LIMIT:
            self._balance -= amount
            return f"Withdrew ${amount}. Remaining balance: ${self._balance:.2f}"
        return "Exceeds overdraft limit or invalid withdrawal amount"


# Class to manage multiple accounts using abstraction
class Bank:
    def __init__(self):
        self.__accounts = {}  # Private dictionary to store accounts (encapsulation)

    def add_account(self, account):
        self.__accounts[account._account_number] = account
        return f"Account {account._account_number} added successfully."

    def get_account(self, account_number):
        return self.__accounts.get(account_number, "Account not found")

    def show_all_accounts(self):
        return [str(account) for account in self.__accounts.values()]


# Usage Example
if __name__ == "__main__":
    # Creating bank and accounts
    bank = Bank()

    acc1 = SavingsAccount("123456", "Alice", 1000)
    acc2 = CheckingAccount("654321", "Bob", 500)

    bank.add_account(acc1)
    bank.add_account(acc2)

    # Operations on accounts
    print(acc1.deposit(500))
    print(acc1.apply_interest())
    print(acc2.withdraw(800))
    print(bank.show_all_accounts())

    # Trying to access encapsulated data (will raise an error)
    # print(bank.__accounts)  # AttributeError: 'Bank' object has no attribute '__accounts'


class Student:
    def __init__(self, student_id, name, grades):
        self._student_id = student_id  # Protected attribute
        self._name = name  # Protected attribute
        self._grades = grades  # List of grades

    def __str__(self):
        # This method returns a nice text description of the student
        avg_grade = sum(self._grades) / len(self._grades) if self._grades else 0
        return f"Student[{self._student_id}] - {self._name}, Average Grade: {avg_grade:.2f}"

    def add_grade(self, grade):
        self._grades.append(grade)
        return f"Grade {grade} added. New average: {sum(self._grades) / len(self._grades):.2f}"

    def get_grades(self):
        return self._grades


class School:
    def __init__(self):
        self.__students = {}  # Private dictionary to store student records

    def add_student(self, student):
        self.__students[student._student_id] = student
        return f"Student {student._name} added successfully."

    def show_all_students(self):
        # This function uses str(student) which calls the __str__ method in Student class
        return [str(student) for student in self.__students.values()]

school = School()

# Creating students
student1 = Student(101, "Alice", [85, 90, 78])
student2 = Student(102, "Bob", [70, 88, 92])

# Adding students to the school
print(school.add_student(student1))
print(school.add_student(student2))
print(school.show_all_students())
print(student1.add_grade(95))
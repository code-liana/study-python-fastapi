import random

import calculator
from module import utilities


def operations(operation, num_1, num_2):
    operation = input("What would you like to do? (add, subtract, multiply, divide): ")
    num_1 = input("Provide first number: ")
    num_2 = input("Provide second number: ")
    if operation == "add":
        calculator.add(num_1, num_2)
    if operation == "subtract":
        calculator.subtract(num_1, num_2)
    if operation == "multiply":
        calculator.multiply(num_1, num_2)
    if operation == "divide":
        calculator.divide(num_1, num_2)

# operations(operation, int(num_1), int(num_2))

random_numbers = [random.randint(1, 100) for _ in range(10)]
print(random_numbers)
print(utilities.calculate_average(random_numbers))
print(utilities.find_max(random_numbers))
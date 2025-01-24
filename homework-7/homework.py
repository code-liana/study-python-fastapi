import json

# Opening JSON file
json_file = open('data.json')

# returns JSON object as a dictionary
data = json.load(json_file)

# Closing file
json_file.close()

# # Iterating through the json list
# for i in data:
#     print(i)
#
# # Closing file
# json_file.close()
# **Завдання 1: Наслідування**
#
# Створіть базовий клас `Vehicle` (транспортний засіб), який містить наступні атрибути:
#
# - `make` (виробник)
# - `model` (модель)
# - `year` (рік виробництва)
#
# Додайте конструктор класу `Vehicle`, який ініціалізує ці атрибути.
#
# Створіть підкласи (похідні класи) від `Vehicle` для різних видів транспорту, наприклад, `Car`, `Motorcycle`, `Bicycle`, тощо. Кожен підклас повинен мати додаткові атрибути та методи, які є специфічними для цього виду транспорту. Наприклад, для класу `Car` можна додати атрибут `fuel_type` та метод `start_engine()`.
#
# Створіть об'єкти для кожного з підкласів та виведіть їхні атрибути на екран.
class Vehicle:
    """Base Class"""

    def __init__(self, brand):
        self._brand = brand

    def display_brand(self):
        for i in data:
            if self._brand == i['brand']:
                return print(f"Your vehicle is {i['brand']}")
        return "Brand not found"

    def display_model(self):
        for i in data:
            if self._brand == i['brand']:
                return print(f"Your vehicle model is {i['model']}")
        return "Model not found"

    def display_year(self):
        for i in data:
            if self._brand == i['brand']:
                return print(f"Your vehicle was created in {i['year_created']}")
        return "Year not found"

    def display_type(self):
        for i in data:
            if self._brand == i['brand']:
                return print(f"Your vehicle type is {i['type']}")
        return "Type not found"

    def display_info(self):
        for i in data:
            if self._brand == i['brand']:
                return print(f"Your {i['type']} is {i['brand']} {i['model']} made in {i['year_created']}")
        return "Type not found"

class Car(Vehicle):
    type_list = []

    def group_by_type(self):
        for i in data:
            if i.get('type') == 'Car':  # Check if 'type' key exists and matches 'Car'
                # Create a filtered copy of the dictionary without the 'type' key
                filtered_item = {key: value for key, value in i.items() if key != 'type'}

                self.type_list.append(filtered_item)
        print(self.type_list)



class Motorcycle(Vehicle):
    type_list = []

    def group_by_type(self):
        for i in data:
            if i.get('type') == 'Motorcycle':  # Check if 'type' key exists and matches 'Motorcycle'
                # Create a filtered copy of the dictionary without the 'type' key
                filtered_item = {key: value for key, value in i.items() if key != 'type'}

                self.type_list.append(filtered_item)
        print(self.type_list)

class Truck(Vehicle):
    type_list = []

    def group_by_type(self):
        for i in data:
            if i.get('type') == 'Truck':  # Check if 'type' key exists and matches 'Truck'
                # Create a filtered copy of the dictionary without the 'type' key
                filtered_item = {key: value for key, value in i.items() if key != 'type'}

                self.type_list.append(filtered_item)
        print(self.type_list)

class SUV(Vehicle):
    type_list = []

    def group_by_type(self):
        for i in data:
            if i.get('type') == 'SUV':  # Check if 'type' key exists and matches 'SUV'
                # Create a filtered copy of the dictionary without the 'type' key
                filtered_item = {key: value for key, value in i.items() if key != 'type'}

                self.type_list.append(filtered_item)
        print(self.type_list)

class Electric(Vehicle):
    type_list = []

    def group_by_type(self):
        for i in data:
            if i.get('type') == 'Electric':  # Check if 'type' key exists and matches 'Electric'
                # Create a filtered copy of the dictionary without the 'type' key
                filtered_item = {key: value for key, value in i.items() if key != 'type'}

                self.type_list.append(filtered_item)
        print(self.type_list)

class Van(Vehicle):
    type_list = []

    def group_by_type(self):
        for i in data:
            if i.get('type') == 'Van':  # Check if 'type' key exists and matches 'Van'
                # Create a filtered copy of the dictionary without the 'type' key
                filtered_item = {key: value for key, value in i.items() if key != 'type'}

                self.type_list.append(filtered_item)
        print(self.type_list)

class Hybrid(Vehicle):
    type_list = []

    def group_by_type(self):
        for i in data:
            if i.get('type') == 'Hybrid':  # Check if 'type' key exists and matches 'Hybrid'
                # Create a filtered copy of the dictionary without the 'type' key
                filtered_item = {key: value for key, value in i.items() if key != 'type'}

                self.type_list.append(filtered_item)
        print(self.type_list)
v= Car('Dodge' )
print(v.display_info())
v.group_by_type()
# **Завдання 2: Поліморфізм**
#
# Створіть метод `display_info()` у базовому класі `Vehicle`, який виводить загальну інформацію про транспортний засіб (наприклад, "Це [виробник] [модель] [рік] року виробництва.").
#
# В кожному з підкласів перевизначте метод `display_info()` для виведення специфічної інформації про цей вид транспорту.
#
# Створіть список об'єктів з різних видів транспорту, викличте метод `display_info()` для кожного об'єкта, і спостерігайте за тим, як поліморфізм дозволяє викликати правильну версію методу для кожного об'єкта.
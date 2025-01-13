from random import randint


#INTEGER
def generateRandomNumber():
    num = randint(1, 5)
    print(f"Looping {num} times ")
    result = 0
    for _ in range(num):
        num_1 = randint(1, 9)
        print(f"Iteration: {_ + 1}")
        result = (result * 10) + num_1
        print(f"Result: {result}")
    return result

print(f"Final Result: {generateRandomNumber()}")

#float
num_1 = 5
num_2 = 2.5
addNum = num_1 + num_2
print(type(addNum))

#int
num_3 = 5
num_4 = 2.5
addNum = num_3 + int(num_4)
print(type(addNum))

#BOOLEAN

num_1 = 5
num_2 = 5.0

print(num_1 == num_2)

print('a' == 'A')

print('a' == 'A'.lower())



#TUPLES
t_1 = ('James', 37, 'Married', 1, 1, 1)
t_2 = ('Jane', 27, 'Single')

print(t_1.count(1), t_2.index('Jane'))

#DICTIONARIES
dictionaries = {"name": "James",
                "age": 37,
                "status": "married",
                "income": None}
print(dictionaries.keys())
print(dictionaries.values())
print(dictionaries.items())
for value in dictionaries.values():
    print(value)
#print(dictionaries.pop("income"))
dictionaries.setdefault('hair_color', "brown")
dictionaries.popitem()
dictionaries.clear()
print(dictionaries)


dictionarie_1 = {"name": "Rose",
                "age": 7,
                "status": "single",
                "income": None}
dictionarie_2 = {"name": "Rose",
                "age": 77,
                "status": "widow",
                "income": 10000}

dictionary_3 = {**dictionarie_1, **dictionarie_2}

print(dictionary_3)
#HOMEWORK
#  1. Cтворити змінну num_str = 125, перевести її в тип string за допогою функції str()
num_str = 125
print(type(str(num_str)))
print(str(num_str))

#  2. Cтворити зміну message = 'Hi, my name is Python!' За допомогою функції replace() замінити   усі букви 'y' на '0' та 'i' на '1'.
message = 'Hi, my name is Python!'
new_message = message.replace('y', '0').replace('i', '1')
print(new_message)

#  3. Cтворити зміну split_test = 'This is a split test' і розділити її по пробілах за допомогою функції split(), а потім знову обʼєднати у строку за допомогою функції join() у змінну string_join
split_test = 'This is a split test'
print(split_test.split(" "))
#  4. Визначити довжину рядку string_join за допомогою функції len()

print(len("string_join"))

# Робота зі списками:
#  1. Cтворити змінну list_append = [1, 2, 3] і за допомогою функції append() додати туди спочатку 4, а потім 5
list_append = [1, 2, 3]
list_append.append(4)
print(list_append)
list_append.append(5)
print(list_append)

#  2. Cтворити змінну list_extend = [4, 5, 6] і розширити цей список іншим списком [7, 8, 9] за допомогою функції extend()
list_extend = [4, 5, 6]
extention=[7,8,9]
list_extend.extend(extention)
print(list_extend)

#  3. Визначити індекс елемента 6 у списку list_extend за допомогою функції index()
print(list_extend.index(6))
#  4. Визначити довжину списку list_append за допомогою функції len()
print(len(list_append))
# Робота зі словниками:
#  1. Cтворити змінну dict_test = {'car': 'Toyota', 'price': 4900, 'where': 'EU'} та вивести на екран дані, які знаходяться в ключах car та where
dict_test = {'car': 'Toyota', 'price': 4900, 'where': 'EU'}
x = (dict_test.get('car'))
y = (dict_test.get('where'))
print(x, y)

print(dict_test['car'], dict_test['where'])

#  2. За допомогою функцій keys() і values() вивести на екран ключі та їх значення
print(dict_test.keys())
print(dict_test.values())

#  3. За допомогою функції items() вивести на екран пари ключ - значення
print(dict_test.items())


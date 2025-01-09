#LISTS

list1 = [1, 2, 3, 4, 5]
list2 = [1, 3, 5, 7]
list3= []
for i in list1:
    for x in list2:
        if i == x:
            list3.append(i)
print(f"Final list {list3}")

x = 'paralelepiped'
y = 'lepid'
list_x = list(x)
list_y = list(y)
a_list = []
for i in list_y:
    for e in list_x:
        if e == i and e not in a_list:
            a_list.append(e)
            list_x.remove(e)
            print(f"DONE {a_list}")
    # print(list_x)


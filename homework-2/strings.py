
greeting = "hello "
first_name = "John"
last_name = "Doe"
age = 30
message = " Today you turned {0}!".format(age)

print(greeting, first_name, " ", last_name, message, " Congrats!")


print(greeting.capitalize())
greeting_upper= greeting.upper()
print(greeting_upper)
print(greeting_upper.casefold())
print(greeting_upper.center(30, '_'))
print(message.count('u'))

txt = "Welcome to my world"
x = txt.title()
print(x)

txt = "My name is Ståle"
print(txt.encode())
print(txt.encode(encoding="ascii",errors="backslashreplace"))
print(txt.encode(encoding="ascii",errors="ignore"))
print(txt.encode(encoding="ascii",errors="namereplace"))
print(txt.encode(encoding="ascii",errors="replace"))
print(txt.encode(encoding="ascii",errors="xmlcharrefreplace"))

txt = "Today is a beautiful weather !!!"
print(txt.endswith("!!!"))
print(txt.endswith(("?", "!!")))

txt = "Hello, welcome to my world."
#If the value is not found, the find() method returns -1, but the index() method will raise an exception:
x = txt.find("?", 5, 10)
y = txt.index("e", 5, 10)
print(x)
print(y)

ltxt=txt.split()
print(ltxt)

jtxt= " ".join(ltxt)
print(jtxt)

txt = "Hi Liz!"
x = "zLi"
y = "eJo"
mytable = str.maketrans(x, y)
print(txt.translate(mytable))

txt = "I like bananas"
x = txt.replace("bananas", "apples")
print(x)


txt = "one one was a race horse, two two was one too."
x = txt.replace("one", "three", 2)
print(x)

txt = "banana"
print(txt.rjust(20, '_'))

txt = "apple, banana, cherry, orange"
x = txt.rsplit(", ", 1)
print(x)
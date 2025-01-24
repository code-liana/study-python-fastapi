class One:
    def __init__(self, a):
        self.a = a
    def __add__(self, object1):
        print(self.a)
        print(object1.a)
        return self.a + object1.a
class Two:
    def __init__(self, a):
        self.a = a
    def __add__(self, object2):
        return self.a + object2.a
a_instance = One(10)
b_instance = Two(20)
print(a_instance + b_instance)
print(a_instance.__dict__, ", ",b_instance.__dict__)


class Str:
    def __init__(self, string_):
        self.string_ = string_
    def __add__(self, string2):
        return self.string_ + string2
instance1 = Str("Hello")
print(instance1 + " Folks")
# Output: Hello Folks

class A:
    def __init__(self, item):
        self.item = item
    def __getitem__(self, index):
        return self.item[index]
a = A([1, 2, 3])
print(f"First item: {a[0]}")
print(f"Second item: {a[1]}")
print(f"Third item: {a[2]}")

class SetItemExample:
    def __init__(self, item):
        self.item = item
    def __setitem__(self, index, item1):
        self.item[index] = item1
setitem_instance = SetItemExample([1, 2, 3])
print(f"Items before setting: {setitem_instance.item}")
setitem_instance[1] = 5
print(f"Items after setting: {setitem_instance.item}")


class ReprExample:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c
    def __repr__(self):
        return f"ReprExample(a={self.a}, b={self.b}, c={self.c})"
repr_instance = ReprExample(1, 2, 3)
print(repr_instance)

class LenExample:
    def __init__(self, item):
        self.item = item
    def __len__(self):
        return len(self.item)
len_instance = LenExample([1, 2, 3])
print(len(len_instance))
# Output: 3

class Comparison:
    def __init__(self, a):
        self.a = a
    def __lt__(self, object2):
        return self.a < object2.a
    def __gt__(self, object2):
        return self.a > object2.a
    def __le__(self, object2):
        return self.a <= object2.a
    def __ge__(self, object2):
        return self.a >= object2.a
    def __eq__(self, object2):
        return self.a == object2.a
    def __ne__(self, object2):
        return self.a != object2.a
a = Comparison(1)
b = Comparison(2)
print(
    a < b,
    a > b,
    a <= b,
    a >= b,
    a == b,
    a != b
)
# Output
# True False True False False True

class ContainsExample:
    def __init__(self, items):
        self.items = items
    def __contains__(self, item):
        return item in self.items
contains_instance = ContainsExample([1, 2, 3, 4, 5])
print(4 in contains_instance)


class WriteFile:
    def __init__(self, file_name):
        self.file_name = file_name
        self.file = None
    def log(self, text):
        self.file.write(text+'\n')
    def __enter__(self):
        self.file = open(self.file_name, "a+")
        return self
    def __exit__(self, exc_type, exc_val, exc_tb):
        self.file.close()
with WriteFile(r"filename.txt") as log_file:
    log_file.log("Log Test 1")
    log_file.log("Log Test 2")
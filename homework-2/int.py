from random import randint

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


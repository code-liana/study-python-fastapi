def calculate_average(numbers):
    summary = 0
    for i in numbers:
        summary += i
    return summary / len(numbers)

def find_max(numbers):
    result = 0
    for i in numbers:
        if i > result:
            result = i
    return result
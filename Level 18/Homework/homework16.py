def calculate_average(numbers):
    total = sum(numbers)
    count = len(numbers)
    average = total / count
    return average

# Test case
numbers = [1, 3, 4, 5, 2]
result = calculate_average(numbers)
print(result)
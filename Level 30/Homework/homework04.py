def sum_numbers(numbers):
    total = sum([int(num) if isinstance(num, str) else num for num in numbers])
    return total

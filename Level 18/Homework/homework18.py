def square_list(numbers):


  squared_list = []
  for num in numbers:
    squared_list.append(num**2)
  return squared_list

numbers = [3, 12, 5, 2, 6]
result = square_list(numbers)
print(result) 
def check_divisibility(number):
  if number % 3 == 0 and number % 5 == 0:
    print(f"{number} იყოფა 3-ზე და 5-ზე.")
  elif number % 3 == 0:
     print(f"{number} იყოფა 3-ზე.")
  elif number % 5 == 0:
    print(f"{number} იყოფა 5-ზე.")
  else:
    print(f"{number}არ იყოფა 3ზე ან ხუთზე")

user_number = int(input("შეიყვანე რიცხვი: "))


check_divisibility(user_number)
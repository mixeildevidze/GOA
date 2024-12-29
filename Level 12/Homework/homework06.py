user_age = int(input("Enter your age: "))

if user_age <= 13:
    print("You are kid")
elif user_age > 13 and user_age < 20:
    print("You are teenager")
elif user_age >= 20:
    print("You are grown up")
else:
    print("Enter right age!")
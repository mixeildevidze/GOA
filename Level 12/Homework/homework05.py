user_input = int(input("Enter your grade: "))

if user_input >= 90:
    print("Grade A")
elif user_input >= 80 and user_input <= 89:
    print("Grade B")
elif user_input >= 50 and user_input <= 79:
    print("Grade C")
elif user_input >= 30 and user_input <= 49:
    print("Grade D")
elif user_input >= 0 and user_input <= 29:
    print("Grade F")
else:
    print("Enter a right number.")
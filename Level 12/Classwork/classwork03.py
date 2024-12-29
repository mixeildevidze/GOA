user_age = int(input("Enter Your Age: "))
user_student = input("Are you a student: ")
if user_age < 18 and user_student == "yes":
    print("discount")
else:
    print("no discount")
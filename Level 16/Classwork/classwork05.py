def check_adulthodd(age):

    if age >= 18:

    
        return "სრულწლოვანი ხარ"
    else:

        return("არ ხარ სრულწლოვანი")

user_age = int(input("Enter Your Age: "))

print(check_adulthodd(user_age))


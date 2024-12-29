def check_pass(points):
    if points >= 80:
        return "ჩააბარე"
    else:
        return "ვერ ჩააბარე"

user_point = int(input("შეიყვანე ქულა: "))
print(check_pass(user_point))

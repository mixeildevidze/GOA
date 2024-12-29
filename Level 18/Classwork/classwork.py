# upper ფუნქცია წერს სტრინგში მოცემულ სიმბოლოებს დიდი ასოებით

str1 = "ragaca"
print(str1.upper())

# lower ფუნქცია წერს სტრინგში მოცემულ სიმბოლოებს პატარა ასოებით
str2 = "RAGACA"
print(str2.lower())

# capitalize ფუნქცია იწყებს წინადადებას დიდი ასოთი



str3 = "hello world"
x = str3.capitalize()
print(x)


# swapcase ფუნქცია უცვლის დიდ და პატარა ასოებს ანუ ამ შემთხვევაში str4 = "RaGaca" output იქნება rAgACA
str4 = "RaGaca"
y = str4.swapcase()
print(y)


# find ფუნქცია საშვალებას გვაძლებს სტრინგში მოვძებნოთ რომელიმე სიმბოლო ან თუნდაც სიტყვა

str5 = "ragaca"
z = str5.find("r")
print(z)

# len ფუნქცია ითვლის სიმბოლოებს



str6 = "ragaca"
print(len(str6))


# index ფუნქცია საშუალებას გვაძლევს ვიპოვოთ ელემეტის ინდექსი ლისტში

fruits = ["apple","banana","orange"]
x = fruits.index("orange")
print(x)

listn = [1,2,3,4,5]
listn.append()
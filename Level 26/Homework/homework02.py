computer = {
    "brand": "Lenovo",
    "processor": "Ryzen 5 5500",
    "ram": "8GB",
    "storage": "256 SSD",
    "os": "Windows 11"
}

#1
for value in computer.values():
    print(value)
#2

for key, value in computer.items():
    print(value)
#3

for key in computer:
    print(computer[key])

from number_task import ism

name = str(input("Ismingizni kiriting : "))
surname = str(input("Familyangizni kiriting : "))
age = str(input("Foydalanuvchi yoshini kiriting :"))

def year(age):
    return age


a = ism(name, surname)
b = year(age)
print(f"{a}\nYoshi:{b}")
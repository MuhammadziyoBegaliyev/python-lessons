

namber = int(input("Enter namber one: "))
namber_2 = int(input("enter namber two:"))

def raqamlar(namber,namber_1):
    if type(namber) != int or type(namber_2) != int:
        print("berilgan son int emas")

    else :

        c = namber * namber_2 
        print(c)
  
        return c

raqamlar(namber,namber_2)

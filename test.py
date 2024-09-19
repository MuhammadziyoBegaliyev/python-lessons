def matinlar(matn_lar):
    mancha = {}
    while matn_lar:
        man = matn_lar.title()
        ism = input(f"Ismingizni kiriting")
        mancha[man] = ism 
    return mancha


# son = int(input("Enter namber one: "))
# son_1 = int(input("enter namber two:"))

# def raqamlar(son,son_1):
#     if type(son) != int or type(son_1) != int:
#         print("berilgan son int emas")

#     else :

#         c = son * son_1 
#         print(c)
  
#         return c

# raqamlar(son, son_1)

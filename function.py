# 1-task
# def ism_tugulgan_yil(ism,tugulgan_yil):
#     """ foydalanuvchining ismi va tugulgan yilini sorab necha yoshdaligini biluvchi funksiya"""
#     print(f"Foydalanuvchining ismi:{ism.title()}\n "
#           f"Foydalanuvchining yoshi :{2024-tugulgan_yil}")
# ism_tugulgan_yil('olim',1978)




# 2-task

# def son(son):
#     """Foydalanuvchidan son olib uning kvadrati va kubini aniqlovchi funksiya"""
#     print(f"kiritilgan sonning kvadrati:{son**2}\n"
#           f"kiritilgan sonning kubi :{son**3}")
# son(2)



# 3-task
# def son(son):
#     """Foydalanuvchi kiritgan sonni juft yoki toq ekanligini takshiruvchi funksiya"""
#     if son%2 == 0:
#         print(f"Foydalanuvchi kiritgan son :{son}-bu son juft son") 
#     else :
#         print(f"Foydalanuvchi kiritgan son:{son}-bu son toq son")
# son(5)


# 4-task
# def son(son_1,son_2):
#     """Foydalanuvchi kiritgan sonlarni katta yoke kichikligini aniqlovchi dastur"""
#     if son_1>son_2:
#         print(f"birinchi son katta {son_1}>{son_2}")
#     elif son_1<son_2:
#         print(f"Ikkinchi son birinchi sondan katta {son_1}<{son_2}")
#     else:
#         print(f"Bu ikkala son o`zaro teng{son_1}={son_2}")
# son(son_1=15,son_2=20)



# 5-task
# def sonlar(son_1,son_2):
#     """Foydalanuvchi kiritgan sonni 'n'chi darajasini hisoblovchi funksiya"""
#     print(son_1**son_2)
#     print(f"Foydalanuvchi kiritgan sonning n-darajasi :{son_1**son_2}")

# sonlar(4,3)

#  6-task
# def sonlar(son_1,son_2=2):
#     """Foydalanuvchi kiritgan sonni 'n'chi darajasini hisoblovchi funksiya"""
#     print(son_1**son_2)
#     print(f"Foydalanuvchi kiritgan sonning n-darajasi :{son_1**son_2}")

# sonlar(4)


# 7- task
def son(son_1):
    son_1=int(input("istalgan sonni kiriting"))
    a = 1
    while a <= 10:
        a += 1
        result = son_1 / a
        print(result)

son(18)
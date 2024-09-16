
#  1-task

# print("Kitoblar Jamgarmasi !")
# book = "Enter favorite book ="
# book_all = ''
# while book_all != 'exit':
#     book_all = input(book)
#     if book_all != 'exit':
#         print(book_all)







#  2-task



# park = "please enter your age "
# park_0 = ''
# while park_0 != 'exit' or  'quit' :
#     park_0 = input(park)
#     if park_0 != 'exit' or 'quit':
#         if park <= 7 :
#             print("Siz uchun chipta narxi 2000")
#         if park <= 18 :
#             print("Siz uchun chipta narxi 3000")
#         if park <=  65 :
#             print("Siz uchun chipta narxi 10000")
#         if park>'65':
#             print("siz uchun tekin !!!")


# age = 'Enter your age  :'

# while True :
#     park = input(age)
#     if park == 'exit ' or park=='quit':
#         break
#     age_0 = int(park)

#     if age_0<7 :
#         sum = 2000
#     elif age_0 <18 :
#         sum =3000
#     elif age_0 <65 :
#         sum = 10000
#     else : sum =0
#     if sum ==0:
#         print('Sizga chipta narxi tekin!')
#     else :
#         print(f'siz uchun chipta narxi {sum}')

# 3-task 
savol ='Kiritilgan sonning ildizini qaytaruvchi dastur .\n'
savol += "Musbat son kiriting"
savol += "(Dasturni to`xtatish uchun 'exit deb yozing ):"
while True :
    qiymat = input(savol)
    
    if qiymat>0:
        continue 
    elif qiymat == 'exit':
        break
    else :
        ildiz = float(qiymat)*(0.5)
        print(f"{qiymat}ning ildizi {ildiz}ga teng")
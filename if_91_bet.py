# 1chi vazifa 

# son = int(input("Juft son kirirting ="))
# if son%2 == 0 :
#     print(f"Raxmat siz juft son kiritingiz !   {son}")
# else :
#     print("iltimos boshqatdan son kiriting ")

# 2 - vazifa 

# yosh = int(input("yoshingizni kiriting ="))
# if yosh <=4 or yosh >=60  :
#     print("Siz uchun tekin !")
# elif yosh <=18 :
#     print(f"siz uchun 10 000 som sabibi sizning yoshingiz {yosh}")
# else :
#     print(" siz uchun 20 000")

# 3 - vazifa

# son = int(input("1- sonni kiriting :"))
# son1 = int(input("2- sonni kiriting :"))
# if son == son1 :
#     print(f"bu sonlar ozaro teng {son}={son1}")
# elif son > son1 :
#     print(f"bu {son}>{son1}")
# elif son <son1 :
#     print(f" bu holtta {son}<{son1}")

# 4- vazifa 
# mahsulotlar = ['karam', ' kartoshka', ' olma ', 'nok ','banan', ' pamildori','somsa ','shashlik','osh','piyoz','tuqum']
# print(mahsulotlar)
# savat =[]
# savat = mahsulotlar[:5]
# savat = str(input("maxshulot tallang  "))
# savat = str(input("maxshulot tallang   "))
# savat = str(input("maxshulot tallang   "))
# savat = str(input("maxshulot tallang   "))
# savat = str(input("maxshulot tallang    "))


# if savat in mahsulotlar:
#     print(f"Bu mahsulotlar bizda bor }")
# else :
#     print(f"bu mahsulot bizda yoq{mahsulotlar} ") 


# # 5-vazifa
# mahsulotlar = ['osh','manti','somsa','hotdog','shashlik','salat', 'choy ','lagmon ']
# savat = []
# print("Taom tanlang 5ta ")
# for n in range(5):
#     savat.append(input(f"{n+1}--taom kiriting "))

# for mahsulot in savat:
#     if mahsulot in mahsulotlar:
#         print("bu mahsulotlar bizda bor")
#     else :
#         print("bu mahsulot bizda yoq  ")

# 6- vazifa 
# login = ['muhammadziyo','doston','humoyun','shahriyor','ozodbek' ]
# login1 = []
# for n in range(1):
#     login1.append(input(f"{n+1}---Loginingizni kiriting >>>"))
# for log in login1 :
#     if log in login:
#         print("bu login bizda mavjud")
#     else :
#         print(f"Xush kelibsiz {log}")




# 7- vazifa o`zim `

# son = int(input("Biron son kiriting ="))
# sonlar = list(range(2,10))
# if son % 2  == 0 :
#     print(f"{son}  bu son qoldiqsiz bolinadi{2}")
# if son % 3  == 0 :
#     print(f"{son}  bu son qoldiqsiz bolinadi{3}")
# if son % 4  == 0 :
#     print(f"{son}  bu son qoldiqsiz bolinadi{4}")
# if son % 5  == 0 :
#     print(f"{son}  bu son qoldiqsiz bolinadi{5}") 
# if son % 6  == 0 :
#     print(f"{son}  bu son qoldiqsiz bolinadi{6}")
# if son % 7  == 0 :
#     print(f"{son}  bu son qoldiqsiz bolinadi{7}")
# if son % 8  == 0 :
#     print(f"{son}  bu son qoldiqsiz bolinadi{8}")
# if son % 9  == 0 :
#     print(f"{son}  bu son qoldiqsiz bolinadi{9}")    
# else :
#     print(f"bu {son}bu ayrim songa qoldiqsiz bolinmidi")



# 7- vazifa abrazes



son = int(input("Istalgan son kirirting  ="))
for n in range(2,10):
    if not (son%n):
        print(f"{son}bu songa qoldiqsiz bolinadi = {n} ")


   
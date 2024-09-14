# 1-error
# son = float(input("Juft son kiriting: "))
# if son%2 == 0: 
#     print("Bu son juft emas.")
# else:
#     print("Rahmat!")

# 2-error
# yosh = int(input("Yoshingiz nechida?"))

# if yosh<=4 or yosh>=60:
#     narh = 0
# elif yosh < 18:
#     narh = 10000
# else:
#     narh = 20000
#     print(f"Chipta {narh} so'm")

# 3-error


# x = float(input("Birinchi sonni kiriting: "))
# y = float(input("Ikkinchi sonni kiriting: "))
# if x==y:
#     print(f"{x}={y}")
# elif x<y:
#     print(f"{x}<{y}")
# else:
#     print(f"{x}>{y}")

# 4- error

# mahsulotlar = ['un', "yog'", "sovun", 'tuxum', 'piyoz',
#                'kartoshka', 'olma', 'banan', 'uzum', 'qovun']


# for n in range(5):
#     mahsulotlar.append(input(f"Savatga {n+1}-mahsulotni qo'shing: "))

# if mahsulotlar :
#     for mahsulot in mahsulotlar:
#         if mahsulot in mahsulotlar:
#             print(f"Do'konimizda {mahsulot} bor")
#         else:
#             print(f"Do'konimizda {mahsulot} yo'q")
# else: 
#     print("Savatingiz bo'sh")            

# 5- error
# mahsulotlar = ['un', "yog'", "sovun", 'tuxum', 'piyoz',
#                'kartoshka', 'olma', 'banan', 'uzum', 'qovun']


# savat = []
# for n in range(5):
#     savat.append(input(f"Savatga {n+1}-mahsulotni qo'shing: "))

# bor_mahsulotlar = []
# mavjud_emas = []
# for mahsulot in savat:
#     if mahsulot in mahsulotlar:
#         bor_mahsulotlar.append(mahsulotlar)
#     else:
#         mavjud_emas.append(mahsulotlar)

# if mavjud_emas:
#   print("Do'konimizda quyidagi mahsulotlar yo'q:")
# for mahsulot in mavjud_emas:
#   print(mahsulot)
# else:
#   print("Siz so'ragan barcha mahsulotlar do'konimizda bor")
#  6-error
users = ['alisher1983','aziza','yasina' 'umar']

login = input("Yangi login tanlang:")

if login in users:
    print('Login band, yangi login tanalng!')
else:
    print("Xush kelibsiz!")

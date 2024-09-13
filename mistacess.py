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

mahsulotlar = ['un', "yog'", "sovun", 'tuxum', 'piyoz',
               'kartoshka', 'olma', 'banan', 'uzum', 'qovun']


for n in range(5):
    mahsulotlar.append(input(f"Savatga {n+1}-mahsulotni qo'shing: "))

if mahsulotlar :
    for mahsulot in mahsulotlar:
        if mahsulot in mahsulotlar:
            print(f"Do'konimizda {mahsulot} bor")
        else:
            print(f"Do'konimizda {mahsulot} yo'q")
else: 
    print("Savatingiz bo'sh")            
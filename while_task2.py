




#  1- task 
# print("Hush kelibsiz hurmatli mijoz !!!")
# buyurtmalar=[]
# n =1 
# while True :
#     savol=f"{n}--- buyurtmangiz hurmatli mijoz!"
#     buyurtma = input(savol)
#     buyurtmalar.append(buyurtma)
#     javob = input("Yana buyurtma qoshasizmi ? ha/ yoq")
#     if javob == 'ha':
#         n+=1
#         continue
#     else:
#         break
# print("royhat tuzuldi")
# print("Buyurtmalar royhati :")
# for buyurtma in buyurtmalar:
#     print(buyurtma.title())



#  2- task


# print("Ma`lumotlar kiriting !")
# mahsulotlar ={}
# ishora = True 
# while ishora :
#     buyurtma = input("Buyurtmangiz ni kirting :")
#     narxlari = input(f"{buyurtma}-ning  Narxlarini kiriting :")
#     mahsulotlar[buyurtma]=int(narxlari)
#     javob =input("Yana buyurtma qoshishni istaysizmi ? ha/yoq")
#     if javob == 'yoq':
#         ishora = False
# for buyurtma , narxlari in mahsulotlar.items():
#     print(f"{buyurtma.title()} bu buyurtma {narxlari} shu narxda ")


    # 3-task

print("Hush kelibsiz hurmatli mijoz !!!")
buyurtmalar=[]
n =1 
while True :
    savol=f"{n}--- buyurtmangiz hurmatli mijoz!"
    buyurtma = input(savol)
    buyurtmalar.append(buyurtma)
    javob = input("Yana buyurtma qoshasizmi ? ha/ yoq")
    if javob == 'ha':
        n+=1
        continue
    else:
        break
print("royhat tuzuldi")
print("Buyurtmalar royhati :")
for buyurtma in buyurtmalar:
    print(buyurtma.title())
e_bozor={
    'osh':20000,
    'somsa':16000,
    'manti':5000,
    'kabob':18000

}
# for buyum in buyurtma:
#     if buyum in e_bozor  :
#         print(e_bozor.values(), end='')
#     else    :
#         print("bizada bundey mahsulot yoq")
if buyurtma in e_bozor :
    for k , v in e_bozor.values():
        print(v)
else:
    print("bizda bundey mahsulot yoq")
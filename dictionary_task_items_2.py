#  1-task 


# python = {
#     'for':'uchun',
#     'every one':'har doim',
#     'allweys':'doimo',
#     'if':'agar',
#     'constante':'o`zgarmas',
#     }
# for kalit , qiymat in sorted(python.items()):
#     print(f"key words >>>{kalit}")
#     print(f"values words >>>{qiymat}")




# 2 -task
# info = {
#     'o`zbekiston':'toshkent',
#     'qozogiston' :'duyshanbe',
#     'AQSH':"new york",
#     'rassiya':'moscow'
#      }
# for key , values in sorted(info.items()):
#     print(f" key words >>>{key.title()}")
#     print(f" values words >>>{values.title()}")      

#  3- task
 

# contry = input("Enter country  desired    ")
# capital ={
#     'o`zbekiston':'toshkent',
#     'qozogiston' :'duyshanbe',
#     'AQSH':"new york",
#     'rassiya':'moscow'
#     }
# print(f"Foydalanuvchi kiritgan country  {contry}")
# print("davlatlar poytaxti ")
# for contry in sorted(capital.values()):
#     print(contry.title())   
# poytaxt = capital.get(contry)
# if poytaxt == None :
#     print("bundey davlat kiritilmagan")
# else:
#     print(f"{contry.upper()} ning poytaxti{poytaxt.title()} shahri")


# restaran ={
#     'osh':20_000,
#     "manti":8_000,
#     'somsa':16_000,
#     'shorva':25_000,
#     'lagmon':27_000,
#     'dolma':30_000,
#     'shashlik':11_000,
#     'tabaka':35_000,
#     'chuchvara':22_000,
#     }
# for n in range(3):
#     taom = input("Qandey taom tallaysiz ?").lower()
# zakaz = restaran.get(taom)
# if zakaz == None :
#     print(f"kechirasiz vizda bundey taom yoq")
# else:
#     zakaz = sum(restaran.values())
#     print(f"Total Price: {zakaz}")

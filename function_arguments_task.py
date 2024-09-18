# def foydalanuvchi_malumotlar(foydalanuvchiniig_ismi,familyasi,tugulgan_yili,tugulgan_joyi,tel_raqami=None,el_manzili=None):
#     """ Foydalanuvchining ma`lumotlar"""
#     malumot ={'ismi':foydalanuvchiniig_ismi,
#               'familyasi':familyasi,
#               'tugulgan_yili':tugulgan_yili,
#               'tugulgan_joyi':tugulgan_joyi,
#               'tel_raqami':tel_raqami,
#               'el_manzili':el_manzili

#     }
#     return malumot
# foydalanuvchi_1 = foydalanuvchi_malumotlar('Muhammadziyo','Begaliyev',2006,'Olimbek qishloq','901431051')
# foydalanuvchi_2 = foydalanuvchi_malumotlar('Husan','Olimov',2006,'toshkent viloyat','None','@Husan_1234')
# foydalanuvchilar = [foydalanuvchi_1,foydalanuvchi_2]
# # print(f"Foydalanuvchilar haqida malumot {foydalanuvchi_1}\n {foydalanuvchi_2}")


# task 2
# def foydalanuvchi_malumotlar(foydalanuvchiniig_ismi,familyasi,tugulgan_yili,tugulgan_joyi,tel_raqami=None,el_manzili=None):
#   malumot ={'ismi':foydalanuvchiniig_ismi,
#               'familyasi':familyasi,
#               'tugulgan_yili':tugulgan_yili,
#               'tugulgan_joyi':tugulgan_joyi,
#               'tel_raqami':tel_raqami,
#               'el_manzili':el_manzili

#     }
#   return malumot
# mijozlar = []
# while True:
#     ismingiz = input("Foydalanuvchi ismingizni kiriting: ")
#     familya = input("Foydalanuvchi familyangizni kiriting :")
#     tugulgan_yil = input("Tugulgan yilingizni kiriting :")
#     tugulgan_joy = input("tugulgan joingizni kiriting :")
#     tel_raqam = input("telefon raqamingizni  kiriting ")
#     mijozlar.append(foydalanuvchi_malumotlar(ismingiz,familya,tugulgan_yil,tugulgan_joy,tel_raqam,))
#     javob = input("YAna ma`lumot kiritasizmi? ha/yoq:")
#     if javob== 'yoq':
#        break
# # print(mijozlar)

# print(f"Kiritilgan malumotlar {foydalanuvchi_malumotlar}")






#  task 3
# def sonlar(son_1,son_2,son_3):
#    if son_1>son_2 and son_1>son_3:
#       print(son_1)
#    elif son_1<son_2 and son_2 > son_3:
#       print(son_2)
#    else :
#       print(son_3)
#    return sonlar
# sonlar(10,15,3)
# print(sonlar)


#  task 4
# royhat = []
# PI=3.14
# def aylana(PI,radius):
#     """Aylanani uzunligi"""
#     radius = int(input("Radiusni kiriting"))
  
    
    
#     aylana_uzunligi= 2*PI*radius ,
#     diametri= 2*radius,
#     yuzi=PI*(radius**2),
#     royhat.append(aylana_uzunligi),
#     royhat.append(diametri),
#     royhat.append(yuzi)
# print(royhat)



# # task 5
# def tub_sonlar_top(min, max):
#     tub_sonlar = []
#     for n in range(min, max + 1):
#         tub = True
#         if n == 1:
#             tub = False
#         elif n == 2:
#             tub = True
#         else:
#             for x in range(2, n):
#                 if n % x == 0:
#                     tub = False
#         if tub:
#             tub_sonlar.append(n)
    #   tub_sonlar_toplami(1,100)
#     return tub_sonlar
#     print(tub_sonlar)


# task 6 

def son(son_0):
    sonlar = []
    son_0 = int(input("Biron son kiriting = "))
    while son_0 == son_0 :
        
        sonlar.append(son_0)
        son_0 +=1
    return sonlar 
son(1)
        

   
 
        

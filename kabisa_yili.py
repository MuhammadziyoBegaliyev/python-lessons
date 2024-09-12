yil = int(input("Istalgan yilingizni kiriting >>>"))
if yil % 4 == 0 or yil % 100 == 0 :
    print(f"bu yil kabisa yilidir {yil}")
else :
    print("bu yil kabisa yili emas! ")
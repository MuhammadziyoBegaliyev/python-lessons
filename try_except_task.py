


# 1- task

# x = input("Son kiriting =")
# y = input("yana bir son kiriting:")
# try :
#     x=int(x)
#     y=int(y)
#     print(f"x / y ning qiymati {(x/y)}")
# except:
#     print("Afsuski siz butun son kiritmadingiz !")

# 2-task


while True:
    x = input("Son kiriting =")
    y = input("yana bir son kiriting:")
    if x.isdigit() and y.isdigit():
        x=int(x)
        y=int(y)
        break
print(f"x/y ning qiymat {x/y} ga teng")

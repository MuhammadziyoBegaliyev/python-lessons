sonlar = []
kublar = []
def get_kvadrat(num):
    c = num * num
    sonlar.append(c)
    return sonlar


def get_kub(num):
    cube = num * num * num
    kublar.append(cube)
    return kublar


numbers = range(1, 11)

for i in numbers:
    kvadrat = get_kvadrat(i)
    cube = get_kub(i)
   


print("kvadrat : ", kvadrat)  
print("cube:", cube)

def nambres(namber_1,namber_2):
    """Sonlar ro'yxatidagi eng katta sonni topuvchi funksiya"""
    namber_1 = int(input("Enter namber one ="))
    namber_2 =int(input("enter namber two ="))
    if namber_1>namber_2 :
        print(namber_1)
    else :
        print(namber_2)
        return namber_2
nambres(5,10)
print(nambres)
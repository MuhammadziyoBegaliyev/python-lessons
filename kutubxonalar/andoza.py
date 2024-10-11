import re
nomer = input("Enter you tel nomer :")
nomer += ("9xonali son , +998dan boshlanishi shart emas ")
andoza = "^N.......s$" 

try:
    print(re.match(andoza.nomer))
except AttributeError:
    print("Xato kiritilmoqda !")
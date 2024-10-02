with open('/home/muhammadziyo/Downloads/pi_million_digits.txt') as fayl:
    pi = fayl.read()
pi = pi.rstrip()
pi = pi.replace('\n','')
pi = pi.replace(" ", "")
  

tkun = '5048767469' 
print(tkun in pi)

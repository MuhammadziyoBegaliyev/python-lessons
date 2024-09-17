print("Istalgan son kirirting !")
sonlar = []
sonlar_1 ={}

n=1
while True :
    savol = f"{n}- Sonni kiriting :"
    son_1 = input(savol)
    son =  sonlar.append(son)
    javob = input('Yana son qoshasizmi? ha/ yoq')
    
    sonlar_1[son]=son_1
    if javob == 'ha':
        n+=1
        
        continue
    else :
        print(sum(sonlar(son)))
        break
      
# print(sonlar)

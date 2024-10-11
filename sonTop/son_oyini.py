import random
def sontop(x=10):
    tasodifiy_son = random.randint(1,x)
    print(f"Men 1 dan {x}gacha son o`ylayman. Topa olasizmi?",end="")

    while True:
        taxmin = int(input(">>>"))
        if taxmin < tasodifiy_son:
            print("Kattaroq son ayting :",end="")
        elif taxmin > tasodifiy_son:
            print("Kichiroq son ayting :", end="")
        else :
            print("Yutdingiz!")
            break


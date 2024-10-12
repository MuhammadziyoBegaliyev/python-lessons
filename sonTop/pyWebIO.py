from pywebio.input import input 
from pywebio.output import put_text , popup
import random 
def sontop(x=10):
    tasodifiy_son = random.randint(1,x)
    while True:
        taxmin = int(input(f"Men 1dan {x}gacha son o`yladim . Topa olasizmi?"))

        if taxmin < tasodifiy_son:
            put_text("Kattaroq son ayting!")
        elif taxmin > tasodifiy_son:
            put_text("Kichikroq son ayting!")
        else :
            popup("Yutdingiz!")
            break
                
sontop()
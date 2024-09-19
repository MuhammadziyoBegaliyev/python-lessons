def summa(*nambers):
    """kiritilgan sonlarni kopaytmasini hisoblovchi dastur"""
    sum = 1
    for namber in  nambers :
        sum *= namber 
    return sum 
print(summa(12,4))
print(summa(12,4,5,4,8,9,74,52,15))
print(summa(12,4.12,45,65,25,56))
students = {
    'Ali': [78, 85, 90],
    'Vali': [88, 76, 92],
    'Olim': [95, 91, 89],
    'Salim': [72, 68, 80],
    'Anvar': [85, 87, 90]
}
bal = students.values()
for ball in bal :
    print(float(sum(ball))//3)
# ball = students['Ali']
# print(sum(ball)//3)
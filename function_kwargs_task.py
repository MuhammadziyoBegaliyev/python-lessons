def students(name,femael,**data):
    """Talabalar haqida malumotlar """
    data['name']=name
    data['femael']=femael
    return data
data1 = students("Alijonov",'shoxrux',bilimi ="Alochi ",turar_joyi="Toshkentdan")
data2 = students('holdorov',"doston",bilimi="Qoniqarli",turar_joy='Chilonzor')
data3 =[data1,data2]
print(data3)
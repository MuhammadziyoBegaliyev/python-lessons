class Avto:
    """Avto -- avtamabil haqida klass"""
    def __init__(self,model,color,karobka,price,km):
        """mOshinaning hususiyatlari :"""
        self.model = model
        self.color = color
        self.karobka = karobka 
        self.price = price
        self.km = km 

    def update_km(self):
        """Avtomobil km ni yangilovchi metod """
        self.km  += 1000 



    def get_info(self):
        """Avtomobil haqida toliq malumot :"""
        return f"Madeli :{self.model},\n , rangi :{self.color},\n, Karobkasi :{self.karobka},\n,Narxi : {self.price},\nKilometri :{self.km}"
    



car_1 = Avto("Cobalt","blue","avtomat","9_000$",km=13_000)
car_2 = Avto("Jentra","white","mehanika","8_000$",km=18_000)
# car_1.update_km()
print(car_1.get_info())
print(car_2.get_info())


class Avto_salon :
    """Avtosalon haqida ma`lumotlar :"""
    def __init__(self,name,address,cars):
        """Avtasol hususiyatlar """
        self.name = name
        self.address =address
        self.cars = cars
        self.cars_soni = 0
        self.cars = []

    
    # def add_cars(self,car):
    #     """Avto salonga talaba qoshish :"""
    #     self.cars_1.append(car)
    #     self.cars_soni += 1


    def get__info__(self):
        """Avto salon haqida malumotlar :"""
        return f"avto salon nomi : {self.name}\n Avtosalon manzili :{self.address}\n"
    

cars_1 =Avto("nexia3","blue","avtomat","9_000$",km=13_000)
cars_2 = Avto("Taxoe","black","avtomat","3_000$",km=14_000)
# Avto_salon.add_cars(cars_1)
# Avto_salon.add_cars(cars_2)
# print(Avto_salon.cars_soni)
print(cars_1.get_info())
print(cars_2.get_info())
print(cars_2.__dict__)


def see_methods(klass):
    return [method for method in dir(klass) if\
            method.startswith('__') is False]



print(see_methods(Avto))

from uuid import uuid4
class Shaxs:
    """Shaxs haqida ma`lumot """
    __num_shaxs = 0
    def __init__(self,ism,familiya,passport,tyil):
        self.ism = ism
        self.familiya = familiya
        self.passport = passport
        self.tyil = tyil
        self.__id = uuid4()
        Shaxs.__num_shaxs += 1
        

    @classmethod
    def get_num_shaxs(cls):
        return cls.__num_shaxs
    

    def get_id(self):
        return self.__id

    def get_info(self):
        """Shaxs haqida ma`lumot """
        info = f"{self.ism} {self.familiya}."
        info += f"Passport : {self.passport} , {self.tyil}-tugulgan yili"
        return info
    
    def get_age(self,yil):
        """Shaxsni yoshini qaytaruvchi metod """
        return yil-self.tyil
    



class Talaba(Shaxs):
    __talabalar_soni = 0
    """Talaba klasi"""
    def __init__(self, ism, familiya, passport, tyil):
        super().__init__(ism, familiya, passport, tyil)
        Talaba.__talabalar_soni += 1

    @classmethod
    def get_talabalar_soni(cls):
        return cls.__talabalar_soni

talaba = Talaba("Vali","Nosirov","FA012124",2003)
print(f"{talaba.get_info()} \n {talaba.get_age(2024)}---yoshda ")
inson = Shaxs("Hasan","Alimov","AD010203",2001)
print(f"{inson.get_info()}. \n {inson.get_age(2024)}---yoshda ")
inson_1 = Shaxs("Doston","Holdorov","AD123123",2006)
talaba_1 = Talaba("Ozodbek","Ma`rufov","Fa012145",2006)
print(Shaxs.get_num_shaxs())
print(Talaba.get_talabalar_soni())




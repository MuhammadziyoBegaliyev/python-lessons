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

    def __repr__(self):
        """SHAXS HAQIDA YANI OBYEKT HAQIDA MA`LUMOT :"""
        return f"Ism:{self.ism}\nFamiyila :{self.familiya}"   

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
    
    def __ep__(self,student):
        """Tenglik"""
        return self.tyil == student.tyil
    
    def __ge__(self,student):
        """Tenglik"""
        return self.tyil >= student.tyil
    
    @classmethod
    def get_talabalar_soni(cls):
        return cls.__talabalar_soni
    
class Fan :
    def __init__(self,name) :
        self.name = name 
        self.talabalar = []


    def __repr__(self):
        """Fan nomini qaytaradi """
        return f"{self.name}--->Fan nomi "
    
    def __len__(self):
        return len(self.talabalar)
    
    def add_studentlar(self,c):
        if isinstance(c,Talaba):
            self.talabalar.append(c)
        else :
            print("Talaba obyektini kiritng ")

    def __getitem__(self,index):
        return self.talabalar[index]
    
    def add_fan(self,*qiymat):
        for fan in qiymat:
            if isinstance(fan,Talaba):
                self.talabalar.append(fan)
            else:
                print("Talaba obyektini kiriting ")
  
    def __add__(self,qiymat):
        if isinstance(qiymat,Fan):
            yangi_fan = Fan(f"{self.name} {qiymat.name}")
            yangi_fan.talabalar = self.talabalar + qiymat.talabalar
            return yangi_fan



fan1 = Fan("Oliy Matematika")
fan2 = Fan("Fizika")
fan3 = fan1 + fan2
print(fan3)
sinf = Fan("Matematika")
talaba_3 = Talaba("Olim","Bozorov","FA123456",1999)
talaba = Talaba("Vali","Nosirov","FA012124",2003)
talaba_1 = Talaba("Ozodbek","Ma`rufov","Fa012145",2006)
talaba_2 = Talaba("Muhammadziyo","Begaliyev","AB133305",2006)
inson = Shaxs("Hasan","Alimov","AD010203",2001)

for c in [talaba,talaba_1,talaba_2]:
    sinf.add_studentlar(c)

    
print(len(sinf))
print(sinf[:])
print(sinf)
# print(inson)
# print(talaba==talaba_1)
# print(talaba>=talaba_1)
# print(f"{talaba.get_info()} \n {talaba.get_age(2024)}---yoshda ")
# print(f"{inson.get_info()}. \n {inson.get_age(2024)}---yoshda ")
# inson_1 = Shaxs("Doston","Holdorov","AD123123",2006)
# print(Shaxs.get_num_shaxs())
# print(Talaba.get_talabalar_soni())


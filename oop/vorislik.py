class Shaxs:
    """Shaxslar haqida ma`lumot"""
    def __init__(self,name,lastname,pasport,birth_day):
        self.name = name
        self.lastname = lastname
        self.pasport = pasport
        self.birth_day = birth_day

    def get_info(self):
         
         """Shaxs haqida ma`lumot"""
         info = f"{self.name}  {self.lastname}."
         info += f"Pasport :{self.pasport}, {self.birth_day}-tugulgan yil"
         return info 
        
    def get_age(self,yil):
        """shaxsni yoshini aniqlovchi metod """
        return yil - self.birth_day
    

inson = Shaxs("Muhammadziyo","Begaliyev","AD133305",2006)
print(f"{inson.get_info()}.{inson.get_age(2024)}-yoshda")



class Professor(Shaxs):
    """Professor voris klasi"""
    def __init__(self, name, lastname, pasport, birth_day,id):
        """Shaxsning hususiyatlari """
        super().__init__(name, lastname, pasport, birth_day)
        self.idraqam = id 

    def get_info(self):
        """Professor haqida ma`lumot """
        info = f"Professor ismi:{self.name} \n Professor familiyasi :{self.lastname} , \n , Professor pasporti :{self.pasport} \n Professor tugulgan yili: {self.birth_day} "
        info += f"ID raqam: {self.idraqam}"
        return info
    

    def get_id(self):
        """Talabaninng id raqami """
        return self.idraqam


odam = Professor("Olim","Olimov","FA8347588",1983,"007")
print(f"{odam.get_info()}. ID: {odam.get_id()}")



class Sotuvchi(Shaxs):
    """Sotuvchi voris klasi  """
    def __init__(self, name, lastname, pasport, birth_day,raqam):
        super().__init__(name, lastname, pasport, birth_day)
        self.raqam = raqam

    def get_info(self):
        """Sotuvchi  haqida ma`lumot """
        info = f"Sotuvchi ismi:{self.name} \n sotuvchi familiyasi :{self.lastname} , \n , sotuvchi pasporti :{self.pasport} \n sotuvchi tugulgan yili: {self.birth_day} \n sotuvchi  raqami :{self.raqam}"
        return info
    
    def get_raqam(self):
        """Sotuvchining raqamini qaytaruvchi odastur """
        return self.raqam
    
sotuvchi_1 = Sotuvchi("Tanzila","Malikova","AD010202",1986,"010101")
print(f"{sotuvchi_1.get_info()}. Sotuv raqami :{sotuvchi_1.get_raqam()}")


class Mijos(Shaxs):
    """Mijos bosqichi va mijos raqami """
    def __init__(self, name, lastname, pasport, birth_day,navbat):
        super().__init__(name, lastname, pasport, birth_day)
        self.navbat = navbat
        self.bosqich = 1

    def get_info(self):
        """Mijos haqida ma`lumot """
        info = f"Mijos ismi:{self.name} \n mijoz familiyasi :{self.lastname} , \n , mijos pasporti :{self.pasport} \n mijos tugulgan yili: {self.birth_day} \n mijos  navbati :{self.navbat}"
        info += f"{self.get_bosqich()}-bosqich"
        return info
    
    def get_navbat(self):
        """Mijozning navbat raqami """
        return self.navbat
    
    def get_bosqich(self):
        """Mijosnuing nechinchi bosqichdagilini qaytaradi """
        return self.bosqich
    

class Admin(Professor):
    def __init__(self, name, lastname, pasport, birth_day):
        super().__init__(name, lastname, pasport, birth_day, id)
   
    def get_info(self):
        """adminka haqida ma`lumot """
        info = f"Adminka ismi:{self.name} \n Adminka familiyasi :{self.lastname} , \n , Adminka pasporti :{self.pasport} \n Adminka tugulgan yili: {self.birth_day} "
        return info
    

    def ban_user(self):
        bu = "Foydalanuvchi bloklangan"
        return bu
    
mijos = Mijos("Nodir","Mavlonov","AB010407",2010,"040")    
print(f"{mijos.get_info()} \n Mijos Navbat :{mijos.get_navbat()} \n Mijosning bosqichi :{mijos.get_bosqich()}")
admionka = Admin("Oisha","Faxriddinova","AA 000001",2028,)
print(f"{admionka.get_info()} \n {admionka.ban_user()}")
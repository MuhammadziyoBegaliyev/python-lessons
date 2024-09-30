class Animal:
    def get_sound(self):
        pass


class Dog(Animal):
    def get_sound(self):
        return "Wow"
    
class Cat(Animal):
    def __init__(self):
        super().__init__()

    def get_sound(self):
        return "miuv"

cat = Cat()  
dog = Dog()
print(f"it - {cat.get_sound()},Mushuk{cat.get_sound()}")
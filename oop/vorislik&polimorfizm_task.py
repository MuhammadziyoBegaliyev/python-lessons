class Talaba:
    def __init__(self): 
        self.fanlar = []

    def add_subjects(self,sub):
        """Royhatga fanlar qoshish :"""
        self.fanlar.append(sub)

    def __del__(self):
        print(self.fanlar)

class Fan:
    def __init__(self, title):
        self.title = title

    def get_info(self):
        return f"Fan nomi: {self.title}"


geogragiya = Fan(title="geogragiya")
info = geogragiya.get_info()
print(info)

   

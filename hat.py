import random

class Hat:
    
    house = ["Ayodhya", "Vrindavan", "Mithila", "Barsana"]
    
    @classmethod
    def sort(cls, name):
        print(name, "is in", random.choice(cls.house))
        
Hat.sort("Ram")
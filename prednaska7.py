import math
from abc import ABC, abstractmethod

class Tvar(ABC):

    @abstractmethod
    def obsah(self):
        print("Není definováno")

class Ctverec(Tvar):

    def __init__(self, hrana):
        self.hrana = hrana

    
    def obsah(self):
        return self.hrana * self.hrana

class Kruh(Tvar):
    
    def __init__(self, polomer=1):
        self.polomer = polomer

    def obsah(self):
        import math
        return math.pi * self.polomer * self.polomer

if __name__ == "__main__":
   
    tvary = [Ctverec(2), Ctverec(3), Kruh(2), Ctverec(1), Kruh(3), Ctverec(2.5)]
    suma = 0
    for tvar in tvary:
        suma += tvar.obsah()
    print(f'Součet obsahů všech tvarů je: {suma}')
    

"""

   obj1 = Ctverec(6)
   print(obj1.obsah())
   obj2 = Kruh(3)
   print(obj2.obsah())

"""
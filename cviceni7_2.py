class Osoba:
    def __init__(self,jmeno, vek):
        self.jmeno = jmeno
        self.vek = vek
        
    def __str__(self):
        return f'Osoba: {self.jmeno}, Věk: {self.vek}'
    
    def pridat_rok(self):
        self.vek += 1
    
class Student(Osoba):

    def __init__(self, jmeno, vek, rocnik=1):
        super().__init__(jmeno, vek)
        self.rocnik = rocnik
    
    def __str__(self):
        return f'Student: {self.jmeno}, Ročník: {self.rocnik}, Věk: {self.vek}'
    
    def pridat_rok(self):
        self.rocnik += 1
        if self.rocnik >= 5:
            self.rocnik = 5
        self.vek += 1
    
class Ucitel(Osoba):
    def __init__(self, jmeno, vek, roky_praxe=0):
        super().__init__(jmeno, vek)
        self.roky_praxe = roky_praxe 
    
    def __str__(self):
        return f'Učitel: {self.jmeno}, roky praxe: {self.roky_praxe}, Věk: {self.vek}'
    
    def pridat_rok(self):
        self.roky_praxe += 1
        self.vek += 1

class Udrzbar(Osoba):
    def __str__(self):
        return f'Údržbář: {self.jmeno}, Věk: {self.vek}'

if __name__ == "__main__":
    student1 = Student("Alice", 18)
    student2 = Student("Bob", 20)

    ucitel1 = Ucitel("Prof", 45)

    udrzbar1 = Udrzbar("Karlík Gotík", 50)

    osoby = [student1, student2, ucitel1, udrzbar1]
    for osoba in osoby:
        for i in range(10):
            osoba.pridat_rok()

    print(student1)
    print(student2)
    print(ucitel1)
    print(udrzbar1)

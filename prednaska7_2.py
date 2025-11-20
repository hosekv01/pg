class Osoba:
    def __init__ (self, jmeno):
        self.jmeno = jmeno
        self.ucet = None

    def prirad_ucet (self, ucet):
        self.ucet = ucet

class Ucet:
    def __init__ (self, majitel):
        self.majitel = majitel
        self.__zustatek = 0

    def zustatek(self):
        return self.__zustatek
    
    def vloz(self, castka):
        if castka > 0:
            self.__zustatek += castka
        else:
            print("Nelze vložit zápornou částku.")

    def vyber(self, castka):
        if 0 < castka <= self.__zustatek:
            self.__zustatek -= castka
        else:
            print("Nedostatečný zůstatek nebo neplatná částka.")

    def __str__(self):
        return f"Ucet majitele {self.majitel.jmeno} se zustatkem {self.__zustatek}"

class Banka:
    def __init__ (self, nazev):
        self.nazev = nazev
        self.ucty = []

    def zaloz_ucet (self, osoba):
        novy_ucet = Ucet(osoba)
        self.ucty.append(novy_ucet)
        osoba.prirad_ucet(novy_ucet)


if __name__ == "__main__":
    osoba1 = Osoba("Jan Novak")
    osoba2 = Osoba("Petr Svoboda")
    
    banka1 = Banka("KB")
    banka1.zaloz_ucet(osoba1)
    banka1.zaloz_ucet(osoba2)

    osoba1.ucet.vloz(1000)
    osoba2.ucet.vloz(500)

    print(osoba1.jmeno," - ", osoba1.ucet)
    print(osoba2.jmeno," - ", osoba2.ucet)

    osoba1.ucet.vyber(200)
    osoba2.ucet.vyber(600)

    print(osoba1.jmeno," - ", osoba1.ucet)
    print(osoba2.jmeno," - ", osoba2.ucet)
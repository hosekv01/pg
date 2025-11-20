class BankovniUcet:
    def __init__(self,jmeno):
        self.jmeno = jmeno
        self.__zustatek = 0

    def vloz(self,suma):
        if suma > 0:
            self.__zustatek += suma
        else:
            print("Nelze vložit zápornou částku.")

    def vyber(self,suma):
        if 0 < suma <= self.__zustatek:
            self.__zustatek -= suma
        else:
            print("Nedostatečný zůstatek nebo neplatná částka.")

    def __str__(self):
        return f"Bankovní účet majitele {self.jmeno} má zůstatek {self.__zustatek} Kč"
    
if __name__ == "__main__":
    ucet1 = BankovniUcet("Andrej Babiš")
    print(ucet1)

    ucet1.vloz(100)
    print(ucet1)
    ucet1.vyber(50)
    print(ucet1)
    ucet1.vloz(10)
    print(ucet1)
    ucet1.vyber(60)

    print(ucet1)
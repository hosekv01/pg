""""
class ChybaDeleniNulou(Exception):
    pass

def vydel(citatel, jmenovatel):
        if jmenovatel == 0:
            raise ChybaDeleniNulou
        return citatel / jmenovatel

if __name__ == "__main__":
    try:
        while True:
            try:
                cislo1 = int(input("Zadejte první číslo (citatel): "))
                break
            except ValueError:
                print("Zadej validní celé číslo pro čitatel.")
        while True:
            try:
                cislo2 = int(input("Zadejte druhé číslo (jmenovatel): "))
                break
            except ValueError:
                print("Zadej validní celé číslo pro jmenovatel.")
        vysledek = vydel(cislo1, cislo2)
        print(vysledek)
    except Exception:
        print("Nastala chyba při dělení.")
        
"""

import sys

if __name__ == "__main__":

    file = open("data.txt", "r")
    data = file.read()
    print(data)
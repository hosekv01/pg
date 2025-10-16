def je_prvocislo(cislo):
    if cislo < 2:
        return False
    for i in range(2, cislo):
        if cislo % i == 0:
            return False
    return True

def vrat_prvocisla(maximum):
    return [i for i in range(2, maximum + 1) if je_prvocislo(i)]

if __name__ == "__main__":
    cislo = int(input("Zadej maximum: "))
    print(cislo, "není prvočíslo" if not je_prvocislo(cislo) else "je prvočíslo")
    prvocisla = vrat_prvocisla(cislo)
    print(prvocisla)
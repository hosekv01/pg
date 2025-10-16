def cislo_text(cislo):
    jednotky = ["nula", "jedna", "dva", "tři", "čtyři", "pět", "šest", "sedm", "osm", "devět"]
    desitky = ["deset", "jedenáct", "dvanáct", "třináct", "čtrnáct", "patnáct", "šestnáct", "sedmnáct", "osmnáct", "devatenáct"]
    dvojciferny = ["","", "dvacet", "třicet", "čtyřicet", "padesát", "šedesát", "sedmdesát", "osmdesát", "devadesát"]
    stovka = "sto"

    if 0 <= cislo < 10:
        return jednotky[cislo]
    elif 10 <= cislo < 20:
        return desitky[cislo - 10]
    elif 20 <= cislo < 100:
        desitka = cislo // 10
        jednotka = cislo % 10
        if jednotka == 0:
            return dvojciferny[desitka]
        else:
            return dvojciferny[desitka] + " " + jednotky[jednotka]
    else:
        if cislo == 100:
            return stovka
        else:
            return "Číslo je mimo rozsah (0-100)"
    
if __name__ == "__main__":
    cislo = int(input("Zadejte číslo mezi 0 a 100: "))
    text = cislo_text(cislo)
    print("Číslo převedené na text:", text)
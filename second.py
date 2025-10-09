def cislo_text(cislo):
    #0-9
    jednotky = ["nula", "jedna", "dva", "tři", "čtyři", "pět", "šest", "sedm", "osm", "devět"]
    #10-19
    desitky = ["deset", "jedenáct", "dvanáct", "třináct", "čtrnáct", "patnáct", "šestnáct", "sedmnáct", "osmnáct", "devatenáct"]
    #20-99
    dvojciferny = ["","", "dvacet", "třicet", "čtyřicet", "padesát", "šedesát", "sedmdesát", "osmdesát", "devadesát"]
    #100
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
            return dvojciferny[desitka] + jednotky[jednotka]
    else:
        if cislo == 100:
            return stovka
        else:
            return "Číslo je mimo rozsah (0-100)"
    
if __name__ == "__main__":
    cislo = int(input("Zadejte číslo mezi 0 a 100: "))
    text = cislo_text(cislo)
    print("Číslo převedené na text:", text)
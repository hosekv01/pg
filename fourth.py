def je_tah_mozny(figurka, cilova_pozice, obsazene_pozice):
    
    if not (1 <= cilova_pozice[0] <= 8 and 1 <= cilova_pozice[1] <= 8):
        return False
    
    if cilova_pozice in obsazene_pozice:
        return False
    
    start = figurka["pozice"]
    typ = figurka["typ"]
    
    if typ == "pěšec":
        if cilova_pozice[1] == start[1]:
            if cilova_pozice[0] == start[0] + 1:
                return True
            if start[0] == 2 and cilova_pozice[0] == start[0] + 2:
                return not je_cesta_blokovana(start, cilova_pozice, obsazene_pozice)
        return False
    
    elif typ == "jezdec":
        return (abs(cilova_pozice[0] - start[0]) == 2 and abs(cilova_pozice[1] - start[1]) == 1) or \
               (abs(cilova_pozice[0] - start[0]) == 1 and abs(cilova_pozice[1] - start[1]) == 2)
    
    elif typ == "věž":
        if start[0] != cilova_pozice[0] and start[1] != cilova_pozice[1]:
            return False
        return not je_cesta_blokovana(start, cilova_pozice, obsazene_pozice)
    
    elif typ == "střelec":
        if abs(cilova_pozice[0] - start[0]) != abs(cilova_pozice[1] - start[1]):
            return False
        return not je_cesta_blokovana(start, cilova_pozice, obsazene_pozice)
    
    elif typ == "dáma":
        if start[0] != cilova_pozice[0] and start[1] != cilova_pozice[1] and \
           abs(cilova_pozice[0] - start[0]) != abs(cilova_pozice[1] - start[1]):
            return False
        return not je_cesta_blokovana(start, cilova_pozice, obsazene_pozice)
    
    elif typ == "král":
        return max(abs(cilova_pozice[0] - start[0]), abs(cilova_pozice[1] - start[1])) == 1
    
    return False


def je_cesta_blokovana(start, cil, obsazene_pozice):
    dx = 0 if start[0] == cil[0] else (1 if cil[0] > start[0] else -1)
    dy = 0 if start[1] == cil[1] else (1 if cil[1] > start[1] else -1)
    
    x, y = start[0] + dx, start[1] + dy
    while (x, y) != cil:
        if (x, y) in obsazene_pozice:
            return True
        x += dx
        y += dy
    
    return False


if __name__ == "__main__":
    pesec = {"typ": "pěšec", "pozice": (2, 2)}
    jezdec = {"typ": "jezdec", "pozice": (3, 3)}
    vez = {"typ": "věž", "pozice": (8, 8)}
    strelec = {"typ": "střelec", "pozice": (6, 3)}
    dama = {"typ": "dáma", "pozice": (8, 3)}
    kral = {"typ": "král", "pozice": (1, 4)}
    obsazene_pozice = {(2, 2), (8, 2), (3, 3), (5, 4), (8, 3), (8, 8), (6, 3), (1, 4)}

    print(je_tah_mozny(pesec, (3, 2), obsazene_pozice))
    print(je_tah_mozny(pesec, (4, 2), obsazene_pozice))
    print(je_tah_mozny(pesec, (1, 2), obsazene_pozice))

    print(je_tah_mozny(jezdec, (4, 4), obsazene_pozice))
    print(je_tah_mozny(jezdec, (5, 4), obsazene_pozice))
    print(je_tah_mozny(jezdec, (1, 2), obsazene_pozice))
    print(je_tah_mozny(jezdec, (9, 3), obsazene_pozice))

    print(je_tah_mozny(dama, (8, 1), obsazene_pozice))
    print(je_tah_mozny(dama, (1, 3), obsazene_pozice))
    print(je_tah_mozny(dama, (3, 8), obsazene_pozice))
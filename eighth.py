def bin_to_dec(binarni_cislo):
    # funkce spocita hodnotu predavaneho binarniho cisla (binarni_cislo muze byt str i int!!!)
    # 111 -> 7
    # "101" -> 5
    if isinstance(binarni_cislo, int):
        binarni_cislo = str(binarni_cislo)
    dekadicke_cislo = 0
    delka = len(binarni_cislo)  
    for i in range(delka):
        cifra = int(binarni_cislo[delka - 1 - i])
        dekadicke_cislo += cifra * (2 ** i)
    return dekadicke_cislo


def test_bin_to_dec():
    assert bin_to_dec("0") == 0
    assert bin_to_dec(1) == 1
    assert bin_to_dec("100") == 4
    assert bin_to_dec(101) == 5
    assert bin_to_dec("010101") == 21
    assert bin_to_dec(10000000) == 128
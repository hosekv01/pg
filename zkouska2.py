# Příklad 2: Práce s externími daty a výpočty
# Zadání:
# Napište funkci `convert_to_czk`, která:
# 1. Přijme částku (`amount`) jako desetinné číslo a kód měny (`currency`) jako řetězec (např. "USD", "EUR").
# 2. Stáhne aktuální kurzovní lístek z URL:
#    http://www.cnb.cz/cs/financni_trhy/devizovy_trh/kurzy_devizoveho_trhu/denni_kurz.txt
# 3. Načte příslušný kurz podle zadaného kódu měny a provede převod zadané částky na české koruny (CZK).
# 4. Funkce vrátí výslednou částku v CZK zaokrouhlenou na dvě desetinná místa.
# Pokud zadaná měna v kurzovním lístku neexistuje, vyhoďte výjimku `ValueError`.
#
# Vaše řešení můžete otestovat pomocí pytest takto:
# pytest zkouska2.py
# pokud Vám pytest nazahlásí žádné chyby, máte hotovo!
#
# instalace pytest:
# pip install pytest

import requests


def convert_to_czk(amount, currency):
    url = "http://www.cnb.cz/cs/financni_trhy/devizovy_trh/kurzy_devizoveho_trhu/denni_kurz.txt"
    response = requests.get(url) # stáhnou se data z linku
    response.raise_for_status()  # Zkontrolujeme, zda byl požadavek úspěšný
    lines = response.text.splitlines() # rozdělíme text na jednotlivé řádky
    for line in lines[2:]:  # Přeskočíme první dva řádky s hlavičkou
        parts = line.split('|') # rozdělíme řádek podle '|'
        if len(parts) < 5: # pokud je řádek neúplný, přeskočíme ho
            continue
        curr_code = parts[3] # kód měny je na čtvrté pozici
        quantity_str = parts[2] # množství je na třetí pozici
        rate_str = parts[4] # kurz je na páté pozici
        if curr_code == currency: # pokud se kód měny shoduje s požadovaným
            quantity = float(quantity_str.replace(',', '.')) # převedeme množství na float a nahradíme čárku tečkou
            rate = float(rate_str.replace(',', '.')) # převedeme kurz na float a nahradíme čárku tečkou
            converted_amount = amount * rate / quantity # provedeme převod na CZK který se rovná počtu * kurz / množství
            return round(converted_amount, 2) # vrátíme zaokrouhlenou částku na 2 desetinná místa
    raise ValueError(f"Currency {currency} not found in the exchange rate list.") # pokud měna nebyla nalezena, vyhodíme chybu


# Unit testy
from unittest.mock import patch, MagicMock

def test_convert_to_czk():
    mock_response = """31.10.2025 #237
země|měna|množství|kód|kurz
Austrálie|dolar|1|AUD|14,894
EMU|euro|1|EUR|25,480
USA|dolar|1|USD|23,000
Velká Británie|libra|1|GBP|29,745
"""
    with patch("requests.get") as mock_get:
        mock_get.return_value = MagicMock(ok=True, status_code=200, text=mock_response)

        assert convert_to_czk(100, "USD") == 2300.00
        assert convert_to_czk(50, "EUR") == 1274.00
        assert convert_to_czk(200, "AUD") == 2978.80
        
        try:
            convert_to_czk(100, "XYZ")
        except ValueError as e:
            assert str(e) == "Currency XYZ not found in the exchange rate list."

if __name__ == "__main__":
    test_convert_to_czk()
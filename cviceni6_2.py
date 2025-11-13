import requests
import json
import sys 

def fetch_rates(url):
    response = requests.get("http://www.cnb.cz/cs/financni_trhy/devizovy_trh/kurzy_devizoveho_trhu/denni_kurz.txt")
    if not response.ok:
        print("Nelze načíst data ze serveru.")
        sys.exit(1)
    
    splitted_text = response.text.splitlines()
    rates = {}
    for line in splitted_text[2:]:
        parts = line.split('|')
        if len(parts) >= 5:
            code = parts[3]
            amount = parts[4]
            amount = amount.replace(',', '.')
            amount = round(float(amount), 2)
            rates[code] = amount
    return rates
    


if __name__ == "__main__":
    listek = fetch_rates("http://www.cnb.cz/cs/financni_trhy/devizovy_trh/kurzy_devizoveho_trhu/denni_kurz.txt")
    print(listek)
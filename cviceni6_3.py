from cviceni6_2 import download_rates
import sys

if __name__ == "__main__":

    if len(sys.argv) != 2:
        print("Usage: python cviceni6_3.py <amount>")
        sys.exit(1)
    amount = sys.argv[1]

    #Kolik za ty peníze si mohu koupit dané měny

    datum, listek = download_rates('http://www.cnb.cz/cs/financni_trhy/devizovy_trh/kurzy_devizoveho_trhu/denni_kurz.txt')
    for mena in ['AUD', 'BRL', 'BGN', 'CNY', 'DKK', 'EUR', 'PHP', 'HKD', 'INR', 'IDR', 'ISK', 'ILS', 'JPY', 'ZAR', 'CAD', 'KRW', 'HUF', 'MYR', 'MXN', 'XDR', 'NOK', 'NZD', 'PLN', 'RON', 'SGD', 'SEK', 'CHF', 'THB', 'TRY', 'USD', 'GBP']:
        if mena in listek:
            kurz = listek[mena]
            mnozstvi = float(amount) / kurz
            print(f'Za {amount} CZK mohu koupit {mnozstvi:.2f} {mena} (kurz: {kurz})')
        else:
            print(f'Měna {mena} není v kurzu.')
import sys
import requests
import re


def download_url_and_get_all_hrefs(url):
    """
    Funkce stahne url predanou v parametru url pomoci volani response = requests.get(),
    zkontroluje navratovy kod response.status_code, ktery musi byt 200,
    pokud ano, najdete ve stazenem obsahu stranky response.content vsechny vyskyty
    <a href="url">odkaz</a> a z nich nactete url, ktere vratite jako seznam pomoci return
    """
    response = requests.get(url)
    if response.status_code != 200:
        raise Exception(f"Chyba stahovani stranky, status code: {response.status_code}")
    
    content = response.content.decode('utf-8')
    
    # Najdi všechny href odkazy pomocí regulárního výrazu
    hrefs = re.findall(r'<a[^>]+href=["\']([^"\']+)["\']', content)
    
    return hrefs


if __name__ == "__main__":
    try:
        if len(sys.argv) < 2:
            print("Použití: python sixth.py <url>")
            sys.exit(1)
        
        url = sys.argv[1]
        hrefs = download_url_and_get_all_hrefs(url)
        print(f"Nalezeno {len(hrefs)} odkazů:")
        for href in hrefs:
            print(href)
    # osetrete potencialni chyby pomoci vetve except
    except Exception as e:
        print(f"Program skoncil chybou: {e}")

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
    try:
        response = requests.get(url)
    except requests.exceptions.RequestException as e:
        raise Exception(f"Chyba při připojování k URL: {e}")

    if response.status_code != 200:
        raise Exception(f"Chyba stahovani stranky, status code: {response.status_code}")
    
    content = response.text
    

    hrefs = re.findall(r'<a[^>]+href\s*=\s*["\']([^"\']+)["\']', content)
    
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

    except Exception as e:
        print(f"Program skoncil chybou: {e}")
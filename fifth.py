
import sys

# definice úvodních binárních sekvencí obrázkových souborů
jpeg_header = b'\xff\xd8'
gif_header1 = b'GIF87a'
gif_header2 = b'GIF89a'
png_header = b'\x89PNG\r\n\x1a\n'


def read_header(file_name):
    """
    Tato funkce načte binární soubor z cesty file_name,
    z něj přečte prvních header_length bytů a ty vrátí pomocí return
    """
    try:
        with open(file_name, "rb") as file:
            return file.read(header_length)
    except Exception as e:
        print(f'Chyba při čtení souboru {file_name}: {e}')
        return None


def is_jpeg(file_name):
    """
    Funkce zkusí přečíst ze souboru hlavičku obrázku jpeg,
    tu srovná s definovanou hlavičkou v proměnné jpeg_header
    """
    # načti hlavičku souboru
    header = read_header(file_name, len(jpeg_header))

    try:
        if header == jpeg_header:
            return True
    except Exception as e:
        print(f'Chyba při porovnávání hlavičky souboru {file_name}: {e}')

    return False


def is_gif(file_name):
    """
    Funkce zkusí přečíst ze souboru hlavičku obrázku jpeg,
    tu srovná s definovanými hlavičkami v proměnných gif_header1 a gif_header2
    """
    # vyhodnoť zda je soubor gif
    header = read_header(file_name, len(gif_header1))
    try:
        if header == gif_header1 or header == gif_header2:
            return True
    except Exception as e:
        print(f'Chyba při porovnávání hlavičky souboru {file_name}: {e}')

    return False


def is_png(file_name):
    """
    Funkce zkusí přečíst ze souboru hlavičku obrázku jpeg,
    tu srovná s definovanou hlavičkou v proměnné png_header
    """
    # vyhodnoť zda je soubor pn
    
    file_name = read_header(file_name, len(png_header))
    try:
        if header == png_header:
            return 
    except Exception as e:
        print(f'Chyba při porovnávání hlavičky souboru {file_name}: {e}')

    return False


def print_file_type(file_name):
    """
    Funkce vypíše typ souboru - tuto funkci není třeba upravovat
    """
    if is_jpeg(file_name):
        print(f'Soubor {file_name} je typu jpeg')
    elif is_gif(file_name):
        print(f'Soubor {file_name} je typu gif')
    elif is_png(file_name):
        print(f'Soubor {file_name} je typu png')
    else:
        print(f'Soubor {file_name} je neznámého typu')


if __name__ == '__main__':
    print ("Postupný test", read_header("fifth-soubory/kitten.jpeg", 4))
    print ("Postupný test2", read_header("fifth-soubory/kitten.png", 4))
    print ("Postupný test3", read_header("fifth-soubory/kitten.gif", 4))
    try:
        file_name = sys.argv[1]
        # Pokud cesta neobsahuje lomítko, předpokládáme že je to soubor ve složce fifth-soubory
        if '/' not in file_name:
            file_name = f'fifth-soubory/{file_name}'
        print_file_type(file_name)
    except Exception as e:
        print(f'Chyba: {e}')

import os
import sys

jpeg_header = b'\xff\xd8'
gif_header1 = b'GIF87a'
gif_header2 = b'GIF89a'
png_header = b'\x89PNG\r\n\x1a\n'


def read_header(file_name, header_length):
    try:
        with open(file_name, "rb") as file:
           return file.read(header_length)
    except Exception as e:
     print(f'Chyba při čtení souboru {file_name}: {e}')

def is_jpeg(file_name):
    header = read_header(file_name, len(jpeg_header))

    try:
        if header == jpeg_header:
            return True
    except Exception as e:
        print(f'Chyba při porovnávání hlavičky souboru {file_name}: {e}')

    return False


def is_gif(file_name):
    header = read_header(file_name, len(gif_header1))
    try:
        if header == gif_header1 or header == gif_header2:
            return True
    except Exception as e:
        print(f'Chyba při porovnávání hlavičky souboru {file_name}: {e}')

    return False


def is_png(file_name):
    header = read_header(file_name, len(png_header))
    try:
        if header == png_header:
            return True
    except Exception as e:
        print(f'Chyba při porovnávání hlavičky souboru {file_name}: {e}')

    return False


def print_file_type(file_name):
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
        if len(sys.argv) < 2:
            folder = "fifth-soubory"
            print(f"\nZpracovávám všechny soubory ve složce {folder}:\n")
            
            for file_name in os.listdir(folder):
                file_path = os.path.join(folder, file_name)
                if os.path.isfile(file_path):
                    print_file_type(file_path)
        else:
            file_name = sys.argv[1]
            if '/' not in file_name:
                file_name = f'fifth-soubory/{file_name}'
            print_file_type(file_name)
    except Exception as e:
        print(f'Chyba: {e}')
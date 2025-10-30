import csv

def precti_hodnoty_a_incrementuj(file):

    all_results = []
    for line in file:
        data = line.split(',')
        result = []
        for value in data:
            value = value.strip().strip('"')
            try:
                value = int(value) + 1
            except ValueError:
                pass
            result.append(value)
        all_results.append(result)
    return all_results

def zapis_data_do_csv(file_name, data):
    with open(file_name, mode='w', newline='') as file:
        writer = csv.writer(file)
        for row in data:
            writer.writerow(row)

def zapis_data_bez_csv(file_name, data):
    with open(file_name, mode='w') as file:
        for row in data:
            line = ','.join(str(value) for value in row)
            file.write(line + '\n')

if __name__ == "__main__":

    try:
        name = input("Zadej jmeno souboru: ")
        name2 = name.split('.')[0]
        cislo = 1
        cislo = cislo + 1
        file = open(name, "r")
        results = precti_hodnoty_a_incrementuj(file)
        print(results)
        zapis_data_do_csv(f"{name2}{cislo}.csv", results)
        zapis_data_bez_csv(f"{name2}{cislo}.csv", results)
    except FileNotFoundError:
        print(f'Soubor {name} neexistuje')
    except Exception as e:
        print(f'Nastala neočekávaná chyba: {e}')
import csv
import os

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

def spoj_data_z_csv(file_name, include_headers=False):
    data = []
    with open(file_name, "r") as file:
        reader = csv.reader(file)
        headers = next(reader)
        if include_headers:
            data.append(headers)
        for row in reader:
            data.append(row)
    return data

def zapis_data_do_csv(file_name, data):
    with open(file_name, "w", newline='') as file:
        writer = csv.writer(file)
        for row in data:
            writer.writerow(row)


if __name__ == "__main__":

    try:
        soubor1 = input("Zadej jmeno prvního souboru: ")
        soubor2 = input("Zadej jmeno druhého souboru: ")
        csv_data1 = spoj_data_z_csv(soubor1, include_headers=True)
        csv_data2 = spoj_data_z_csv(soubor2, include_headers=False)
        vysledna_data = csv_data1 + csv_data2
        zapis_data_do_csv("spojeny_soubor.csv", vysledna_data)
        print("Soubory byly úspěšně spojeny do 'spojeny_soubor.csv'")
    except FileNotFoundError as e:
        print(f'Soubor nebyl nalezen: {e.filename}')

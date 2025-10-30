def precti_hodnoty_a_incrementuj(file):
    for line in file:
        print(line)

if __name__ == "__main__":
    name = input("Zadej jméno souboru: ")
    file = open(name, "r")

    precti_hodnoty_a_incrementuj(file)
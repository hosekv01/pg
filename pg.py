def sudy_nebo_lichy(cislo):
        cislo = int(cislo)
        if cislo % 2 == 0:
            print("Cislo je sude")
            return True
        else:
            print("Cislo je liche")
            return False



if __name__ == "__main__":
    sudy_nebo_lichy(5)
    sudy_nebo_lichy(1000000)
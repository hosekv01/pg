class Vektor:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__ (self):
        return f'Vektor({self.x}, {self.y})'
    
    def secti(self, jiny_vektor):
        x = self.x + jiny_vektor.x
        y = self.y + jiny_vektor.y
        return Vektor(x, y)
    
    def vynasob(self, skalar):
        x = self.x * skalar
        y = self.y * skalar
        return Vektor(x, y)
    
if __name__ == "__main__":

    v1 = Vektor(10, 5)
    v2 = Vektor(10, 10)

    print(f"Vektor 1: {v1}")
    print(f"Vektor 2: {v2}")

    v_soucet = v1.secti(v2)
    print(f"Součet: {v_soucet}")

    v_nasobek = v1.vynasob(5)
    print(f"Násobek pěti: {v_nasobek}")
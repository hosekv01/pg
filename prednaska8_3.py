class Ucet:
    def __init__(self):
        self.zustatek = 0
    
    @property
    def zustatek(self):
        return self._zustatek
    
    @zustatek.setter
    def zustatek(self, hodnota):
        if hodnota < 0:
            raise ValueError("Zustatek nemuze byt zaporny")
        self._zustatek = hodnota

if __name__ == "__main__":
    ucet = Ucet()
    print(f"Zustatek: {ucet.zustatek}")
    ucet.zustatek = 100
    print(f"Zustatek: {ucet.zustatek}")
    try:
        ucet.zustatek = -50
    except ValueError as e:
        print(f"Chyba: {e}")
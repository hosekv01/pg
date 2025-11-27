
import sys
import json

class Car:
    def __init__(self, znacka, model, barva):
        self.znacka = znacka
        self.model = model
        self.barva = barva

    def __str__(self):
        return f"Auto {self.znacka} {self.model} v barve {self.barva}"
    
    @classmethod
    def parse(cls, jdata):
        data = json.loads(jdata)
        for value in ["Znacka", "Model", "barva"]:
            if value not in data:
                raise KeyError(f"Chybi klic {value}")
        return cls(data["Znacka"], data["Model"], data["barva"])
    
if __name__ == "__main__":

    data = [
        '{"Znacka": "Skoda", "Model": "Octavia", "barva": "modra"}',
        '{"Znacka": "Ford", "Model": "Focus", "barva": "cervena"}'
        
    ]
    
    for jdata in data:
        try:
            auto = Car.parse(jdata)
            print(auto)
        except InvalidData as e:
            print(f"Chyba: {e}")
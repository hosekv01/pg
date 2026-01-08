# Příklad 3: Základy OOP (dědičnost, abstrakce, zapouzdření)
# Zadání:
# Vytvořte dvě podtřídy třídy `Shape`: `Rectangle` a `Circle`.
# - `Rectangle` má atributy `width` a `height` a implementuje metodu `area`, která spočítá plochu obdelníku (zaokrouhlenou na 1 desetinné místo).
# - `Circle` má atribut `radius` a implementuje metodu `area`, která spočítá plochu kruhu (zaokrouhlenou na 1 desetinné místo).
# - ve třídě `Circle` navíc implementujte metodu `__str__`, která vrátí řetězec ve tvaru `{self.shape_name} with a radius of {self.radius} has an area of {self.area}`.
#
# Vaše řešení můžete otestovat pomocí pytest takto:
# pytest zkouska3.py
# pokud Vám pytest nazahlásí žádné chyby, máte hotovo!
#
# instalace pytest:
# pip install pytest

import math


class Shape():

    def __init__(self, shape_name=None):
        self.shape_name = shape_name
    
    def __str__(self):
        return f'{self.shape_name} shape with area {self.area():.1f}' #vrátí řetězec s názvem a plochou zaokrouhlenou na 1 desetinné místo

    def area(self):
        return 0.0


# ZDE NAPIŠTE VÁŠ KÓD

class Rectangle(Shape): #třída Rectangle dědí ze Shape
    def __init__(self, width, height): #parametry šířka a výška
        super().__init__("Rectangle")#dědění z Shape s názvem Rectangle
        self.width = width #šířka
        self.height = height #výška
    
    def area(self): #metoda pro výpočet plochy
        return round(self.width * self.height, 1) #zaokrouhlení na 1 desetinné místo + vynásobení šířky a výšky


class Circle(Shape):
    def __init__(self, radius): #parametr poloměr
        super().__init__("Circle") #dědění z Shape s názvem Circle
        self.radius = radius #poloměr
    
    def area(self): #metoda pro výpočet plochy
        return round(math.pi * self.radius ** 2, 1) #zaokrouhlení na 1 desetinné místo + výpočet plochy kruhu (πr²)
    
    def __str__(self): #metoda pro vrácení řetězce
        return f'Circle shape with a radius of {self.radius} has an area of {self.area()}' #vrácení řetězce s poloměrem a plochou kruhu


from unittest.mock import patch, MagicMock, mock_open


# Unit testy
def test_shapes():
    rect = Rectangle(4, 5) #zadá šířku a výšku
    assert rect.area() == 20.0 #zkontroluje plochu
    assert str(rect) == "Rectangle shape with area 20.0"

    circle = Circle(3) #zadá poloměr
    assert round(circle.area(), 1) == 28.3 #zkontroluje plochu
    assert str(circle) == "Circle shape with a radius of 3 has an area of 28.3"


if __name__ == "__main__":
    shape = Shape()
    print(shape)
    rect = Rectangle(4, 5)
    print(rect)
    circle = Circle(3)
    print(circle)
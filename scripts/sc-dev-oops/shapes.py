from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def get_perimeter(self) -> float:
        pass

    @abstractmethod
    def get_area(self) -> float:
        pass

class Circle(Shape):
    def __init__(self, circle_radius) -> None:
        self.radius = circle_radius

    def get_perimeter(self) -> float:
        return 2 * self.radius * 3.14
    
    def get_area(self) -> float:
        return 3.14 * self.radius ** 2
    
class Square(Shape):
    def __init__(self, square_width, square_height) -> None:
        self.width = square_width
        self.height = square_height

    def get_perimeter(self) -> float:
        return 2 * self.width + self.height * 2
    
    def get_area(self) -> float:
        return self.radius * self.height
    

class Engineer():
    def __init__(self, engineer_name) -> None:
        self.name = engineer_name

    def measure_perimeter(self, shape: Shape) -> str:
        perimeter = shape.get_perimeter()
        return f'Engenheiro {self.name} mediu o perímetro do shape: {perimeter}'
    
    def measure_area(self, shape: Shape) -> str:
        perimeter = shape.get_area()
        return f'Engenheiro {self.name} mediu a área do shape: {area}'
    

engenheiroA = Engineer('EngenheiroA')
square = Square(1, 1)
circle = Circle(1)

print(engenheiroA.measure_perimeter(square))
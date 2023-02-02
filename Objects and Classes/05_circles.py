class Circle:
    __pi = 3.14

    def __init__(self, diameter):
        self.diameter = diameter
        self.radius = diameter / 2

    def calculate_circumference(self):
        return Circle.__pi * self.diameter

    def calculate_area(self):
        return Circle.__pi * (self.diameter / 2) ** 2

    def calculate_area_of_sector(self, angle):
        radius = self.diameter / 2
        return (angle / 360) * Circle.__pi * (radius ** 2)


circle = Circle(10)
angle = 5
print(circle.calculate_circumference())
print(circle.calculate_area_of_sector(angle))
print(circle.calculate_area())
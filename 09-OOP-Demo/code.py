# Exercise Name:
# 	09-OOP-Demo
# Description:
# 	Create a class and demonstrate how @property decorator is used

class Circle:
    def __init__(self, radius):
        self._radius = radius

    @property
    def radius(self):
        return self._radius

    @property
    def diameter(self):
        return self._radius * 2

    @property
    def area(self):
        return 3.14 * self._radius ** 2

    @radius.setter
    def radius(self, value):
        if value < 0:
            raise ValueError("Radius cannot be negative")
        self._radius = value

circle = Circle(radius=5)

print("Radius:", circle.radius)
print("Diameter:", circle.diameter)
print("Area:", circle.area)

circle.radius = 7
print("Updated Radius:", circle.radius)
print("Updated Diameter:", circle.diameter)
print("Updated Area:", circle.area)

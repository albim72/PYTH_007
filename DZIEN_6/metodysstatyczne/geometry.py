import math
class Geometry:
    @staticmethod
    def area_of_circle(radius):
        return math.pi * radius ** 2

    @staticmethod
    def area_of_triangle(base, height):
        return 0.5 * base * height

    @staticmethod
    def area_of_rectangle(base, height):
        return base * height

print(f"pole koła: {Geometry.area_of_circle(5):.2f}")
print(f"pole trójkąta: {Geometry.area_of_triangle(3.2, 7.3):.2f}")
print(f"pole prostokąta: {Geometry.area_of_rectangle(2, 4.88):.2f}")

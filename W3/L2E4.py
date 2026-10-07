import math

radius = float(input("radius in cm: "))

area = math.pi * (radius ** 2)
circumference = 2 * math.pi * radius

print("area =", math.ceil(area, 2), "cm²")
print("circumference =", round(circumference, 2), "cm")
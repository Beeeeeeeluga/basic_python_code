import math

radius = int(input("Radius:"))
slant = int(input("slant:"))

surface_area = math.pi * radius * slant + 2 * math.pi * (radius ^ 2)
height = math.sqrt((slant ^ 2) - (radius ^ 2))
volume = (1 / 3) * math.pi * (radius ^ 2) * height

print("cone")
print(radius)
print(slant)
print("Height =", format(height, '10g'))
print("Surface area =", format(surface_area, "10g"))


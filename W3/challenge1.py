import math

radius = int(input("radius: "))
height = int(input("height: "))

volume = math.pi * (radius ^ 2) * height

surface_area = 2 * math.pi * radius * height + 2 * math.pi * (radius ^ 2)

print("Volume =", volume)
print("Surface area =", surface_area)

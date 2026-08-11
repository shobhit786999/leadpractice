import math
def area(radius):
    area = math.pi*radius**2
    circumference = 2*math.pi*radius
    return area,circumference
a,c = area(3)
print(a,c)
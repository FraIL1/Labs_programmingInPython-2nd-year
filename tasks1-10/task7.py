import math

def calculate_circle_area(r):
    return math.pi * r ** 2

def is_positive(num):
    return num > 0


radius = int(input())
num = int(input())

print(calculate_circle_area(radius))
print(is_positive(num))

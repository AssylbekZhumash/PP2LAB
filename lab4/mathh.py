import math

# 1.
def degrees_to_radians(deg):
    return math.radians(deg)

degree = 15
print("Input degree:", degree)
print("Output radian:", degrees_to_radians(degree))

# 2. 
def trapezoid_area(height, base1, base2):
    return 0.5 * (base1 + base2) * height

height = 5
base1 = 5
base2 = 6
print("Expected Output:", trapezoid_area(height, base1, base2))

# 3. 
def regular_polygon_area(sides, side_length):
    return (sides * side_length**2) / (4 * math.tan(math.pi / sides))

sides = 4
side_length = 25
print("The area of the polygon is:", regular_polygon_area(sides, side_length))

# 4. 
def parallelogram_area(base, height):
    return base * height

base = 5
height = 6
print("Expected Output:", parallelogram_area(base, height))

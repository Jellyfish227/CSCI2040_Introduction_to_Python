import math


# your statement follows
def check_invalid(triangle):
    a, b, c = triangle
    return (a > 0) & (b > 0) & (c > 0) & ((a + b > c) | (b + c > a) | (a + c > b))

def is_obtuse_triangle(triangle):
    side = [triangle[0], triangle[1], triangle[2]]
    max_side = side.index(max(side))
    max_side = side.pop(max_side)
    ab = 0
    for x in side:
        ab += x**2
    return max_side**2 > ab

def perimeter(triangle):
    return sum(triangle)

def area(triangle):
    a, b, c = triangle
    s = perimeter(triangle) / 2
    return math.sqrt(s * (s - a) * (s - b) * (s - c))

def outer_radius(triangle):
    a, b, c = triangle
    return (a * b * c) / (4 * area(triangle))
    
if __name__ == '__main__':
    triangles = [(3,4,5),(3,6,1),(6,8,5),(6,8,10),(5,12,13)]
    print(check_invalid(triangles[0]))
    print(is_obtuse_triangle(triangles[0]))
    print(area(triangles[0]))
    print(perimeter(triangles[0]))
    print(outer_radius(triangles[0]))




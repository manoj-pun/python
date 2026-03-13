# A 3D point is stored as a tuple (x, y, z). Write a function distance(p1, p2) that computes the
# Euclidean distance between two points. Then write closest_to_origin(points) that takes a list of
# point tuples and returns the one closest to (0, 0, 0). Use tuple unpacking.

#Euclidean Distance Function
import math

def distance(p1, p2):
    x1, y1, z1 = p1
    x2, y2, z2 = p2
    
    return math.sqrt((x2-x1)**2 + (y2-y1)**2 + (z2-z1)**2)

p1 = (1,2,3)
p2 = (4,5,6)

print(distance(p1, p2))


# Closest Point to Origin
def closest_to_origin(points):
    origin = (0,0,0)
    
    closest = points[0]
    min_dist = distance(points[0], origin)
    
    for point in points:
        if distance(point, origin) < min_dist:
            min_dist = distance(point, origin)
            closest = point
            
    return closest

points = [
    (3,4,5),
    (1,1,1),
    (2,2,2),
    (10,10,10)
]

print(closest_to_origin(points))
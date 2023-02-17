import math

def distance(p1, p2):
    x1, y1 = float(p1[0]), float(p1[1])
    x2, y2 = float(p2[0]), float(p2[1])
    return math.sqrt((x2-x1)**2 + (y2 -y1)**2)


def max_distance_point(initial_point, points):
    """
        Find point that with max_distance from initial_point
    """
    if not points:
        return None
    return max(points, key=lambda current_point: distance(initial_point,current_point))
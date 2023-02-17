import distance
from distance import max_distance_point
import pytest
def test_distance():
    for point in [
        (0,0),
        (1,1),
        (-1,-1),
        (-1,1),
        (1,-1)]:
        assert distance.distance(point, point) == pytest.approx(0)

def test_max_distance_point():
    initial_point = (0,0)
    point_coud = [
        (0,0), (1,1), (2,4), (5,-5),
        (100,2), (5,100)
    ]
    result = max_distance_point(initial_point, point_coud)
    assert result == (5,100)


# TASK (10 min): Do better coverage for distance and max_distance_point function

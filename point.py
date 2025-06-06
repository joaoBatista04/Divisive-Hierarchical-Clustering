from typing import List
import math

class Point:
    def __init__(self, id: int, coordinates: List[float]):
        self.id = id
        self.coordinates = coordinates

    def euclidean_distance(self, point: 'Point') -> float:
        return math.sqrt(sum((a-b) ** 2 for a, b in zip(self.coordinates, point.coordinates)))

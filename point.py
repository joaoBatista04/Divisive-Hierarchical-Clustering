from typing import List
import math

#Class that represents the informations of data points
class Point:
    def __init__(self, id: int, coordinates: List[float]):
        #Each point has an id and a list of coordinates
        self.id = id
        self.coordinates = coordinates

    #Calculating euclidean distance between two points, following the formula: srqt((x1-y1)^2 + (x2-y2)^2 + ... + (xn-yn)^2)
    def euclidean_distance(self, point: 'Point') -> float:
        return math.sqrt(sum((a-b) ** 2 for a, b in zip(self.coordinates, point.coordinates)))

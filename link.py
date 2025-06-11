from point import Point

#Class that represents the links between points
class Link:
    def __init__(self, a_point: Point, b_point: Point, distance: float):
        #Each link has an origin point, a final point and a distance
        self.a = a_point
        self.b = b_point
        self.distance = distance

    #To compare two links. If links have the same distance, the algorithm will consider the link with smaller first point (id of the first point)
    def __lt__(self, link: 'Link')-> bool:
        if self.distance != link.distance:
            return self.distance < link.distance
        
        return (min(self.a.id, self.b.id),
                max(self.a.id, self.b.id)) < (
                    min(link.a.id, link.b.id),
                    max(link.a.id, link.b.id)
                )
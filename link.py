from point import Point

class Link:
    def __init__(self, a_point: Point, b_point: Point, distance: float):
        self.a = a_point
        self.b = b_point
        self.distance = distance

    def __lt__(self, link: 'Link')-> bool:
        if self.distance != link.distance:
            return self.distance < link.distance
        
            return (min(self.a.id, self.b.id),
                    max(self.a.id, self.b.id)) < (
                        min(link.a.id, link.b.id),
                        max(link.a.id, link.b.id)
                    )
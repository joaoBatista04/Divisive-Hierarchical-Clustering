import csv

from typing import List, Dict
from point import Point
from link import Link
from unionfind import UnionFind

def read_csv(fp_input_path: str) -> List[Point]:
    points = []

    #Extracts the coordinates of each point in each row of the CSV file
    with open(fp_input_path, 'r') as f:
        reader = csv.reader(f)
        for i, line in enumerate(reader, start=1):
            coordinates = [float(value) for value in line]
            points.append(Point(i, coordinates))
    
    return points

def build_links(points: List[Point]) -> List[Link]:
    points_amount = len(points)
    chosen = set()
    links = []

    #Initializing the current point with the first point
    curr = points[0]
    #Adding the first point to set of chosen points
    chosen.add(curr.id)

    while len(chosen) < points_amount:
        min_link = None

        for point in points:
            #Evaluates whether each point is not on the list of already chosen ones
            if point.id not in chosen:
                #If not, the distance from the evaluated point to the current point is calculated and the link is assembled
                dist = curr.euclidean_distance(point)
                new_link = Link(curr, point, dist)

                #If the distance found is the smallest among the points to be evaluated, the minimum distance is updated
                if min_link is None or new_link < min_link:
                    min_link = new_link

        #The point with the minimum distance to the current point is marked as chosen and set as current
        links.append(min_link)
        chosen.add(min_link.b.id)
        curr = min_link.b 

    return links

def cut_links(links: List[Link], K: int) -> List[Link]:
    #Orders the link list by distance and return the K largest distances
    ordered_links = sorted(links, key=lambda l: l.distance, reverse=True)
    return ordered_links[K - 1:]

def build_groups(links: List[Link], points: List[Point]) -> List[List[int]]:
    #Initializes the Union-Find structure with all the point IDs
    uf = UnionFind([point.id for point in points])

    #Joins the points linked by remaining cut links (after the K largest cuts)
    for link in links:
        uf.union(link.a.id, link.b.id)

    #Creates a dictionary to store the groups, where the keys are the roots of the groups and the values are the list of points that belong to specific group
    groups_dict: Dict[int, List[int]] = {}
    for point in points:
        #Finds the root of the set to which the point belongs
        root = uf.find(point.id)
        if root not in groups_dict:
            groups_dict[root] = []
        #Groups point IDs by their root
        groups_dict[root].append(point.id)

    #Returns the internally ordered groups
    return [sorted(group) for group in groups_dict.values()]

def print_groups(groups: List[List[int]]):
    print("Agrupamentos:")
    #Printing the point IDs of each group
    for group in groups:
        print(", ".join(map(str, group)))

def save_output(fp_output_path, groups):
    #Save each group as a line in the CSV file
    with open(fp_output_path, 'w', newline='') as f:
        writer = csv.writer(f)
        for group in groups:
            writer.writerow(group)
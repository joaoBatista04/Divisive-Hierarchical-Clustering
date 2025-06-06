import csv

from typing import List, Dict
from point import Point
from link import Link
from unionfind import UnionFind

def read_csv(fp_input_path: str) -> List[Point]:
    points = []

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

    curr = points[0]
    chosen.add(curr.id)

    while len(chosen) < points_amount:
        min_link = None

        for point in points:
            if point.id not in chosen:
                dist = curr.euclidean_distance(point)
                new_link = Link(curr, point, dist)

                if min_link is None or new_link < min_link:
                    min_link = new_link

        links.append(min_link)
        chosen.add(min_link.b.id)
        curr = min_link.b 

    return links

def cut_links(links: List[Link], K: int) -> List[Link]:
    ordered_links = sorted(links, key=lambda l: l.distance, reverse=True)
    return ordered_links[K - 1:]

def build_groups(links: List[Link], points: List[Point]) -> List[List[int]]:
    uf = UnionFind([point.id for point in points])

    for link in links:
        uf.union(link.a.id, link.b.id)

    groups_dict: Dict[int, List[int]] = {}
    for point in points:
        root = uf.find(point.id)
        if root not in groups_dict:
            groups_dict[root] = []
        groups_dict[root].append(point.id)

    return sorted([sorted(group) for group in groups_dict.values()],
                  key=lambda g: g[0], reverse=True)

def print_groups(groups: List[List[int]]):
    print("Agrupamentos:")
    for group in groups:
        print(", ".join(map(str, group)))

def save_output(fp_output_path, groups):
    with open(fp_output_path, 'w', newline='') as f:
        writer = csv.writer(f)
        for group in groups:
            writer.writerow(group)
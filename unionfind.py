from typing import List

#At the end of the algorithm, the formation of clusters from the cut links becomes a Union-Find problem (Disjoint Set Union), which can be optimized with path suppression
class UnionFind:
    def __init__(self, elements: List[int]):
        #Each element starts as the leader of the set
        self.parent = {x: x for x in elements}
        #The rank is the depth of the tree rooted at the element
        self.rank = {x: 0 for x in elements}

    def find(self, x: int) -> int:
        #Find the root of the set containing x
        if self.parent[x] != x:
            #Path compression: directly connects x to the root, flattening the tree
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]
    
    def union(self, x: int, y: int):
        #Find the roots of the two sets
        rx, ry = self.find(x), self.find(y)

        if rx == ry:
            return
        
        #Union by rank: the set with the lowest rank joins the set with the highest rank
        if self.rank[rx] < self.rank[ry]:
            self.parent[rx] = ry
        else:
            self.parent[ry] = rx

            #If the ranks were equal, the new leader's rank increases
            if self.rank[rx] == self.rank[ry]:
                self.rank[rx] += 1
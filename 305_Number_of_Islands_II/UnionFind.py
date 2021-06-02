class UF:
    def __init__(self, size: int):
        self.parents = list(range(size))
        self.tree_sizes = [1 for _ in range(size)]

    def union(self, node1: int, node2: int):
        r1, r2 = self.get_root(node1), self.get_root(node2)
        if r1 == r2:
            return

        if self.tree_sizes[r1] > self.tree_sizes[r2]:
            self.parents[r2] = r1
            self.tree_sizes[r1] += self.tree_sizes[r2]
        else:
            self.parents[r1] = r2
            self.tree_sizes[r2] += self.tree_sizes[r1]

    def find(self, node1: int, node2: int) -> bool:
        return self.get_root(node1) == self.get_root(node2)

    def get_root(self, node: int):
        while node != self.parents[node]:
            self.parents[node] = self.parents[self.parents[node]]
            node = self.parents[node]

        return node
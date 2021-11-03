""" Representing graph present in code as an adjacency list"""


class Graph:
    def __init__(self, cap):
        self.capacity = cap
        self.arr = [[] for _ in range(cap)]

    def insert(self, u, v):
        if self.capacity > len(self.arr[u]):
            self.arr[u].append(v)
        else:
            print("Graph is Full for:", u)
        if self.capacity > len(self.arr[v]):
            self.arr[v].append(u)
        else:
            print("Graph is Full for:", v)
        return


def main():
    v = 5
    g = Graph(v)
    g.insert(0, 1)
    g.insert(0, 2)
    g.insert(1, 2)
    g.insert(1, 3)
    print(g.arr)


if __name__ == "__main__":
    main()

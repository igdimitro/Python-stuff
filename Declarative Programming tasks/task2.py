# Задача 4:
# Да се реализира итератор, който изброява ребрата от даден граф с тежести
# по ребрата, по които се сформира минимално покриващо дърво по алгоритъма
# на Крускал.

graph = {
    'vertices': {'A', 'B', 'C', 'D', 'E', 'F', 'G'},
    'edges': [
        (7, 'A', 'B'),
        (5, 'A', 'D'),
        (9, 'D', 'B'),
        (6, 'D', 'F'),
        (15, 'D', 'E'),
        (8, 'F', 'E'),
        (11, 'F', 'G'),
        (9, 'G', 'E'),
        (7, 'B', 'E'),
        (5, 'C', 'E'),
        (8, 'B', 'C')
    ]
}


def helper(minimal_edge, forest):
    u = next(filter(lambda subset: minimal_edge[1] in subset, forest))
    v = next(filter(lambda subset: minimal_edge[2] in subset, forest))
    if u != v:
        forest.remove(u)
        forest.remove(v)
        u = u | v
        forest.append(u | v)
        return minimal_edge
    else:
        return None


def Kruskal_iterator(graph):
    g = graph
    forest = list(map(lambda v: set(v), graph['vertices']))
    g['edges'].sort()
    return filter(lambda x: x is not None,
                  map(lambda minimal_edge: helper(minimal_edge, forest),
                      g['edges']))


if __name__ == "__main__":
    it = Kruskal_iterator(graph)
    for i in range(100):
        print(next(it))

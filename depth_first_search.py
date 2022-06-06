graph = {'A': {'B', 'C'},
         'B': {'A', 'D', 'E'},
         'C': {'A', 'F'},
         'D': {'B'},
         'E': {'B', 'F'},
         'F': {'C', 'E'}}


def depth_first_search(graph, start, goal, path=None):
    if path is None:
        path = [start]
    if start == goal:
        yield path
    for next in graph[start] - set(path):
        yield from depth_first_search(graph, next, goal, path + [next])


print(list(depth_first_search(graph, 'F', 'C')))
print(list(depth_first_search(graph, 'D', 'F')))

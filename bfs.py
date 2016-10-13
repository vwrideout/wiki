
#inspiration from http://eddmann.com/posts/depth-first-search-and-breadth-first-search-in-python/
def bfs(graph, start, end):
    visited = set()
    queue = [(start, [])]
    while queue:
        vertex, path = queue.pop(0)
        if vertex == end:
            return path + [end]
        if vertex not in visited and vertex in graph.keys():
            visited.add(vertex)
            for neighbor in graph[vertex]:
                queue.append((neighbor, path + [vertex]))
    return False




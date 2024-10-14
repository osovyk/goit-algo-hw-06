from task_1 import G_metro
from collections import deque

# Реалізація алгоритму DFS для знаходження шляху
def dfs(graph, start, goal, path=None):
    if path is None:
        path = []
    path = path + [start]
    if start == goal:
        return path
    for neighbor in graph.neighbors(start):
        if neighbor not in path:
            new_path = dfs(graph, neighbor, goal, path)
            if new_path:
                return new_path
    return None


# Реалізація алгоритму BFS для знаходження шляху
def bfs(graph, start, goal):
    visited = set()
    queue = deque([[start]])

    if start == goal:
        return [start]

    while queue:
        path = queue.popleft()
        node = path[-1]
        if node not in visited:
            neighbors = list(graph.neighbors(node))
            for neighbor in neighbors:
                new_path = list(path)
                new_path.append(neighbor)
                if neighbor == goal:
                    return new_path
                queue.append(new_path)
            visited.add(node)
    return None

if __name__ == "__main__":
    # Тестування DFS та BFS на графі
    start_node = "Лісова"
    goal_node = "Сирець"

    dfs_path = dfs(G_metro, start_node, goal_node)
    bfs_path = bfs(G_metro, start_node, goal_node)

    print(f"Шлях, знайдений DFS: {dfs_path}")
    print(f"Шлях, знайдений BFS: {bfs_path}")
from task_1 import *


# Алгоритм Дейкстри для пошуку найкоротшого шляху
def dijkstra(graph, start):
    # Ініціалізація відстаней до всіх вершин як "нескінченних"
    distances = {vertex: float('infinity') for vertex in graph}
    distances[start] = 0

    # Словник для зберігання попередників
    previous_vertices = {vertex: None for vertex in graph}

    visited = set()

    while len(visited) < len(graph):
        # Вибираємо невідвідану вершину з мінімальною поточною відстанню
        min_distance = float('infinity')
        current_vertex = None
        for vertex in graph:
            if vertex not in visited and distances[vertex] < min_distance:
                min_distance = distances[vertex]
                current_vertex = vertex

        # Якщо всі досяжні вершини оброблені, виходимо з циклу
        if current_vertex is None:
            break

        print(f"Обрана вершина: {current_vertex} з відстанню {distances[current_vertex]}")

        # Оновлюємо відстані до сусідніх вершин
        for neighbor, weight_data in graph[current_vertex].items():
            weight = weight_data['weight']
            new_distance = distances[current_vertex] + weight
            if new_distance < distances[neighbor]:
                distances[neighbor] = new_distance
                previous_vertices[neighbor] = current_vertex  # Зберігаємо попередника

        # Позначаємо вершину як відвідану
        visited.add(current_vertex)
        print(f"Відвідані вершини: {visited}")

    return distances, previous_vertices



# Функція для відновлення найкоротшого шляху
def get_shortest_path(previous_vertices, goal):
    path = []
    current_node = goal
    while current_node is not None:
        path.append(current_node)
        current_node = previous_vertices[current_node]
    path = path[::-1]
    print(f"Найкоротший шлях: {path}")
    return path


if __name__ == "__main__":
    start_node = "Е_Микільська Слобідка"
    goal_node = "Контрактова площа"

    # Перевіряємо, чи є вершини у графі
    if start_node not in G_metro:
        print(f"Станція {start_node} не знайдена у графі.")
    elif goal_node not in G_metro:
        print(f"Станція {goal_node} не знайдена у графі.")
    else:
        # Знаходимо найкоротші шляхи з вершини start_node до всіх інших вершин
        distances, previous_vertices = dijkstra(G_metro, start_node)

        # Отримуємо найкоротший шлях з start_node до goal_node
        shortest_path = get_shortest_path(previous_vertices, goal_node)
        shortest_path_distance = distances[goal_node]

        if shortest_path_distance == float('infinity'):
            print(f"Шляху від {start_node} до {goal_node} не існує.")
        else:
            print(f"Найкоротший шлях за Дейкстрою: {shortest_path}")
            print(f"Загальна вага шляху: {shortest_path_distance}")
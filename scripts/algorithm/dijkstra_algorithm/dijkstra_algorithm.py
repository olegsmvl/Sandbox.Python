import heapq

def dijkstra(graph, start):
    # Инициализация расстояний
    distances = {vertex: float('infinity') for vertex in graph}
    print(distances)
    distances[start] = 0

    # Очередь приоритетов для хранения вершин
    priority_queue = [(0, start)]
    print(priority_queue)

    i = 0

    while priority_queue:
        print(f"===={i}====")
        print(f"distanses {distances}")
        i+=1
        current_distance, current_vertex = heapq.heappop(priority_queue)
        print(f"pop {current_vertex} : {current_distance}")

        # Если текущее расстояние больше записанного, пропускаем
        if current_distance > distances[current_vertex]:
            continue

        # Перебор соседей текущей вершины
        for neighbor, weight in graph[current_vertex].items():
            distance = current_distance + weight
            print(f"vertex={neighbor} weight={weight} distance={distance}")
            print(f"distances[{neighbor}] {distances[neighbor]}")
            # Если найден более короткий путь к соседу
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(priority_queue, (distance, neighbor))
        print(f"distanses {distances}")
        print(f"priority_queue {priority_queue}")

    return distances

# Пример использования
if __name__ == "__main__":
    # Граф представлен в виде словаря, где ключи - вершины, а значения - словари соседей с весами
    graph = {
        'A': {'B': 1, 'C': 4},
        'B': {'A': 1, 'C': 2, 'D': 5},
        'C': {'A': 4, 'B': 2, 'D': 1},
        'D': {'B': 5, 'C': 1}
    }

    start_vertex = 'A'
    distances = dijkstra(graph, start_vertex)

    print(f"Кратчайшие расстояния от вершины {start_vertex}:")
    for vertex, distance in distances.items():
        print(f"До вершины {vertex}: {distance}")
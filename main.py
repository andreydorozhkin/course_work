from typing import Optional, Dict, List
from dijkstra import Dijkstra
from weighted_graph import WeightedGraph
from weighted_edge import WeightedEdge
import sys

WeightedPath = List[WeightedEdge]  # type alias for paths


def default_data():
    city_graph2: WeightedGraph[str] = WeightedGraph(
        ["Seattle", "San Francisco", "Los Angeles", "Riverside", "Phoenix", "Chicago", "Boston", "New York", "Atlanta",
         "Miami", "Dallas", "Houston", "Detroit", "Philadelphia", "Washington"])
    city_graph2.add_edge_by_vertices("Seattle", "Chicago", 1737)
    city_graph2.add_edge_by_vertices("Seattle", "San Francisco", 678)
    city_graph2.add_edge_by_vertices("San Francisco", "Riverside", 386)
    city_graph2.add_edge_by_vertices("San Francisco", "Los Angeles", 348)
    city_graph2.add_edge_by_vertices("Los Angeles", "Riverside", 50)
    city_graph2.add_edge_by_vertices("Los Angeles", "Phoenix", 357)
    city_graph2.add_edge_by_vertices("Riverside", "Phoenix", 307)
    city_graph2.add_edge_by_vertices("Riverside", "Chicago", 1704)
    city_graph2.add_edge_by_vertices("Phoenix", "Dallas", 887)
    city_graph2.add_edge_by_vertices("Phoenix", "Houston", 1015)
    city_graph2.add_edge_by_vertices("Dallas", "Chicago", 805)
    city_graph2.add_edge_by_vertices("Dallas", "Atlanta", 721)
    city_graph2.add_edge_by_vertices("Dallas", "Houston", 225)
    city_graph2.add_edge_by_vertices("Houston", "Atlanta", 702)
    city_graph2.add_edge_by_vertices("Houston", "Miami", 968)
    city_graph2.add_edge_by_vertices("Atlanta", "Chicago", 588)
    city_graph2.add_edge_by_vertices("Atlanta", "Washington", 543)
    city_graph2.add_edge_by_vertices("Atlanta", "Miami", 604)
    city_graph2.add_edge_by_vertices("Miami", "Washington", 923)
    city_graph2.add_edge_by_vertices("Chicago", "Detroit", 238)
    city_graph2.add_edge_by_vertices("Detroit", "Boston", 613)
    city_graph2.add_edge_by_vertices("Detroit", "Washington", 396)
    city_graph2.add_edge_by_vertices("Detroit", "New York", 482)
    city_graph2.add_edge_by_vertices("Boston", "New York", 190)
    city_graph2.add_edge_by_vertices("New York", "Philadelphia", 81)
    city_graph2.add_edge_by_vertices("Philadelphia", "Washington", 123)

    _Path = Dijkstra()
    distances, path_dict = _Path.execute_alg(city_graph2, "Los Angeles")
    name_distance: Dict[str, Optional[int]] = _Path.distance_array_to_vertex_dict(city_graph2, distances)
    print("Расстояние от Los Angeles:")
    for key, value in name_distance.items():
        print(f"{key} : {value}")
    print("")  # blank line

    print("Кратчайшее расстояние от Los Angeles до Boston:")
    path: WeightedPath = _Path.path_dict_to_path(city_graph2.index_of("Los Angeles"), city_graph2.index_of("Boston"),
                                                 path_dict)
    _Path.print_weighted_path(city_graph2, path)


def create_graph() -> WeightedGraph:
    result: list = []
    input_city: str = ''
    while input_city != 'exit':
        print("Введите название вершины: ")
        input_city = input()
        if input_city == 'exit':
            break
        result.append(input_city)
    city_graph: WeightedGraph[str] = WeightedGraph(result)
    return city_graph


def create_edge(graph: WeightedGraph) -> None:
    a: str
    b: str
    weight: float
    print("Введите название вершины 1: ")
    a = input()
    print("Введите название вершины 2: ")
    b = input()
    print("Введите вес ребра: ")
    weight = float(input())
    graph.add_edge_by_vertices(a, b, weight)


def start_dijkstra():
    graph: WeightedGraph = create_graph()
    input_edge: str = ''
    while input_edge != 'exit':
        print("Для выхода напишите exit")
        input_edge = input()
        if input_edge == 'exit': break
        create_edge(graph)
    _Path = Dijkstra()
    print("Введите вершину из которой строить маршруты: ")
    start_point: str = input()
    distances, path_dict = _Path.execute_alg(graph, start_point)
    name_distance: Dict[str, Optional[int]] = _Path.distance_array_to_vertex_dict(graph, distances)
    print(f"Расстояние от {start_point}:")
    for key, value in name_distance.items():
        print(f"{key} : {value}")
    print("")  # blank line
    print("Введите вершину куда строить маршрут: ")
    end_point: str = input()
    print(f"Кратчайшее расстояние от {start_point} до {end_point}:")
    path: WeightedPath = _Path.path_dict_to_path(graph.index_of(start_point), graph.index_of(end_point),
                                                 path_dict)
    _Path.print_weighted_path(graph, path)


if __name__ == "__main__":
    command_line: str = ""
    while command_line != 'exit':
        print("Введите комманду (default): \n 1. create для создания своего графа \n "
              "2. default для использования данных по умолчанию"
              "\n 3. exit для выхода"
              "\n $> ")
        command_line = input()
        if command_line == "default":
            default_data()
        elif command_line == "create":
            start_dijkstra()
        elif command_line == "exit":
            try:
                sys.exit()
            except:
                print("Работы программы завершена")





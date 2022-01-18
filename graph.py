from typing import TypeVar, Generic, List, Optional
from edge import Edge


V = TypeVar('V')  # тип вершин графа


class Graph(Generic[V]):
    def __init__(self, vertices: List[V] = []) -> None:
        self._vertices: List[V] = vertices
        self._edges: List[List[Edge]] = [[] for _ in vertices]

    @property
    def vertex_count(self) -> int:
        return len(self._vertices)  # количество вершин

    @property
    def edge_count(self) -> int:
        return sum(map(len, self._edges))  # количество ребер

    # Add a vertex to the graph and return its index
    def add_vertex(self, vertex: V) -> int:
        self._vertices.append(vertex)
        self._edges.append([])  # добавляет пустой список ребер
        return self.vertex_count - 1  # возвращает индекс вершина

    # Для ненаправленного графа,
    # требуется добавить путь в обоих направлениях
    def add_edge(self, edge: Edge) -> None:
        self._edges[edge.u].append(edge)
        self._edges[edge.v].append(edge.reversed())

    # Добавить ребро, используя индексы вершин
    def add_edge_by_indices(self, u: int, v: int) -> None:
        edge: Edge = Edge(u, v)
        self.add_edge(edge)

    # Добавить ребро между двумя вершины по названию
    def add_edge_by_vertices(self, first: V, second: V) -> None:
        u: int = self._vertices.index(first)
        v: int = self._vertices.index(second)
        self.add_edge_by_indices(u, v)

    # Поиск вершины по индексу
    def vertex_at(self, index: int) -> V:
        return self._vertices[index]

    # Поиск индекса вершины по названию
    def index_of(self, vertex: V) -> int:
        return self._vertices.index(vertex)

    # Поиск вершин, с которыми связана вершина с заданным индексом
    def neighbors_for_index(self, index: int) -> List[V]:
        return list(map(self.vertex_at, [e.v for e in self._edges[index]]))

    # Поиск вершин, с которыми связана вершина для людей)
    def neighbors_for_vertex(self, vertex: V) -> List[V]:
        return self.neighbors_for_index(self.index_of(vertex))

    # Вернуть все ребра связанные с вершиной по индексу
    def edges_for_index(self, index: int) -> List[Edge]:
        return self._edges[index]

    # Вернуть все ребра связанные с вершиной по названию вершины
    def edges_for_vertex(self, vertex: V) -> List[Edge]:
        return self.edges_for_index(self.index_of(vertex))

    # Вывод списков смежности графа
    def __str__(self) -> str:
        desc: str = ""
        for i in range(self.vertex_count):
            desc += f"{self.vertex_at(i)} -> {self.neighbors_for_index(i)}\n"
        return desc



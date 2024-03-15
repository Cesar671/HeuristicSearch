from Search.graph import Node
from Search.state import State
from enum import Enum


class SearchType(Enum):
    MAX_LOCAL = lambda a, b: (a <= b)
    MIN_LOCAL = lambda a, b: (b <= a)


class HeuristicSearch(object):
    def __init__(self):
        self._condition = SearchType.MAX_LOCAL
        self._last_node = None
        self._tolerance = 1000

    @property
    def last_graph(self):
        return self._last_node

    def set_search_by_min_local(self):
        self._condition = SearchType.MIN_LOCAL

    def set_search_by_max_local(self):
        self._condition = SearchType.MAX_LOCAL

    # obtenemos el valor que requerimos segun si buscamos un mximo local o un minimo local
    def _get_best_neighbor(self, current):
        if self._condition == SearchType.MAX_LOCAL:
            return current.largest_neighbor
        elif self._condition == SearchType.MIN_LOCAL:
            return current.smallest_neighbor

    # refinando aun, se me hace fea esa condicional self._condition(a , b)
    def hill_climbing(self, initial: State):
        current: Node = Node(initial)  # creamos el nodo con el problema inicial
        self._last_node = current  # guardamos el nodo para visualizarlo luego
        for i in range(0, self._tolerance):
            current.generate_neighbors()  # recuperamos los estados vecinos del nodo
            best_neighbor = self._get_best_neighbor(current)  # obtenemos el mejor vecino que se adecue a la busqueda
            if ((best_neighbor is None) or
                    self._condition(best_neighbor.content.h,
                                    current.content.h)):  # esta condicional es la que verifica si es maximo o minimo local
                return current.content  # devolvemos el maximo o minimo local encontrado
            current = best_neighbor  # seguimos iterando
        return current.content  # termino de iterar y recuperamos el ultimo estado de la meseta.

from Search.graph import Node
from Search.state import State
from enum import Enum


class SearchType(Enum):
    MAX_LOCAL = lambda a, b: (a <= b)
    MIN_LOCAL = lambda a, b: (b <= a)


class HeuristicSearch(object):
    TOLERANCE = 100

    def __init__(self):
        self._condition = SearchType.MAX_LOCAL
        self._last_node = None

    @property
    def last_graph(self):
        return self._last_node

    def set_search_by_min_local(self):
        self._condition = SearchType.MIN_LOCAL

    def set_search_by_max_local(self):
        self._condition = SearchType.MAX_LOCAL

    def _get_best_neighbor(self, current):
        if self._condition == SearchType.MAX_LOCAL:
            return current.largest_neighbor
        elif self._condition == SearchType.MIN_LOCAL:
            return current.smallest_neighbor

    #refinando aun, se me hace fea esa condicional self._condition(a , b)
    def hill_climbing(self, initial: State):
        current: Node = Node(initial)
        self._last_node = current
        for i in range(0, self.TOLERANCE):
            current.generate_neighbors()
            best_neighbor = self._get_best_neighbor(current)
            if ((best_neighbor is None) or
                    self._condition(best_neighbor.content.h, current.content.h)):
                return current.content
            current = best_neighbor
        return current.content

from Search.graph import Node
from Search.state import State
from enum import Enum


class SearchType(Enum):
    MAX_LOCAL = "MAX LOCAL"
    MIN_LOCAL = "MIN LOCAL"

    def get_conditional(self, a, b):
        if self == self.MAX_LOCAL:
            return a <= b
        elif self == self.MIN_LOCAL:
            return b <= a


class HeuristicSearch(object):
    def __init__(self):
        self._search_type: SearchType = SearchType.MAX_LOCAL
        self._last_node = None
        self._tolerance = 1000

    @property
    def last_graph(self):
        return self._last_node

    def set_search_by_min_local(self):
        self._search_type = SearchType.MIN_LOCAL

    def set_search_by_max_local(self):
        self._search_type = SearchType.MAX_LOCAL

    def _get_best_neighbor(self, current):
        if self._search_type == SearchType.MAX_LOCAL:
            return current.largest_neighbor
        elif self._search_type == SearchType.MIN_LOCAL:
            return current.smallest_neighbor

    def hill_climbing(self, initial: State):
        current = Node(initial)
        self._last_node = current
        for i in range(0, self._tolerance):
            current.generate_neighbors()
            best_neighbor = self._get_best_neighbor(current)
            conditional = self._search_type.get_conditional
            if ((best_neighbor is None) or
                    conditional(best_neighbor.content.h, current.content.h)):
                return current.content
            current = best_neighbor
        return current.content

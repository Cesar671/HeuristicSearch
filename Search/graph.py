
class Node(object):
    def __init__(self, state):
        self._content = state
        self._neighbors = list()
        self._best_neighbor = None
        self._worst_neighbor = None

    @property
    def content(self):
        return self._content

    @property
    def neighbors(self):
        return self._neighbors

    @property
    def largest_neighbor(self):
        return self._best_neighbor

    @property
    def smallest_neighbor(self):
        return self._worst_neighbor

    def generate_neighbors(self):
        states = self._content.get_neighbor_states()
        for i in states:
            self._add_neighbor(Node(i))

    def _add_neighbor(self, target):
        self._neighbors.append(target)

        if self._best_neighbor is None:
            self._best_neighbor = target
        elif self._best_neighbor._content.h < target._content.h:
            self._best_neighbor = target

        if self._worst_neighbor is None:
            self._worst_neighbor = target
        elif self._worst_neighbor._content.h > target._content.h:
            self._worst_neighbor = target









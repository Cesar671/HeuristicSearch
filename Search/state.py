from abc import ABC, abstractmethod


class State(ABC):

    @abstractmethod
    def h(self):
        pass

    @abstractmethod
    def get_neighbor_states(self) -> list:
        pass

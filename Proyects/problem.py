from Search.state import State
import random
import string

class ProblemP(State):

    def __init__(self, name:str):
        super().__init__()
        self._name = name
        self._h = random.randint(10, 100)

    @property
    def name(self):
        return self._name

    #valor del estaado
    @property
    def h(self):
        return self._h

    #obtencion de los estados vecinos
    @staticmethod
    def get_neighbor_states() -> list:
        states = list()
        child_qtty = random.randint(1, 4)
        for i in range(0, child_qtty):
            letters = string.ascii_letters
            name = ''.join(random.choice(letters) for _ in range(4))
            problem = ProblemP(name)
            states.append(problem)
        return states



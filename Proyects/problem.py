from Search.state import State
import random
import string


# Problema de ejemplo, solo debe heredar a State e implementar h y get_neighbor_states
# h devuelve el valor del estado el cual es definido por el usuario
# get_neighbor_states devuelve una lista de todos los estados vecinos definido por el usuaario
class ProblemP(State):

    def __init__(self, name: str):
        self._name = name  # simplemente para darle un ID el cual no es determinante a la hora de resolver
        self._h = random.randint(10, 100)  # establezco un numero aleatorio como valor para el ejemplo

    @property
    def name(self):
        return self._name

    # valor del estado
    @property
    def h(self):
        return self._h

    # obtencion de los estados vecinos
    @staticmethod
    def get_neighbor_states(**kwargs) -> list:
        states = list()
        child_qtty = random.randint(1, 4)
        for i in range(0, child_qtty):
            letters = string.ascii_letters
            name = ''.join(random.choice(letters) for _ in range(4))
            problem = ProblemP(name)
            states.append(problem)
        return states

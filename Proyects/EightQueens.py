from Search.state import State
import random
import string


class ProblemQueen(State):

    def __init__(self, name: str, cells: int, positions=[]):
        self._name = name
        self._cells = cells
        self._queen_positions = positions
        if len(positions) == 0:
            for i in range(0, cells):
                self._queen_positions.append(random.randint(0, 7))

    @property
    def queens_position(self):
        return self._queen_positions

    @property
    def name(self):
        return self._name

    # valor del estado
    @property
    def h(self):
        pairs = 0
        for i in range(0, self._cells):
            # posicion(fila) de la reina en la columna i
            queen_position = self._queen_positions[i]

            # ciclo para contar con que otras reinas se ataca
            for j in range(i + 1, self._cells):
                other_queen_position = self._queen_positions[j]
                # se atacan horizontal
                if queen_position == other_queen_position:
                    pairs += 1
                else:
                    # cálculo de ataques en diagonal

                    # cálculo de la diferencia horizontal (columnas)
                    diff_h = j - i

                    # cálculo de la diferencia vertical (filas / valores de las celdas)
                    diff_v = abs(queen_position - other_queen_position)

                    if diff_h == diff_v:
                        pairs += 1

        return pairs

    # obtencion de los estados vecinos
    def get_neighbor_states(self) -> list:
        states = list()
        for i in range(0, self._cells):
            # posicion(fila) de la reina en la columna i
            queen_position = self._queen_positions[i]

            # ciclo para obtener las opciones de esa reina en las otras filas
            for j in range(0, self._cells):
                # condicion para no repetir el est ado actual
                if j != queen_position:
                    new_state = self._queen_positions.copy()
                    new_state[i] = j
                    letters = string.ascii_letters
                    name = ''.join(random.choice(letters) for _ in range(4))
                    problem_state = ProblemQueen(name, len(new_state), new_state)
                    states.append(problem_state)
        return states

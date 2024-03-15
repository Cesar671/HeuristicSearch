from queue import Queue


class Printer(object):
    def print_graph_values(self, node):
        qu = Queue()
        qu.put(node)
        while not qu.empty():
            current = qu.get()
            neighbors = current.neighbors
            print("Inicio Nodo")
            print(f"""Actual: {current.content.h}     """)
            print("""vecinos: (""", end="")
            for i in neighbors:
                print(f"""{i.content.h} """, end="")
                if len(i.neighbors) > 0:
                    qu.put(i)
            print(""")""", end="")
            print()
            print("fin nodo")

    def print_table_queens(self, state):
        print(f"""State : {state.name}""")
        positions = state.queens_position
        print(f"""positions : {positions} """)
        print(f"""value : {state.h}""")
        size = len(positions)
        for i in range(0, size):
            for j in range(0, size):
                pos_queen = positions[j]
                to_print = "1" if pos_queen == i else "0"
                print(f"""{to_print}  """, end="")
            print()
        print("-" * size * 3)

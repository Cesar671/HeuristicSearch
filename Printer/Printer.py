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

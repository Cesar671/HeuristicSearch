from Proyects.problem import ProblemP
from Search.search import HeuristicSearch
from Printer.Printer import Printer


def main():
    initial_problem = ProblemP("qawe")  # inicializamos el problema que hereda de State
    prnt = Printer()  # inicializamos el printer
    shc = HeuristicSearch()  # inicializamos la clase busqueda
    shc.set_search_by_min_local()  # establecemos que queremos buscar el minimo local
    result = shc.hill_climbing(initial_problem)  # guardamos el estado encontrado
    graph = shc.last_graph  # recuperamos el grafo que creó el buscador
    prnt.print_graph_values(graph)  # usamos el printer para ver el grafo que dibujó
    print(f""" el resultado es :  {result.h} """)  # imprimimos el resultado final


if __name__ == '__main__':
    main()

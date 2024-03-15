from Proyects.problem import ProblemP
from Search.search import HeuristicSearch
from Printer.Printer import Printer


def main():
    initial_problem = ProblemP("qawe")
    prnt = Printer()
    shc = HeuristicSearch()
    shc.set_search_by_min_local()
    result = shc.hill_climbing(initial_problem)
    graph = shc.last_graph
    prnt.print_graph_values(graph)
    print(f""" el resultado es :  {result.h} """)


if __name__ == '__main__':
    main()

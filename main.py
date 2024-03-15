from Proyects.problem import ProblemP
from Search.search import HeuristicSearch
from Printer.Printer import Printer
from Proyects.EightQueens import ProblemQueen


def main():
    initial_problem = ProblemQueen("asd", 8)
    hsc = HeuristicSearch()
    prnt = Printer()

    prnt.print_table_queens(initial_problem)
    hsc.set_search_by_min_local()
    result = hsc.hill_climbing(initial_problem)
    prnt.print_table_queens(result)


if __name__ == '__main__':
    main()

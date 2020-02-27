import os
from time import time

from context import Context

from dfs import DFS
from bfs import BFS
from astar import AStar


def performance(fn):
    """
    Performance decorator that calculates the time needed to execute a function
    :param fn: function to be executed
    :return: execution time
    """

    def wrapper(*args, **kwargs):
        t1 = time()
        result = fn(*args, **kwargs)
        t2 = time()
        if "a" in args[1]:
            print(f'A* took {t2 - t1} seconds.')
        else:
            print(f'{args[1].upper()} took {t2 - t1} seconds.')
        return result

    return wrapper


def touched_to_string(n):
    """
    This function converts a numerical representation of a board tile to an alphanumerical one.

    :param n: string of length 2 where the left is the row and the right is the column
    :return: coordinates on a game board
    """
    return str(chr(int(n[0]) + 65)) + str(int(n[1]) + 1)


@performance
def solve_and_write(context, search_type, ip):
    """
    Solves the inputted puzzles based on a chosen strategy and writes to files.

    :param context: context of the strategy chosen
    :param search_type: string used to differentiate output files
    :param ip: input puzzles
    :return: None
    """
    count = 0
    for i in ip:
        f1 = open(f"{count}_{search_type}_solution.txt", "w")
        f2 = open(f"{count}_{search_type}_search.txt", "w")
        solution = context.find_solution(i, f2)
        f2.close()
        if not solution:
            f1.write("no solution")
            count += 1
            continue
        parent = solution
        solution_path = []
        while parent:
            solution_path.append(parent)
            parent = parent.p
        node = solution_path.pop()
        f1.write("0 " + node.string_v + "\n")
        while solution_path:
            node = solution_path.pop()
            f1.write(touched_to_string(node.touched) + " " + node.string_v + "\n")
        count += 1
        f1.close()


if __name__ == "__main__":
    # Delete previous output files
    old_files = os.listdir('./')
    for item in old_files:
        if item.endswith("search.txt") or item.endswith("solution.txt"):
            os.remove(os.path.join('./', item))

    # Open input files and transform inputs for search methods
    f = open('input.txt', "r")
    puzzles = f.readlines()
    input_puzzles = []

    for puzzle in puzzles:
        # Converts all inputs into ints except the last one
        input_puzzle = [val if idx == 3 else int(val) for idx, val in enumerate(puzzle.strip().split(" "))]
        input_puzzles.append(input_puzzle)
    f.close()

    # Create a search context to allow interchangeable strategies
    search_context = Context(None)

    # Solve using Depth First Search
    search_context.strategy = DFS()
    solve_and_write(search_context, 'dfs', input_puzzles)

    # Solve using Best First Search
    search_context.strategy = BFS()
    solve_and_write(search_context, 'bfs', input_puzzles)

    # Solve using A*
    search_context.strategy = AStar()
    solve_and_write(search_context, 'astar', input_puzzles)

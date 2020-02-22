from context import Context

from dfs import DFS


def touched_to_string(n):
    return str(chr(int(n[0]) + 65)) + str(int(n[1]) + 1)


if __name__ == "__main__":
    # Open input files and transform inputs for search methods

    f = open('input.txt', "r")
    puzzles = f.readlines()
    input_puzzles = []

    for puzzle in puzzles:
        # Converts all inputs into ints except the last one
        input_puzzle = [val if idx == 3 else int(val) for idx, val in enumerate(puzzle.strip().split(" "))]
        input_puzzles.append(input_puzzle)

    f.close()

    # Start the search algorithm and write to files
    count = 0
    context = Context(DFS())
    for i in input_puzzles:
        f1 = open(f"{count}_dfs_solution.txt", "w")
        f2 = open(f"{count}_dfs_search.txt", "w")
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
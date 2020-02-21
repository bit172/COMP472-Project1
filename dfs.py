import numpy as np
from node import Node
from queue import PriorityQueue

f = open('input.txt', "r")

puzzles = f.readlines()
input_puzzles = []

for puzzle in puzzles:
    # Converts all inputs into ints except the last one
    input_puzzle = [val if idx == 3 else int(val) for idx, val in enumerate(puzzle.strip().split(" "))]
    input_puzzles.append(input_puzzle)

f.close()


def touched_to_string(n):
    return str(chr(int(n[0]) + 65)) + str(int(n[1]) + 1)


def dfs(params, search_file):
    initial_board = Node(params[0], params[3])
    goal = np.zeros((params[0], params[0]), dtype=np.uint8)
    max_d = params[1]
    # Open Stack with elements like (current board value, parent, depth)
    open_stack = [(initial_board, 1)]
    closed_set = set()

    while open_stack:
        current = open_stack.pop()
        # adding depth to closed_set
        # closed_set.add((current[0].string_v, current[1]))

        # adding the board only
        closed_set.add(current[0].string_v)
        search_file.write("0 0 0 " + current[0].string_v + "\n")
        depth = current[1] + 1

        if np.array_equal(current[0].v, goal):
            return current[0]

        if depth <= max_d:
            children = current[0].find_children()
            for child in children:
                # checking for the board only
                if child.string_v not in closed_set:
                    # checking for the board and depth
                    # if (child.string_v, depth) not in closed_set:
                    child.p = current[0]
                    open_stack.append((child, depth))


def bfs(params, search_file):
    open_q = PriorityQueue()
    closed = set()
    current = open_q.get()
    length = 0
    max_l = params[2]
    goal = np.zeros((params[0], params[0]), dtype=np.uint8)

    while length <= max_l:
        if current not in closed:
            closed.add(current)
            length += 1
        else:
            continue

        if current == goal:
            return current

        for child in current.find_children():
            newChild = (h(child), child)
            open_q.put(newChild)


def h(x):
    black = 0
    for i in range(Node.n):
        for j in range(Node.n):
            if x[i, j] == 1:
                black += 1
    return black


if __name__ == '__main__':
    count = 0
    for i in input_puzzles:
        f1 = open(f"{count}_dfs_solution.txt", "w")
        f2 = open(f"{count}_dfs_search.txt", "w")
        solution = dfs(i, f2)
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

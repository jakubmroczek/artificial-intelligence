from lib.model.puzzle_plane_history import *
from collections import deque


def generate_neighbour(puzzle_plane):
    return [puzzle_plane.move_down(), puzzle_plane.move_left(), puzzle_plane.move_up(), puzzle_plane.move_right()]


def bfs(puzzle_plane, solved_puzzle_plane):
    puzzle_plane = PuzzlePlaneHistory(puzzle_plane)

    fifo = deque([])
    seed = generate_neighbour(puzzle_plane)
    for s in seed:
        fifo.append(s)
    visited_nodes = set()

    while fifo:
        node = fifo.popleft()

        if node in visited_nodes:
            continue

        visited_nodes.add(node)
        if node.parent == solved_puzzle_plane:
            print("znalezione")
            print(node.moves)
            return node

        # move to distinct functions
        new_nodes = generate_neighbour(node)
        new_nodes = [n for n in new_nodes if n not in visited_nodes]

        # print(node.plane)

        for n in new_nodes:
            fifo.append(n)

    # impossible
    print("the solution does not exist")
    return ""

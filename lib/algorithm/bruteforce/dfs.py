from lib.model.puzzle_plane_history import *

#todo code duplication as in bs
def generate_neighbour(puzzle_plane):
    return [puzzle_plane.move_down(), puzzle_plane.move_left(), puzzle_plane.move_up(), puzzle_plane.move_right()]


def dfs(puzzle_plane, solved_puzzle_plane):
    puzzle_plane = PuzzlePlaneHistory(puzzle_plane)

    stack = []
    seed = generate_neighbour(puzzle_plane)
    for s in seed:
        stack.append(s)
    visited_nodes = set()

    while stack:
        node = stack.pop()

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

        for n in new_nodes:
            stack.append(n)

    # impossible
    return ""

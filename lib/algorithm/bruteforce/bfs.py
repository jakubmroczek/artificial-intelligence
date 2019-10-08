import queue


def generate_neighbour(puzzle_plane):
    return [puzzle_plane.move_down(), puzzle_plane.move_up(), puzzle_plane.move_right(), puzzle_plane.move_left()]


def bfs(puzzle_plane, solved_puzzle_plane):
    neighbours = queue.Queue()
    neighbours.put(generate_neighbour(puzzle_plane))
    visited_nodes = set()

    while not neighbours.empty():
        node = neighbours.get()
        if node == solved_puzzle_plane:
            return node

        # move to distinct functions
        new_nodes = generate_neighbour(node)
        new_nodes = [n for n in new_nodes if n not in visited_nodes]

        neighbours.put(new_nodes)

    # impossible
    raise Exception

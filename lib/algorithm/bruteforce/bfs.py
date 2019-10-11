import queue


def generate_neighbour(puzzle_plane):
    return [puzzle_plane.move_down(), puzzle_plane.move_left(), puzzle_plane.move_up(), puzzle_plane.move_right()]


def bfs(puzzle_plane, solved_puzzle_plane):
    neighbours = queue.Queue()
    seed = generate_neighbour(puzzle_plane)
    for s in seed:
        neighbours.put(s)
    visited_nodes = set()

    while not neighbours.empty():
        node = neighbours.get()

        if node in visited_nodes:
            continue

        visited_nodes.add(node)
        if node == solved_puzzle_plane:
            print("znalezione")
            return node

        # move to distinct functions
        new_nodes = generate_neighbour(node)
        new_nodes = [n for n in new_nodes if n not in visited_nodes]

        # print(node.plane)

        for n in new_nodes:
            neighbours.put(n)

    # impossible
    raise Exception

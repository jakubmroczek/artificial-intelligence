from lib.model.puzzle_plane_history import *
from lib.algorithm.bruteforce.neighbor_search_strategy import *
from collections import deque


def bfs(puzzle_plane, solved_puzzle_plane, neighbor_search_strategy=RandomNeighborSearchStrategy()):
    fifo = deque([])
    seed = neighbor_search_strategy.neighbors(PuzzlePlaneHistory(puzzle_plane))
    for s in seed:
        fifo.append(s)
    visited_nodes = set()

    while fifo:
        node = fifo.popleft()

        if node in visited_nodes:
            continue

        visited_nodes.add(node)

        if node.parent == solved_puzzle_plane:
            return node

        new_nodes = neighbor_search_strategy.neighbors(node)
        new_nodes = [n for n in new_nodes if n not in visited_nodes]

        for n in new_nodes:
            fifo.append(n)

    return PuzzlePlaneHistory(puzzle_plane)

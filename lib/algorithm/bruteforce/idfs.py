from lib.algorithm.bruteforce.neighbor_search_strategy import RandomNeighborSearchStrategy
from lib.model.puzzle_plane_history import PuzzlePlaneHistory
import math


def idfs(puzzle_plane, solved_puzzle_plane, neighbor_search_strategy=RandomNeighborSearchStrategy()):
    """
    Iterative deepening DFS.
    :param puzzle_plane: shuffled puzzle plane.
    :param solved_puzzle_plane: the puzzle plane to be transformed from the shuffled one.
    :param neighbor_search_strategy: a strategy which determines the order in which neighbors are visted.
    """
    print(max_depth(puzzle_plane))
    depth = max_depth(puzzle_plane)
    puzzle_plane = PuzzlePlaneHistory(puzzle_plane)
    for i in range(0, depth + 1):
        result = dls(puzzle_plane, solved_puzzle_plane, i, neighbor_search_strategy)
        if result:
            return result


def dls(puzzle_plane, solved_puzzle_plane, depth, neighbor_search_strategy=RandomNeighborSearchStrategy()):
    print(puzzle_plane.parent.plane)
    if puzzle_plane == solved_puzzle_plane:
        #todo: .parent destroys the Liskov principle, imporve __eq__ int PuzzlePlaneHistory
        return puzzle_plane.parent == solved_puzzle_plane

    if depth == 0:
        return None

    for child in neighbor_search_strategy.neighbors(puzzle_plane):
        result = dls(child, solved_puzzle_plane, depth - 1, neighbor_search_strategy)
        if result:
            return result


def max_depth(puzzle_plane):
    # It is not true, because sometimes there is no possible to solve the riddle I assume that the tree is well
    # balanced and that the total number of children equals to the all possible permutations but it is not true (
    # bigger than in reality)
    number_of_elements = puzzle_plane.row_n * puzzle_plane.column_n
    depth = math.log(3, 4) + 1
    for i in range(1, number_of_elements + 1):
        depth += math.log(i, 4)
    return math.ceil(depth)

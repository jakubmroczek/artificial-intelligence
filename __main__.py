from itertools import permutations

from lib.algorithm.bruteforce.dfs import dfs
from lib.algorithm.bruteforce.idfs import idfs
from lib.model.puzzle_plane import *
from lib.algorithm.bruteforce.bfs import bfs
from lib.algorithm.bruteforce.neighbor_search_strategy import RandomNeighborSearchStrategy, \
    StrictNeighborSearchStrategy, Move
import argparse


def create_neighbors_visiting_strategy(key):
    if key == "R":
        return RandomNeighborSearchStrategy()
    else:
        #todo: fix me!
        # return StrictNeighborSearchStrategy([Move[s] for s in list(key)])
        return RandomNeighborSearchStrategy()

def cli():
    parser = argparse.ArgumentParser(description="solve fifteen puzzle riddle using various techniques")
    parser.add_argument("-g", "--gui", action="store_true", help="runs program with the graphical interface")
    parser.add_argument("-r", "--random", action="store_true", help="the content of the puzzle plane riddle is "
                                                                    "auto generated")

    group = parser.add_mutually_exclusive_group()
    # TODO code duplication here, and the default equals to R is a magic constant
    allowed_order = ["".join(p) for p in permutations("DULR")].append("R")
    group.add_argument("-b", "--bfs", help="", type=str, choices=allowed_order)
    group.add_argument("-d", "--dfs", help="", type=str, choices=allowed_order)
    group.add_argument("-i", "--idfs", help="", type=str, choices=allowed_order)

    parser.add_argument("rows", type=int, help="the number of rows in the puzzle plane")
    parser.add_argument("columns", type=int, help="the number of columns in the puzzle plane")

    args = parser.parse_args()

    if args.random:
        riddle = generate_random_puzzle_plane(args.rows, args.columns)
        print(riddle.plane)
    else:
        raise Exception("implement user provided riddle")

    solution = generate_ordered_puzzle_plane(args.rows, args.columns)
    if args.bfs:
        result = bfs(riddle, solution, create_neighbors_visiting_strategy(args.bfs))
        print(len(result.moves))
        print(result.moves)
    elif args.dfs:
        result = dfs(riddle, solution, create_neighbors_visiting_strategy(args.dfs))
        print(len(result.moves))
        print(result.moves)
    elif args.idfs:
        #does not work yet
        result = idfs(riddle, solution, create_neighbors_visiting_strategy(args.dfs))
        # result can be of type None, or PuzzlePlaneHistory, so this should be unified
        if result:
            print(len(result.moves))
            print(result.moves)


if __name__ == '__main__':
    cli()

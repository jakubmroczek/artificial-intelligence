from lib.model.puzzle_plane import *
from lib.algorithm.bruteforce.bfs import bfs
from lib.algorithm.bruteforce.neighbor_search_strategy import *
import argparse


def cli():
    parser = argparse.ArgumentParser(description="solve fifteen puzzle riddle using various techniques")
    parser.add_argument("-g", "--gui", action="store_true", help="runs program with the graphical interface")
    parser.add_argument("-r", "--random", action="store_true", help="the content of the puzzle plane riddle is "
                                                                    "auto generated")

    group = parser.add_mutually_exclusive_group()
    group.add_argument("-b", "--bfs", help="", action="store_true")
    group.add_argument("-d", "--dfs", help="")

    parser.add_argument("rows", type=int, help="the number of rows in the puzzle plane")
    parser.add_argument("columns", type=int, help="the number of columns in the puzzle plane")

    args = parser.parse_args()

    if args.random:
        riddle = generate_random_puzzle_plane(args.rows, args.columns)
        print(riddle.plane)
    else:
        riddle = []
        raise Exception("implement user provided riddle")

    solution = generate_ordered_puzzle_plane(args.rows, args.columns)
    if args.bfs:
        result = bfs(riddle, solution)
        print(len(result.moves))
        print(result.moves)
    elif args.dfs:
        result = dfs(riddle, solution)
        print(result)


if __name__ == '__main__':
    cli()

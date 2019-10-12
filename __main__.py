from lib.model.puzzle_plane import *
from lib.algorithm.bruteforce.bfs import bfs
from lib.algorithm.bruteforce.neighbor_search_strategy import *
import argparse


def cli():
    pass
    # parser = ar


def main():
    row, columns = 3, 3
    riddle = generate_random_puzzle_plane(row, columns)
    solution = generate_ordered_puzzle_plane(row, columns)
    print(riddle.plane)
    print(riddle.empty_element_index)
    print(solution.plane)
    print(solution.empty_element_index)
    result = bfs(riddle, solution)
    print(len(result.moves))
    print(result.moves)


if __name__ == '__main__':
    main()

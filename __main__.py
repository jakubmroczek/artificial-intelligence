from lib.model.puzzle_plane import *
from lib.algorithm.bruteforce.bfs import bfs
from lib.algorithm.bruteforce.neighbor_search_strategy import *

def main():
    row, columns = 3, 3
    riddle = generate_random_puzzle_plane(row, columns)
    solution = generate_ordered_puzzle_plane(row, columns)
    print(riddle.plane)
    print(riddle.empty_element_index)
    print(solution.plane)
    print(solution.empty_element_index)
    bfs(riddle, solution)


if __name__ == '__main__':
    main()
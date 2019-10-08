from lib.model.puzzle_plane import *
from lib.algorithm.bruteforce import bfs

def main():
    data = generate_random_array()
    puzzle_plain = PuzzlePlane(data[0], data[1])
    print(puzzle_plain.plane)
    print(puzzle_plain.move_right().plane)
    print(puzzle_plain.move_right().move_right().plane)
    print(puzzle_plain.move_right().move_right().move_right().plane)
    print(puzzle_plain.move_right().move_right().move_right().move_right().plane)
    print(puzzle_plain.plane)

main()
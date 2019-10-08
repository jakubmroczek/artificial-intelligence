from lib.model.puzzle_plane import PuzzlePlane
from lib.algorithm.bruteforce import bfs

def main():
    puzzle_plain = PuzzlePlane()
    result = bfs(puzzle_plain)
    print(result)

main()
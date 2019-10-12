from lib.model.puzzle_plane import *
from lib.algorithm.bruteforce.bfs import bfs


def main():
    size  = 3
    solution = []
    for i in range(0, size):
        row = []
        for j in range(i * size, i * size  + size):
            row.append(j)
        solution.append(row)

    #enacpuslte it
    data = generate_random_array(size)
    # foo = [[1,2,3,0], [4,5,6,7], [8,9,10,11], [12,13,14,15]]
    riddle = PuzzlePlane(data[0], data[1])
    # riddle = PuzzlePlane(foo, [0, 3])
    # solution = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 0]]
    # print(solution)
    print(riddle.plane)
    bfs(riddle, PuzzlePlane(solution, [0, 0]))

if __name__ == '__main__':
    main()

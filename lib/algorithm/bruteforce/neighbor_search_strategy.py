from abc import ABC
import random


class NeighborSearchStrategy(ABC):
    def neighbors(self, puzzle_plane):
        raise NotImplementedError('neighbors method not defined')


class RandomNeighborSearchStrategy(NeighborSearchStrategy):

    def neighbors(self, puzzle_plane):
        neighbors = [puzzle_plane.move_down(), puzzle_plane.move_left(), puzzle_plane.move_up(), puzzle_plane.move_right()]
        random.shuffle(neighbors)
        return neighbors

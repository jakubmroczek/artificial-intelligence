from abc import ABC
from enum import Enum
import random


class NeighborSearchStrategy(ABC):
    def neighbors(self, puzzle_plane):
        raise NotImplementedError('neighbors method not defined')


class RandomNeighborSearchStrategy(NeighborSearchStrategy):

    def neighbors(self, puzzle_plane):
        neighbors = [puzzle_plane.move_down(), puzzle_plane.move_left(), puzzle_plane.move_up(),
                     puzzle_plane.move_right()]
        random.shuffle(neighbors)
        return neighbors


class Move(Enum):
    UP = 0,
    DOWN = 1,
    LEFT = 2,
    RIGHT = 3


class StrictNeighborSearchStrategy(NeighborSearchStrategy):
    transforms = {Move.UP: lambda puzzle_plain: puzzle_plain.move_up(),
                  Move.DOWN: lambda puzzle_plain: puzzle_plain.move_down(),
                  Move.LEFT: lambda puzzle_plain: puzzle_plain.move_left(),
                  Move.RIGHT: lambda puzzle_plain: puzzle_plain.move_right()}

    """
        Pass here a list of moves e.g UP, DOWN, LEFT, RIGHT to follow
        :param order list of Move enum
    """

    def __init__(self, order):
        self.order = order

    def neighbors(self, puzzle_plane):
        return map(lambda move : self.transforms.get(move)(puzzle_plane), self.order)

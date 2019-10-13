from abc import ABC
import random
from enum import Enum


class NeighborSearchStrategy(ABC):
    def neighbors(self, puzzle_plane):
        raise NotImplementedError('neighbors method not defined')


class RandomNeighborSearchStrategy(NeighborSearchStrategy):

    def neighbors(self, puzzle_plane):
        neighbors = [puzzle_plane.move_down(), puzzle_plane.move_left(), puzzle_plane.move_up(),
                     puzzle_plane.move_right()]
        random.shuffle(neighbors)
        return neighbors


# todo: no one usess it, it is internal dependency of the StrictNeighborSearch class. move it there
class Move(Enum):
    # Up
    U = 'U',
    # Down
    D = 'D',
    # Left
    L = 'L',
    # Right
    R = 'R'


class StrictNeighborSearchStrategy(NeighborSearchStrategy):
    transforms = {Move.U: lambda puzzle_plain: puzzle_plain.move_up(),
                  Move.D: lambda puzzle_plain: puzzle_plain.move_down(),
                  Move.L: lambda puzzle_plain: puzzle_plain.move_left(),
                  Move.R: lambda puzzle_plain: puzzle_plain.move_right()}

    """
        Pass here a list of moves e.g UP, DOWN, LEFT, RIGHT to follow
        :param order list of Move enum
    """

    def __init__(self, order):
        self.order = order

    def neighbors(self, puzzle_plane):
        return map(lambda move: self.transforms.get(move)(puzzle_plane), self.order)

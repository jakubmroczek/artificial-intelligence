from lib.model.puzzle_plane import PuzzlePlane
import copy


# todo needs some improvements, is plane avaliable in PuzzlePlane history, dummy in python inheritance
# decorator design pattern
class PuzzlePlaneHistory(PuzzlePlane):

    def __init__(self, puzzle_plane, moves=[]):
        self.moves = moves
        self.parent = puzzle_plane

    def __eq__(self, o: object) -> bool:
        if not isinstance(o, PuzzlePlaneHistory):
            return False
        return self.parent.__eq__(o.parent)

    def __hash__(self) -> int:
        return self.parent.__hash__()

    def move_up(self):
        puzzle_plane = self.parent.move_up()
        if puzzle_plane is not self.parent:
            # TODO Move it to some enum
            self.moves.append("UP")
        return PuzzlePlaneHistory(puzzle_plane, copy.deepcopy(self.moves))

    def move_down(self):
        puzzle_plane = self.parent.move_down()
        if puzzle_plane is not self.parent:
            # todo enum
            self.moves.append("DOWN")
        return PuzzlePlaneHistory(puzzle_plane, copy.deepcopy(self.moves))

    def move_right(self):
        puzzle_plane = self.parent.move_right()
        if puzzle_plane is not self.parent:
            # todo enum
            self.moves.append("RIGHT")
        return PuzzlePlaneHistory(puzzle_plane, copy.deepcopy(self.moves))

    def move_left(self):
        puzzle_plane = self.parent.move_left()
        if puzzle_plane is not self.parent:
            # todo enum
            self.moves.append("LEFT")
        return PuzzlePlaneHistory(puzzle_plane, copy.deepcopy(self.moves))

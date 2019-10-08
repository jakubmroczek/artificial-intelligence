import random, copy


def generate_random_array():
    empty_element = 0
    plane = []

    # todo: remove magic numbers
    numbers = []
    for n in range(0, 16):
        numbers.append(n)

    random.shuffle(numbers)

    # todo: move to distinct function
    start = 0
    begin = 4

    # getting indices of the empty element
    empty_element_index = numbers.index(empty_element)
    empty_element_index = [int(empty_element_index / 4), int(empty_element_index % 4)]

    while begin <= 16:
        plane.append(numbers[start:begin])
        start += 4
        begin += 4
    return [plane, empty_element_index]


class PuzzlePlane:
    empty_element = 0

    """Pupulates the plane with provided data"""
    """plane is a 2D arrays numbers ranging from 0 to 15 exclusive"""

    def __init__(self, plane, empty_element_index):
        self.plane = plane
        self.empty_element_index = empty_element_index

    def empty_element_index(self):
        return self.empty_element_index

    # return a new PuzzlePlane with the whole move upward
    # if the move was not possible a copy of the original PuzzlePlane is returne
    def move_down(self):
        copied_plane = copy.deepcopy(self.plane)
        new_empty_element_index = [0, 0]
        # rows
        # todo: bad magic numbers
        if self.empty_element_index[0] != 3:
            new_empty_element_index = [self.empty_element_index[0] + 1, self.empty_element_index[1]]
            copied_plane[self.empty_element_index[0]][self.empty_element_index[1]], \
            copied_plane[new_empty_element_index[0]][new_empty_element_index[1]] = \
                copied_plane[new_empty_element_index[0]][new_empty_element_index[1]], \
                copied_plane[self.empty_element_index[0]][self.empty_element_index[1]]

        return PuzzlePlane(copied_plane, new_empty_element_index)

    def move_up(self):
        copied_plane = copy.deepcopy(self.plane)
        new_empty_element_index = [0, 0]
        # rows
        # todo: bad magic numbers
        if self.empty_element_index[0] != 0:
            new_empty_element_index = [self.empty_element_index[0] - 1, self.empty_element_index[1]]
            copied_plane[self.empty_element_index[0]][self.empty_element_index[1]], \
            copied_plane[new_empty_element_index[0]][new_empty_element_index[1]] = \
                copied_plane[new_empty_element_index[0]][new_empty_element_index[1]], \
                copied_plane[self.empty_element_index[0]][self.empty_element_index[1]]

        return PuzzlePlane(copied_plane, new_empty_element_index)

    def move_right(self):
        copied_plane = copy.deepcopy(self.plane)
        new_empty_element_index = [0, 0]
        # rows
        # todo: bad magic numbers
        if self.empty_element_index[1] != 3:
            new_empty_element_index = [self.empty_element_index[0], self.empty_element_index[1] + 1]
            copied_plane[self.empty_element_index[0]][self.empty_element_index[1]], \
            copied_plane[new_empty_element_index[0]][new_empty_element_index[1]] = \
                copied_plane[new_empty_element_index[0]][new_empty_element_index[1]], \
                copied_plane[self.empty_element_index[0]][self.empty_element_index[1]]

        return PuzzlePlane(copied_plane, new_empty_element_index)

    def move_left(self):
        copied_plane = copy.deepcopy(self.plane)
        new_empty_element_index = [0, 0]
        # rows
        # todo: bad magic numbers
        if self.empty_element_index[1] != 0:
            new_empty_element_index = [self.empty_element_index[0], self.empty_element_index[1] - 1]
            copied_plane[self.empty_element_index[0]][self.empty_element_index[1]], \
            copied_plane[new_empty_element_index[0]][new_empty_element_index[1]] = \
                copied_plane[new_empty_element_index[0]][new_empty_element_index[1]], \
                copied_plane[self.empty_element_index[0]][self.empty_element_index[1]]

        return PuzzlePlane(copied_plane, new_empty_element_index)

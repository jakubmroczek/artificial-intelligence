import random, copy


def generate_ordered_puzzle_plane(row, column):
    """
       Creates a PuzzlePlane of a size row x column with ordered numbers in range <0, row x column)
       :param row: numbers of rows.
       :param column: numbers of columns.
       :return: ordered PuzzlePlane
       """
    plane = []
    size = row * column
    empty_element_index = [0, 0]

    # Generating ordered numbers list
    numbers = []
    for n in range(0, size):
        numbers.append(n)

    # Getting a index of an empty_element
    start = 0
    begin = row

    # Creating a 2D plane from 1D
    while begin <= row * column:
        plane.append(numbers[start:begin])
        start += row
        begin += row

    return PuzzlePlane(plane, empty_element_index)


def generate_random_puzzle_plane(row, column):
    """
    Creates a PuzzlePlane of a size row x column with random shuffled numbers in range <0, row x column)
    :param row: numbers of rows.
    :param column: numbers of columns.
    :return: a shuffled PuzzlePlane
    """
    empty_element = 0
    plane = []
    size = row * column

    # Generating ordered numbers list
    numbers = []
    for n in range(0, size):
        numbers.append(n)

    random.shuffle(numbers)

    # Getting a index of an empty_element
    empty_element_index = numbers.index(empty_element)
    empty_element_index = [int(empty_element_index / row), int(empty_element_index % row)]

    start = 0
    begin = row

    # Creating a 2D plane from 1D
    while begin <= row * column:
        plane.append(numbers[start:begin])
        start += row
        begin += row

    return PuzzlePlane(plane, empty_element_index)


"""
    Representation of the puzzle problem domain.
    Allows to easily move elements around.
"""


class PuzzlePlane:
    """Pupulates the plane with provided data"""
    """plane is a 2D arrays numbers ranging from 0 to 15 exclusive"""

    def __init__(self, plane, empty_element_index):
        self.plane = plane
        self.empty_element_index = empty_element_index
        self.row_n = len(plane)
        self.column_n = len(plane[0])

    def __eq__(self, o: object) -> bool:
        if not isinstance(o, PuzzlePlane):
            return False

        hsh = "".join(str(x) for x in self.plane)
        other_hsh = "".join(str(x) for x in o.plane)
        return hsh == other_hsh

    def __hash__(self) -> int:
        # todo: fix me
        hsh = "".join(str(x) for x in self.plane)
        return hash(hsh)

    """
        Moves the "hole" down, if possible and returns new PuzzlePlane.
        Otherwise the original object is returned.
    """

    def move_down(self):
        if self.empty_element_index[0] != self.row_n - 1:
            moved_puzzle_plane = copy.deepcopy(self)
            new_empty_element_index = [self.empty_element_index[0] + 1, self.empty_element_index[1]]
            moved_puzzle_plane.empty_element_index = new_empty_element_index
            return moved_puzzle_plane.swap(self.empty_element_index, new_empty_element_index)
        else:
            return self

    """
           Moves the "hole" up, if possible and returns new PuzzlePlane.
           Otherwise the original object is returned.
       """

    def move_up(self):
        if self.empty_element_index[0] != 0:
            moved_puzzle_plane = copy.deepcopy(self)
            new_empty_element_index = [self.empty_element_index[0] - 1, self.empty_element_index[1]]
            moved_puzzle_plane.empty_element_index = new_empty_element_index
            return moved_puzzle_plane.swap(self.empty_element_index, new_empty_element_index)
        else:
            return self

    """
            Moves the "hole" right, if possible and returns new PuzzlePlane.
            Otherwise the original object is returned.
    """

    def move_right(self):
        if self.empty_element_index[1] != self.column_n - 1:
            moved_puzzle_plane = copy.deepcopy(self)
            new_empty_element_index = [self.empty_element_index[0], self.empty_element_index[1] + 1]
            moved_puzzle_plane.empty_element_index = new_empty_element_index
            return moved_puzzle_plane.swap(self.empty_element_index, new_empty_element_index)
        else:
            return self

    """
            Moves the "hole" left, if possible and returns new PuzzlePlane.
            Otherwise the original object is returned.    
    """

    def move_left(self):
        if self.empty_element_index[1] != 0:
            moved_puzzle_plane = copy.deepcopy(self)
            new_empty_element_index = [self.empty_element_index[0], self.empty_element_index[1] - 1]
            moved_puzzle_plane.empty_element_index = new_empty_element_index
            return moved_puzzle_plane.swap(self.empty_element_index, new_empty_element_index)
        else:
            return self

    """
            Helper function for swapping elements in the PuzzlePlane.
            Element at first_index goes under the second_index, and second_index goes under the first_index
    """

    def swap(self, first_index, second_index):
        self.plane[first_index[0]][first_index[1]], \
        self.plane[second_index[0]][second_index[1]] = \
            self.plane[second_index[0]][second_index[1]], \
            self.plane[first_index[0]][first_index[1]]
        return self

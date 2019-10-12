import random, copy

"""
    Generates a plane with size of rows x columns = size x size
"""


def generate_random_array(size):
    empty_element = 0
    plane = []

    numbers = []
    for n in range(0, size ** 2):
        numbers.append(n)

    random.shuffle(numbers)

    # todo: move to distinct function
    start = 0
    begin = size

    # getting indices of the empty element
    empty_element_index = numbers.index(empty_element)
    empty_element_index = [int(empty_element_index / size), int(empty_element_index % size)]

    while begin <= size ** 2:
        plane.append(numbers[start:begin])
        start += size
        begin += size
    return [plane, empty_element_index]


"""
    Representation of the puzzle problem domain.
    Allows to easily move elements around.
"""


class PuzzlePlane:
    empty_element = 0

    """Pupulates the plane with provided data"""
    """plane is a 2D arrays numbers ranging from 0 to 15 exclusive"""

    def __init__(self, plane, empty_element_index):
        self.plane = plane
        self.empty_element_index = empty_element_index

    def __eq__(self, o: object) -> bool:
        if not isinstance(o, PuzzlePlane):
            return False

        hsh = "".join(str(x) for x in self.plane)
        other_hsh = "".join(str(x) for x in o.plane)
        return hsh == other_hsh

    def __hash__(self) -> int:
        # todo: fix me
        hsh = "".join(str(x) for x in self.plane);
        return hash(hsh)

    """
        Moves the "hole" down, if possible and returns new PuzzlePlane.
        Otherwise the original object is returned.
    """

    def move_down(self):
        if self.empty_element_index[0] != len(self.plane) - 1:
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
        if self.empty_element_index[1] != len(self.plane) - 1:
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

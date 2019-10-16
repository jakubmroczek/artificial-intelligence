import unittest
from lib.model.puzzle_plane import PuzzlePlane


class TestPuzzlePlane(unittest.TestCase):
    def test_eq(self):
        left = PuzzlePlane([[7, 0, 4], [6, 3, 5], [8, 1, 2]], [0, 1])
        right = PuzzlePlane([[7, 0, 4], [6, 3, 5], [8, 1, 2]], [0, 1])

        self.assertTrue(left == right)

    def test_not_eq(self):
        left = PuzzlePlane([[0, 7, 4], [6, 3, 5], [8, 1, 2]], [0, 0])
        right = PuzzlePlane([[7, 0, 4], [6, 3, 5], [8, 1, 2]], [0, 1])

        self.assertFalse(left == right)

    def test_move_up_with_zero_in_top(self):
        plane = [[7, 0, 4], [6, 3, 5], [8, 1, 2]]
        empty_element_index = [0, 1]

        puzzle_plane = PuzzlePlane(plane, empty_element_index)
        sut = puzzle_plane.move_up()

        self.assertIs(puzzle_plane, sut)
        self.assertEqual([[7, 0, 4], [6, 3, 5], [8, 1, 2]], sut.plane)
        self.assertEqual([0, 1], sut.empty_element_index)

    def test_move_up_with_zero_in_middle(self):
        plane = [[7, 3, 4], [6, 0, 5], [8, 1, 2]]
        empty_element_index = [1, 1]

        puzzle_plane = PuzzlePlane(plane, empty_element_index)
        sut = puzzle_plane.move_up()

        self.assertIsNot(sut, puzzle_plane)
        self.assertEqual([[7, 0, 4], [6, 3, 5], [8, 1, 2]], sut.plane)
        self.assertEqual([0, 1], sut.empty_element_index)

    def test_move_up_with_zero_in_bottom(self):
        plane = [[7, 3, 4], [6, 1, 5], [8, 0, 2]]
        empty_element_index = [2, 1]

        puzzle_plane = PuzzlePlane(plane, empty_element_index)
        sut = puzzle_plane.move_up()

        self.assertIsNot(sut, puzzle_plane)
        self.assertEqual([[7, 3, 4], [6, 0, 5], [8, 1, 2]], sut.plane)
        self.assertEqual([1, 1], sut.empty_element_index)

    def test_move_down_with_zero_in_top(self):
        plane = [[7, 0, 4], [6, 3, 5], [8, 1, 2]]
        empty_element_index = [0, 1]

        puzzle_plane = PuzzlePlane(plane, empty_element_index)
        sut = puzzle_plane.move_down()

        self.assertIsNot(puzzle_plane, sut)
        self.assertEqual([[7, 3, 4], [6, 0, 5], [8, 1, 2]], sut.plane)
        self.assertEqual([1, 1], sut.empty_element_index)

    def test_move_down_with_zero_in_middle(self):
        plane = [[7, 3, 4], [6, 0, 5], [8, 1, 2]]
        empty_element_index = [1, 1]

        puzzle_plane = PuzzlePlane(plane, empty_element_index)
        sut = puzzle_plane.move_down()

        self.assertIsNot(sut, puzzle_plane)
        self.assertEqual([[7, 3, 4], [6, 1, 5], [8, 0, 2]], sut.plane)
        self.assertEqual([2, 1], sut.empty_element_index)

    def test_move_down_with_zero_in_bottom(self):
        plane = [[7, 3, 4], [6, 1, 5], [8, 0, 2]]
        empty_element_index = [2, 1]

        puzzle_plane = PuzzlePlane(plane, empty_element_index)
        sut = puzzle_plane.move_down()

        self.assertIs(sut, puzzle_plane)
        self.assertEqual([[7, 3, 4], [6, 1, 5], [8, 0, 2]], sut.plane)
        self.assertEqual([2, 1], sut.empty_element_index)

    def test_move_left_with_zero_on_left(self):
        plane = [[0, 3, 4], [6, 1, 5], [8, 7, 2]]
        empty_element_index = [0, 0]

        puzzle_plane = PuzzlePlane(plane, empty_element_index)
        sut = puzzle_plane.move_left()

        self.assertIs(puzzle_plane, sut)
        self.assertEqual([[0, 3, 4], [6, 1, 5], [8, 7, 2]], sut.plane)
        self.assertEqual([0, 0], sut.empty_element_index)

    def test_move_left_with_zero_in_middle(self):
        plane = [[3, 0, 4], [6, 1, 5], [8, 7, 2]]
        empty_element_index = [0, 1]

        puzzle_plane = PuzzlePlane(plane, empty_element_index)
        sut = puzzle_plane.move_left()

        self.assertIsNot(puzzle_plane, sut)
        self.assertEqual([[0, 3, 4], [6, 1, 5], [8, 7, 2]], sut.plane)
        self.assertEqual([0, 0], sut.empty_element_index)

    def test_move_left_with_zero_on_right(self):
        plane = [[3, 4, 0], [6, 1, 5], [8, 7, 2]]
        empty_element_index = [0, 2]

        puzzle_plane = PuzzlePlane(plane, empty_element_index)
        sut = puzzle_plane.move_left()

        self.assertIsNot(puzzle_plane, sut)
        self.assertEqual([[3, 0, 4], [6, 1, 5], [8, 7, 2]], sut.plane)
        self.assertEqual([0, 1], sut.empty_element_index)

    def test_move_right_with_zero_on_right(self):
        plane = [[3, 4, 0], [6, 1, 5], [8, 7, 2]]
        empty_element_index = [0, 2]

        puzzle_plane = PuzzlePlane(plane, empty_element_index)
        sut = puzzle_plane.move_right()

        self.assertIs(puzzle_plane, sut)
        self.assertEqual([[3, 4, 0], [6, 1, 5], [8, 7, 2]], sut.plane)
        self.assertEqual([0, 2], sut.empty_element_index)

    def test_move_right_with_zero_in_middle(self):
        plane = [[3, 0, 4], [6, 1, 5], [8, 7, 2]]
        empty_element_index = [0, 1]

        puzzle_plane = PuzzlePlane(plane, empty_element_index)
        sut = puzzle_plane.move_right()

        self.assertIsNot(puzzle_plane, sut)
        self.assertEqual([[3, 4, 0], [6, 1, 5], [8, 7, 2]], sut.plane)
        self.assertEqual([0, 2], sut.empty_element_index)

    def test_move_right_with_zero_on_left(self):
        plane = [[0, 3, 4], [6, 1, 5], [8, 7, 2]]
        empty_element_index = [0, 0]

        puzzle_plane = PuzzlePlane(plane, empty_element_index)
        sut = puzzle_plane.move_right()

        self.assertIsNot(puzzle_plane, sut)
        self.assertEqual([[3, 0, 4], [6, 1, 5], [8, 7, 2]], sut.plane)
        self.assertEqual([0, 1], sut.empty_element_index)

    def test_constructor(self):
        plane = [[3, 0, 4], [6, 1, 5], [8, 7, 2]]
        empty_element_index = [0, 1]

        sut = PuzzlePlane(plane, empty_element_index)
        self.assertIs(plane, sut.plane)
        self.assertEqual(empty_element_index, sut.empty_element_index)


if __name__ == '__main__':
    unittest.main()

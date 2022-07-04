import unittest

from task_01 import search_zero_index, rectangles


class Task01TestCase(unittest.TestCase):

    def test_search_zero_index_01(self):
        data = "111111111110000000000000000"
        result = search_zero_index(data)
        self.assertEqual(result, 11)

    def test_search_zero_index_02(self):
        data = "00000000000000001"
        result = search_zero_index(data)
        self.assertEqual(result, 0)

    def test_search_zero_index_03(self):
        data = "1100000000000000001"
        result = search_zero_index(data)
        self.assertEqual(result, 2)

    def test_rectangles_01(self):
        points = [1, 1, 2, 2, 3, 3, 4, 4]
        result = rectangles(*points)
        self.assertEqual(result, False)

    def test_rectangles_02(self):
        points = [1, 1, 5, 2, 3, 1, 5, 2]
        result = rectangles(*points)
        self.assertEqual(result, 2)

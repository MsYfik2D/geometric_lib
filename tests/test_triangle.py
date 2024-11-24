import unittest
from triangle import area, perimeter


class TestTriangle(unittest.TestCase):
    def test_area(self):
        a, b, c = 3, 4, 5
        result = area(a, b, c)
        self.assertEqual(result, 6)

    def test_area_negative(self):
        with self.assertRaises(AssertionError):
            area(-3, 4, 5)

    def test_area_invalid(self):
        with self.assertRaises(AssertionError):
            area(1, 2, 3)

    def test_perimeter(self):
        a, b, c = 3, 4, 5
        result = perimeter(a, b, c)
        self.assertEqual(result, 12)

    def test_perimeter_negative(self):
        with self.assertRaises(AssertionError):
            perimeter(3, -4, 5)

    def test_perimeter_invalid(self):
        with self.assertRaises(AssertionError):
            perimeter(1, 2, 3)


if __name__ == '__main__':
    unittest.main()

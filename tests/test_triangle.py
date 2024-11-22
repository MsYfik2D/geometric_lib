import unittest
from triangle import area, perimeter


class TestTriangle(unittest.TestCase):
    def test_area(self):
        # Arrange (given)
        a, b, c = 3, 4, 5

        # Act (when)
        result = area(a, b, c)

        # Assert (then )
        self.assertEqual(result, 6)

    def test_perimeter(self):
        a, b, c = 3, 4, 5
        result = perimeter(a, b, c)
        self.assertEqual(result, 12)


if __name__ == '__main__':
    unittest.main()

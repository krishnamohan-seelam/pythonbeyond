import unittest
from sortedset import SortedSet


class TestConstruction(unittest.TestCase):

    def test_empty(self):
        s = SortedSet([])

    def test_from_sequence(self):
        s = SortedSet([15, 7, 3, 9])

    def test_from_duplicates(self):
        s = SortedSet([111, 2, 3, 4, 4, 4])

    def test_from_iterable(self):
        def gen6842():
            yield 6
            yield 8
            yield 4
            yield 2
        g = gen6842()
        s = SortedSet(g)

    def test_default_empty(self):
        s = SortedSet()


class TestContainerProtocol(unittest.TestCase):

    def setUp(self):
        self.s = SortedSet([6, 3, 7, 4])

    def test_positive_contained(self):
        self.assertTrue(6 in self.s)

    def test_negative_contained(self):
        self.assertFalse(1 in self.s)

    def test_positive_not_contained(self):
        self.assertTrue(9 not in self.s)

    def test_negative_not_contained(self):
        self.assertFalse(4 not in self.s)


class TestSizedProtocol(unittest.TestCase):
    def test_zero_size(self):
        s = SortedSet()
        self.assertEqual(len(s), 0)

    def test_one_size(self):
        s = SortedSet([1])
        self.assertEqual(len(s), 1)

    def test_one_ten(self):
        s = SortedSet(range(10))
        self.assertEqual(len(s), 10)

    def test_duplicate_items(self):
        s = SortedSet([1, 1, 1, 2, 2, 2])
        self.assertEqual(len(s), 2)


class TestIterableProtocol(unittest.TestCase):

    def setUp(self):
        self.s = SortedSet([1, 4, 3, 8, 5, 2])

    def test_iter(self):
        i = iter(self.s)
        self.assertEqual(next(i), 1)
        self.assertEqual(next(i), 2)
        self.assertEqual(next(i), 3)
        self.assertEqual(next(i), 4)
        self.assertEqual(next(i), 5)
        self.assertEqual(next(i), 8)
        self.assertRaises(StopIteration, lambda: next(i))

    def test_for_loop(self):
        index = 0
        expected = [1, 2, 3, 4, 5, 8]
        for item in self.s:
            self.assertEqual(item, expected[index])
            index += 1


if __name__ == '__main__':
    unittest.main()

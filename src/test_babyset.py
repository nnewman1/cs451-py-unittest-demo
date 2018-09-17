# test_babyset.py
# Nicholas Newman
import unittest

from baby_set import BabySet

class TestBabySetMethods(unittest.TestCase):
    """A collection of unit tests for the BabySet class. 
    Used to demonstrate and introduce unit testing in Python.
    Related docs: https://docs.python.org/3/library/unittest.html
    """

    def test_init(self):
        bset = BabySet([2, 4, 4])
        self.assertEqual(bset.size(), 2)

    def test_init_empty(self):
        bset = BabySet()
        self.assertEqual(bset.size(), 0)

    def test_add(self):
        bset = BabySet([2, 4, 4])
        bset.add(4)
        self.assertEqual(bset.size(), 2)
    
    def test_addSeq(self):
        bset = BabySet([2, 4, 4])
        bset.addSeq([3, 4, 5,])
        self.assertEqual(bset.size(), 4)

    def test_get(self):
        bset = BabySet([2, 4, 4])
        with self.assertRaises(KeyError):
            bset.get(3)

    def test_remove(self):
        bset = BabySet([2,4,4])
        bset.remove(2)
        self.assertEqual(bset.size(), 1)

    def test_clear(self):
        bset = BabySet([2,4,4])
        bset.clear()
        self.assertEqual(bset.size(), 0)


if __name__ == '__main__':
    unittest.main()
#assert sum([1,2,5]) == 6



"""
def test_sum():
    assert sum([1, 2, 3]) == 6

def test_sum_tuple():
    assert sum((1, 2, 3)) == 6

if __name__ == "__main__":
    test_sum()
    test_sum_tuple()
    print("Everything passed")
"""


#unittest

"""
import unittest

class TestSum(unittest.TestCase):

    def test_sum(self):
        self.assertEqual(sum([1,2,3]),6,"Should be 6")


    def test_sum_tuple(self):
        self.assertEqual(sum((1,2,2)),6,"Should be 6")


if __name__ == '__main__':
    unittest.main()
"""


"""
akılda kalmasında fayda var

target = __import__("my_sum.py")
sum = target.sum

"""

from fb_pyton_questions.main import problems

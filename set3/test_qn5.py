import unittest

import qn5

class testSet3qn5(unittest.TestCase):
#
    def test_add(self):
        result=qn5.calc(10,20).add()
        self.assertEqual(result, 30)

    def test_add(self):
        result=qn5.calc(10,20).sub()
        self.assertEqual(result, -10)

    def test_add(self):
        result=qn5.calc(10,20).mul()
        self.assertEqual(result, 200)

    def test_add(self):
        result=qn5.calc(10,20).div()
        self.assertEqual(result, .5)



import unittest

from sub import subsequence
from vagner import distance
from matrix import repeat_substring
from lis import lis1
from common import common
from binary import binary_search
from interpolar import interpolar
from binary_near import binary_near

class TestSub(unittest.TestCase):
    def test_list_int(self):
        data1 = 'abcdacbdbgfab'
        data2 = 'abc'
        result = subsequence(data1, data2)
        self.assertEqual(result, [0, 1, 2])

class TestVagner(unittest.TestCase):
    def test_list_int(self):
        data1 = 'abcdacbdbgfab'
        data2 = 'abc'
        result = distance(data1, data2)
        self.assertEqual(result, 10)

class TestLis(unittest.TestCase):
    def test_list_int(self):
        data= [34, 23, 56, 2, 78, 90]
        result = lis1(data)
        self.assertEqual(result, 4)

class TestMatrix(unittest.TestCase):
    def test_list_int(self):
        data = "abccdabdd"
        result = repeat_substring(data)
        self.assertEqual(result, 'ab')

class TestCommon(unittest.TestCase):
    def test_list_int(self):
        data1 = 'sdgsdsmbk'
        data2 = 'dshjsdal'
        result = common(data1, data2)
        self.assertEqual(result, 4)

class TestSub(unittest.TestCase):
    def test_list_int(self):
        data1 = '"sdgsdsmbk"'
        data2 = 'dshjsdal'
        result = subsequence(data1, data2)
        self.assertEqual(result, 4)

class TestBinary(unittest.TestCase):
    def test_list_int(self):
        data1 =  [6, 54, 34, 78, 1, 4, 80]
        data1.sort()
        data2 = 78
        result = binary_search(data1,0, 7, data2)
        self.assertEqual(result, 5)

class TestInterpolar(unittest.TestCase):
    def test_list_int(self):
        data1 =  [0, 2, 4, 6, 7, 10, 11, 14, 15]
        data2 = 4
        result = interpolar(data1,0, 7, data2)
        self.assertEqual(result, 2)

class TestBinarynear(unittest.TestCase):
    def test_list_int(self):
        data1 =  [0, 2, 4, 6, 7, 10, 11, 14, 15]
        data2 = 8
        result = binary_near(data1,  data2)
        self.assertEqual(result, 4)

if __name__ == '__main__':
    unittest.main()
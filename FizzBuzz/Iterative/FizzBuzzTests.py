import unittest
from FizzBuzz import *

class TestFizzBuzz(unittest.TestCase):

    def setUp(self):
    	self.game = FizzBuzz()

    def tearDown(self):
	    del self.game

    def test_classRuns(self):
        print("________________")
        print("Testing FizzBuzz")
        self.assertEqual(True, True)

    def test_translateNumberToWord(self):
        self.assertEqual(self.game.translateNumberToWord(0), [])
        self.assertEqual(self.game.translateNumberToWord(1), [1])

    # def test_getRandomWord(self):
	# 	self.assertIsNotNone(self.game.getRandomWord())
    

	# def test_isInvalidInput(self):
	# 	self.assertEqual(isInvalidInput(-0), False)
	# 	self.assertEqual(isInvalidInput(-1), True)
	# 	self.assertEqual(isInvalidInput("afesg"), True)

	# def test_howManyDigits(self):
	# 	self.assertEqual(howManyDigits(123), 3)
	# 	self.assertEqual(howManyDigits(0), 1)

if (__name__ == '__main__'):
	unittest.main()
import re
import unittest

def sumNums(fileName):
    read_file = open(fileName, "r")
    read_file = read_file.readlines()
    L = []
    for x in read_file:
        sum_nums = re.findall('[0-9]+', x)
        L = L + sum_nums

    L_2 = []
    for x in L:
        L_2.append(int(x))



    return sum(L_2) 

def countWord(fileName, word):
    pass

def listURLs(fileName):
    pass


class TestHW6(unittest.TestCase):
    """ Class to test this homework """

    def test_sumNums1(self):
        """ test sumNums on the first file """
        self.assertEqual(sumNums("regex_sum_42.txt"), 445833)

    def test_sumNums2(self):
        """ test sumNums on the second file """
        self.assertEqual(sumNums("regex_sum_132198.txt"), 374566)

    def test_countWord(self):
        """ test count word on the first file """
        self.assertEqual(countWord("regex_sum_42.txt", "computer"),21)

    def test_listURLs(self):
        """ test list URLs on the first file """
        self.assertEqual(len(listURLs("regex_sum_42.txt")), 3)

# run the tests
unittest.main(verbosity=2)

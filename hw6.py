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
    read_file = open(fileName, "r")
    read_file = read_file.readlines()

    new_list = []

    for x in read_file:
        y = x.lower()
        sum_words = re.findall(r"\b{}\b".format(word), y)
        new_list = new_list + sum_words

    return len(new_list)

def listURLs(fileName):
    read_file = open(fileName, "r")
    read_file = read_file.readlines()
    URL_l = []

    for x in read_file:
        URL_find = re.findall(r"\bwww.\b", x)
        URL_list = URL_list + URL_find

    return URL_l


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

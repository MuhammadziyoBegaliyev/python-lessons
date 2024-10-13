import unittest
from word_game import get_word , display


class GameTest(unittest.TestCase):
    def test_game(self):
        name = get_word()
        self.assertEqual(type(name),str)


unittest.main()
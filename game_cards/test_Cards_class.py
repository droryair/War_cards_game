from unittest import TestCase

from game_cards.Card_class import Card

"""
test__init__1: value out of range, value not int
test__init__2: suit out of range, suit not int
test__init__3: running standard tests.
test__gt__1: other not of type 'Card'
test__gt__2: two identical cards
test__gt__3: standard tests (other greater, other smaller, other value equal)
"""


class TestCard(TestCase):
    def test__init__1(self):
        # value out of range, value not int
        with self.assertRaises(ValueError):
            new_card = Card(14, 1)
            new_card = Card(0, 1)
        with self.assertRaises(TypeError):
            new_card = Card('14', 1)
            new_card = Card('abc', 1)

    def test__init__2(self):
        # suit out of range, suit not int
        with self.assertRaises(ValueError):
            new_card = Card(1, 5)
            new_card = Card(1, 0)
        with self.assertRaises(TypeError):
            new_card = Card(1, '5')
            new_card = Card(1, 'abc')

    def test__init__3(self):
        # test__init__3: running standard tests.
        # value's edges
        new_card_1 = Card(1, 3)
        self.assertEqual(new_card_1.value, 1)
        self.assertEqual(new_card_1.suit, 3)
        new_card_2 = Card(13, 3)
        self.assertEqual(new_card_2.value, 13)
        self.assertEqual(new_card_2.suit, 3)

        # suit's edges
        new_card_3 = Card(5, 1)
        self.assertEqual(new_card_3.value, 5)
        self.assertEqual(new_card_3.suit, 1)
        new_card_4 = Card(5, 4)
        self.assertEqual(new_card_4.value, 5)
        self.assertEqual(new_card_4.suit, 4)

    def test__gt__1(self):
        # other is not of type 'Card'
        my_card = Card(1, 4)
        with self.assertRaises(TypeError):
            my_card > {2: 4}

    def test__gt__2(self):
        # two identical cards
        my_card = Card(1, 4)
        other_card = Card(1, 4)
        with self.assertRaises(ValueError):
            my_card > other_card

    def test__gt__3(self):
        # test__gt__3: standard tests
        my_card = Card(5, 3)

        # other's value is bigger
        other_card_1 = Card(13, 2)
        self.assertTrue(my_card < other_card_1)

        # other's value is smaller
        other_card_2 = Card(2, 3)
        self.assertTrue(my_card > other_card_2)

        # other's value is equal, and suit is bigger
        other_card_3 = Card(5, 4)
        self.assertTrue(my_card < other_card_3)

        # other's value is equal, and suit is smaller
        other_card_4 = Card(5, 2)
        self.assertTrue(my_card > other_card_4)

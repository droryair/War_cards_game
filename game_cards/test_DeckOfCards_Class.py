"""
This page contains unit test for the class DeckOfCards which creates the Deck of the cards in the game.
The Class DeckOfCards doesn't get any parameter , it only builds the deck.
The tests is according to the checking we did in the Class.

Test Descriptions:
1. setUp - Set up function Creates the object deck

2. test__init__1 - The deck should include 52 cards and this test
    checks if the length of the list is really 52.

3. test__init__2 - Check for identical cards to see if there is a card that appears twice or more

4. test_cards_shuffle_1 - checks if the value error works in case of the list deck of cards is empty

5. test_cards_shuffle_2 - Checks if card_shuffle works

6. test_deal_one1 - checks if the list deck of cards is not empty

7. test_deal_one2 - we check if the type of the cell is Card and not something else -
        we do this by adding integer to the list and we see if the function fails
"""

from unittest import TestCase
from game_cards.DeckOfCards_Class import DeckOfCards


class TestDeckOfCards(TestCase):

    def setUp(self):
        self.deck = DeckOfCards()

    def test__init__1(self):
        self.assertEqual(len(self.deck.deck) , 52)

    def test__init__2(self):
        self.deck.deck = set(self.deck.deck)
        self.assertEqual(len(self.deck.deck), 52)

    def test_cards_shuffle_1(self):
        self.deck.deck = []     # update the list to be empty
        with self.assertRaises(ValueError):
            self.deck.cards_shuffle()

    def test_cards_shuffle_2(self):
        sorted_list = self.deck.deck.copy() # copy of self.deck.deck - store the organized list
        self.deck.cards_shuffle() # Shuffle the deck
        shuffle_list = self.deck.deck
        self.assertNotEqual(sorted_list, shuffle_list) # check if the deck was shuffled

    def test_deal_one1(self):
        self.deck.deck = []     # update the list to be empty
        with self.assertRaises(ValueError):
            self.deck.deal_one()

    def test_deal_one2(self):
        self.deck.deck = []
        self.deck.deck.append(1)    # adding an integer to the list type!=Card
        with self.assertRaises(TypeError):
            self.deck.deal_one()




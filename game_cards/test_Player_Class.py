from unittest import TestCase, mock
from unittest.mock import patch

from game_cards.Card_class import Card
from game_cards.DeckOfCards_Class import DeckOfCards
from game_cards.Player_Class import Player

"""
Testing Description:
test__init__1: player's name is not string.
test__init__2: player_cards_amount: negative number, large number, not int
test__init__3: running standard tests.
test_set_hand_1: deck_of_cards: empty list (deck_of_cards.deck), not type 'DeckOfCards'.
test_set_hand_2: running standard tests.
test_set_hand_3: mock 'deal_one'
test_get_card_1: self.deck: empty list (supposed to be impossible based on the game rules).
test_get_card_2: running standard tests.
test_add_card_1: card: not type 'Card' 
test_add_card_2: running standard tests.
"""


class TestPlayer(TestCase):

    def setUp(self):
        self.player_1 = Player('Player1', 10)
        self.game_deck = DeckOfCards()

    def test__init__1(self):
        # player's name is not string.
        new_player_1 = Player(2683, 23)
        self.assertEqual(new_player_1.name, '2683')
        new_player_2 = Player([2683], 23)
        self.assertEqual(new_player_2.name, '[2683]')
        new_player_3 = Player('', 23)
        self.assertEqual(new_player_3.name, '')

    def test__init__2(self):
        # player_cards_amount: negative number, large number, not int
        new_player_1 = Player('Player1', -1)
        self.assertEqual(new_player_1.cards_amount, 26)

        new_player_2 = Player('Player2', 100)
        self.assertEqual(new_player_2.cards_amount, 26)

        new_player_3 = Player('Player3', '15')
        self.assertEqual(new_player_3.cards_amount, 15)

        with self.assertRaises(ValueError):
            new_player_4 = Player('Player3', 'abc')

    def test__init__3(self):
        # test__init__3: running standard tests.
        self.assertEqual(self.player_1.name, 'Player1')
        self.assertEqual(self.player_1.cards_amount, 10)

    def test_set_hand_1(self):
        # deck_of_cards: empty list (deck_of_cards.deck), not type 'DeckOfCards'.
        self.game_deck.deck = []
        with self.assertRaises(SystemError):
            self.player_1.set_hand(self.game_deck)

        with self.assertRaises(TypeError):
            self.player_1.set_hand({1: 1, 2: 4, 13: 5, 10: 2, 9: 4, 7: 1, 7: 2, 8: 1, 9: 2, 10: 4})

    def test_set_hand_2(self):
        # test_set_hand_2: running standard tests.
        self.player_1.set_hand(self.game_deck)
        self.assertEqual(len(self.player_1.deck), 10)

    def test_set_hand_3(self):
        new_deck = DeckOfCards()
        new_player_1 = Player('Player1', 10)
        new_player_2 = Player('Player2', 10)
        with patch('game_cards.DeckOfCards_Class.DeckOfCards.deal_one') as mock_obj:
            # checking if the function 'set_hand' inserts the value given to it by 'del_one' into the player's deck
            # no matter what that value is.

            # valid value (instance of 'Card' class)
            new_card = Card(1, 1)
            mock_obj.return_value = new_card
            new_player_1.set_hand(new_deck)
            self.assertTrue(new_card in new_player_1.deck)

            # invalid value (int)
            new_card = 5
            mock_obj.return_value = new_card
            new_player_2.set_hand(new_deck)
            self.assertTrue(new_card in new_player_2.deck)

            """
            explanation:
            the function set_hand checks if the deck given to it is of instance 'DeckOfCards',
            the 'deal_one' function checks the validity of the values in the 'DeckOfCards' list (deck),
            therefore there is no need to check each card in the deck in the 'set_hand' function.
            """

    def test_get_card_1(self):
        # self.deck: empty list (supposed to be impossible based on the game rules).
        new_player_1 = Player('Player1', 10)
        new_player_1.deck = []
        with self.assertRaises(ValueError):
            new_player_1.get_card()

    def test_get_card_2(self):
        # test_get_card_2:running standard tests.
        self.player_1.set_hand(self.game_deck)
        card = self.player_1.get_card()
        self.assertTrue(card not in self.player_1.deck)
        self.assertEqual(len(self.player_1.deck), 9)

    def test_add_card_1(self):
        # test_add_card_1: card: not type 'Card'
        with self.assertRaises(TypeError):
            self.player_1.add_card({1: 1})

    def test_add_card_2(self):
        # test_add_card_2: card: running standard tests.
        self.player_1.set_hand(self.game_deck)
        new_card = self.game_deck.deal_one()
        self.player_1.add_card(new_card)
        self.assertTrue(new_card in self.player_1.deck)
        self.assertEqual(len(self.player_1.deck), 11)




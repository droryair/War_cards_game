from unittest import TestCase
import random
from game_cards.CardGame_Class import CardGame
from game_cards.Card_class import Card
from game_cards.DeckOfCards_Class import DeckOfCards
from game_cards.Player_Class import Player


class TestCardGame(TestCase):
    def setUp(self):
        print('Set up')
        self.amount_of_card = random.randint(10 , 26)
        self.game = CardGame('Daniel' , 'Dror ', self.amount_of_card)

    def test__init__1(self):
        pass


    def test_new_game1(self):
        print('test new game 1')
        with self.assertRaises(SystemError): # Checks if new_game runs more than once
            self.game.new_game()

    def test_new_game2(self):
        print('test new game 2')
        # Checks if the length of player's 1 deck equal to player's 2 deck
        print(" Deck length :" , self.amount_of_card)
        self.assertEqual(len(self.game.player1.deck) , len(self.game.player2.deck))

    def test_get_winner(self):
        pass

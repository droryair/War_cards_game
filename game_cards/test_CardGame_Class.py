"""
This page contains unit test for the class Card game class which runs the game and checks who is the winner.
we have 3 functions in this class: init,new game and get winner.

Test Descriptions:
1. setUp - Set up function Creates the object game , in type of CardGame

2. tearDown - we have a global parameter called counter_new_game:
                every time the function is called the counter added by 1.
                it is allowed to call new game only once. When we call the function
                new game more than once it will fail so we use tear down function
                to reset the counter to 0.

3. test__init__1 - 'pass' because all the testing on the players are being done
                    in the test player class.

4. test_new_game1 - checks if the function new_game() runs more than once(by calling it again)

5. test_new_game2 - checks if the players' decks have the same amount of cards

6. test_get_winner1 - we take down one card from player's 2 deck with the function get_card()
                        and we check if player 1 is the winner.

7. test_get_winner2 - we take down one card from player's 1 deck with the function get_card()
                        and we check if player 2 is the winner.

8.  test_get_winner3 - we check if it is a tie between players
"""


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
        self.game = CardGame('Daniel', 'Dror ', self.amount_of_card)

    def tearDown(self):
        self.game.get_winner()  # Reset the counter

    def test__init__1(self):
        pass

    def test_new_game1(self):
        with self.assertRaises(SystemError): # Checks if new_game runs more than once
            self.game.new_game()

    def test_new_game2(self):
        # Checks if the length of player's 1 deck equal to player's 2 deck
        print(" Deck length :" , self.amount_of_card)
        self.assertEqual(len(self.game.player1.deck) , len(self.game.player2.deck))

    def test_get_winner1(self):
        self.game.player2.get_card()
        self.assertEqual(self.game.get_winner(),self.game.player1)

    def test_get_winner2(self):
        self.game.player1.get_card()
        self.assertEqual(self.game.get_winner(),self.game.player2)

    def test_get_winner3(self):
        self.assertEqual(len(self.game.player1.deck),len(self.game.player2.deck))


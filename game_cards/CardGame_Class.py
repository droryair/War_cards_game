"""
Class CardGame - This is the class that manage the game between two players
Constructor init : gets the names of the players --> Two players in the game
                    and gets the number of the card for each player --> 10<= number of cards <=26

"""
# --------------------------
# importing all the classes
# --------------------------
import random
import inspect
from game_cards.Cards_class import Card
from game_cards.DeckOfCards_Class import DeckOfCards
from game_cards.Player_Class import Player


class CardGame:

    def __init__(self , player_name1 , player_name2 , num_of_cards):
        # Checks the if the type of the names is string
        if type(player_name1) != str or type(player_name2) != str:
            raise TypeError("The names of the players should be string type!!!")

        # Checks if the type of the number of cards is integer
        if type(num_of_cards) != int:
            raise TypeError("The number of cards to each player should be int type!!!")

        # Checks if the number of cards is eligible
        if num_of_cards<10 or num_of_cards >26 or num_of_cards<0:
            raise ValueError("The number of cards is illegal 10<=num of cards<=26")

        self.player1 = Player(player_name1, num_of_cards)
        self.player2 = Player(player_name2, num_of_cards)
        self.new_game()



    def new_game(self):
        if inspect.stack()[1][3] != "__init__":
            raise SystemError("The Function new_game() activated more than one time!!")
        main_deck = DeckOfCards()
        main_deck.cards_shuffle()
        # now we randomize which player gets cards first
        if random.randint(1,2) == 1:
            self.player1.set_hand(main_deck)
            self.player2.set_hand(main_deck)
        else:
            self.player2.set_hand(main_deck)
            self.player1.set_hand(main_deck)

    def get_winner(self):
        pass















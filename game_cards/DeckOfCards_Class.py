"""
- class description-
The class Deck of cards represents a list that each cell is an object of Card.
There are 4 suits to the cards, and each suit has 13 cards.-->total of 52 cards.
A deck of cards is a list of 52 Cards. --> This is the feature(constructor) of the class
"""
from game_cards.Cards_class import *

"""
--init--
we will have 2 loops: The external loop runs on the suit of the card:
Diamond,spade,heart,club
The internal loop runs on the value of the card:1-13 
"""
class DeckOfCards:

    def __init__(self):
        self.Deck = []              # creating an empty list
        for i in range(4):
            list_of_keys = list(suit_dict.keys())
            card_suit = list_of_keys[i]
                for x in range(13):



if __name__=="__main__":
    print(suit_dict)




"""
מחלקה Player- שחקן
מאפייני המחלקה:
player_name,
player_deck
player_cards_amount
מספר הקלפים ייקבע בעת התחלת משחק חדש, ויהיה 26 כברירת מחדל.
ניתן יהיה להגדיר שמספר הקלפים יהיה שונה בהתאם למה שייקבע בתחילת המשחק.
בכל מקרה, מספר הקלפים לשחקן לא יכול להיות כבוה מ- 26 ולא נמוך מ- 10.

מתודות המחלקה:
__init__
תקבל את שם השחקן ואת מספר הקלפים שיש לחלק לשחקן
(ברירת מחדל- 26. אם התקבל מספר גבוה מ- 26 או נמוך מ- 10, המספר יהיה 26.)
המתודה תאתחל את חבילת הקלפים של השחקן כרשימה ריקה.

set_hand
מקבלת חבילת קלפים של המשחק (מסוג DeckOfCards)
ומחלקת מתוכה קלפים אקראיים עבור השחקן, עפ"י מספר הקלפים שאמור השחקן לקבל.
יש להשתמש במתודה deal_one ששולפת קלף מהחבילה של המשחק. המתודה לא מחזירה כלום.

get_card
שולפת קלף אקראי מהחבילה של השחקן. המתודה תחזיר את הקלף ששלפה.

add_card
מתודה שמקבלת קלף ומוסיפה אותו לחבילת הקלפים של השחקן. לא מחזירה כלום.

הערות המפתחת:
שם שחקן- עניין בעייתי כי יכולים להיות שני שחקנים עם אותו השם. להוסיף מספר ששחקן (id)?
לקרוא על random.choice
"""
from DeckOfCards_Class import DeckOfCards
class Player:

    """
    תקבל את שם השחקן ואת מספר הקלפים שיש לחלק לשחקן
(ברירת מחדל- 26. אם התקבל מספר גבוה מ- 26 או נמוך מ- 10, המספר יהיה 26.)
המתודה תאתחל את חבילת הקלפים של השחקן כרשימה ריקה.
player_name,
player_deck
player_cards_amount
    """
    def __init__(self, player_name, player_cards_amount=26):
        # checking for valid numbers of cards for the player (valid amount: 10 < amount < 26)
        if player_cards_amount > 26 or player_cards_amount < 10:
            self.cards_amount = 26
        else:
            self.cards_amount = player_cards_amount

        self.name = player_name
        self.deck = []  # player's deck will include instances of the 'Card' class.

    def __str__(self):
        return f" player: {self.name}, deck(max:{self.cards_amount}): {self.deck}"

    def __repr__(self):
        return f" player: {self.name}, deck(max:{self.cards_amount}): {self.deck}"


    """
    מקבלת חבילת קלפים של המשחק (מסוג DeckOfCards)
    ומחלקת מתוכה קלפים אקראיים עבור השחקן, עפ"י מספר הקלפים שאמור השחקן לקבל.
    יש להשתמש במתודה deal_one ששולפת קלף מהחבילה של המשחק. המתודה לא מחזירה כלום.
    """
    def set_hand(self, deck_of_cards: DeckOfCards):
        # checking the type of the variable deck_of_cards
        if type(deck_of_cards) != DeckOfCards:
            raise TypeError(f"{deck_of_cards} is not of type DeckOfCards!")

        for i in range (self.cards_amount):



    """
    שולפת קלף אקראי מהחבילה של השחקן. המתודה תחזיר את הקלף ששלפה.
    """
    def get_card(self):
        pass


    """
    מתודה שמקבלת קלף ומוסיפה אותו לחבילת הקלפים של השחקן. לא מחזירה כלום.
    """
    def add_card(self):
        pass
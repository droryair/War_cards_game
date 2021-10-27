"""
הגדירו מחלקה בשם
Cards
המייצגת קלף במשחק קלפים.
לקלף יש מאפיינים:
ערך- value
וסמל - suit
הסמל קובע את סוג הקלף.
הערך 1-13, כאשר המספרים מייצגים:
1-  Ace
11- Jack
12- Queen
13- King

הקלף בעל הערך הגבוה ביותר הוא Ace.

"""

class Card:
    def __init__(self, value, suit):
        self.value = value
        self.suit = suit

        # creating a dictionary to convert cards numbers to values names, for printing purposes.
        self.val_dict = {
            13: 'King',
            12: 'Queen',
            11: 'Jack',
            1: 'Ace'
        }

        # creating a dictionary to convert numbers to suit names , for comparing printing and purposes.
        self.suit_dict = {
            'Diamond': 1,
            'Spade': 2,
            'Heart': 3,
            'Club': 4
        }

    def __str__(self):
        return f"value: {self.value}, suit:{self.suit}"

    def __repr__(self):
        return f"value: {self.value}, suit:{self.suit}"

    # compares between two cards, and returns boolean value.
    # also raising exceptions when encountering bugs.
    def __gt__(self, other):
        if type(other) != Card:
            raise TypeError("Got an object not from 'Card' type.")

        if self.value > other.value:
            return True
        elif self.value == other.value:
            if self.suit_dict[self.suit] > other.suit_dict[other.suit]:
                return True

            elif self.suit_dict[self.suit] == other.suit_dict[other.suit]:
                raise ValueError("Got two identical cards. How can it be??")
        return False


if __name__ == '__main__':
    new_card = Card()
    new_card2 = Card()
    print([new_card, new_card2])

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

    def __str__(self):
        return f"{self.value}:{self.suit}"

    def __repr__(self):
        return f"{self.value}:{self.suit}"

    # compares between two cards, and returns boolean value.
    # also raising exceptions when encountering bugs.
    def __gt__(self, other):
        """
        :param other: another instance of class 'Card'.
        :return: boolean value for whether the first card (self) is greater than the second (other)
        """
        # checking the type of 'other'.
        if type(other) != Card:
            raise TypeError("Got an object not from 'Card' type.")

        if self.value > other.value:
            return True
        elif self.value == other.value:
            if self.suit > other.suit:
                return True
            # taking care of possible incident: two identical cards.
            elif self.suit == other.suit:
                raise ValueError("Got two identical cards. How can it be??")
        return False


if __name__ == '__main__':
    new_card = Card()
    new_card2 = Card()
    print([new_card, new_card2])

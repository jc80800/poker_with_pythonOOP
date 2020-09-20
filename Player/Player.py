from Hand.Hand import Hand


class Player:
    """A class modelled for the players"""


    def __init__(self, name, amount_of_chips):
        """Initialize a player with name attribute"""
        self.name = name
        self.hand = Hand(name)
        self.amount_of_chips = amount_of_chips

    def fold_hand(self):
        """Player folds his hand"""
        self.hand.empty_hand()

    def raise_value(self, amount):
        """Raises pot by 'amount'"""


    def check(self):
        """Player calls 'check' """
        pass

    def all_in(self):
        """Player calls 'all-in'"""

    def show_hand(self):
        print(f"{self.name} has " + self.hand.show_hand())







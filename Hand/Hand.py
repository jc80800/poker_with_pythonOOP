class Hand:

    """A class modelled for the hand of a player"""
    def __init__(self, player):
        """Initialize the hand of the player"""

        self.player = player
        self.hand = []

    def add_card(self, card):
        if len(self.hand) < 3:
            self.hand.append(card)

        else:
            print(f"{self.player} can't add anymore cards")

    def empty_hand(self):
        self.hand.clear()

    def show_hand(self):
        string = ''
        for cards in self.hand:
            string = string + " " + cards.return_card()
        return string






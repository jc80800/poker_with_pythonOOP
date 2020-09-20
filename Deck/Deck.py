from Card.Card import Card
import random


class Deck:
    """A class modelled for a deck"""

    def __init__(self):
        """Initializes a deck, builds and shuffles the cards"""
        self.cards = []
        self.build()
        self.shuffle()

    def build(self):
        """Builds the deck"""
        for suit in ["Spades", "Clubs", "Diamond", "Hearts"]:
            for value in range(1, 14):
                self.cards.append(Card(value, suit))

    def shuffle(self):
        """Shuffles the deck"""
        for i in range(len(self.cards) - 1, 0, -1):
            r = random.randint(0, i)
            self.cards[i], self.cards[r] = self.cards[r], self.cards[i]

    def find_amount(self):
        """Finds the amount of cards left in the deck"""
        return len(self.cards)

    def draw_card(self):
        """Draws a card"""
        return self.cards.pop()

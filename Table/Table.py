from Deck.Deck import Deck
from Hand.Hand import Hand
class Table:
    """Class modelled for the table"""

    def __init__(self):
        self.table_seats = []
        self.table_card = Hand("Table")
        self.pot = 0
        self.deck = Deck()

    def add_player(self, player):

        if (len(self.table_seats) < 7):
            self.table_seats.append(player)

        else:
            print("Table is full")

    def add_value_to_pot(self, amount):
        self.pot += amount

    def pot_winner(self, player):
        player.amount_of_chips += self.pot
        self.pot = 0

    def deal_cards(self):
        for players in self.table_seats:
            for i in range(1, 3):
                players.hand.add_card(self.deck.draw_card())

    def all_player_show_hand(self):
        for players in self.table_seats:
            players.show_hand()

    def deal_table(self):
        self.table_card.add_card(self.deck.draw_card())
        print(f"Table: " + self.table_card.show_hand())
















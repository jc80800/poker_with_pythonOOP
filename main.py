from Player.Player import Player
from Table.Table import Table


def register_player(name, chips):
    return Player(name, chips)

def register_table():
    return Table()

def main():
    print("Welcome to Jasong's Gambling den")
    num_of_players = int(input("How many players? (0-6): "))
    table1 = register_table()
    for i in range(num_of_players):
        player_name = input("Player " + str(i + 1) + "'s name ")
        player_chips = input("How many chips do they have?(1k-10k): ")
        player = register_player(player_name, player_chips)
        table1.add_player(player)
    print("Starting the game!")
    table1.deal_cards()
    table1.deal_table()
    table1.deal_table()


    table1.all_player_show_hand()

main()




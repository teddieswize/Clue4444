from card import Card
from checklist import Checklist
from player import Player
import random

# Create Deck
deck = []

# Suspects
deck.append(Card(0, "Blue", 0))
deck.append(Card(1, "Orange", 0))
deck.append(Card(2, "Red", 0))
deck.append(Card(3, "Yellow", 0))
deck.append(Card(4, "Green", 0))
deck.append(Card(5, "Purple", 0))

# Weapons
deck.append(Card(6, "Knife", 1))
deck.append(Card(7, "Gun", 1))
deck.append(Card(8, "Rope", 1))
deck.append(Card(9, "Pipe", 1))
deck.append(Card(10, "Wrench", 1))
deck.append(Card(11, "Candle", 1))

# Rooms
deck.append(Card(12, "Dining", 2))
deck.append(Card(13, "Ballroom", 2))
deck.append(Card(14, "Billiards", 2))
deck.append(Card(15, "Kitchen", 2))
deck.append(Card(16, "Hallway", 2))
deck.append(Card(17, "Porch", 2))
deck.append(Card(18, "Library", 2))
deck.append(Card(19, "Office", 2))

reference_checklist = Checklist(deck)

# Create Players (human is player 0)
players = []
players.append(Player(0, "Player 0", Checklist(deck), False))
players.append(Player(1, "Player 1", Checklist(deck), True))
players.append(Player(2, "Player 2", Checklist(deck), True))
players.append(Player(3, "Player 3", Checklist(deck), True))

# Select the crime scene
possible_weapons = []
possible_suspects =[]
possible_rooms = []

for card in deck:
    if card.get_category() == 0:
        possible_suspects.append(card)
    elif card.get_category() == 1:
        possible_weapons.append(card)
    elif card.get_category() == 2:
        possible_rooms.append(card)

true_suspect = possible_suspects[random.randint(0, len(possible_suspects) - 1)]
true_weapon = possible_weapons[random.randint(0, len(possible_weapons) - 1)]
true_room = possible_rooms[random.randint(0, len(possible_rooms) - 1)]

if true_suspect in deck:
    deck.remove(true_suspect)
if true_weapon in deck:
    deck.remove(true_weapon)
if true_room in deck:
    deck.remove(true_room)

# Deal cards
random.shuffle(deck)
turn = 0
while len(deck) > 0:
    players[turn].add_to_hand(deck[0])
    deck.pop(0)
    turn += 1
    if turn > 3:
        turn = 0

# Make first eliminations from hand
for player in players:
    player.eliminate_hand()

# Start Game
truth_found = False
# First Turn

turn = 0
next_player = 0

def get_next_player():
    next = next_player + 1
    if next == len(players):
        next = 0
    return next

iterations = 0
while truth_found == False:
    iterations += 1
    suggest_or_accuse = players[turn].suggest_or_accuse()

    if suggest_or_accuse == 1:
        # Suggest Something
        suggestion = players[turn].begin_suggestion()
        print(players[turn].get_name() + 
            " suggested: " + reference_checklist.id_to_name(suggestion[0]) + 
            " with the " + reference_checklist.id_to_name(suggestion[1]) + 
            " in the " + reference_checklist.id_to_name(suggestion[2]))

        # Set bool variables
        found_match = False
        no_matches = False

        next_player = turn

        while found_match == False and no_matches == False:
            next_player = get_next_player()
            if next_player == turn:
                print("No Matches")
                no_matches = True
                break
            else:
                matches = players[next_player].check_for_matching_cards(suggestion)
                if matches != []:
                    found_match = True
                    players[next_player].show_card(matches, players[turn])
                    break
    elif suggest_or_accuse == 2:
        accusation = players[turn].begin_accusation()
        print(players[turn].get_name() + 
            " IS ACCUSING: " + reference_checklist.id_to_name(accusation[0]) + 
            " with the " + reference_checklist.id_to_name(accusation[1]) + 
            " in the " + reference_checklist.id_to_name(accusation[2]))
        if (true_suspect.get_id() == accusation[0] and 
            true_weapon.get_id() == accusation[1] and
            true_room.get_id() == accusation[2]):
            truth_found = True
            print("The truth has been found!")
            print("It was " + true_suspect.get_name() + " with the " + true_weapon.get_name() + " in the " + true_room.get_name())
            print(players[turn].get_name() + " is the winner!")
            print("This game took " + str(iterations) + " turns.")
        else:
            pass
    
    turn = turn + 1
    if turn == len(players):
        turn = 0
    next_player = turn
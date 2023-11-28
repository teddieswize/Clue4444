import re
import random

class Player:
    def __init__(self, id, name, checklist, computer):
        self.id = id
        self.name = name
        self.hand = []
        self.checklist = checklist
        self.computer = computer
    
    def get_id(self):
        return self.id
    
    def get_name(self):
        return self.name
    
    def get_hand(self):
        return self.hand
    
    def add_to_hand(self, item):
        self.hand.append(item)
    
    def print_hand(self):
        for card in self.hand:
            print(card.get_name())
    
    def print_checklist(self):
        self.checklist.print_checklist()

    def eliminate_option(self, card):
        target_id = card.get_id()
        for checkbox in self.checklist.get_list():
            if checkbox.get_id() == target_id:
                checkbox.set_seen(True)
                return
    
    def eliminate_hand(self):
        for card in self.hand:
            self.eliminate_option(card)
    
    def suggest_or_accuse(self):
        if self.computer == False:
            while True:
                user_input = input("Type 1 to Suggest, Type 2 to Accuse")
                if user_input in ['1', '2']:
                    user_input = int(user_input)
                    break
                else:
                    print("Invalid input. Please enter 1 or 2")
            return user_input
        elif self.computer == True:
            return(self.check_for_accusation())
    
    def check_for_accusation(self):
        unseen_counter = self.checklist.get_number_of_unseen()
        if unseen_counter == 3:
            return 2
        else:
            return 1

    def begin_suggestion(self):
        sugg_sus = -1
        sugg_weap = -1
        sugg_room = -1
        if self.computer == False:
            pattern = r'^\[\s*\d+\s*,\s*\d+\s*,\s*\d+\s*\]$'
            while True:
                print("To make a Suggestion, please provide a Suspect ID, a Weapon ID, and a Room ID in Brackets")
                print("e.g [1, 2, 3]")
                print("To see your checklist, type checklist")
                user_input = input()
                if user_input in ['checklist']:
                    self.print_checklist()
                elif re.match(pattern, user_input):
                    values = user_input.strip("[]").split(", ")
                    sugg_sus, sugg_weap, sugg_room = map(int, values)
                    if (self.checklist.check_category(sugg_sus, 0) == True and 
                        self.checklist.check_category(sugg_weap, 1) == True and
                        self.checklist.check_category(sugg_room, 2) == True):
                        return [sugg_sus, sugg_weap, sugg_room]
                    else:
                        print("Index out of bounds, wrong order, or category repeats. Try again")
                else:
                    print("Input not recognized, try again")
        elif self.computer == True:
            unseen_sus = self.checklist.get_unseen(0)
            unseen_weaps = self.checklist.get_unseen(1)
            unseen_rooms = self.checklist.get_unseen(2)
            sugg_sus = random.choice(unseen_sus)
            sugg_weap = random.choice(unseen_weaps)
            sugg_room = random.choice(unseen_rooms)
            return [sugg_sus, sugg_weap, sugg_room]
    
    def begin_accusation(self):
        acc_sus = -1
        acc_weap = -1
        acc_room = -1
        if self.computer == False:
            pattern = r'^\[\s*\d+\s*,\s*\d+\s*,\s*\d+\s*\]$'
            while True:
                print("To make a Suggestion, please provide a Suspect ID, a Weapon ID, and a Room ID in Brackets")
                print("e.g [1, 2, 3]")
                print("To see your checklist, type checklist")
                user_input = input()
                if user_input in ['checklist']:
                    self.print_checklist()
                elif re.match(pattern, user_input):
                    values = user_input.strip("[]").split(", ")
                    sugg_sus, sugg_weap, sugg_room = map(int, values)
                    if (self.checklist.check_category(sugg_sus, 0) == True and 
                        self.checklist.check_category(sugg_weap, 1) == True and
                        self.checklist.check_category(sugg_room, 2) == True):
                        return [sugg_sus, sugg_weap, sugg_room]
                    else:
                        print("Index out of bounds, wrong order, or category repeats. Try again")
                else:
                    print("Input not recognized, try again")
        elif self.computer == True:
            unseen_sus = self.checklist.get_unseen(0)
            unseen_weaps = self.checklist.get_unseen(1)
            unseen_rooms = self.checklist.get_unseen(2)
            acc_sus = random.choice(unseen_sus)
            acc_weap = random.choice(unseen_weaps)
            acc_room = random.choice(unseen_rooms)
            return [acc_sus, acc_weap, acc_room]
    
    def check_for_matching_cards(self, suggestion):
        matches = []
        for card in self.hand:
            if card.get_id() == suggestion[0]:
                matches.append(card)
            elif card.get_id() == suggestion[1]:
                matches.append(card)
            elif card.get_id() == suggestion[2]:
                matches.append(card)
        return matches

    def get_card_from_hand(self, id):
        for card in self.hand:
            if card.get_id() == id:
                return card

    def show_card(self, matches, seer):
        if len(matches) == 1:
            shown_card = matches[0]
        else:
            # If computer, random choice
            if self.computer == True:
                shown_card = random.choice(matches)
            else:
                # If human, decide which index 
                print("You have multiple matches, which would you like to show?")
                string = ""
                correct_choices = []
                for card in matches:
                    string += (card.get_name() + " : " + str(card.get_id()) + " -- ")
                    correct_choices.append(card.get_id())
                while True:
                    print(string)
                    user_input = input("Enter the index of your choice: ")
                    if int(user_input) in correct_choices:
                        shown_card = self.get_card_from_hand(int(user_input))
                        break
        seer.eliminate_option(shown_card)
        print(self.get_name() + " showed " + seer.get_name() + " a card!")


            


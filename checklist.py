from checkbox import Checkbox

class Checklist:
    def __init__(self, deck):
        self.deck = deck
        self.list = []
        for card in deck:
            self.list.append(Checkbox(card.get_id(), card.get_name(), card.get_category()))
    
    def get_list(self):
        return self.list
    
    def check_category(self, id, category):
        for box in self.list:
            if box.get_id() == id:
                if box.get_category() == category:
                    return True
                else:
                    return False
        return False
    
    def id_to_name(self, id):
        for box in self.list:
            if box.get_id() == id:
                return box.get_name()
        return "ID Out of Checklist Bounds"

    
    def print_checklist(self):
        # Find the maximum length of item names for formatting
        max_name_length = max(len(item.get_name()) for item in self.list)

        for item in self.list:
            item_name = item.get_name()
            seen_status = "Seen" if item.get_seen() else "Not Seen"
            item_id = item.get_id()
            # Use string formatting to align the columns
            formatted_line = "{:<{name_len}} : {:<10} : {:>5}".format(item_name, seen_status, item_id, name_len=max_name_length)
            print(formatted_line)
    
    def get_unseen(self, category):
        unseen = []
        for box in self.list:
            if box.get_category() == category:
                if box.get_seen() == False:
                    unseen.append(box.get_id())
        return unseen

    def get_number_of_unseen(self):
        unseen_counter = 0
        for box in self.list:
            if box.get_seen() == False:
                unseen_counter += 1
        return unseen_counter
        
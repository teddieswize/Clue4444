class Card:
    def __init__(self, id, name, category):
        self.id = id
        self.name = name
        self.category = category
    
    def get_id(self):
        return self.id
    def get_name(self):
        return self.name
    def get_category(self):
        return self.category
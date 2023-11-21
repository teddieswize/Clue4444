class Checkbox:
    def __init__(self, id, name, category):
        self.id = id
        self.name = name
        self.seen = False
        self.owner = None
        self.category = category
    
    def set_seen(self, tf):
        self.seen = tf

    def get_id(self):
        return self.id

    def get_name(self):
        return self.name
    
    def get_seen(self):
        return self.seen
    
    def get_category(self):
        return self.category
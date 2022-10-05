class Topping:
    def __init__(self, name, vegetarian, cal_count, spicy, amount):
        self.name = name
        self.vegetarian = vegetarian
        self.cal_count = cal_count #per serving
        self.spicy = spicy
        self.amount = amount #"regular" or "extra"
    
    def add_spice(self):
        self.spicy = True
    
    def get_total_cals(self):
        if self.amount == "extra":
            return self.cal_count * 2
        else: #"regular"
            return self.cal_count

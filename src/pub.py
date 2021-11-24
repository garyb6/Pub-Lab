class Pub:
    
    def __init__(self, name, till, drinks):
        self.name = name
        self.till = till
        self.drinks = drinks

    def check_till(self):
        return self.till 

    def drinks_list(self):
        return self.drinks 

    def find_drink_by_name(self, name):
        for drink in self.drinks:
            if name == drink.name:
                return drink

    def remove_drink(self, drink_name):
        self.drinks.remove(self.find_drink_by_name(drink_name))

    def get_id(self, customer):
        if customer.age >= 18:
            return True
        else: return False

    def sell_drink(self, customer, drink_name):
        drink = self.find_drink_by_name(drink_name)
        customer.stomach.append(drink)
        customer.wallet -= drink.price
        self.till += drink.price
        self.drinks.remove(drink)
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
        if customer.can_afford(drink) and customer.get_drunkeness() < 8:
            if self.get_id (customer):
                customer.increase_drunkeness(drink)
                customer.stomach.append(drink)
                customer.wallet -= drink.price
                self.till += drink.price
                self.drinks.remove(drink)
            elif not drink.alco_status: #alternatively use elif drink.alco_status == False
                customer.stomach.append(drink)
                customer.wallet -= drink.price
                self.till += drink.price
                self.drinks.remove(drink)
        
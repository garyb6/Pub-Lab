class Customer:
    def __init__(self, name, stomach, wallet):
        self.name = name
        self.stomach = stomach
        self.wallet = wallet

    def buy_drink(self, pub, drink_name):
        drink = pub.find_drink_by_name(drink_name)

        self.stomach.append(drink)
        self.wallet -= drink.price

        pub.till += drink.price
        pub.drinks.remove(drink)
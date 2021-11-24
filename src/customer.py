class Customer:
    def __init__(self, name, stomach, wallet, age):
        self.name = name
        self.stomach = stomach
        self.wallet = wallet
        self.age = age

    def can_afford(self, drink):
        if self.wallet >= drink.price:
            return True 
        else:
             return False 
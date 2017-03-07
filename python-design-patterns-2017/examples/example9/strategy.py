class Customer:
    def __init__(self, strategy):
        self.drinks = []
        self.strategy = strategy
    
    def add(self, price, quantity):
        drinks.append(strategy(price * quantity))

    def print_bill(self):
        ...

# strategy is just a function that returns a price

c = Customer(lambda x: x)
c.add(5.50, 2)
c.add(4.30, 1)
# Happy hour
c.strategy = lambda x: x * 0.5
c.add(4.30, 6)

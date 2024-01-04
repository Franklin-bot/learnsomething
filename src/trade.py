

class Trade:
    def __init__(self, name, side, ticker, quantity, price):
        self.name = name
        self.side = side
        self.ticker = ticker
        self.quantity = quantity
        self.price = price

    def __lt__(self, other):
        return self.price < other.price


class Account:
    def __init__(self, name, initialBalance):
        self.name = name
        self.positions = {}
        self.balance = initialBalance
    
    def giveStocks(self, ticker, quantity):
        self.positions[ticker] = self.positions.get(ticker, 0) + quantity

class PriceQueue:
    def __init__(self):
        self.queue = []



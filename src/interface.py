from trade import Trade
from trade import Account
from collections import defaultdict
from collections import deque
from queue import Queue

class Exchange:
    # implement this!

    def __init__(self, initialBalance):
       self.sellOrders = defaultdict(Queue) 
       self.buyOrders = defaultdict(Queue)
       self.initialBalance = initialBalance
       self.accounts = {}

    def addAccount(self, account):
        if account.name not in self.accounts:
            self.accounts[account.name] = account


    def add_trade(self, trade):
        """Adds a trade to the exchange (validation required)
        and returns a match if required. It is up to you on how you will
        handle representing trades. """

        # if there is no account for this person yet, add it
        if trade.name not in self.accounts:
            self.accounts[trade.name] = Account(trade.name, self.initialBalance)

        currAccount = self.accounts[trade.name]
        
        # buy order
        if trade.side == "BUY":
            
            if currAccount.balance >= trade.price * trade.quantity:
                # keep track of buy orders
                self.buyOrders[trade.ticker].put(trade)
                
                # execute trade if possible
                while trade.quantity > 0 and not self.sellOrders[trade.ticker].empty() and self.sellOrders[trade.ticker].queue[0].price <= trade.price:
                    currSell = self.sellOrders[trade.ticker].queue[0]
                    currSellAccount = self.accounts[currSell.name]

                    if trade.quantity >= currSell.quantity:
                        trade.quantity -= currSell.quantity
                        self.sellOrders[trade.ticker].get()

                        currAccount.positions[trade.ticker] = self.accounts[trade.name].positions.get(trade.ticker, 0) + currSell.quantity
                        currAccount.balance -= currSell.quantity * currSell.price 
                        currSellAccount.positions[trade.ticker] = self.accounts[trade.name].positions.get(trade.ticker, 0) - currSell.quantity
                        currSellAccount.balance += currSell.quantity * currSell.price 
                    else:
                        currSell.quantity -= trade.quantity
                        currAccount.positions[trade.ticker] = currAccount.positions.get(trade.ticker, 0) + trade.quantity
                        currAccount.balance -= trade.quantity * currSell.price
                        currSellAccount.positions[trade.ticker] = currAccount.positions.get(trade.ticker, 0) - trade.quantity
                        currSellAccount.balance += trade.quantity * currSell.price
            else:
                return -1
        # sell order
        else:

            if currAccount.positions.get(trade.ticker, 0) >= trade.quantity:
                # keep track of sell orders
                self.sellOrders[trade.ticker].put(trade)
                
                # execute trade if possible
                while trade.quantity > 0 and not self.buyOrders[trade.ticker].empty() and self.buyOrders[trade.ticker].queue[0].price <= trade.price:
                    currBuy = self.buyOrders[trade.ticker].queue[0]
                    currBuyAccount = self.accounts[trade.name]

                    if trade.quantity >= currBuy.quantity:
                        trade.quantity -= currBuy.quantity
                        self.buyOrders[trade.ticker].get()

                        currAccount.positions[trade.ticker] -= currBuy.quantity
                        currAccount.balance += currBuy.quantity * currBuy.price
                        currBuyAccount.positions[trade.ticker] += currBuy.quantity
                        currBuyAccount.balance -= currBuy.quantity * currBuy.price
                    else:
                        currBuy.quantity -= trade.quantity

                        currAccount.positions[trade.ticker] -= trade.quantity
                        currAccount.balance += trade.quantity * currBuy.price

                        currBuyAccount.positions[trade.ticker] += trade.quantity
                        currBuyAccount.balance -= trade.quantity * currBuy.price
            else:
                return -2




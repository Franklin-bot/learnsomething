from interface import Exchange
from trade import Trade, Account

# test adding orders to the exchange
exchange = Exchange(100)
account1 = Account("Bob", exchange.initialBalance)
exchange.addAccount(account1)
account1.giveStocks("A", 65)
Trade1 = Trade("Bob", "SELL", "A", 50, 1)
exchange.add_trade(Trade1)
assert exchange.sellOrders["A"].queue[0].quantity == 50

# test fulfilling buying orders partially
Trade2 = Trade("Jim", "BUY", "A", 65, 1)
exchange.add_trade(Trade2)
assert exchange.accounts["Bob"].balance == 150
assert exchange.accounts["Jim"].balance == 50

# test only allow buying when asking price is below bidding price
account2 = Account("Percy", exchange.initialBalance)
exchange.addAccount(account1)
account2.giveStocks("A", 50)
Trade1 = Trade("Percy", "SELL", "A", 50, 2)
assert exchange.accounts["Jim"].positions["A"] == 50

# test error message -2 for selling stocks you do not have
account3 = Account("Maggie", exchange.initialBalance)
exchange.addAccount(account3)
assert exchange.add_trade(Trade("Maggie", "SELL", "A", 50, 1)) == -2

# test error message -1 for buying stocks you cannot afford
account4 = Account("Benny", exchange.initialBalance)
exchange.addAccount(account4)
assert exchange.add_trade(Trade("Benny", "BUY", "A", 100, 100)) == -1

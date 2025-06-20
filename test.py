from fintual import Stock, Portfolio

# Definiré 6 stocks con sus respectivos precios para hacer las pruebas
aapl = Stock("Apple", 195)
meta = Stock("Meta", 420)
tsla = Stock("Tesla", 182)
amzn = Stock("Amazon", 185)
nvda = Stock("Nvidia", 130)
intc = Stock("Intel", 35)

my_portfolio = Portfolio()
my_portfolio.buyStocks([(aapl, 12),(meta,8),(tsla,5),(amzn,10),(nvda,6)])

# Test 1: Todas las stocks que quiero ya están en mi portfolio
my_portfolio.setDistribution([(aapl, 0.2),(meta,0.1),(tsla,0.3),(amzn,0.15),(nvda,0.25)])
print("\nTest 1:")
sell1, buy1 = my_portfolio.rebalance()
# Los valores parecen estar bien, pero quiero visualizar como quedarían los porcetanjes
# aplicando las acciones reportadas. Para esto defino otra función auxiliar.
my_portfolio.getNewDistribution(sell1, buy1)

# Test 2: Hay alguna stock que quiero que no está en mi portfolio
my_portfolio.setDistribution([(aapl, 0.2),(meta,0.1),(tsla,0.18),(amzn,0.15),(nvda,0.25),(intc,0.12)])
print("\nTest 2:")
sell2, buy2 = my_portfolio.rebalance()
my_portfolio.getNewDistribution(sell2, buy2)

# Test 3: Hay alguna stock que tengo pero que no quiero
my_portfolio.setDistribution([(aapl, 0.45),(meta,0.22),(tsla,0.18),(amzn,0.15)])
print("\nTest 3:")
sell3, buy3 = my_portfolio.rebalance()
my_portfolio.getNewDistribution(sell3, buy3)

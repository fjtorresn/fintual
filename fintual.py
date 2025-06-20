from collections import defaultdict

class Stock:
    def __init__(self, name, price):
        # En principio, el nombre y el precio bastan para definir una stock
        self.name = name
        self.price = price
    def currentPrice(self, price):
        self.price = price

class Portfolio:
    def __init__(self):
        # Los stocks del portfolio se guardarán de la forma {stock: cantidad}
        self.stocks = defaultdict(int)
        # La distribución deseada se guardará de la forma {stock:porcentaje}
        self.allocated = defaultdict()
    
    def rebalance(self):
        pass

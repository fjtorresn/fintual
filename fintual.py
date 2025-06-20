from collections import defaultdict

class Stock:
    def __init__(self, name, price):
        # En principio, el nombre y el precio bastan para definir una stock
        self.name = name
        self.price = price
    def currentPrice(self, price):
        self.price = price 
    def __hash__(self):
        # Como voy a usar las stocks como las keys de un dict, tienen que ser hasheables
        return hash(self.name)

class Portfolio:
    def __init__(self):
        # Los stocks del portfolio se guardarán de la forma {stock: cantidad}
        self.stocks = defaultdict(int)
        # La distribución deseada se guardará de la forma {stock:porcentaje}
        self.allocated = defaultdict()

    # Necesito testear que esté funcionando. Para esto agrego las funciones
    # buyStocks y setDistributios que me ayudaran a setear el portfolio
    def buyStocks(self, stocks):
        for stock, n in stocks:
            self.stocks[stock] += n
    
    def setDistribution(self, dist):
        self.allocated = defaultdict()
        for stock, d in dist:
            self.allocated[stock] = d

    def getPrice(self):
        value = 0
        for stock, n in self.stocks.items():
            value += n*stock.price
        return value
    
    # Función para visualizar el cambio de porcentajes según
    # las acciones propuestas
    def getNewDistribution(self, sell, buy):
        value = self.getPrice()
        unmodified_stocks = set(self.stocks.keys())
        print("\n")
        print("Stock\tAmount\tValue\tPercentage")
        for stock, n, _ in sell:
            tmp = self.stocks[stock]-n
            if tmp>0:
                print(f"{stock.name}\t{tmp:.2f}\t{tmp*stock.price:.2f}\t{tmp*stock.price*100/value:.2f}%")
            unmodified_stocks.remove(stock)
        for stock, n, _ in buy:
            tmp = n+self.stocks[stock]
            print(f"{stock.name}\t{tmp:.2f}\t{tmp*stock.price:.2f}\t{tmp*stock.price*100/value:.2f}%")
            if stock in unmodified_stocks:
                unmodified_stocks.remove(stock)
        for stock in unmodified_stocks:
            tmp = self.stocks[stock]
            print(f"{stock.name}\t{tmp:.2f}\t{tmp*stock.price:.2f}\t{tmp*stock.price*100/value:.2f}%")
        print("\n")

    # Al principio me confundí y creí que el procentaje era relativo a la cantidad de stocks,
    # después entendí que era relativo al valor de estas y del portfolio
    def rebalance(self):
        # Necesito el valor total del portfolio para calcular los porcentaje
        # es mejor implementar esto como un método aparte ya que es una funcionalidad
        # útil para la clase. Pensé en guardarlo como un atributo de la clase pero
        # no tiene mucho sentido ya que varía con el precio de las acciones.
        value = self.getPrice()
        # en principio planeo guardar lo que hay que comprar/vender en listas de tuplas
        sell = []
        buy = []
        # Voy a iterar sobre los stocks del portfolio, sin embargo, pueden haber
        # stocks requeridos que no estén en él. 
        # ~~Por lo tanto, guardaré un set con las stocks que deseo tener, a medida 
        # que vaya revisando las stocks que tengo las eliminaré del set y luego 
        # revisaré las que quedan para agregarlas a la lista de las que hay que comprar~~
        # Mejor utilizaré directamente la resta de los sets, la complejidad algoritmica es
        # la misma y es más legible
        stocks_i_dont_have = set(self.allocated.keys()) - set(self.stocks.keys())
        for stock, n in self.stocks.items():
            # Si la stock no está entre la que pretendo tener, hay que venderla
            if stock not in self.allocated:
                # El formato de la tupla es (stock, cantidad a comprar/vender, valor total asociado)
                sell.append((stock, n, n*stock.price))
            else:
                # Si tengo que comprar o vender dependerá de cuánto tengo en relación al
                # porcentaje deseado. Utilizo la variable diff para no tener que recalcular
                # la diferencia repetidas veces
                diff = n*stock.price - value*self.allocated[stock]
                # En la realidad podría utilizarse un margen (e.g: si la diferencia es de un 0.5%
                # respecto del valor que quiero no es necesario comprar/vender) eso se puede controlar aca
                if diff > 0:
                    sell.append((stock, diff/stock.price, diff))
                else:
                    buy.append((stock, diff*-1/stock.price, diff*-1))
        # Ahora tengo que hacerme cargo de las stock que deseo tener pero que no he revisado, para
        # eso reviso las stocks en i_dont_have y las agrego en la lista de compra
        for stock in stocks_i_dont_have:
            buy.append((stock, value*self.allocated[stock]/stock.price, value*self.allocated[stock]))

        # En este punto ya tengo la información requerida en las listas sell y buy.
        # Mostraré la info contenida y retornaré ambas listas, sin embargo, en la práctica,
        # qué hacer ahora estará determinado por cómo se quiera manejar la info

        print("\nSell:")
        print("Stock\tAmount\tValue")
        for stock, n, val in sell:
            print(f"{stock.name}\t{n:.2f}\t{val:.2f}")
        print("\nBuy:")
        print("Stock\tAmount\tValue")
        for stock, n, val in buy:
            print(f"{stock.name}\t{n:.2f}\t{val:.2f}")

        # Tendré que modificar la composición del portfolio? Yo creo que no, porque según
        # el enunciado se busca "saber que stocks DEBERÍAN ser vendidas/compradas"
        # no se habla de ejecutar
        return sell, buy

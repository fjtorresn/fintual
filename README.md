# Tarea para postular a Fintual

Buenos días/tardes/noches.

Les dejo el código que desarrollé para implementar un Portfolio con la capacidad de cálcular qué stocks debería comprar o vender para seguir cierta estrategia definida.

El código está implementado en Python y los comentarios son exageradamente largos y descriptivos con el fin de describir en qué estaba pensando mientras lo desarrollaba.

A modo de resumen, el flujo de implementación fue el siguiente:
1. Declarar las clases y los métodos solicitados con sus atributos básicos
2. Implementar el método requerido (rebalance)
3. Definir los tests
4. Implementar funciones auxiliares
5. Testear y arreglar bugs

Esto se puede ver reflejado también en los commits.

Una breve descripción de las clases:

## Clase Stock
Representa cada stock que conforma el Portfolio
### Atributos
* 'name': Nombre de la empresa (string)
* 'price': Precio de la acción (float)

## Clase Portfolio
Representa el Portfolio, es decir, el cojunto de acciones
### Atributos
* 'stocks': collección de stocks y sus cantidades (dict)
* 'allocated': distribución deseada de stocks (dict)
### Métodos
* 'buyStocks(stocks)': agrega las stocks dadas a la collección del portfolio
* 'setDistribution()': setea la distribución deseada de stocks
* 'getPrice()': retorna el valor total del portfolio
* 'getNewDistribution(sell, buy)': imprime la distribución resultante de ejecutarse las órdenes entregadas
* 'rebalance()': calcula qué stocks se deberían comprar o vender para acercarse a la distribución deseada

Saludos

Francisco

# stock.py
#
# Exercise 4.1


class Stock:
    """
    Class to represent details of a stock like name, quantity and price.
    One thing to emphasize here is that the class Stock acts like a factory
    for creating instances of objects. Basically, you call it as a function,
    and it creates a new object for you. Also, it must be emphasized that
    each object is distinct - they each have their own data that is separate
    from other objects that have been created.
    """

    __slots__ = ('name', '_shares', 'price')

    def __init__(self, name, shares, price):
        self._shares = None
        self.name = name
        self.shares = shares
        self.price = price

    def __repr__(self):
        return f"Stock('{self.name}', {self.shares}, {self.price})"

    @property
    def shares(self):
        return self._shares

    @shares.setter
    def shares(self, value):
        if not isinstance(value, int):
            raise TypeError(f"Expected an int but found {type(value)} and value = {value}")
        self._shares = value

    @property
    def cost(self):
        """
        Function to calculate total cost of the stock.
        """
        return self.shares * self.price

    def sell(self, quantity):
        """
        Function to sell 'quantity' amount of stock.
        """
        self.shares = self.shares - quantity if self.shares >= quantity else 0

# portfolio.py

from collections import Counter
from fileparse import parse_csv
from stock import Stock


class Portfolio:

    def __init__(self):
        self._holdings = []

    def __iter__(self):
        return self._holdings.__iter__()

    def __len__(self):
        return len(self._holdings)

    def __getitem__(self, index):
        return self._holdings[index]

    def __contains__(self, name):
        return any([s.name == name for s in self._holdings])

    @property
    def total_cost(self):
        return sum([s.cost for s in self._holdings])

    def append(self, holding):
        if not isinstance(holding, Stock):
            raise TypeError('Expected a Stock instance')
        self._holdings.append(holding)

    @classmethod
    def from_csv(cls, filename, **opts):
        self = cls()
        portfolio_dicts = parse_csv(filename,
                                    select=['name', 'shares', 'price'],
                                    types=[str, int, float],
                                    **opts)

        for d in portfolio_dicts:
            self.append(Stock(**d))

        return self

    def tabulate_shares(self):
        total_shares = Counter()
        for s in self._holdings:
            total_shares[s.name] += s.shares
        return total_shares

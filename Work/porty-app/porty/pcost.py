# pcost.py
#
# Exercise 1.27

from .report import read_portfolio
import sys


def portfolio_cost(filename):
    """
    This takes a portfolio file and outputs the value of total cost.
    """

    portfolio = read_portfolio(filename)
    return portfolio.total_cost


def main(argv):
    print('Total cost:', portfolio_cost(argv[1]))


if __name__ == '__main__':
    main(sys.argv)

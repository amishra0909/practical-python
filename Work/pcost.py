# pcost.py
#
# Exercise 1.27

from report import read_portfolio
import csv
import sys


def portfolio_cost(filename):
    """
    This takes a portfolio file and outputs the value of total cost.
    """
    total = 0.0

    portfolio = read_portfolio(filename)
    for i, row in enumerate(portfolio, start=1):
        try:
            total += row['shares'] * row['price']
        except Exception:
            print(f'Row {i:>2}: Could not convert: {row}')
    # with open(filename, 'rt') as f:
    #     rows = csv.reader(f)
    #     header = next(rows)
    #     for i, row in enumerate(rows, start=1):
    #         record = dict(zip(header, row))
    #         try:
    #             name, shares, price = (record['name'], int(record['shares']), float(record['price']))
    #             total += shares * price
    #         except Exception:
    #             print(f'Row {i:>2}: Could not convert: {row}')
    return total


def main(argv):
    print('Total cost:', portfolio_cost(argv[1]))


if __name__ == '__main__':
    main(sys.argv)

# pcost.py
#
# Exercise 1.27

import csv
import sys

def portfolio_cost(filename):
    '''
    This takes a portfolio file and outputs the value of total cost.
    '''
    total = 0.0
    with open(filename, 'rt') as f:
        rows = csv.reader(f)
        header = next(rows)
        for i, row in enumerate(rows, start = 1):
            record = dict(zip(header, row))
            try:
                name, shares, price = (record['name'], int(record['shares']), float(record['price']))
                total += shares * price
            except:
                print(f'Row {i:>2}: Couldn\'t convert: {row}')
    return total

filename = 'Data/portfolio.csv'
if len(sys.argv) == 2:
    filename = sys.argv[1]

cost = portfolio_cost(filename)
print('Total cost:', cost)

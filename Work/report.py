# report.py
#
# Exercise 2.4

import csv
import sys

def read_portfolio(filename):
    portfolio = []

    with open(filename, 'rt') as f:
        rows = csv.reader(f)
        header = next(rows)
        for row in rows:
            holding = { 'name': row[0], 'shares': int(row[1]), 'price':float(row[2])}
            portfolio.append(holding)

    return portfolio

def read_prices(filename):
    prices = {}

    with open(filename, 'rt') as f:
        rows = csv.reader(f)
        for row in rows:
            try:
                name, price = row[0], float(row[1])
                prices[name] = price
            except:
                print('Invalid row :', row)
    return prices

def gain_or_loss():
    portfolio = read_portfolio('Data/portfolio.csv')
    prices = read_prices('Data/prices.csv')

    total_cost = 0.0
    total_current = 0.0

    for s in portfolio:
        total_cost += s['shares'] * s['price']
        total_current += s['shares'] * prices[s['name']]

    gain = total_cost < total_current
    return total_current, gain

def make_report(portfolio, prices):
    report = []
    for s in portfolio:
        holding = (s['name'], s['shares'], prices[s['name']], round(prices[s['name']] - s['price'], 2))
        report.append(holding)
    return report

def print_report(report):
    for name, shares, price, change in report:
        print(f'{name:>10s} {shares:>10d} {price:>10.2f} {change:>10.2f}')


filename = 'Data/portfolio.csv'
if len(sys.argv) == 2:
    filename = sys.argv[1]

# print(read_portfolio(filename))

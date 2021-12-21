# report.py
#
# Exercise 2.4

import csv
import sys

def read_portfolio(filename):
    '''
    Read a stock portfolio file into a list of dictionaries with keys
    name, shares and price.
    '''
    portfolio = []

    with open(filename, 'rt') as f:
        rows = csv.reader(f)
        header = next(rows)
        for row in rows:
            holding = { 
                    'name': row[0],
                    'shares': int(row[1]),
                    'price':float(row[2])
                }
            portfolio.append(holding)

    return portfolio

def read_prices(filename):
    '''
    Read a stock price file into a dictionary with keys as stock symbols
    and values as prices of the stocks.
    '''
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
    '''
    Calculate the total gain (or loss) using the portfolio and prices
    files.
    '''
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
    '''
    Create a report of each stock from a portfolio list and prices dictionary to show
    name, number of shares, price and current gain (or loss).
    '''
    report = []
    for s in portfolio:
        holding = (s['name'], s['shares'], prices[s['name']], round(prices[s['name']] - s['price'], 2))
        report.append(holding)
    return report

def print_report(report):
    '''
    Print the report calculated from make_report() function.
    '''
    header = ('Name', 'Shares', 'Price', 'Change')
    print(f'{header[0]:>10s} {header[1]:>10s} {header[2]:>10s} {header[3]:>10s}')

    dashes = '-'*10
    print(f'{dashes:>10s} {dashes:>10s} {dashes:>10s} {dashes:>10s}')
    for name, shares, price, change in report:
        price = '$' + str(price)
        print(f'{name:>10s} {shares:>10d} {price:>10s} {change:>10.2f}')

def portfolio_report(portfolio_filename, prices_filename):
    print_report(make_report(read_portfolio(portfolio_filename), read_prices(prices_filename)))

filename = 'Data/portfolio.csv'
if len(sys.argv) == 2:
    filename = sys.argv[1]

# print(read_portfolio(filename))

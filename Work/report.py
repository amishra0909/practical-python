# report.py
#
# Exercise 2.4

from fileparse import parse_csv
import tableformatter
import stock
import sys


def read_portfolio(filename):
    """
    Read a stock portfolio file into a list of dictionaries with keys
    name, shares and price.
    """
    portfolio_dicts = parse_csv('Data/portfolio.csv',
                                select=['name', 'shares', 'price'],
                                types=[str, int, float],
                                has_headers=True)
    portfolio = [stock.Stock(d['name'], d['shares'], d['price']) for d in portfolio_dicts]
    return portfolio


def read_prices(filename):
    """
    Read a stock price file into a dictionary with keys as stock symbols
    and values as prices of the stocks.
    """
    prices = dict(parse_csv(filename, has_headers=False, types=[str, float]))
    return prices


def gain_or_loss():
    """
    Calculate the total gain (or loss) using the portfolio and prices
    files.
    """
    portfolio = read_portfolio('Data/portfolio.csv')
    prices = read_prices('Data/prices.csv')

    total_cost = 0.0
    total_current = 0.0

    for s in portfolio:
        total_cost += s.shares * s.price
        total_current += s.shares * prices[s.name]

    gain = total_cost < total_current
    return total_current, gain


def make_report(portfolio, prices):
    """
    Create a report of each stock from a portfolio list and prices dictionary to show
    name, number of shares, price and current gain (or loss).
    """
    report = []
    for s in portfolio:
        holding = (s.name, s.shares, prices[s.name], round(prices[s.name] - s.price, 2))
        report.append(holding)
    return report


def print_report(report, formatter):
    """
    Print the report calculated from make_report() function.
    """
    formatter.headings(['Name', 'Shares', 'Price', 'Change']);

    for name, shares, price, change in report:
        rowdata = [name, str(shares), '$' + str(price), str(change)]
        formatter.row(rowdata)


def portfolio_report(portfolio_filename, prices_filename):
    formatter = tableformatter.HTMLTableFormatter()
    print_report(make_report(read_portfolio(portfolio_filename), read_prices(prices_filename)), formatter)


def main(argv):
    portfolio_report(argv[1], argv[2])


if __name__ == '__main__':
    main(sys.argv)

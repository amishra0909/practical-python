# ticker.py

from follow import follow
import csv
import report
import tableformatter


def select_columns(rows, indices):
    for current_row in rows:
        yield [current_row[i] for i in indices]


def convert_types(rows, types):
    for current_row in rows:
        yield [func(val) for func, val in zip(types, current_row)]


def make_dicts(rows, headers):
    for current_row in rows:
        yield dict(zip(headers, current_row))


def parse_stock_data(lines):
    rows = csv.reader(lines)
    rows = select_columns(rows, [0, 1, 4])
    rows = convert_types(rows, [str, float, float])
    rows = make_dicts(rows, ['name', 'price', 'change'])
    return rows


def filter_symbols(rows, names):
    # for row in rows:
    #    if row['name'] in names:
    #        yield row
    return (row for row in rows if row['name'] in names)


def ticker(portfolio_filename, stocklog_filename, format):
    headers = ['Name', 'Price', 'Change']

    portfolio = report.read_portfolio(portfolio_filename)
    formatter = tableformatter.create_formatter(format)

    formatter.headings(headers)

    rows = parse_stock_data(follow(stocklog_filename))
    rows = filter_symbols(rows, portfolio)
    for row in rows:
        formatter.row([ row['name'], str(row['price']), str(row['change'])])


if __name__ == '__main__':
    portfolio = report.read_portfolio('Data/portfolio.csv')
    rows = parse_stock_data(follow('Data/stocklog.csv'))
    rows = filter_symbols(rows, portfolio)
    for row in rows:
        print(row)
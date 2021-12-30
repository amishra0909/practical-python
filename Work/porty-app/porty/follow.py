# follow.py

import os
import time
import report


def follow(filename):
    """
    Generator that produces sequence of lines being written at the end of the file.
    """
    file = open(filename, 'r')
    file.seek(0, os.SEEK_END)

    while True:
        file_line = file.readline()
        if file_line == '':
            time.sleep(0.2)
            continue
        yield file_line


if __name__ == '__main__':

    portfolio = report.read_portfolio('Data/portfolio.csv')

    for line in follow('Data/stocklog.csv'):
        fields = line.split(',')
        name = fields[0].strip('"')
        price = float(fields[1])
        change = float(fields[4])
        if name in portfolio:
            print(f'{name:>10s} {price:>10.2f} {change:>10.2f}')

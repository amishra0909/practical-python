# fileparse.py
#
# Exercise 3.3

import csv


def parse_csv(filename, select=None, types=[str, int, float], has_headers=True, delimiter=',', silence_error=False):
    """
    Parse a CSV file into a list of records.
    The param select is optional to choose which columns from the csv file should be read.
    """

    with open(filename) as f:
        rows = csv.reader(f, delimiter=delimiter)

        # Read the file header
        if has_headers:
            headers = next(rows)

        # If a column selector was given, find indices of the specified columns.
        # Also, narrow the set of headers used for resulting dictionaries
        if select:
            if not has_headers:
                raise RuntimeError("select argument requires column headers")
            indices = [headers.index(colname) for colname in select]
            headers = select

        records = []
        for row_number, row in enumerate(rows, start=1):
            if not row:
                continue
            # Filter the row if specific columns are to be selected
            if select:
                row = [row[index] for index in indices]

            if types:
                try:
                    row = [func(val) for func, val in zip(types, row)]
                except Exception as e:
                    if not silence_error:
                        print(f'Row {row_number:>2}: Couldn\'t convert {row}')
                        print(f'Row {row_number:>2}: Reason {e}')

            if has_headers:
                record = dict(zip(headers, row))
                records.append(record)
            else:
                records.append(tuple(row))

        return records

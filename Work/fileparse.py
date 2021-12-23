# fileparse.py
#
# Exercise 3.3

import csv


def parse_internal(enumerator, select=None, types=[str, int, float], has_headers=True, delimiter=',', silence_error=False):
    """
    Parse a CSV record iterator into a list of records.
    The param select is optional to choose which columns from the csv file should be read.
    """

    rows = csv.reader(enumerator)
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
                    print(f'Row {row_number:>2}: Could not convert {row}')
                    print(f'Row {row_number:>2}: Reason {e}')

        if has_headers:
            record = dict(zip(headers, row))
            records.append(record)
        else:
            records.append(tuple(row))

    return records


def parse_csv(filename_or_rows, select=None, types=[str, int, float], has_headers=True, delimiter=',', silence_error=False):
    """
    Parse a CSV record iterator into a list of records.
    The param select is optional to choose which columns from the csv file should be read.
    """
    if type(filename_or_rows) is str:
        with open(filename_or_rows) as f:
            return parse_internal(f, select, types, has_headers, delimiter, silence_error)

    return parse_internal(filename_or_rows, select, types, has_headers, delimiter, silence_error)
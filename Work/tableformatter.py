# tableformatter.py

class TableFormatter:
    """
    A class to define methods for formatting a report in tabular format.
    The two methods exposed are for formatted header section and formatted
    rows.
    """

    def headings(self, headers):
        """
        Emit the table headings
        """
        raise NotImplementedError()

    def row(self, row):
        """
        Emit a single row of table data.
        """
        raise NotImplementedError()


class TextTableFormatter(TableFormatter):
    """
    Emit a table in a plain text format.
    """

    def headings(self, headers):
        for h in headers:
            print(f'{h:>10s}', end=' ')
        print()
        print(('-' * 10 + ' ') * len(headers))

    def row(self, row):
        for d in row:
            print(f'{d:>10s}', end=' ')
        print()


class CSVTableFormatter(TableFormatter):
    """
    Output portfolio data in CSV format.
    """

    def headings(self, headers):
        print(','.join(headers))

    def row(self, row):
        print(','.join(row))


class HTMLTableFormatter(TableFormatter):
    """
    Output portfolio data in HTML format.
    """
    def headings(self, headers):
        header_row = ''.join(['<th>' + header + '</th>' for header in headers])
        print('<tr>' + header_row + '</tr>')

    def row(self, row):
        row_values = ''.join(['<td>' + row_data + '</td>' for row_data in row])
        print('<tr>' + row_values + '</tr>')
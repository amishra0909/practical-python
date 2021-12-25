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
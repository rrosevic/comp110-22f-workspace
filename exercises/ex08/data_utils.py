"""Some helpful utility functions for working with CSV files."""
__author__: str = "730575822"

from csv import DictReader


def read_csv_rows(filename: str) -> list[dict[str, str]]:
    """Read the rows of a CSV into a 'table'."""
    result: list[dict[str, str]] = []
    file_handle = open(filename, "r", encoding="utf8")
    csv_reader = DictReader(file_handle)
    for row in csv_reader:
        result.append(row)
    file_handle.close()

    return result


def column_values(table: list[dict[str, str]], column: str) -> str:
    """Reduce a list[str] of all values in a single column."""
    result: list[str] = []
    for row in table:
        item: str = row[column]
        result.append(item)
    return result


def columnar(row_table: list[dict[str, str]]) -> dict[str, list[str]]:
    """Transform a row-oriented table to a column-oriented table."""
    result: dict[str, list[str]] = {}
    
    first_row: dict[str, str] = row_table[0]
    for column in first_row:
        result[column] = column_values(row_table, column)
    return result


def head(column_data: dict[str, list[str]], num_of_rows: int) -> dict[str, list[str]]:
    """Produce a column-based table with only the first few rows of data per column."""
    result: dict[str, list[str]] = {}
    if num_of_rows >= len(column_data):
        num_of_rows = len(column_data)
    for column in column_data:
        values: list[str] = []
        i: int = 0
        while i < num_of_rows:
            values.append(column_data[column][i])
            i += 1
        result[column] = values
    return result


def select(data_table: dict[str, list[str]], column_name: list[str]) -> dict[str, list[str]]:
    """Produce a column-based table with only the columns you'd need."""
    result: dict[str, list[str]] = {}
    for column in column_name:
        if column in data_table:
            result[column] = data_table[column]
    return result


def concat(data_table_one: dict[str, list[str]], data_table_two: dict[str, list[str]]) -> dict[str, list[str]]:
    """Produce a column-based table with two column-based tables combined."""
    result: dict[str, list[str]] = {}
    for column in data_table_one:
        result[column] = data_table_one[column]
    for column_two in data_table_two:
        if column_two in result:
            result[column_two] += data_table_two[column_two]
        else:
            result[column_two] = data_table_two[column_two]
    return result


def count(list_of_values: list[str]) -> dict[str, int]:
    """Produce a dictionary where each key is a value in the list, each value is how many times it appeared."""
    result: dict[str, int] = {}
    for value in list_of_values:
        if value in result:
            result[value] += 1
        else:
            result[value] = 1
    return result
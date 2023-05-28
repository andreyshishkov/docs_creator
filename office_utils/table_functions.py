import pandas as pd


def get_df(table_path: str):
    return pd.read_excel(table_path)


def get_row(table, row_num):
    return table.values[row_num]
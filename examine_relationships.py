import polars as pl

columns = ['_from', '_to', 'from', 'to', 'number', 'remark', 'resembling', 'type']
main = pl.read_csv('relationships_main.csv', new_columns=columns)
refactored = pl.read_csv('relationships_refactored.csv', new_columns=columns)

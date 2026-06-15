import polars as pl

columns = ['_from', '_to', 'from', 'to', 'number', 'remark', 'resembling', 'type']


def get_main() -> pl.DataFrame:
    return pl.read_csv('relationships_main.csv', new_columns=columns)


def get_refactored() -> pl.DataFrame:
    return pl.read_csv('relationships_refactored.csv', new_columns=columns)


def combine() -> pl.DataFrame:
    return pl.concat(
        [
            get_main().with_columns(pl.lit('main').alias('branch')),
            get_refactored().with_columns(pl.lit('refactored').alias('branch'))
        ]
    )


def branch_count() -> pl.expr.Expr:
    return pl.col('branch').n_unique().over(pl.struct(pl.exclude('branch')))

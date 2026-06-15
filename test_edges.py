import polars as pl
from polars.testing import assert_series_equal

from edges import branch_count


def test_series_equality():
    assert_series_equal(pl.Series('a', [1, 2, 3]), pl.Series('a', [1, 2, 3]))


def test_branch_count():
    df = pl.DataFrame(
        {
            '_to': ['abc', 'abc', 'abc'],
            '_from': ['pqr', 'pqr', 'xyz'],
            'branch': ['main', 'refactored', 'refactored'],
        }
    )

    df = df.with_columns(
        branch_count().alias('branch_count')
    )
    assert_series_equal(df['branch_count'], pl.Series('branch_count', [2, 2, 1], dtype=pl.UInt32))

import polars as pl
from polars.testing import assert_series_equal, assert_frame_equal

from edges import branch_count, in_both_branches, resembling_mentions


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


def test_both_branches():
    count = pl.Series('branch_count', [2, 2, 1], dtype=pl.UInt32)
    assert_series_equal(
        in_both_branches(count).alias('in_both_branches'),
        pl.Series('in_both_branches', [True, True, False], dtype=pl.Boolean)
    )


def test_resembling_mentions():
    df = pl.DataFrame(
        {
            'id': ['a', 'b', 'c', 'd'],
            'type': ['mention', 'mention', 'full', 'full'],
            'resembling': [True, False, True, False],
        }
    )

    assert_frame_equal(
        resembling_mentions(df),
        pl.DataFrame(
            {
                'id': ['a'],
                'type': ['mention'],
                'resembling': [True]
            }
        )
    )

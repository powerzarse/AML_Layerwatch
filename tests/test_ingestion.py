"""Tests for layerwatch.ingestion.

Fixture rows (tests/fixtures/transactions_small.csv):
  1. bank ID "010" with a leading zero
  2. Bitcoin amount 0.000008 (6 decimal places)
  3. exact duplicate of row 2
  4. label 1; to_bank "00220", which collides with "0220" (row 2) as an integer
"""

from pathlib import Path

import pytest

FIXTURE_CSV = Path(__file__).parent / "fixtures" / "transactions_small.csv"


def test_row_count() -> None:
    pytest.skip("TODO: all 4 rows are written, including the duplicate")


def test_bank_ids_keep_leading_zeros() -> None:
    pytest.skip('TODO: from_bank of row 1 is "010"; "0220" and "00220" stay distinct')


def test_amounts_are_exact_decimals() -> None:
    pytest.skip('TODO: amount_paid of row 2 equals Decimal("0.000008")')


def test_label_is_boolean() -> None:
    pytest.skip("TODO: is_laundering is BOOLEAN, only row 4 is True")


def test_transaction_id_is_unique() -> None:
    pytest.skip("TODO: 4 distinct transaction_ids, also for the duplicate rows")


def test_rerun_is_idempotent() -> None:
    pytest.skip("TODO: two runs produce identical data, including transaction_id")

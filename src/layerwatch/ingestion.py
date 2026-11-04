"""Ingest the raw HI-Small transactions CSV into Parquet."""

from pathlib import Path

import duckdb  # noqa: F401  (remove once used)

# Explicit schema: column name -> DuckDB type, in the column order of the raw CSV.
# These names replace the raw header, which contains "Account" twice.
# Decisions: docs/decisions.md (2026-10-30, 2026-11-04).
TRANSACTION_COLUMNS: dict[str, str] = {
    # TODO: 11 entries, e.g. "ts": "TIMESTAMP", ...
}

RAW_TIMESTAMP_FORMAT = "%Y/%m/%d %H:%M"


def ingest_transactions(raw_csv: Path, out_parquet: Path) -> int:
    """Read the raw transactions CSV with an explicit schema and write it to Parquet.

    Adds ``transaction_id`` (row number in file order). Writes to a temporary file
    first and then renames it, so a failed run never leaves a partial Parquet file.

    Args:
        raw_csv: Path to ``HI-Small_Trans.csv``. Read only, never modified.
        out_parquet: Target Parquet file. Overwritten if it exists.

    Returns:
        Number of rows written.
    """
    raise NotImplementedError

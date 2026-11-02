# Decision log

Format: date · decision · alternatives · trade-off.

## 2026-10-27 · Python 3.12

- **Decision:** Pin Python to 3.12 (`>=3.12,<3.13`), using a uv-managed interpreter.
- **Alternatives:** 3.13.
- **Trade-off:** 3.12 has the broadest prebuilt wheel coverage for the ML stack (xgboost, shap, numba). The cost is missing the newest language and runtime features, which this project does not need.

## 2026-10-27 · uv workspace: pipeline and code agents as separate packages

- **Decision:** `layerwatch` (pipeline) and the code agents become separate uv workspace members, each with its own dependencies. The agents member is added in phase 3.
- **Alternatives:** One package containing both, with the boundary enforced by an import-linter rule in CI.
- **Trade-off:** The boundary is enforced by structure: LLM SDKs never enter the pipeline environment, and `layerwatch` cannot import the agents because they are not installed with it. The cost is slightly more configuration than a single package.

## 2026-10-27 · Dependencies added per phase

- **Decision:** Only the dependencies the current phase needs go into `pyproject.toml` / `uv.lock`.
- **Alternatives:** Declare the full stack upfront.
- **Trade-off:** The lockfile stays small and every dependency is justified when it is introduced. The cost is running `uv add` more often.

## 2026-10-27 · Assistant configuration stays out of the repository

- **Decision:** Claude Code instructions live in `.claude/` and are ignored by Git, together with `CLAUDE.md` / `CLAUDE.local.md`.
- **Alternatives:** Commit the instructions, or put them in a generic folder inside the repo.
- **Trade-off:** The repository only contains project artifacts. The cost is that the instructions are not versioned or backed up with the repo.

## 2026-10-29 · Use only the HI-Small variant

- **Decision:** Use only the HI-Small files (`_Trans.csv`, `_Patterns.txt`, `_accounts.csv`). The other variants were deleted locally.
- **Alternatives:** Combine several variants; use Medium or Large.
- **Trade-off:** The variants are independent simulator runs, not parts of one dataset, so combining them would mix unrelated transaction networks. HI-Small fits in laptop memory. The cost is a smaller sample. LI-Small remains an option for a prior-drift experiment in phase 10.

## 2026-10-29 · Ingestion with DuckDB, called from Python

- **Decision:** Read the CSV with DuckDB (`read_csv` with an explicit column schema) and write Parquet with `COPY ... TO`, wrapped in a Python function.
- **Alternatives:** pandas `read_csv(engine="pyarrow")` followed by `to_parquet`.
- **Trade-off:** DuckDB declares the schema in one place, streams the file without loading it fully into memory, and is also the query layer for phase 1. The cost is that type handling is practised in SQL rather than pandas, while later feature work is in pandas.

## 2026-10-30 · Amounts stored as DECIMAL, converted to float in a dedicated function

- **Decision:** Store `amount_received` and `amount_paid` as `DECIMAL` in Parquet. A dedicated function converts them to float for modelling.
- **Alternatives:** `DOUBLE` everywhere.
- **Trade-off:** DECIMAL keeps exact cent values, so equality checks and "just below round threshold" features stay correct. The cost is an explicit conversion step and slightly slower arithmetic. The precision (digits before the decimal point) must be checked against the maximum amount in the file.

## 2026-10-30 · Parquet as the single source of truth, no persistent DuckDB file

- **Decision:** Processed data lives only in Parquet. DuckDB queries it with `read_parquet` or views on an in-memory connection.
- **Alternatives:** Also persist tables in a `.duckdb` file.
- **Trade-off:** With one copy of the data, two stores cannot drift apart and there is less to maintain. The cost is that every query session re-reads Parquet, which is fast enough at this size.

## 2026-10-30 · Timestamps as naive TIMESTAMP

- **Decision:** Store the timestamp as `TIMESTAMP` without time zone.
- **Alternatives:** `TIMESTAMPTZ` with an assumed UTC.
- **Trade-off:** The raw data has no time zone, so a naive type does not invent information. Assumption: all timestamps share one unknown time zone and there are no DST shifts. The cost is that time-of-day features cannot be interpreted as local business hours.

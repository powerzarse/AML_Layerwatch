# AML_Layerwatch

AML transaction monitoring prototype on the IBM AML dataset (HI-Small): typology-based features, rule baseline vs. supervised vs. unsupervised models, time-based evaluation with Precision@k, drift checks, back-testing and a model card. Includes custom LLM code agents with their own eval set.

## Data source

IBM *Transactions for Anti Money Laundering (AML)*, variant **HI-Small** — synthetic account-to-account transfers with an `Is Laundering` label and a file describing the embedded laundering patterns.

- Kaggle: https://www.kaggle.com/datasets/ealtman2019/ibm-transactions-for-anti-money-laundering-aml
- Paper: Altman et al., *Realistic Synthetic Financial Transactions for Anti-Money Laundering Models* (NeurIPS 2023 Datasets and Benchmarks)

Download the HI-Small files manually into `data/raw/`. Raw data is never modified and never committed.

## Repository layout

| Path | Content |
|---|---|
| `data/raw/` | Original files (immutable, not in Git) |
| `data/processed/` | Derived Parquet files (not in Git) |
| `notebooks/` | Lean EDA; reusable logic lives in `src/` |
| `src/layerwatch/` | AML pipeline code |
| `tests/` | Tests |
| `configs/` | Paths, time windows, thresholds, model parameters |
| `docs/` | Model card, decision log |

## Setup

Requires [uv](https://docs.astral.sh/uv/).

```bash
uv sync
uv run pre-commit install
uv run pytest
```

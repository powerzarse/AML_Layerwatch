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

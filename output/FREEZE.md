# Frozen submission · team HSA Connection

- **Frozen on:** 2026-11-06, agreed with the team.
- **File:** `HSA_Connection.csv` (199,319 frames, `frame,label`), SHA-256 `92a943257cf73aaa057aa81cf29902732b72f2b545b95410ae5b2608b1a0f8fb`, checked with the official validator.
- **Model description:** `frozen_model.json`, SHA-256 `9e95cc7201feca1d7f6ca7a0891a46fce5f913b6cb97656c3d3448353057ef0b`.
- **Created by:** `notebooks/04_submission.ipynb`, run order 01 → 02 → 03 → 04. A full run from the raw data reproduces the submission file bit for bit.

## Model

- D model: boosting on base, multi-scale and possession features (159 features).
- H model: boosting on possession features and robust team shape (59 features).
- Decoder: joint Viterbi with c_HA = 10, c_D = 40, then kick snap, kick-off rule and restart prior (w = 4).
- Trained on 7 DFL matches (degraded, d67s) and 3 Metrica sample matches.

## External validation (spellF1, leave-one-match-out over 10 matches)

| | Metrica (main criterion) | DFL d67s |
|---|---:|---:|
| Submission | 0.646 | 0.477 |
| Baseline smooth50 | 0.405 | 0.214 |

The public 5-minute ground truth did not influence any decision.

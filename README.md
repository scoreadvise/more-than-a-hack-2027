# HSA Connection · Ball possession from tracking

Submission of team **HSA Connection** for More Than A Hack 2027, Initial Challenge. For every frame of Barcelona–Athletic we predict `H`, `A`, `D` or `X` from the automatic tracking only. All models are trained on external matches, not on the challenge ground truth or the video.

- How the approach works and what it takes into account: [EXPLANATION.md](EXPLANATION.md)
- Technical document of the submission: [HSA_Connection.md](HSA_Connection.md) or [HSA_Connection.pdf](HSA_Connection.pdf)

## Contents

```
├── notebooks/
│   ├── 01_dfl_data.ipynb        load the DFL matches, H/A/D labels
│   ├── 02_degradation.ipynb     match the DFL data to the dropouts of the challenge tracking (d67s)
│   ├── 03_metrica.ipynb         Metrica sample matches, labels from events
│   └── 04_submission.ipynb      training, cost selection, prediction, CSV, validation
├── output/                      frozen submission: HSA_Connection.csv, frozen_model.json, FREEZE.md
├── external_data/               download lists and checksums (no raw data)
├── reference/                   official challenge repository as an archive (scorer/validator, MIT; github.com/metrica-sports/more-than-a-hack-2027, commit 3de6b60)
├── tactical/                    put the challenge inputs here (not included)
└── requirements.txt
```

**Not included:** raw data (DFL 2.5 GB, Metrica 0.2 GB), challenge match data and intermediate files (`artifacts/`, created when the notebooks run). The challenge data must not be redistributed.

## Result

| spellF1, leave-one-match-out over 10 external matches | Metrica | DFL (degraded) |
|---|---:|---:|
| Official baseline smooth50 | 0.405 | 0.214 |
| **Our approach** | **0.646** | **0.477** |

Submission file `output/HSA_Connection.csv`, SHA-256 `92a943257cf73aaa057aa81cf29902732b72f2b545b95410ae5b2608b1a0f8fb`, frozen on 2026-11-06.

## Reproduction

1. Environment (Python 3.11):

   ```bash
   python3.11 -m venv ~/.venvs/mtah_v2 && ~/.venvs/mtah_v2/bin/pip install -r requirements.txt && ~/.venvs/mtah_v2/bin/python -m ipykernel install --user --name mtah_v2
   ```

2. Download the DFL raw data (21 files, about 2.5 GB, MD5-checked against figshare):

   ```bash
   cd external_data/dfl_idsse && mkdir -p raw && while IFS=$'\t' read -r name url md5 size; do curl -sSL --retry 3 -o "raw/$name" "$url" && [ "$(md5 -q "raw/$name")" = "$md5" ] && echo "$name OK"; done < files.tsv
   ```

3. Download the Metrica data (9 files, about 215 MB, commit e706dd5, SHA-256-checked):

   ```bash
   cd external_data/metrica_sample && mkdir -p raw && for f in Sample_Game_1/Sample_Game_1_RawEventsData.csv Sample_Game_1/Sample_Game_1_RawTrackingData_Away_Team.csv Sample_Game_1/Sample_Game_1_RawTrackingData_Home_Team.csv Sample_Game_2/Sample_Game_2_RawEventsData.csv Sample_Game_2/Sample_Game_2_RawTrackingData_Away_Team.csv Sample_Game_2/Sample_Game_2_RawTrackingData_Home_Team.csv Sample_Game_3/Sample_Game_3_events.json Sample_Game_3/Sample_Game_3_metadata.xml Sample_Game_3/Sample_Game_3_tracking.txt; do curl -sSL -o "raw/$(basename $f)" "https://raw.githubusercontent.com/metrica-sports/sample-data/e706dd506b360d69d9d123d5b8026e7294b13996/data/$f"; done && (cd raw && shasum -a 256 -c ../sha256.txt --ignore-missing)
   ```

4. Copy `BAR-ATH_tactical_atd.txt` and `BAR-ATH_tactical_atd.xml` into `tactical/`.

5. Run the four notebooks in order:

   ```bash
   cd notebooks && for nb in 01_dfl_data 02_degradation 03_metrica 04_submission; do ~/.venvs/mtah_v2/bin/jupyter nbconvert --to notebook --execute --inplace --ExecutePreprocessor.kernel_name=mtah_v2 --ExecutePreprocessor.timeout=10800 $nb.ipynb; done
   ```

Notebook 04 writes `output/HSA_Connection.csv` and prints its SHA-256. With the pinned packages the file is bit-identical to the submission. A full run takes about 20 minutes on a laptop.

Note for macOS with ExFAT drives: do not put the venv on such a drive; the `._` files macOS creates there break Python.

## Data and licences

- DFL/IDSSE: Bassek, Rein, Weber & Memmert (2025), *Scientific Data*, https://doi.org/10.1038/s41597-025-04505-y. Data © DFL Deutsche Fußball Liga, CC BY 4.0.
- Metrica Sports Sample Data (https://github.com/metrica-sports/sample-data, commit e706dd5): 3 anonymised matches without a formal licence file; the README asks for attribution. Details in `external_data/metrica_sample/README.md`.
- Challenge data and frame data derived from it stay local.

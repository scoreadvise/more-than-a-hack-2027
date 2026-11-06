# External data · DFL/IDSSE open data

External training and tuning data. These are **other matches** than Barcelona–Athletic; under the rules email of 2026-11-04, training and tuning are only allowed on external data.

- **Source:** figshare, article 28196177, DOI [10.6084/m9.figshare.28196177](https://doi.org/10.6084/m9.figshare.28196177), published 2025-02-02. Mirror: Hugging Face `pysport/idsse-data`.
- **Content:** 7 matches, 1st and 2nd Bundesliga 2022/23, TRACAB position data at 25 Hz (XML), event data, match information. Ball frames contain `BallPossession` (1 = home, 2 = away) and `BallStatus` (0 = dead, 1 = alive).
- **Licence:** [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/). Attribution to DFL and the paper, link to the licence, changes marked.
- **Retrieved:** 2026-11-05 via the figshare API. `figshare_article.json` holds the original metadata, `files.tsv` file name, URL, MD5 and size, `manifest.json` additionally the SHA-256 of the local files.
- **Storage:** local only, under `raw/`, not in the public repository; the repository downloads it via `files.tsv` instead.

## Citation

Bassek, M., Rein, R., Weber, H. & Memmert, D. (2025). An integrated dataset of spatiotemporal and event data in elite soccer. *Scientific Data*. https://doi.org/10.1038/s41597-025-04505-y

Data © DFL Deutsche Fußball Liga, licensed under CC BY 4.0.

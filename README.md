# HSA Connection · Ballbesitz aus Tracking

Abgabe von Team **HSA Connection** für More Than A Hack 2027, Initial Challenge. Für jeden Frame von Barcelona–Athletic wird `H`, `A`, `D` oder `X` vorhergesagt, und zwar nur aus dem automatischen Tracking. Alle Modelle sind auf externen Spielen trainiert, nicht auf der Challenge-GT oder dem Video.

- Wie der Ansatz funktioniert und was er beachtet: [ERKLAERUNG.md](ERKLAERUNG.md)
- Technisches Dokument für die Abgabe: [HSA_Connection.md](HSA_Connection.md) bzw. [HSA_Connection.pdf](HSA_Connection.pdf)

## Inhalt

```
├── notebooks/
│   ├── 01_dfl_daten.ipynb       DFL-Spiele laden, H/A/D-Labels
│   ├── 02_degradation.ipynb     DFL an die Ausfälle des Challenge-Trackings angleichen (d67s)
│   ├── 03_metrica.ipynb         Metrica-Beispielspiele, Labels aus Events
│   └── 04_abgabe.ipynb          Training, Kostenwahl, Vorhersage, CSV, Validierung
├── output/                      eingefrorene Abgabe: HSA_Connection.csv, frozen_model.json, FREEZE.md
├── external_data/               Download-Listen und Prüfsummen (ohne Rohdaten)
├── reference/                   offizielles Challenge-Repository als Archiv (Scorer/Validator, MIT; github.com/metrica-sports/more-than-a-hack-2027, Commit 3de6b60)
├── tactical/                    hier die Challenge-Eingaben ablegen (nicht enthalten)
└── requirements.txt
```

**Nicht enthalten:** Rohdaten (DFL 2,5 GB, Metrica 0,2 GB), Challenge-Daten und Zwischenstände (`artifacts/`, wird beim Lauf erzeugt). Die Challenge-Daten dürfen nicht weitergegeben werden.

## Ergebnis

| spellF1, Leave-one-match-out über 10 externe Spiele | Metrica | DFL (degradiert) |
|---|---:|---:|
| Offizielle Baseline smooth50 | 0,405 | 0,214 |
| **unser Ansatz** | **0,646** | **0,477** |

Abgabedatei `output/HSA_Connection.csv`, SHA-256 `92a943257cf73aaa057aa81cf29902732b72f2b545b95410ae5b2608b1a0f8fb`, eingefroren am 06.11.2026.

## Reproduktion

1. Umgebung (Python 3.11):

   ```bash
   python3.11 -m venv ~/.venvs/mtah_v2 && ~/.venvs/mtah_v2/bin/pip install -r requirements.txt && ~/.venvs/mtah_v2/bin/python -m ipykernel install --user --name mtah_v2
   ```

2. DFL-Rohdaten laden (21 Dateien, ca. 2,5 GB, MD5 gegen Figshare geprüft):

   ```bash
   cd external_data/dfl_idsse && mkdir -p raw && while IFS=$'\t' read -r name url md5 size; do curl -sSL --retry 3 -o "raw/$name" "$url" && [ "$(md5 -q "raw/$name")" = "$md5" ] && echo "$name OK"; done < files.tsv
   ```

3. Metrica-Daten laden (9 Dateien, ca. 215 MB, Commit e706dd5, SHA-256 geprüft):

   ```bash
   cd external_data/metrica_sample && mkdir -p raw && for f in Sample_Game_1/Sample_Game_1_RawEventsData.csv Sample_Game_1/Sample_Game_1_RawTrackingData_Away_Team.csv Sample_Game_1/Sample_Game_1_RawTrackingData_Home_Team.csv Sample_Game_2/Sample_Game_2_RawEventsData.csv Sample_Game_2/Sample_Game_2_RawTrackingData_Away_Team.csv Sample_Game_2/Sample_Game_2_RawTrackingData_Home_Team.csv Sample_Game_3/Sample_Game_3_events.json Sample_Game_3/Sample_Game_3_metadata.xml Sample_Game_3/Sample_Game_3_tracking.txt; do curl -sSL -o "raw/$(basename $f)" "https://raw.githubusercontent.com/metrica-sports/sample-data/e706dd506b360d69d9d123d5b8026e7294b13996/data/$f"; done && (cd raw && shasum -a 256 -c ../sha256.txt --ignore-missing)
   ```

4. `BAR-ATH_tactical_atd.txt` und `BAR-ATH_tactical_atd.xml` nach `tactical/` kopieren.

5. Die vier Notebooks der Reihe nach ausführen:

   ```bash
   cd notebooks && for nb in 01_dfl_daten 02_degradation 03_metrica 04_abgabe; do ~/.venvs/mtah_v2/bin/jupyter nbconvert --to notebook --execute --inplace --ExecutePreprocessor.kernel_name=mtah_v2 --ExecutePreprocessor.timeout=10800 $nb.ipynb; done
   ```

Notebook 04 schreibt `output/HSA_Connection.csv` und gibt den SHA-256 aus. Mit den gepinnten Paketen ist die Datei bitgleich mit der Abgabe.

Hinweis für macOS mit ExFAT-Laufwerken: Die venv nicht auf das Laufwerk legen, die `._`-Dateien von macOS stören Python.

## Daten und Lizenz

- DFL/IDSSE: Bassek, Rein, Weber & Memmert (2025), *Scientific Data*, https://doi.org/10.1038/s41597-025-04505-y. Daten © DFL Deutsche Fußball Liga, CC BY 4.0.
- Metrica Sports Sample Data (https://github.com/metrica-sports/sample-data, Commit e706dd5): 3 anonymisierte Spiele ohne formale Lizenzdatei; die README bittet um Quellenangabe. Details in `external_data/metrica_sample/README.md`.
- Challenge-Daten und daraus abgeleitete Frame-Daten bleiben lokal.

Die Entwicklung (Notebooks zu Varianten, Fehleranalysen und verworfenen Ideen) liegt im Hauptprojekt unter `approach_v2/` und ist nicht Teil dieses Pakets.

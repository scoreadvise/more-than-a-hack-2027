# Externe Daten · DFL/IDSSE Open Data

Externe Trainings- und Tuningdaten. **Andere Spiele** als Barcelona–Athletic; gemäß Regel-Mail vom 04.11.2026 ist Training/Tuning ausschließlich auf externen Daten erlaubt.

- **Quelle:** Figshare, Artikel 28196177, DOI [10.6084/m9.figshare.28196177](https://doi.org/10.6084/m9.figshare.28196177), veröffentlicht 02.02.2025. Spiegel: Hugging Face `pysport/idsse-data`.
- **Inhalt:** 7 Spiele, 1. und 2. Bundesliga 2022/23, TRACAB-Positionsdaten mit 25 Hz (XML), Eventdaten, Matchinformationen. Ballframes enthalten `BallPossession` (1 = Heim, 2 = Auswärts) und `BallStatus` (0 = unterbrochen, 1 = aktiv).
- **Lizenz:** [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/). Namensnennung von DFL und Paper, Lizenzlink, Änderungen kennzeichnen.
- **Abruf:** 05.11.2026 per Figshare-API. `figshare_article.json` enthält die Original-Metadaten, `files.tsv` Dateiname, URL, MD5 und Größe, `manifest.json` zusätzlich SHA-256 der lokalen Dateien.
- **Ablage:** Nur lokal unter `raw/`, nicht ins öffentliche Repository; dort wird stattdessen über `files.tsv` nachgeladen.

## Zitation

Bassek, M., Rein, R., Weber, H. & Memmert, D. (2025). An integrated dataset of spatiotemporal and event data in elite soccer. *Scientific Data*. https://doi.org/10.1038/s41597-025-04505-y

Data © DFL Deutsche Fußball Liga, lizenziert unter CC BY 4.0.

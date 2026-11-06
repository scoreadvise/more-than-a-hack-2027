# Metrica Sports sample data

- Source: https://github.com/metrica-sports/sample-data, commit `e706dd506b360d69d9d123d5b8026e7294b13996`, downloaded on 2026-11-06 via raw.githubusercontent.com.
- Content: 3 anonymised matches with tracking (25 fps, coordinates 0–1, pitch 105 × 68 m) and synchronised events. Matches 1 and 2 are CSV files, match 3 uses the EPTS FIFA format (`.txt` + `.xml`) with events as JSON.
- Checksums: `sha256.txt` (SHA-256 per file in `raw/`).
- Use: there is no formal licence file. The repository README asks for responsible use and for attribution when used publicly. The data was published for interested people and the analytics community to experiment with. The publisher is Metrica Sports, the organiser of the challenge. A question to the organiser about using it in the challenge is pending.
- Role here: additional external training and validation matches. Labels are derived automatically from the events of these matches by a documented rule. Data of the challenge match is not involved.
- Raw data and derived frame data are not in the public repository; it only contains the download command.

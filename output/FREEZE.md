# Eingefrorene Abgabe · Team HSA Connection

- **Eingefroren am:** 2026-11-06, mit dem Team abgestimmt.
- **Datei:** `HSA_Connection.csv` (199.319 Frames, `frame,label`), SHA-256 `92a943257cf73aaa057aa81cf29902732b72f2b545b95410ae5b2608b1a0f8fb`, vom offiziellen Validator geprüft.
- **Modellbeschreibung:** `frozen_model.json`, SHA-256 `9e95cc7201feca1d7f6ca7a0891a46fce5f913b6cb97656c3d3448353057ef0b`.
- **Erzeugt durch:** `notebooks/04_abgabe.ipynb`, Reihenfolge 01 → 02 → 03 → 04. Nach der Vereinfachung des Codes am 06.11.2026 ergibt ein vollständiger Lauf ab den Rohdaten dieselbe Abgabedatei.

## Modell

- D-Modell: Boosting auf Basis-, mehrskaligen und Besitzmerkmalen (159 Merkmale).
- H-Modell: Boosting auf Besitzmerkmalen und robuster Teamform (59 Merkmale).
- Decoder: gemeinsamer Viterbi mit c_HA = 10, c_D = 40, danach Kick-Snap, Anstoß-Regel und Wiederanpfiff-Prior (w = 4).
- Trainiert auf 7 DFL-Spielen (degradiert, d67s) und 3 Metrica-Beispielspielen.

## Externe Validierung (spellF1, Leave-one-match-out über 10 Spiele)

| | Metrica (Hauptkriterium) | DFL d67s |
|---|---:|---:|
| Abgabe | 0,646 | 0,477 |
| Baseline smooth50 | 0,405 | 0,214 |

Die öffentliche 5-Minuten-GT hat keine Entscheidung beeinflusst.

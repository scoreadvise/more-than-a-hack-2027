# More Than A Hack 2027 · Ballbesitzklassifikation

Wir schätzen für jeden Frame von Barcelona–Athletic ein Label: `H` (Barcelona), `A` (Athletic), `D` (Unterbrechung) oder `X` (keine Aussage). Das taktische Video umfasst 199.319 Frames bei 25 FPS.

## Ansatz

**Spatial Hybrid v1 ist der aktuelle Hauptstand.** Physics v3 kombiniert bestehende Statusvorhersagen, Heuristiken und physikalische Evidenz mit Viterbi. Innerhalb von LIVE entstehen H/A-Besitzphasen aus Heuristik- und Kontaktlabels. Der Hybrid richtet bestehende H/A-Grenzen anhand räumlicher Ballnähe zeitlich aus: höchstens ±3 Sekunden, begrenzt durch benachbarte Phasen. D/X und die Phasenfolge bleiben erhalten. Das Verfahren arbeitet offline.

Der anschließende Videopilot untersucht T-DEED-Aktionsvorhersagen als zusätzliche Kontaktevidenz. Er hat bisher keine Ballbesitzentscheidung verändert.

## Notebooks in Lesereihenfolge

| Schritt | Notebook | Inhalt und Ergebnis |
|---|---|---|
| 1 | [01 · Vorbereitung](main%20approach/01_vorbereitung/01_vorbereitung.ipynb) | Tracking und gespeicherte Vorstufen → Physics v3 und Distanzdifferenz als NPZ |
| 2 | [02 · Spatial Hybrid v1](main%20approach/02_spatial_hybrid_v1/02_spatial_hybrid_v1.ipynb) | Räumliche Kandidaten → zeitliche Ausrichtung → Diagnosen und vollständige CSVs |
| 3 | [03 · Videoaktionen](main%20approach/03_videoaktionen/03_videoaktionen.ipynb) | Fünf automatische Clips → T-DEED auf CPU → Vorhersagen und lokale Videoansicht |
| 4 | [04 · Kontaktdiagnose](main%20approach/04_kontaktdiagnose/04_kontaktdiagnose.ipynb) | Videoevents und Trackingkontakte → Zuordnung, Negativkontrolle und Featuretabelle |
| 5 | [05 · Fusionspilot](main%20approach/05_fusionspilot/05_fusionspilot.ipynb) | Kontaktevidenz und begrenztes Grenzalignment → Vergleich mit v1 |

Bei vorhandener NPZ direkt mit Notebook 02 beginnen. Die Videostrecke 03–05 folgt danach in dieser Reihenfolge; Notebook 05 liest die von 03/04 erzeugten Ergebnisse unter `output/`.

Jedes aktive Notebook folgt Eingaben → Methode → Berechnung → Ergebnisse → Fazit. Alle eigenen Imports stehen in der ersten Codezelle. Assertions, wiederholte Datei-Hashkontrollen, Audit-/Freigabetexte und automatische Langberichte sind aus diesen fünf Notebooks entfernt. Die frühere Fassung liegt unter `_archive/notebook_cleanup_20261029/`.

## Bisherige Ergebnisse

| Stand | Spell-F1 | Macro-F1 |
|---|---:|---:|
| Physics v3 | 0,543590 | 0,854311 |
| Spatial Hybrid v1 | 0,564103 | 0,865360 |

Historische Werte der offiziellen öffentlichen Evaluation vom 28. Oktober 2026; die aktiven Modellnotebooks zeigen sie als Vergleich und berechnen sie nicht erneut. Das bekannte Entwicklungsfenster umfasst 7.500 Frames; es ist kein unabhängiger Generalisierungsnachweis.

- v1 verschiebt 150 von 258 direkten H/A-Grenzen und ändert insgesamt 2.143 Frames.
- T-DEED erzeugt im bisherigen 60-Sekunden-Pilot 47 Vorhersagen: 25 PASS, 20 DRIVE, 2 HIGH PASS. Event-/Teamqualität ist nicht unabhängig validiert.
- In der Kontaktdiagnose werden 19/47 Events innerhalb ±0,5 s zugeordnet. Die Negativkontrolle zeigt keine robuste überzufällige Ausrichtung.
- Beide v2-Varianten ändern 0 Frames und 0 Besitzgrenzen. Die Clips überdecken das öffentliche Fenster nicht; der öffentliche Score kann ihren Fusionsnutzen nicht bewerten.

## Lokal ausführen

Benötigt werden die berechtigten lokalen Matchdaten unter `tactical/`, die [gespeicherten Eingaben](artifacts/README.md) und für Notebook 03 die [separate Video-Umgebung](artifacts/video_event_spotting/README.md). v1 wurde mit Python 3.11.7, NumPy 1.26.4, pandas 2.3.3 und Matplotlib 3.10.7 ausgeführt.

Notebook 01 berechnet die Physics-v3-Eingaben mit vorhandenen Heuristik-, AdaBoost-/OOF-Vorhersagen und Bewegungsfeatures. Die frühere Hybridvorhersage dient nur als gespeicherter Vergleichswert für Notebook 02. Ein vollständiger Neuaufbau aller Vorstufen allein aus Rohdaten ist weiterhin nicht nachgewiesen.

Die [Methodik](main%20approach/SPATIAL_HYBRID_V1_TEAM_METHODIK.md) erläutert Parameter und Herkunft. Neue quantitative Entwicklung benötigt zulässige unabhängige Daten.

## Historische Quellen

- [Aufgabenbeschreibung und Abgabeüberblick](docs/CHALLENGE_OVERVIEW.md): bisherige Repository-README.

- [Entwicklungsnotebook 05](main%20approach/05_hierachical_modell.ipynb) und [Vorstufen 04/06/08](main%20approach/upstream/README.md): erhaltene Originalentwicklung.
- [Exploration](exploration/README.md) und [offizielle Baseline](evaluation/02_offizielle_baseline.ipynb): Datenverständnis und Ausgangsverfahren.
- [Videopilot](reports/EVENT_SPOTTING_PILOT_REPORT.md), [Kontaktdiagnose](reports/ALIGNMENT_REPORT.md) und [Fusion](reports/FUSION_PILOT_REPORT.md): historische Berichte des Piloten.
- [Abgeschlossener Audit](reports/compliance_audit/FINAL_COMPLIANCE_REPORT.md): historische Dokumentation; v1 bleibt gemäß Projektklarstellung vom 29. Oktober als Bestandsstand akzeptiert.

Originalentwicklung und historische Berichte bleiben unverändert. Ihre Zellnummern, Prüfabläufe und Pfade beschreiben die damaligen Fassungen.

## Teamübergabe

Für die Codeübergabe werden Notebook-Ausgaben entfernt; Rohdaten, Bilder, Clips, Trackingauszüge und externe Gewichte bleiben lokal. Das Übergabepaket dient dem Code-Review und benötigt die dokumentierten lokalen Eingaben zur Ausführung.

Dieses Paket enthält Codekopien ohne gespeicherte Notebook-Ausgaben. Archivstände, lokale Eingaben und in historischen Berichten erwähnte Evidenzdateien liegen im Gesamtprojekt; das Paket allein ist kein vollständiger Raw-to-Submission-Build.

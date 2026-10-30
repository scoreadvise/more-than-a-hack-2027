# Lokale Eingaben

| Pfad | Inhalt |
|---|---|
| `upstream/contact_classification/` | Ursprüngliche Kontaktlabels, Baseline und Kontaktparameter |
| `upstream/stoppage_detection/` | Heuristik-06-Labels und ursprüngliche Metadaten |
| `upstream/player_status_ml/` | Gespeicherte AdaBoost-/OOF-Vorhersagen, Modelle und Trainingsmetadaten |
| `upstream/movement_features.csv` | Bewegungsfeatures für Physics v3 |
| `spatial_hybrid_v1/inputs/` | NPZ für Notebook 02 |
| `spatial_hybrid_v1/references/` | Frühere Physics-/Hybrid-Vorhersagen als feste Vergleichswerte |
| `spatial_hybrid_v1/provenance/` | Historische Herkunfts- und Umzugsprotokolle |
| `video_event_spotting/` | Lokale T-DEED-Quellen, Gewichte und separate Laufzeitbeschreibung |

Notebook 01 berechnet Physics v3 und die räumliche Distanzdifferenz aus Rohtracking und gespeicherten Vorstufen. Die frühere Hybridvorhersage wird als Vergleichswert in die NPZ übernommen. Ein vorhandener NPZ-Export bleibt unverändert; bei fehlender Datei wird er neu gespeichert. Der externe Exporter bleibt als historisches Werkzeug erhalten und wird im aktiven Ablauf nicht mehr benötigt.

Notebook 02 berechnet den Hybrid und schreibt neue CSVs, Diagnosen und Abbildungen nach `output/`. Das vollständige Trainieren und Erzeugen aller Vorstufen allein aus Rohdaten ist weiterhin nicht nachgewiesen.

Für die Videostrecke zuerst Notebook 03 ausführen, danach 04 und 05. Deren lokale Ergebnisse unter `output/video_event_spotting_pilot/` dienen den folgenden Notebooks als Eingaben. Ein Löschen von `output/` erfordert deshalb die erneute Ausführung dieser Vorstufen.

Die Daten, Modelle, Trackingauszüge und externen Gewichte bleiben außerhalb des Codepakets für GitHub.

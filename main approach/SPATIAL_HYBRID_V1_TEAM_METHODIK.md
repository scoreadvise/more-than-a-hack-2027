# Spatial Hybrid v1 · Methodik

Stand: 29. Oktober 2026. Vorbereitung in Notebook 01, Hybrid und Export in Notebook 02. Die ursprüngliche Entwicklung bleibt in `05_hierachical_modell.ipynb` erhalten.

## Ziel und Daten

Für alle 199.319 Frames bei 25 FPS wird `H`, `A`, `D` oder `X` ausgegeben. `H` steht für kontrollierten Barcelona-Besitz, `A` für Athletic, `D` für Unterbrechung und `X` für keine Aussage. Eine Berührung allein ist kein Besitzwechsel.

Grundlage ist das taktische Tracking. Die 46 Track-Slots sind keine stabilen Spieleridentitäten. Die Halbzeiten umfassen Frames 11.185–90.651 und 110.808–190.197, jeweils inklusive. Fehlende Ballbeobachtungen bleiben fehlende räumliche Evidenz.

## 1. Vorbereitung: Physics v3

Notebook 01 lädt die bestehenden Heuristik-06-, Kontakt-04- und AdaBoost-08-Vorhersagen sowie Bewegungsfeatures. Im ursprünglichen öffentlichen Abschnitt werden die gespeicherten OOF-Statusvorhersagen eingesetzt. Die historische Trainingsherkunft bleibt in Notebook 08 und im abgeschlossenen Audit dokumentiert; die Vorbereitung trainiert kein Modell.

Rohkoordinaten werden anhand der XML-Metadaten in Meter und Teams überführt. Die Kontaktgeometrie verwendet RTS-Glättung auf vollständigen beobachteten Ballruns. Parameter aus `artifacts/upstream/contact_classification/run_manifest.json`: Mess-Sigma 0,25 m, Prozess-Sigma 20 m/s², minimale Ballrun-Länge 1 s, Randschutz 0,4 s, Beschleunigungspeak mindestens 4 m/s² und nächster Spieler höchstens 2 m entfernt.

Die D/L-Evidenz verbindet AdaBoost und Heuristik. Bei Modellwiderspruch schwächen Spielerbewegung, Ballgeschwindigkeit, Ballabdeckung und Nähe die D-Evidenz ab. Die No-Ball-Regel ergänzt deutliche Spielerbewegung bei weitgehend fehlendem Balltracking. Beide Gewichte bleiben 1,5; Viterbi verwendet `logit / FPS` und Wechselkosten 1,0.

`reconstruct_possession` priorisiert H/A aus Heuristik 06 und ergänzt fehlende Signale aus Kontaktmodell 04. Innerhalb eines LIVE-Segments wird das letzte verfügbare Label fortgeführt; am Anfang wird das erste spätere Signal rückwärts übernommen. D trennt die Segmente.

## 2. Räumliche Evidenz

Aus den ursprünglichen Trackingkoordinaten wird je Team die kleinste Ball-Spieler-Distanz berechnet:

\[
d_H(t)=\min_{i\in H}\lVert b(t)-p_i(t)\rVert_2,\qquad
d_A(t)=\min_{j\in A}\lVert b(t)-p_j(t)\rVert_2.
\]

Die Differenz `d_A − d_H` ist positiv, wenn H näher ist. Diese Teamdistanzen verwenden den ursprünglichen Ball; die physikalische Nähe in Physics v3 verwendet dagegen den RTS-geglätteten Ball.

Ein zentrierter Rolling-Median über elf Frames mit mindestens acht gültigen Werten glättet die Differenz. Direkte Vorzeichenwechsel liefern A→H- bzw. H→A-Kandidaten. Ein fehlender oder nullwertiger geglätteter Wert unterbricht die direkte Folge; einzelne fehlende Rohwerte können bei ausreichender Fensterabdeckung dennoch einen Median erlauben.

## 3. Zeitliche Ausrichtung

Notebook 02 betrachtet jeden bestehenden direkten Physics-v3-H/A-Wechsel innerhalb LIVE und der Halbzeiten. Der Suchradius lautet:

```python
min(round(3.0 * fps), (frame - left - 1) // 2, (right - frame - 1) // 2)
```

`left` und `right` bezeichnen benachbarte ursprüngliche Wechsel bzw. LIVE-Segmentgrenzen; das rechte Segmentende ist exklusiv. Der nächstgelegene räumliche Kandidat gleicher Wechselrichtung wird gewählt, bei Gleichstand der erste zeitlich sortierte Kandidat. Ohne Kandidaten bleibt die Grenze erhalten.

Nur die Frames zwischen alter und neuer Grenze werden umgeschrieben. Phasenfolge, Phasenanzahl und D/X bleiben erhalten. Zentrierte Glättung und beidseitige Suche verwenden zukünftige Frames: Das Verfahren ist offline.

## Ergebnisse

Historische offizielle Werte aus dem öffentlichen Entwicklungsfenster:

| Modell | Spell-F1 | Macro-F1 |
|---|---:|---:|
| Physics v3 | 0,543590 | 0,854311 |
| Spatial Hybrid v1 | 0,564103 | 0,865360 |

150 von 258 direkten H/A-Grenzen wurden verschoben; insgesamt ändern sich 2.143 Frames. Im öffentlichen Fenster waren es 261 Frames, davon 179 zuvor falsch und anschließend richtig sowie 82 zuvor richtig und anschließend falsch.

Die fünf öffentlichen Minuten wurden bereits während der Entwicklung verwendet. Diese Werte sind historische Vergleichswerte, kein unabhängiger Generalisierungsnachweis. Die bereinigten Notebooks berechnen sie nicht neu.

## Ausführung und Herkunft

Notebook 01 schreibt bei fehlender Datei die NPZ unter `artifacts/spatial_hybrid_v1/inputs/`. Sie enthält Physics-v3-Labels, Status, Distanzdifferenz, Halbzeiten, Framezahl und FPS. `expected_hybrid` stammt aus der erhaltenen früheren Hybridvorhersage und dient ausschließlich dem nachgelagerten Vergleich in Notebook 02.

Notebook 02 lädt die NPZ, berechnet den Hybrid, zeigt Verteilungen und Zeitverschiebungen und schreibt CSVs, Diagnosen und Abbildungen in einen neuen Laufordner unter `output/team_spatial_hybrid_v1/`. Die Ausgabe hat die Spalten `frame,label`, beginnend mit Frame 0.

Ein vollständiger Neuaufbau aller Vorstufen allein aus Rohdaten ist noch nicht nachgewiesen. Die unveränderte Originalentwicklung und die Fassung vor der Bereinigung liegen lokal vor. Die alte ausführliche Methodik ist unter `_archive/notebook_cleanup_20261029/` erhalten.

## Videopilot

Notebook 03 wendet T-DEED auf fünf automatische zwölfsekündige Clips an. Notebook 04 verbindet die Vorhersagen mit Trackingkontakten und untersucht ihre zeitliche Übereinstimmung einschließlich der ursprünglichen Negativkontrolle. Notebook 05 ergänzt Kontaktevidenz und testet eine zusätzliche Grenzausrichtung von höchstens 0,4 s.

Im bisherigen Lauf bleiben beide v2-Besitzfolgen identisch zu v1. Die Videoklassen liefern keine unabhängigen Team- oder Kontrolllabels. Das öffentliche Fenster wird von den Pilotclips nicht überdeckt und kann ihren Zusatznutzen nicht bewerten.

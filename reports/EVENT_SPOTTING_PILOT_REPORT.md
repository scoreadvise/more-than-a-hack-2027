# Event-Spotting-Machbarkeitsbericht · freigegebener Pilot A–E

**Empfehlung: T-DEED `SoccerNetBall_challenge1` ist unter den geprüften Kandidaten die realistischste technische Erstwahl.** Der Task-Checkpoint wurde tatsächlich strikt geladen und auf fünf taktischen Clips ausgeführt. Der Pilot belegt lauffähige semantische Aktionsvorhersagen; ein Nutzen für Ballbesitzwechsel oder ein besserer spellF1 ist damit **noch nicht belegt**. Für Spatial Hybrid v2 empfiehlt sich zunächst Variante A, Kontaktevidenz als getrennte Diagnose.

## Tatsächliche Ausführung

- Fünf vorab GT-frei ausgewählte, nicht überlappende Clips à 12 s, insgesamt 60 s. Keine Vollvideoinferenz, kein Training, keine Test-Time-Anpassung, kein Lesen öffentlicher Besitz-GT.
- 47 Event-Vorhersagen nach Original-Soft-NMS, entsprechend 47 Vorhersagen je Minute **Clipmaterial**. Es ist keine Treffer-/Fehlalarmrate.
- CPU-Clipverarbeitung insgesamt **201.39 s**; Faktor 3.36 zur Videolänge. Dies umfasst Dekodierung, drei Fenster pro Clip, Modell, Nachverarbeitung und Speicherung. Installation, Gewichtsimport, A/B-Audit und zusätzlicher MPS-Vergleich sind nicht enthalten.
- Tatsächlicher Rechner **Apple M1 Pro, 16 GB**, macOS arm64; kein gemessener M4-Pro-Wert. CPU FP32, Batch 1, vier Threads.
- Kumulierter Prozess-Peak-RSS über den Lauf **5175.5 MiB (5.05 GiB)**. Der Wert umfasst auch zuvor ausgeführte Audits und den MPS-Vergleich, nicht nur Modellaktivierungen; er ist keine isolierte GPU-Speichermessung. Ein Float32-Inputfenster allein belegt 408,1 MiB.
- MPS verfügbar; gruppierte Conv3d und ein echtes vollständiges Fenster bestanden. Dieses Fenster benötigte **11.28 s**, maximale absolute Scoreabweichung zur CPU **0.00000155**. Kein konfigurierter automatischer CPU-Operatorfallback. Ein Fenster ohne Wiederholungen ist kein belastbarer Durchsatzbenchmark. Die exportierten Vorhersagen stammen einheitlich von CPU.
- Isolierte Python-3.11.7-Umgebung im internen temporären Speicher. Auf T7/ExFAT scheiterte der erste Laufzeitversuch an AppleDouble-`._*.pth`; die bestehende Modellumgebung wurde nicht verändert. Gespeicherter Paketstand und Wiederherstellung unter `artifacts/video_event_spotting/README.md`.

| Kontext | Vorhersagen | Vorhersagen/min (12-s-Clip) | CPU-Clipzeit [s] | Positionen mit Scores |
|---|---:|---:|---:|---:|
| build_up | 6 | 30 | 43.94 | 144/150 |
| attacking_transition | 15 | 75 | 39.19 | 145/150 |
| defending_transition | 11 | 55 | 39.23 | 145/150 |
| throw_in | 6 | 30 | 39.46 | 145/150 |
| goal_kick | 9 | 45 | 39.57 | 143/150 |

Die Kontextnamen stammen aus automatischen Smart Tags. Sie bestätigen keine einzelnen Pässe, Tacklings oder Spielfortsetzungen. Insbesondere können unterschiedliche Klassen in derselben zeitlichen Nähe ausgegeben werden; Soft-NMS arbeitet klassenweise. Die hohe Dichte einzelner Clips ist ein Prüfhinweis, kein Nachweis von Fehlalarmen.

## Welche Ausgaben tatsächlich entstanden

| Native vorhergesagte Klasse | Anzahl |
|---|---:|
| PASS | 25 |
| DRIVE | 20 |
| HIGH PASS | 2 |

**Im Pilot aktiv waren nur PASS (25), DRIVE (20) und HIGH PASS (2).** Es entstanden keine Tackle-, Block-, Out- oder Throw-in-Vorhersagen oberhalb der unveränderten Schwelle. Daraus folgt weder, dass solche Aktionen in den Clips fehlen, noch dass das Modell sie in dieser Perspektive zuverlässig erkennen kann. Gerade der gewünschte Mehrwert für Zweikämpfe und kontrollierte Übernahmen ist damit noch nicht gezeigt.

Die vollständige native Taxonomie enthält zwölf Klassen; nicht vorhergesagte Klassen erhalten keine erfundenen Zeilen. Der exportierte `event_confidence` ist der durch Displacement, Überlappungsaggregation und Soft-NMS entstandene Modellscore, keine kalibrierte Wahrscheinlichkeit. Minimum 0.209, Median 0.347, Maximum 0.819. Die unveränderte CLI-Schwelle ist 0,2, der Soft-NMS-Radius 12 abgetastete Positionen (0,96 s).

Der Erstkandidat besitzt keinen Aktor-/Teamhead: **alle 47 Zeilen `team_side=unknown`, `player_track_id` leer**. Ein Pass- oder Tackling-Label bestimmt weder das handelnde Team noch einen Ballbesitzwechsel. Native Reception-, Interception-, Turnover- und Controlled-Possession-Klassen fehlen; `DRIVE` wird nicht in eine bestätigte kontrollierte Ballführung umbenannt.

## Zeitliche Zuordnung und fehlende Abdeckung

Die vollständige A/B-Prüfung hat alle 199.319 Video-Pakete, ATD-Zeilenzähler und Homographie-Frame-IDs untersucht: CFR 25 FPS, Datei-/Trackingoffset null. Die exportierten Ereignisse verwenden exakt:

`tracking_frame = clip_first_frame + 2 × native_sampled_event_index`

`video_timestamp_s = tracking_frame / 25`

Das ist die Originalvideozeit, nicht die eingeblendete Spieluhr. Der Stride wird genau einmal angewendet. Alle CSV-Zeilen liegen im jeweiligen Clip und außerhalb des öffentlichen Ballbesitzfensters.

Native Fensterstarts sind `[-5, 20, 45]` auf dem Stride-2-Raster. Die Originalimplementierung verwirft unvollständige Endfenster: **145/150 Rasterpositionen geometrisch abgedeckt, die letzten 0,40 s jedes Clips nicht abgedeckt**. Zusätzlich können durch Displacement einzelne geometrisch abgedeckte Positionen ohne Score bleiben; tatsächliche Unterstützung steht oben und in den NPZ. Fehlende Unterstützung bedeutet keine Aussage, nicht „kein Ereignis“.

Das Ausgaberaster beträgt **80 ms / zwei Originalframes**. Eine technisch eindeutige Trackingadresse ist keine gemessene semantische Framegenauigkeit. Systematischer Event-Zeitversatz, Kontaktzeitfehler und frühe/späte Aktionen sind ohne zulässige unabhängige Ereignislabels **unbekannt**. Es wurde kein Offset an Besitz-GT angepasst.

## Phase D: Was wir wissenschaftlich sagen können

| Frage | Ergebnis dieses Piloten |
|---|---|
| Task-Gewichte und reale taktische Clips lauffähig? | Ja: 598 Tensoren strikt geladen; 15 CPU-Pilotfenster sowie ein zusätzliches CPU/MPS-Vergleichspaar |
| Welche Klassen werden ausgegeben? | Obige Vorhersageverteilung; nicht unabhängig als korrekte Aktionen bestätigt |
| Präzision, Recall, F1 / Anzahl tatsächlicher Fehlalarme? | Nicht bestimmt; keine unabhängige zulässige Event-GT |
| Systematischer Zeitversatz oder framegenaue Eventgüte? | Nicht bestimmt; nur technische Zeitabbildung geprüft |
| Team-/Spielerzuordnung? | Nicht unterstützt; unbekannt/leer |
| Mehrwert gegenüber Kontaktkandidaten? | Potenzielle zusätzliche Aktionssemantik; empirischer Informationsgewinn noch nicht nachgewiesen |
| Korrektur falscher H/A-Wechsel / Verbesserung spellF1? | Nicht getestet; kein Decoder geändert |

Die Diagnostik zeigt Vorhersagen und unveränderte v1-H/A-Grenzen auf derselben Zeitachse (`figures/event_timeline_v1_context.png`). `diagnostics/event_v1_switch_context.csv` enthält rein deskriptive Abstände zu v1-Grenzen. Diese Grenzen sind keine Event-GT und kein Nachweis korrekter Wechsel. Der Vergleich ersetzt keinen Join zu den ursprünglichen vollständigen Kontaktkandidaten. Die zusätzliche Rekonstruktion dieser Kandidaten wurde in diesem kleinen Pilot nicht durchgeführt.

Die taktische Gesamtansicht unterscheidet sich von den Broadcast-Trainingsdaten, der Ball ist klein und wird für das Modell auf 796×448 verkleinert. Die fünf Projektionsbilder dienen der Kamera-/Trackingprüfung, nicht einer menschlich erzeugten Event-Annotation. Ohne passende unabhängige Labels lässt sich nicht belastbar sagen, welche Klassensemantik in dieser Ansicht tatsächlich zuverlässig unterscheidbar ist.

## Modell-, Daten- und Regelgrenzen

- Gewichte: 49.579.222 Byte, SHA-256 `f7b5cee134a2cfffc5b76922bbf528fe24cb6cc35c550dba23b9eb1bd4ff3d35`. `torch.load(weights_only=True, map_location="cpu")`, alle 598 Tensoren strikt geladen, keine fehlenden oder unerwarteten Schlüssel. Modell nach zweitem Kopf: 12,316,972 Parameter.
- Quellrevision `d953b4de8a2ad941c565e1683c5b07255cbe644e`. Nur Namensraum, deaktivierter zusätzlicher Backbone-Download und geräteneutraler Kopf geändert. Vollständiger Gewichtsimport ersetzt alle initialisierten Parameter. RGB, interne Normalisierung, Fenster, Stride, Displacement, klassenweise Soft-NMS und Schwelle original. Kein neuer eigener Python-Modulcode außerhalb des Notebooks.
- Code GPLv3 plus mitgelieferte Komponentenlizenzen; Drive-Gewichte ohne separat ausdrücklich dokumentierte Gewichtslizenz. Rechte für Code, Checkpoint und SoccerNet-Trainingsdaten/NDA getrennt behandeln; insbesondere vor Weitergabe/Einreichung klären. Die vollständige Quellenprüfung steht in `research/OPEN_SOURCE_MODEL_COMPARISON.md`.
- Geprüfte Ball-Action-Matchlisten nennen EFL 2019/20; das Challenge-Spiel Barcelona–Athletic 2024/25 erscheint dort nicht. Das ist kein lückenloser Ausschluss sämtlicher Vortrainings-/Checkpointquellen. Keine Gewichtsinspektion kann allein die vollständige Trainingsherkunft beweisen.
- Aktuelle [offizielle Regeln](https://github.com/metrica-sports/more-than-a-hack-2027/blob/main/RULES.md) erlauben dokumentierte verfügbare externe Modelle, untersagen aber menschliche Labels auf diesem Spiel auch für Training/Validierung sowie menschlich erzeugte externe Eventdaten desselben Spiels. Deshalb keine neuen Event-Frame-Labels hier; quantitative Eventvalidierung benötigt andere zulässige Spiele. Der in A/B dokumentierte Konflikt der historischen öffentlichen Statuslabel-Nutzung von v1 mit dem neueren Regeltext bleibt offen; v1 wird nicht eigenmächtig umgebaut.

## Artefakte und reproduzierbarer Stand

`main approach/13_video_event_spotting_pilot.ipynb` wurde in der isolierten Umgebung vollständig von oben nach unten ausgeführt. Nach dem vollständigen Frischkernel-Lauf wurde ausschließlich die Diagrammzelle aus identischen gespeicherten CSV-/NPZ-Werten erneut ausgeführt, um den unteren Achsenrand zu korrigieren; keine weitere Inferenz oder Analyseänderung. Der Qualitätsmanifest unterscheidet beide Schritte. Alle eigenen Imports stehen in einer zentralen ersten Codezelle. Wesentliche Zwischenergebnisse, technische Prüfungen und die Zeitgrafik sind gespeichert. Die Qualitätsprüfung protokolliert vollständige Ausführung, Zeit-/CSV-Abbildung und Hashvergleich.

- `predictions/video_events_pilot.csv`: tatsächliche 47 Vorhersagen mit den vereinbarten neun Feldern.
- `diagnostics/model_scores/*.npz`: summierte native 13-Klassen-Scores einschließlich Hintergrund, Unterstützung, Fensterabdeckung und lokale Rasterframes.
- `diagnostics/clip_inference_summary.json`, `predicted_class_counts.csv`, `event_v1_switch_context.csv`.
- `manifests/inference_runtime.json`, `checkpoint_load.json`, `mps_model_check.json`, `phase_c_audit.json`: Versionen, Quellen-/Gewichtshashes, Gerätestest, Einstellungen und Schutz der v1-Dateien.
- `reports/SPATIAL_HYBRID_V2_INTEGRATION_PROPOSAL.md`: konkreter Vergleich A/B/C und vorgeschlagene Folgearbeit.

Spatial Hybrid v1 bleibt unverändert: zuvor reproduzierter öffentlicher spellF1 **0,564103**, macroF1 **0,865360**. Neun geschützte Quell-/Eingabe-/Referenzdateien wurden per SHA-256 gegen den ursprünglichen A/B-Stand geprüft. Hier wurde kein neuer Besitzscore berechnet; Eventdichte und v1-Besitzmetriken dürfen nicht gleichgesetzt werden.


## Videoansicht der Pilotvorhersagen

Die fünf Clips stehen zusätzlich als 60-Sekunden-Montage unter `diagnostics/annotated/video_events_pilot_annotated.mp4` bereit. Der lokale `event_spotting_player.html` und Notebookabschnitt 15 enthalten eine anklickbare Liste aller 47 Vorhersagen. Ein Klick startet die Wiedergabe 0,60 s vor dem Ereignis innerhalb seines Clips. Klasse, Score, Originalvideozeit und Trackingframe sind eingeblendet; die Anzeige von ±0,40 s ist keine Aktionsdauer oder Gütemessung. Es werden keine Spielerpositionen erfunden.

Die Darstellung wurde aus unveränderten CSV-/NPZ-Dateien erzeugt, separat ausgeführt und technisch geprüft (1.500 Frames, H.264, 60 s, 47 passende Sprungziele). Keine neue Modellinferenz. Der integrierte Browser blockiert lokale `file:`-URLs; daher wurde der standalone HTML-Player nicht über diesen Browser interaktiv geprüft. Der Player ist zusätzlich im Notebook ohne lokale URL eingebettet.

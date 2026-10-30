# Spatial Hybrid v2: tatsächlich ausgeführter T-DEED-Fusionspilot

## Ergebnis

Beide Varianten verändern die Besitzlabels nicht. Das ist das tatsächliche Ergebnis der konservativen Regeln, kein künstlich erzeugter Unterschied. A ergänzt Kontaktevidenz, B hat einen aktiven getesteten Änderungszweig, aber keine fachlich zulässige Änderungsentscheidung in diesem Pilot.

Die fünf vorhandenen Clips umfassen1.500 Frames /60s. Davon sind 1450 Frames durch vollständige Modellfenster abgedeckt, 913 sind für mögliche LIVE-H/A-Interventionen zugelassen. Alle Vorhersagen liegen als vollständige199.319-Frame-Arrays und offizielle CSVs vor. v1 bleibt unverändert. Kein Training, keine neue Videoinferenz, keine manuellen Matchlabels, keine GT bei der Vorhersage.

## Welche Events wurden tatsächlich verwendet?

- **Lokale Evidenzkanäle:** alle47 unveränderten T-DEED-Events (PASS/DRIVE/HIGH PASS), auf dem25-FPS-Raster deterministisch mit±0,5s-Dreieckskern lokalisiert. Native Zeitauflösung80ms. Scores bleiben unkalibriert; kein Event = keine zusätzliche positive Unterstützung, kein Gegenbeweis.
- **A-Kontaktbestätigung:** 15 eindeutige vorhandene Kontakte mit zusätzlicher positiver Videoevidenz; davon 7 mit der vorhandenen unvalidierten Trackingkonsenszuordnung. Verwendete Event-IDs: V000, V001, V003, V006, V012, V023, V024, V027, V028, V029, V030, V033, V040, V043, V044. Diese IDs stützen Kontakt-/Kontinuitätsevidenz, nicht neue unabhängige Teamlabels. Alle47 Annahmen/Ablehnungsgründe stehen in `diagnostics/all_47_event_usage.csv` und `variant_A_contact_confirmations.csv`.
- **B-zulässige Boundary-Aktionsanker:** 5, IDs: V001, V012, V029, V033, V040. DRIVE wird ausschließlich als Kontinuitätssignal verwendet. Mehrdeutige/unzureichende Teamhinweise werden nicht zu H/A gezwungen.
- **B tatsächlich für eine Grenzänderung verwendet:** 0, IDs: keine. Ein zulässiger Eventanker ist noch keine tatsächlich wirksame Änderungsentscheidung.

## Welche konkreten Besitzentscheidungen änderten sich?

| Variante | Geänderte Frames | Verschobene H/A-Grenzen | Zusätzliche/entfernte Wechsel | D/X verändert | Außerhalb Clips geändert | Kurze Phasen: Länge geändert |
|---|---:|---:|---:|---:|---:|---:|
| spatial_hybrid_v1_reference | 0 | 0 | 0/0 | 0 | 0 | 0 |
| spatial_hybrid_v2_A | 0 | 0 | 0/0 | 0 | 0 | 0 |
| spatial_hybrid_v2_B | 0 | 0 | 0/0 | 0 | 0 | 0 |

Bei null Änderungen ist der prozentuale Anteil der Änderungen innerhalb der Clips nicht definiert; es gibt0 Änderungen außerhalb. Alle Varianten erhalten dieselbe Phasenfolge und258 direkte H/A-Wechsel innerhalb vorhergesagtem LIVE. Kurze Phasen (<4s) bleiben als eigenständige Phasen erhalten; die vollständige Vorher-/Nachher-Tabelle steht in `diagnostics/short_possession_phase_comparison.csv`.

Die v1-Grenzen im tatsächlich abgedeckten Pilotbereich und ihre Entscheidungen:

| Ursprünglicher Frame | Neuer Frame | Richtung | Zusätzlicher Shift [s] | Entscheidung |
|---|---:|---|---:|---|
| 19861 | 19861 | H→A | 0.00 | no_eligible_new_team_action_anchor_in_live_segment |
| 22803 | 22803 | A→H | 0.00 | no_eligible_new_team_action_anchor_in_live_segment |
| 22839 | 22839 | H→A | 0.00 | no_nearby_spatial_crossing |
| 32712 | 32712 | H→A | 0.00 | no_strict_joint_support_improvement |

## Warum diese Regeln vorsichtig sind

**A:** Positive Aktions-/Kontinuitätsevidenz kann vorhandene Kandidaten stützen. Sie liefert bei fehlender unabhängiger Akteur-/Kontrollsemantik kein neues kontrollierendes Team und keine bestätigte neue Kontrollgrenze. Eine Änderung harter v1-Labels nur durch „mehr Confidence“ wäre eine zusätzliche unvalidierte Modellannahme. Deshalb erhält A die Besitzfolge und exportiert die positive Kontaktevidenz transparent.

**B:** Der Decoder bewertet vorhandene räumliche Crossings zum bereits erkannten neuen Team. Nur wenn ein zulässiger Videoaktionsanker über einen Originalkontakt räumlich und zeitlich dazu passt, kann eine Grenze verschoben werden. Die neue Position wird **nicht einfach auf den Videoeventframe gesetzt**. Radius höchstens0,4s /10Frames, zusätzliche Nachbarphasen-Schutzgrenzen, vollständige Deckung der geänderten Frames und strikt höherer positiver Joint-Support. Alle Parameter stehen vor jeder öffentlichen Evaluation fest. Die Kandidaten- und Grenzentscheidungen sind vollständig gespeichert.

Die Bezeichnung Trackingkonsens bedeutet Übereinstimmung vorhandener, teilweise voneinander abhängiger Tracking-/Modellindizien; kein unabhängig validiertes Video-Teamlabel. Ein Pass ist nicht automatisch ein Besitzwechsel; DRIVE ist kein Grenzanker. Es wurden keine Grenzen manuell ausgewählt oder korrigiert.

## Offizielle Validierung und öffentliche Scores

Alle drei vollständigen CSVs wurden mit dem unveränderten offiziellen Validator geprüft. Der öffentliche Evaluator wurde für diesen eingefrorenen Dateisatz **einmal** aufgerufen. Ein erneutes Run All verwendet nach Hashprüfung dieselbe gespeicherte offizielle Auswertung; neue Parameter/Submissions führen zum Stopp statt erneuter Publicoptimierung.

| Submission | spell_f1_mean | macro_f1 |
|---|---:|---:|
| spatial_hybrid_v1_reference | 0.564103 | 0.865360 |
| spatial_hybrid_v2_A | 0.564103 | 0.865360 |
| spatial_hybrid_v2_B | 0.564103 | 0.865360 |

Die öffentliche GT umfasst Frames 11185–18684. **Überdeckung durch Pilotclips: 0 Frames; durch tatsächliche Modellabdeckung: 0 Frames.** Der öffentliche Score kann die Fusion in diesen Clips deshalb nicht beurteilen. Identische Werte sind kein Leistungsnachweis und waren auch bei nichtöffentlichen Änderungen zu erwarten. Die Scorewerte wurden nicht zur Anpassung oder Auswahl der Fusionsparameter verwendet.

## Ausführung und Regression

- Notebook15 vollständig in frischem Kernel ausgeführt, zentrale Imports, alle Helfer sichtbar im Notebook; keine neuen externen Python-Module.
- Sieben synthetische Programmlogikprüfungen einschließlich echtem4-Frame-Shift bei passenden künstlichen Hinweisen; sie zeigen Funktionsfähigkeit des Änderungszweigs, keine Eventqualität und keine Challenge-Annotation.
- Vollspielprüfungen: gültige199.319 Labels, außerhalb Clips und tatsächlicher Abdeckung exakt v1, D/X unverändert, keine unbeabsichtigten Phasen, zusätzliche Shifts höchstens0,4s.
- Geschützte Originalquellen, Modelle, v1-/Physics-Referenzen und Diagnoseeingaben vor/nach dem Lauf per SHA-256 unverändert.
- Softwarestand: Python3.11.7; {'numpy': '1.26.4', 'pandas': '2.3.3', 'matplotlib': '3.10.7'}. `frozen_predictions_before_evaluation.json` dokumentiert den Stand vor dem ersten GT-Zugriff. Offizielle Logs und einmaliger Auswertungsbeleg liegen unter `diagnostics/official_evaluation/`.

## Grenzen und nächster Entscheidungspunkt

Die Diagnose aus14 liefert keine robust bestätigte überzufällige Übereinstimmung und keine unabhängige semantische Event-/Teamgüte. Dieser Prototyp testet die technische Fusion konservativ; er belegt keine bessere Ballbesitzklassifikation. Ein Nullergebnis wird nicht durch nachträgliches Lockern von Teamgates, Suchradien oder Schwellwerten „repariert“.

Eine automatische Vollspielinferenz wurde **nicht** gestartet. Die Entscheidung darüber bleibt offen. Sinnvoll wäre zuerst zu klären, ob die bislang seltenen eindeutigen Team-/Kontakt-/Grenzkombinationen und die Eventsemantik auf geeigneten zulässigen Daten ausreichend tragen. Mehr Videominuten allein lösen das Problem fehlender unabhängiger Team-/Kontrollinformation nicht. Weitere Decoderänderungen oder Inferenzumfänge benötigen eure nächste Freigabe.

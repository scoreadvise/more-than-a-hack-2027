# Wissenschaftliche Leakage- und Validierungsprüfung

Auditdatum: **29. Oktober 2026, Europe/Berlin** (Clientdatum). Projekt: `/Volumes/T7/More Than A Hack 2027/Initial Challenge`. Online-Stand: `f8f2629ff1e0985f81d7e59d8413678514ee1530`. Lokales Archiv: `3de6b60aeabd2475d95879a651d38b72bc4fba00`. Technische UTC-Abrufzeiten und SHA-256 stehen in [Versionsmanifest](evidence/official_version_manifest.json). Alle Aussagen betreffen den vorgefundenen Stand; keine nachträgliche Änderung der Entwicklungshistorie.


## Zusammenfassender Befund

Der zentrale Fehler ist die Nutzung von Zielinformationen des Challenge-Spiels zum Training und zur wiederholten Entwicklung. **Nicht jede zeitliche Überlappung, Zukunftsnutzung oder gesamte Matchstatistik ist deshalb automatisch Target Leakage.** Die bestehende purged Status-CV enthält mehrere sinnvolle Schutzmaßnahmen, stellt aber weder Regelkonformität noch einen unabhängigen Test des finalen Hybrids her.

| Prüffrage | Tatsächlicher Befund | Schlussfolgerung |
|---|---|---|
| Train/Validation-Frameüberschneidung in08 | Rekonstruierte vier Folds: jeweils0 gemeinsame Zentren/Prüfframes. Nächster Trainingsabstand304/302/302/304 Frames. | Kein unmittelbarer Frame-Overlap dieser Fits gefunden. |
| Überlappende Rohdatenkontexte | Merkmalsradius110 Frames; Medianrand45; geforderter Abstand2×110+45=265. Tatsächliche Reserve39/37/37/39 Frames. | Die dokumentierte Purge12s genügt für diesen ML-Feature-/Filterpfad. Das sind Code-/Maskennachweise, kein erneuter Trainingslauf. |
| Preprocessing vor Split | `Pipeline`: Medianimputer und Missingindikatoren; StandardScaler nur bei LogReg. `fit` erhält ausschließlich `train_idx`. | Keine Vollmatch-/Validierungsfit-Imputation oder -Skalierung im überwachten Pipelinepfad gefunden. |
| Foldauswahl aus Labels | D-Intervalle der öffentlichen GT bilden Mittelpunkte und Foldgrenzen. | Explizit labelgestütztes Versuchsdesign, kein Modellmerkmal. Vier Stopps desselben Spiels sind keine unabhängige Matchstichprobe; aktuelle Trainings-/Validierungsregel bleibt verletzt. |
| Trainingszielherkunft | Öffentliche H/A/D wird nach D/L binarisiert; 1.500 öffentliche Zentren für beide Finalfits. | Direkte Zielnutzung des Challenge-Spiels belegt. OOF ändert die verbotene Herkunft nicht. |
| Finalfit mit eigenem Publicscore | Vollspielcache enthält Finalfit auf Public, aber05 ersetzt öffentliche Statuslabels durch OOF. | Den finalen Score nicht pauschal unmittelbaren Finalfit-Trainingsscore nennen; trotzdem entwicklungsnah/regelwidrige Lernquelle. |
| OOF des **gesamten** Hybrids |05 mischt öffentliche OOF-Statuslabels und Full-fit-Ausgaben außerhalb Public, dann läuft ein globaler Viterbi. Andere OOF-Fits haben jeweils andere Publicblöcke gesehen. | **Keine vollständig cross-gefittete End-to-End-Pipeline belegt.** Globale Decodierung kann Informationen aus Fits mit Kenntnis anderer Zielblöcke eintragen; konkreter numerischer Einfluss wurde ohne neue Decoderläufe nicht quantifiziert. |
| Zeitlicher Test | Bidirektionale Trainingsblöcke desselben Matches, bekannte vier Unterbrechungen, viele aufeinanderfolgende Frames. | Als explorative Offline-Blockprüfung verständlich; keine Aussage über neue Spiele oder unbekannte private Possessions. |
| Wiederholte öffentliche Evaluation |58 Scorezeilen/28 Namen plus AUC, Oracle-/Grenz-/Kontaktanalysen. | Adaptiver Selektionsbias wahrscheinlich/strukturell begründet; Umfang numerischer Überanpassung nicht aus diesen Daten schätzbar. Kein unabhängiger Test verbleibt im bereits gesehenen Publicfenster. |
| Versteckte GT-Spalten in Merkmalen | Bewegungs-CSV6 Spalten einschließlich Frame; ML216 Kontextspalten, Fit selektiert `features`. GT/Trainregion in Diagnosecache, nicht als Eingangsmerkmal in `features` gefunden. | Keine direkte GT-Spalte als ML-Feature entdeckt. GT-trainierte Vorhersagen bleiben abgeleitete Zielinformation. |
| Oracle-Status |05 C45 kopiert Public-D/L in `oracle_status`, nur Diagnostik, kein Export als Submission gefunden. | Klar zielinformierte obere Diagnosegrenze; kein Nachweis, dass die finale Hybriddatei heimlich aus Oracle stammt. |
| Nichtöffentliche Score-Skalierung | Soft-Varianten C27 verwenden .90-Quantil aus ML-Scores außerhalb Public, ohne dortige Ziele. | Transduktive Matchstatistik, nicht automatisch Zugriff auf private GT; außerdem kein finaler v1-Pfad. |
| Rückwärts-/Zukunftsverarbeitung | RTS, zentrierte Fenster, ±4-s-ML-Kontext, Viterbi-Rückverfolgung, `bfill` im LIVE-Segment, räumliche ±3-s-Suche. | Bei Offline-Gesamtspielanalyse nicht für sich Target Leakage. Das Verfahren wäre nicht kausal livefähig; keine zukünftigen Zielwerte dürfen daraus legitimiert werden. |
| Geometrische Datenmasken |86.900 nichtendliche rohe Proximity-Margen. Median11/min8, Sign0 bei Null/NaN; nur direkter±-Vorzeichenwechsel. | Kein Überspringen kompletter geglätteter NaN-/Null-Zeichenfolgen im Crossingcode. Kurze Rohlücken können bei genügend gültigen Fenstereinträgen einen Median erhalten; das ist eine sichtbare Glättungsannahme. |
| Halbzeit-/LIVE-Masken | Offizielle Halbzeitblöcke, v1 räumlich nur innerhalb vorhergesagtem LIVE; D/X und Phasenfolge bleiben in den vorhandenen Releaseprüfungen erhalten. | Kein Befund unzulässiger GT-Timingverschiebung über Halbzeitgrenzen. Offiziell mitgelieferte Metadaten von privat erschlossenen Wahrheitslabels trennen. |
| Video-/Trackingzeit | Vorliegender vollständiger Audit:199.319 PTS-Schritte à.04s, Raw-ID−1=Videoframe, Homographie framegleich, Offset0. Aktuelle games.py unverändert. | Technische Synchronisierung belegt; keine öffentliche Offsetoptimierung in13 gefunden. Broadcast hat andere Zeitachse und wurde nicht als Indexgrundlage des finalen v1 festgestellt. |
| Externes Modell / Trainingsüberschneidung | T-DEED-Task-Split6 EFL 2019/20-Spiele; kompletter Checkpoint-/Vortrainingslauf nicht vollständig attestiert. | Keine belegte Überschneidung mit Barcelona–Athletic 2024/25; vollständiger Ausschluss nicht verifizierbar. Nicht automatisch ein Regelverstoß. |

## Die relevanten Schutzmaßnahmen im Code

Notebook 08 C11 erzeugt für jeden Fold ein frisches Modell, lernt Imputer/Scaler nur im Training und berechnet auch die Medianränder mit **demselben** Foldmodell. Es mischt nicht mehrere Foldvorhersagen in diesem lokalen91-Frame-Filter. [Rekonstruierte Grenzen](evidence/reconstructed_cv_boundaries.csv), [E02](evidence/CODE_EVIDENCE.md#e02).

Der spätere globale Statusdecoder ist davon gesondert zu beurteilen. Für einen unabhängigen wissenschaftlichen End-to-End-Test müssten alle gelernten Komponenten und sämtliche entscheidungsrelevanten Parameter ohne Kenntnis der Ziele des Prüfblocks feststehen; nachgelagerte Auswertung dürfe nicht über andere, auf diesen Zielen trainierte Modellzustände zurückwirken. Dieser Nachweis liegt nicht vor. Im Audit wurden bewusst keine Gegenvarianten, Scores oder Decoder neu berechnet.

## Reproduktion ist ein anderer Prüfgegenstand

Die vorhandenen Releaseartefakte zeigen: Notebook 10/11 können aus eingefrorenen Vorstufen bytegleiche Physics-/Hybrid-CSVs herstellen. NPZ-Referenz- und Expected-Arrays passen zu den gespeicherten CSVs. Das belegt **technische Wiederherstellung**, nicht rechtmäßige Labelherkunft oder unabhängige Modellgüte. Vollständig dokumentierte Raw-to-Submission-Regeneration einschließlich Statusfits, Vorstufen und Bewegungsexport ist nach der vorhandenen Methodik noch offen. Ein erfolgreicher Validator prüft Format, kein Compliancezertifikat.

## Privat-GT und wissenschaftliche Aussagegrenzen

Im offiziellen Archiv wurde genau eine GT-CSV gefunden, die öffentliche Datei mit7.500 nicht-X-Zeilen; kein privates Vollmatch-GT im inventarisierten Projekt identifiziert. Benennungen wie `gt_lookup`, `gt_transition_timing` oder `expected_hybrid` wurden anhand ihres Ursprungs geprüft: Public-Diagnose bzw. Regression, kein allein aus Namen abgeleiteter privater Leak. Das ist keine forensische Garantie über außerhalb dieses Projekts vorhandene oder gelöschte Dateien.

Die bekannten .564103/.865360 bleiben historische öffentliche Entwicklungswerte. Es wurden keine Konfidenzintervalle, private Scores oder Generalisierungseffekte aus dem Audit erfunden. Eine regelkonforme Neuentwicklung muss andere erlaubte Spiele für Training/Validierung nutzen oder ohne menschliche Challenge-Ziele lernen; Details und Freigabepunkte im Sanierungsplan.

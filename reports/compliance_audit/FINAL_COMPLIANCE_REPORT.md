# Abschließender Compliance- und Data-Leakage-Audit

Auditdatum: **29. Oktober 2026, Europe/Berlin** (Clientdatum). Projekt: `/Volumes/T7/More Than A Hack 2027/Initial Challenge`. Online-Stand: `f8f2629ff1e0985f81d7e59d8413678514ee1530`. Lokales Archiv: `3de6b60aeabd2475d95879a651d38b72bc4fba00`. Technische UTC-Abrufzeiten und SHA-256 stehen in [Versionsmanifest](evidence/official_version_manifest.json). Alle Aussagen betreffen den vorgefundenen Stand; keine nachträgliche Änderung der Entwicklungshistorie.


## Urteil

**Spatial Hybrid v1 ist nach dem aktuell dokumentierten Regelwortlaut nicht als regelkonforme Submission belegbar. Der klarste Konflikt ist nachgewiesen: Das Statusmodell wurde auf öffentlichen GT-Labels des Challenge-Spiels trainiert, und seine Vorhersagen gehen bis in den finalen Hybrid ein.** Das widerspricht [RULES §2](https://github.com/metrica-sports/more-than-a-hack-2027/blob/f8f2629ff1e0985f81d7e59d8413678514ee1530/RULES.md#2-use-the-private-ground-truth-or-any-human-produced-data-about-the-game) und der ausdrücklichen Trainings-/Tuningantwort in der [FAQ](https://github.com/metrica-sports/more-than-a-hack-2027/blob/f8f2629ff1e0985f81d7e59d8413678514ee1530/FAQ.md#can-i-train-or-tune-a-model-on-the-5-public-minutes).

Das ist eine evidenzbasierte Regelzuordnung, keine Behauptung vorsätzlichen Fehlverhaltens und keine verbindliche Disqualifikationsentscheidung. Das ältere lokale Archiv enthält eine materiell andere Handannotationsregel und keine gleich klare Public-Trainingsklausel. Geltungsbeginn, rückwirkende Bewertung und akzeptierte Sanierung können nur die Organisatoren festlegen. Der Audit hat weder Entwicklungsgeschichte umgeschrieben noch ein vermeintlich sauberes Modell erzeugt.

## 1. Wurde öffentliche GT nachweislich beim Training oder bei der Auswahl verwendet?

**Training: ja, eindeutig.** Notebook 08 C5 leitet `y_dead` aus der offiziellen öffentlichen H/A/D-Datei ab. C11 führt acht Fold-Fits aus (vier je Modell). C16 trainiert je einen finalen AdaBoost und eine logistische Regression auf **1.500 öffentlichen Zentren, Frames 11185–18680**, darunter293 D-Zentren. Alle diese Labels stammen aus den7.500 veröffentlichten Frames 11185–18684. Quellcode, Fitaufzeichnungen, Modellartefakte und OOF-/Vollspielcaches sind konsistent. [E01](evidence/CODE_EVIDENCE.md#e01), [E02](evidence/CODE_EVIDENCE.md#e02), [E03](evidence/CODE_EVIDENCE.md#e03), [nachgerechnete Filter](evidence/data_lineage_checks.json).

**Leistungsbezogene öffentliche Beurteilung: ja.** Gespeicherte Scoreboards enthalten58 Zeilen/28 unterschiedliche Submissionnamen; zusätzlich gibt es öffentliche AUC-, Oracle-, Kontakt- und Wechsel-Timinganalysen. Die Entwicklung untersucht konkrete GT-Wechsel vor der räumlichen Modellergänzung. Das öffentliche Fenster wurde also nicht nur zum CSV-/Frame-Debugging benutzt. **Welche einzelne Parameter-/Übernahmeentscheidung ausschließlich wegen welcher Kennzahl fiel, ist nicht lückenlos rekonstruierbar.** Kein dokumentierter großflächiger Hyperparametersearch gefunden; nicht jede Sensitivitätsanalyse ist GT-Tuning.

Wichtige Entlastungspräzisierung: Öffentliche AdaBoost-Labels werden im finalen Pfad durch blockweise OOF-Vorhersagen ersetzt; diese unterscheiden sich an615 Frames von Full-fit-Vorhersagen. Deshalb kein pauschales Etikett „direkter In-Sample-Endscore“. OOF beseitigt jedoch weder die verbotene Labelherkunft noch die wiederholte Adaptionsnutzung. [E05](evidence/CODE_EVIDENCE.md#e05).

## 2. Welche Komponenten sind unabhängig von öffentlicher GT entstanden?

**Belegt ohne Zielwerte im Berechnungsweg:** offizielle smooth50-Baseline, Raw-/XML-Laden, metrische Teamdistanzen und Raw-Bewegungsformeln. Kontakt-RTS-/Nähe-Kandidaten und die endgültige räumliche Framewahl benötigen im eigenen Rechenschritt ebenfalls keine GT. Die offizielle Baseline wurde vorgegeben übernommen; ihr öffentlich besseres125-Fenster wurde gerade nicht als neue Hauptreferenz ausgewählt.

**Nicht im gleichen Sinn historisch als GT-unabhängig zertifiziert:** sämtliche selbst gewählten Kontakt-/Heuristik-/Physik-/Alignmentkonstanten und die Entscheidung, welche Variante Hauptmodell wird. Es gibt deklarierte feste Annahmen, physikalisch sinnvolle Einheiten und keinen dokumentierten Fit vieler Schwellen. Gleichzeitig sind vorherige GT-/Videosichtungen und Leistungsanalysen vorhanden. Eine nachträgliche Behauptung reiner A-priori-Entstehung wäre nicht gedeckt.

**Separater Video-Pilot:** T-DEED nutzt externe Taskgewichte, festeCLI 0,2 und automatisch gewählte Clips; im eigenen Inferenzpfad keine öffentliche Besitz-GT, kein Training und keine Fusion in v1. Das begründet eine getrennte technische GT-Unabhängigkeit dieses Pilots, nicht einen vollständigen Freispruch für Gewichtsrechte, vollständige Vortrainingsherkunft oder frühere Cloud-Bildübermittlung.

## 3. Welche konkreten Risiken bestehen für eine v1-Einreichung?

1. **Klarer aktueller Regelkonflikt:** öffentliches GT-Training in08 → AdaBoost-Cache/OOF → Status-Viterbi/Physics v3 → Besitzrekonstruktion → Spatial Hybrid. Ein GT-freier letzter Notebookabschnitt heilt die Abhängigkeit nicht.
2. **Öffentliche Adaptions-/Selektionsverzerrung:** zahlreiche Leistungsdiagnosen desselben Fensters; kein unabhängiger Test. Die genaue numerische Optimierungswirkung und einzelne Entscheidungskausalität bleiben offen.
3. **Vorannotation/Videozeiten:**13 visuelle Codex-Segmente wurden trotz fehlender menschlicher Bestätigung tatsächlich zur Bewertung von04/06 verwendet;2.939 Frames wurden bewertet. Kein Training auf diesen Segmenten und kein direkter finaler Rückfluss gefunden. Ob diese interaktive KI-Vorannotation unter zulässige algorithmische Pseudolabels fällt, ist offen. Sicher menschlich bestätigte Nachannotation wurde nicht gefunden.
4. **Datenübermittlung:** Vor dem Audit wurden Matchframe-Vorschauen dem Assistenten als Bildinhalt gegeben. Bei Drittanbieter-gehostetem/Cloud-LLM widerspricht das der bereits im alten FAQ enthaltenen Uploadklausel. Hosting-/Transport-/Sonderfreigaben nicht vollständig verfügbar; dieser Sachverhalt ist zu klären und darf nicht verschwiegen werden. Der Audit selbst hat keine Videoframes geöffnet oder übertragen.
5. **Reproduzierbarkeit/Veröffentlichung:** Exakte Regeneration ab gespeicherten Vorstufen ist belegt, vollständige Raw-to-Submission-Kette nicht abschließend nachgewiesen.19 Notebooks enthalten Bilder/Medien-HTML, einige Matchclips in Base64. Eine öffentliche Veröffentlichung wäre gesondert zu prüfen; kein Beleg, dass sie bereits stattgefunden hat.
6. **Externe Rechte:** T-DEED ist separat vom v1-Modell. Seine Code-/Komponentenlizenzen sind vorhanden, separate ausdrückliche Weight-Rechte und vollständige Trainingsattestation fehlen. Bei künftigem Einsatz nicht Code-Lizenz, Gewichtslizenz und Datensatz-NDA gleichsetzen.

Die Matrix zählt Komponenten und übernommene Abhängigkeiten, **keine unabhängigen Regelverstöße pro Zeile**:

| Befundkategorie | Zeilen |
|---|---:|
| Regelverstoß nach dokumentiertem Regelwortlaut | 9 |
| Potenziell problematisch | 7 |
| Regelkonform belegt | 3 |
| Nicht ausreichend verifizierbar | 2 |

Vollständige technische Tatsachen, Labelquellen, Parameterwahl, Auslegung und Evidenz stehen in [COMPLIANCE_MATRIX.csv](COMPLIANCE_MATRIX.csv).

## 4. Wie wird ein sauber belegter Stand möglich, ohne die Architektur zu verwerfen?

**Statusquelle ersetzen, Architektur transparent erhalten, Entwicklung neu und zulässig validieren.** Zuerst schriftlich klären, welche Sanierung nach der bisherigen GT-Nutzung akzeptiert wird. Anschließend eine ausdrücklich neue Pipeline ohne öffentliche Match-Trainings-/Tuninglabels erstellen: bevorzugt Statustraining auf zugänglichen erlaubten **anderen Spielen**, alternativ nachvollziehbare algorithmische/physikalische Statusregeln oder zulässige automatisierte Pseudolabels. Keine Destillation aus den belasteten alten Lehrermodellen.

Raw-Features, Kontaktidee, Viterbi-Struktur und räumliche Funktion können weiter als dokumentierte Bausteine dienen. Numerische Altparameter brauchen eine unabhängige zulässige Begründung; die bereits gesehene öffentliche Leistung darf nicht zur erneuten Wahl dienen. Unabhängige Matchvalidierung und vollständige Raw-/Modellprovenienz vor dem final eingefrorenen Lauf festlegen. Alte Befunde und Artefakte als belastete historische Referenz erhalten. Der genaue stufenweise Plan, Aufwand und Risiken stehen in [REMEDIATION_PLAN.md](REMEDIATION_PLAN.md). **Nichts davon wurde im Audit umgesetzt.**

Ein „nachweislich sauberer“ Ersatz kann heute noch nicht zugesagt werden: Daten, Rechte, Organisatorenentscheidung und ein neuer reproduzierbarer Entwicklungsnachweis fehlen noch. Ein bloßes erneutes Ausführen von10/11 wäre Reproduktion desselben belasteten Stands.

## 5. Welche offenen Fragen sollten an die Organisatoren gehen?

- Welcher Regelstand ist für unser Team verbindlich, seit wann, und wie sollen wir die Abweichung des lokalen15.10.-Archivs zu den22./23.10.-Klarstellungen offenlegen?
- Wie bewerten sie das dokumentierte Training auf1.500 öffentlichen Statuszentren einschließlich OOF, und welcher konkrete Neuentwicklungs-/Sanierungsumfang wird akzeptiert?
- Darf eine neue zulässige Pipeline dieselbe Architektur/Trackingformeln verwenden, wenn die belasteten Fits/Labels und entscheidungsrelevanten Parameterquellen ersetzt werden? Wie ist bereits erfolgte Public-Kenntnis offenzulegen?
- Wo ziehen sie die Grenze zwischen technischer Evaluatorprüfung, öffentlicher Fehlerdiagnose und unerlaubter leistungsorientierter Auswahl, insbesondere nach den hier dokumentierten Timing-/Oracleanalysen?
- Wie wird die konkrete assistenzgestützte visuelle Vorannotation ohne menschliche Bestätigung bewertet? Welche Anforderungen gelten an vollständig algorithmische Pseudolabels und ihre Reproduzierbarkeit?
- Welche konkrete Hosting-/Übermittlungsprüfung und Meldung erwarten sie für früher an einen KI-Assistenten übergebene Matchbilder/-ausschnitte? Gibt es eine relevante Sonderfreigabe oder verbindliche anwendbare Vertragsausnahme?
- Welche Unterlagen reichen bei öffentlichen externen Checkpoints mit unvollständigem Trainings-/Gewichtsrechtnachweis? Was muss bei möglicher unbekannter Vortrainingsüberschneidung geprüft werden?
- Welche vorhandenen Gewichte/Caches dürfen in einem zulässigen Raw-to-Submission-Repository mitgeliefert werden, und wie sind lokale Notebookmedien von der öffentlichen Codeabgabe zu trennen?

Diese Fragen sind formuliert, **nicht versendet**. Ohne Antworten werden mehrdeutige Punkte nicht als eindeutig erlaubt ausgelegt.

## Prüfstand, Integrität und Reichweite

-24 bestehende Notebooks mit Quellcode und gespeicherten Textausgaben, aktuelle und archivierte Varianten,573 inventarisierte Dateien;139 einzigartige CSV-/NPZ-Schemas, zwei Joblib-Statusmodelle und ein externer Taskcheckpoint. Abgeleitete Diagnosefiles wurden bis zu ihrer echten Quelle verfolgt. Keine Parquet-Dateien im inventarisierten Bestand.
- Aktuelle offizielle Dokumente auf festem Commit, vollständige Diffs zum lokalen Archiv; öffentlicher GT-, Validator-, Metrik-, Baseline- und `games.py`-Inhalt bytegleich. Regelkonflikt ist keine neue Bewertungsformel.
- Keine private Vollmatch-GT im untersuchten Projekt identifiziert. Das ist ein begrenzter Suchbefund, kein Beweis über externe/gelöschte Daten. Keine vollständige ursprüngliche Entscheidungs-/Git-Historie verfügbar.
- Keine Fits, Decoder-/Modellneuläufe, neuen Varianten, Grenz-/Schwellenanpassungen oder offiziellen Neuscores. Keine manuelle Neuannotation. Keine bestehenden wissenschaftlichen Dateien geändert, keine Historie bereinigt. Neue Dateien ausschließlich unter `output/compliance_audit/`.
- Vollständiger Vorher-/Nachher-Vergleich aller inventarisierten Nichtvideodateien per SHA-256, Videos per Größe/mtime: siehe [Integritätsmanifest](evidence/audit_integrity.json). Video selbst wurde für diesen Audit nicht neu gelesen, dekodiert oder an externe Dienste gegeben.
- Wissenschaftliche Stärken bleiben benannt: Pipeline-Preprocessing pro Fold, ausreichend großer Purge für08, explizite NaN-/Frame-/Maskenprüfungen, OOF statt einfacher In-Sample-Bewertung und ehrliche Offline-Kennzeichnung. Diese Schutzmaßnahmen beheben den Wettbewerbs-Labelkonflikt nicht.

## Dateien und nächste Entscheidung

1. [RULES_COMPARISON.md](RULES_COMPARISON.md): konkrete Regelworte, Commitstände und Diffs.
2. [DATA_LINEAGE_AUDIT.md](DATA_LINEAGE_AUDIT.md): Labelkette, Fits, Caches und externe Modellherkunft.
3. [MODEL_SELECTION_AUDIT.md](MODEL_SELECTION_AUDIT.md): Varianten/Parameter und Grenzen der Entscheidungsrekonstruktion.
4. [MANUAL_ANNOTATION_AUDIT.md](MANUAL_ANNOTATION_AUDIT.md): tatsächliche Vorannotation, Nutzung, Hosting-/Medienfragen.
5. [LEAKAGE_AUDIT.md](LEAKAGE_AUDIT.md): zeitliche Validierung, Preprocessing, Offline-Kontext und End-to-End-Grenzen.
6. [COMPLIANCE_MATRIX.csv](COMPLIANCE_MATRIX.csv): Komponentenbefunde mit Evidenz und getrennter Auslegung.
7. [REMEDIATION_PLAN.md](REMEDIATION_PLAN.md): nicht umgesetzte Alternativen und konkrete Schritte.

**Empfehlung für die nächste freizugebende Stufe:** zuerst eine kurze, sachliche Organisatorenanfrage mit dieser belegten Herkunftskette und Fragen zum akzeptierten Sanierungsweg vorbereiten. Alternativ kann zunächst ein Daten-/Aufwandsplan für einen neuen zulässigen Statusbaustein ausgearbeitet werden. Vor einer neuen Modellstufe ist gemäß AGENTS.md §41 eure Entscheidung erforderlich; dieser Auftrag autorisiert ausdrücklich nur Feststellung und Planung.

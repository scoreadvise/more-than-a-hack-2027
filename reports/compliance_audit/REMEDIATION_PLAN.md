# Sanierungsplan ohne Umsetzung

Auditdatum: **29. Oktober 2026, Europe/Berlin** (Clientdatum). Projekt: `/Volumes/T7/More Than A Hack 2027/Initial Challenge`. Online-Stand: `f8f2629ff1e0985f81d7e59d8413678514ee1530`. Lokales Archiv: `3de6b60aeabd2475d95879a651d38b72bc4fba00`. Technische UTC-Abrufzeiten und SHA-256 stehen in [Versionsmanifest](evidence/official_version_manifest.json). Alle Aussagen betreffen den vorgefundenen Stand; keine nachträgliche Änderung der Entwicklungshistorie.


## Was sich bereits entscheiden lässt

Die Architektur **Status → H/A-Kontakte → zeitlicher Decoder → räumliches Alignment** muss nicht verworfen werden. Der vorhandene öffentliche GT-trainierte Statuspfad und seine Ableitungen können aber nicht allein durch Entfernen der GT-Ladedatei, Umbenennen, Caching oder OOF als regelkonform deklariert werden. Auch eine Destillation aus diesem Teacher erbt dessen unzulässige Matchlabelinformation.

Es wurde **nichts** neu trainiert, keine Variante erstellt und keine Schwelle geändert. Die folgenden Schritte sind konkrete, freizugebende Alternativen; sie sind keine nachträglich erfundene Entwicklungsgeschichte.

## Zuerst mit den Organisatoren klären

1. Welcher Regelstand/Geltungsbeginn ist für das Team verbindlich, und wie ist bereits geschehene Nutzung unter dem älteren Archiv offenzulegen? Welche Sanierung akzeptieren sie nach Public-GT-Training und wiederholter öffentlicher Diagnose?
2. Kann eine neue, vollständig dokumentierte Pipeline auf derselben Architektur eingereicht werden, wenn alle öffentlichen Match-Trainingslabels, betroffenen Fits und Lehrer-/Parameterabhängigkeiten ersetzt werden? Wie soll die bereits vorhandene menschliche/assistenzgestützte Kenntnis des Publicfensters behandelt werden?
3. Wie wird der konkrete Codex-Visual-Vorentwurf ohne menschliche Bestätigung unter der Pseudolabel-Regel bewertet, und welche Hosting-/Datenübermittlungsunterlagen brauchen sie? Nicht darauf aufbauen, bevor es geklärt ist.

Keine dieser Fragen wurde im Audit an Dritte gesendet. Ein Entwurf einer transparenten Anfrage ist ein möglicher nächster Schritt, keine bereits erteilte Ausnahme.

## Alternativen im Vergleich

| Alternative | Aufwand / verfügbare Daten | Wissenschaftliche Aussagekraft | Reproduktion / Risiken | Auswirkung auf bestehende Architektur |
|---|---|---|---|---|
| A: Rein algorithmischer Status aus Raw, automatischen Tags und/oder Signalphysik | Mittel. Raw/Tags liegen vor;6-freie Regeln müssen mit unabhängig belegten Konstanten neu spezifiziert werden. | Transparente Basis; kann Trackingausfälle weiterhin mit D verwechseln. Kein Güteversprechen. | Jede Regelherkunft dokumentieren. Alte06-Schwellen nicht ohne Prüfung als unbelastet übernehmen. | Ersetzt nur Status-/Evidenzquelle; Kontakte, Decoder, räumliches Modul grundsätzlich weiterverwendbar. |
| B: Statusmodell auf erlaubten **anderen Spielen** trainieren | Mittel bis hoch. Passende Daten/Statuslabels sind derzeit nicht im Projekt nachgewiesen; Zugangs-/NDA-Rechte prüfen. | Beste Chance für echte Train/Validation/Test-Trennung nach Spiel; Domainshift beachten. | Modell + Trainingsquellen/IDs, Split, Fitparameter einfrieren; keine Challenge-GT für Auswahl. | AdaBoost/LogReg-Struktur und216-Featureidee können nach unabhängiger Begründung bleiben; alte Fits ersetzen. |
| C: Algorithmische Pseudolabels / unüberwachtes Lernen | Mittel bis hoch. Unbeschriftete Challenge-Eingaben verfügbar; zulässigen Teacher erst festlegen. | Unsichere Pseudolabels, keine unabhängige Güte allein aus Teacher-Übereinstimmung. | Kein Public-trainierter Teacher, keine handkorrigierten Matchlabels; vollständige automatische Labelerzeugung dokumentieren. | Bestehendes Statusmodell könnte eine neue zulässige Labelquelle erhalten; zusätzliche Freigabe nötig. |
| D: Extern vortrainiertes Video-Eventmodell als separate Evidenz | Mittel. T-DEED technisch vorhanden; Rechte/Herkunft teilweise offen. |47 bisher unvalidierte Events belegen Machbarkeit, keinen Kontroll-/Wechselgewinn. Kein eigener Team-/Aktorhead. | Lokal inferieren; keine Matchauszüge an gehostete LLMs; Validierung auf erlaubten anderen Spielen. | Zunächst nur Kontaktevidenz ergänzen; ersetzt einen regelwidrig trainierten Status nicht automatisch. |
| E: Externe/physikalisch begründete, vorab festgelegte Konstanten | Niedrig bis mittel; Literatur/physikalische Einheiten vorhanden, vollständige Herleitung noch nötig. | Verhindert gezielte Publicanpassung, garantiert aber keine hohe Leistung. | Parameterledger mit Quelle, Zweck, Festlegungszeit, zulässigem Entwicklungsdatensatz; keine nachträglich erfundene A-priori-Erzählung. | Übertragbare Formeln behalten, numerische Altentscheidungen einzeln prüfen/ersetzen. |

## Empfohlene Reihenfolge

**Zuerst verbindliche Organisatorenklärung; danach B, falls passende andere Spiele verfügbar sind, ansonsten A als transparente Ausgangsbasis.** Das entfernt die klarste unzulässige Abhängigkeit mit begrenztem Eingriff. D ist eine zusätzliche Forschungsrichtung, keine Compliance-Abkürzung. C ist nur sinnvoll, wenn seine Labelherkunft selbst sauber und reproduzierbar ist.

Nach Freigabe wäre ein nachvollziehbarer neuer Stand so herzustellen:

1. **Historie erhalten:** Dieser Audit, alter Stand und Hashes bleiben als Herkunftsnachweis bestehen. Neuer Entwicklungsstand in einem ausdrücklich neuen Ordner/Branch; kein Überschreiben oder „Bereinigen“ alter Belege.
2. **Daten-/Parametervertrag vor Fits:** Zulässige Quellen/Spiele, Train-/Validierungs-/Testrollen und Auswahlkriterium festlegen. Challenge-Spiel kein menschlich gelabelter Trainings-/Tuning-/Validierungssatz. Gesehene Publiclabels nicht erneut zum Leistungsentscheid verwenden.
3. **Belastete Ableitungen identifizieren:** Alte08-Modelle, Full-fit-/OOF-Caches, daraus erzeugte Viterbi-/Physicslabels und finales NPZ sind keine sauberen Startlabels. Auch finale H/A-Sequenz und Statusabhängigkeiten ersetzen, statt nur Statuscache umbenennen. Quellen des Algorithmus dürfen transparent als Ausgangspunkt dokumentiert werden.
4. **Architektur erhalten, Statusquelle ersetzen:** Raw-Featureberechnung, Kontakt-/Viterbi-/räumliche Funktionen getrennt herleiten. Keine framespezifische Korrekturliste. Bereits GT-geprüfte numerische Werte nur nach erlaubter unabhängiger Begründung übernehmen; Kenntnis der alten Resultate offenlassen.
5. **Einmalige eingefrorene Inferenz:** Alle neuen Abhängigkeiten aus Raw oder zugelassenen externen Gewichten erzeugen; Hashes und Model-/Feature-/Labelprovenienz dokumentieren. Kein GT-Laden vor oder während der Inferenz; keine alten Expected-Labels als Inferenzquelle.
6. **Unabhängige Bewertung:** Modellauswahl auf vorab erlaubten anderen Spielen, ggf. nach Spiel gruppiert. End-to-End-Folds müssen alle gelernten Komponenten umfassen; öffentliche Challenge-GT nur technische Checks, keine weitere Scoreoptimierung. Original v1 als historischer, belasteter Vergleich separat kennzeichnen.
7. **Raw-to-Submission und Freigabe:** Frischer sequenzieller Notebooklauf auf zulässigen Rohdaten plus zugänglichen Modellen muss dieselbe komplette CSV erzeugen. Validator, Framezuordnung, feste Konfiguration und Datenfreigaben prüfen. Erst dann vollständige öffentliche Code-/Dokumentationsabgabe vorbereiten.
8. **Publikationspaket separat erstellen:** Notebookausgaben mit Matchmedien, lokale Videos, Rohtracking, rekonstruierbare Exporte und private Daten nicht veröffentlichen. Alte lokale Wissenschaftsdateien bleiben dabei erhalten; ein bereinigtes separates Release ist erst nach entsprechender Freigabe zu erstellen. Code-/Komponenten-/Gewichtslizenzen einzeln beachten.

## Was ausdrücklich keine Sanierung wäre

- OOF statt Full-fit verwenden und öffentliche Labels weiterhin zum Lernen nutzen.
- Public-GT-Spalte löschen, während GT-trainierte Gewichte/Predictions/NPZ erhalten bleiben.
- Neue Labels aus bereits belasteten Lehrermodellen „automatisch“ nennen.
- Auf anderen Frames desselben Spiels menschlich annotieren und dies als externen Test bezeichnen.
- Den Scoreanstieg als Beleg der Regelkonformität oder die MIT-Lizenz als Trainingserlaubnis im Wettbewerb auslegen.
- Die heutige Begründung rückwirkend als ursprüngliche Parameterfestlegung ausgeben.

**Offen:** Ohne akzeptierte Veranstaltervorgaben, passende erlaubte Daten und nachgewiesene neue Provenienz lässt sich heute kein nachweislich sauberer Ersatzstand garantieren. Dieser Plan beschreibt den Weg dorthin, nicht eine bereits vollzogene Sanierung.

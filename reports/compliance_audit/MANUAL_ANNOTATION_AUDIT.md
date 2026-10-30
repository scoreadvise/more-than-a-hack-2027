# Video-Sichtung, Vorannotation und mögliche Nutzung

Auditdatum: **29. Oktober 2026, Europe/Berlin** (Clientdatum). Projekt: `/Volumes/T7/More Than A Hack 2027/Initial Challenge`. Online-Stand: `f8f2629ff1e0985f81d7e59d8413678514ee1530`. Lokales Archiv: `3de6b60aeabd2475d95879a651d38b72bc4fba00`. Technische UTC-Abrufzeiten und SHA-256 stehen in [Versionsmanifest](evidence/official_version_manifest.json). Alle Aussagen betreffen den vorgefundenen Stand; keine nachträgliche Änderung der Entwicklungshistorie.


## Gefundene Dateien und tatsächlicher Stand

Ein archivierter Annotationsworkflow existiert: `_archive/cleanup_20261028T161028Z/output/jupyter-notebook/07_kontrollszenen_annotieren.ipynb` sowie `_archive/cleanup_20261028T161028Z/output/stoppage_annotation/`. Er enthält `segments.csv`, `annotation_protocol.json`, `reference_frame_diagnostics.csv`, `provisional_binary_metrics.csv`, Fehlerabschnitte und `run_manifest.json`. Diese Dateien wurden **nur als Text/Daten gelesen**, keine darin eingebetteten Clips geöffnet.

`segments.csv` hat **13 Segmente / 3.525 Frames / 141 s** aus drei Kontrollclips. D:1.219, L:1.720, U:586 Frames. **Kein Segment ist menschlich bestätigt**, alle nennen `codex_visual_first_pass`; keine `reviewed_segments.csv` wurde im inventarisierten Projekt gefunden. Die Bereiche liegen außerhalb Public 11185–18684, sind aber **dasselbe Challenge-Spiel**. Ein Wechsel zu anderen Frames dieses Spiels erfüllt daher nicht die aktuelle Regel „other games“.

| Szene | Frames, inklusive | Vorliegende Kennzeichnung |
|---|---|---|
| control_free_kick | 46008–47182 | Feste D/L/U-Grenzen und Notizen zu Vorbereitung, Aktion/Torsituation. |
| control_goal_kick | 37076–38250 | Feste L/U/L-Grenzen; Torwartphase ausdrücklich unsicher. |
| control_throw_in | 19335–20509 | Feste D/U/L/U/L-Grenzen; Freigabe und spätere Seitenlinienaktion unsicher. |

Die Grenzen wurden im Audit nicht korrigiert oder als neue Wahrheit bestätigt. Quelle: [E21](evidence/CODE_EVIDENCE.md#e21), [E22](evidence/CODE_EVIDENCE.md#e22); nachgezählte Mengen in [Datenprüfungen](evidence/data_lineage_checks.json).

## Wurden sie tatsächlich verwendet?

**Ja, zur vorläufigen Bewertung von Kontakt04 und Heuristik06.** Notebook 07 Zellindex3 setzt `REQUIRE_HUMAN_CONFIRMATION=False`. Zellindex13 entfaltet die Abschnitte zu Frame-Referenzen und bewertet D/L; Zellindex14 berechnet binäre Präzision/Recall/F1. Gespeichertes Manifest: **2.939 bewertete Frames, 586 ungewisse Frames**, Bestätigungszwang false, kein Training/keine Parameteränderung. Es wäre falsch, die Referenz allein wegen `human_confirmed=False` als unbenutzt zu bezeichnen. [E20](evidence/CODE_EVIDENCE.md#e20).

**Kein direkter Eingang in AdaBoost/Physics/Hybrid nachgewiesen.** Notebook 08 erwähnt die Annotationsdateien ausdrücklich als nicht gelesene Dateien; tatsächliche Lader/Fits verwenden öffentliche GT und Tracking. Im weiteren finalen Berechnungspfad wurde kein Lesen von `segments.csv`/`reviewed_segments.csv` und kein Anwenden dieser 13 Segmentlabels gefunden. Die Quelltextsuche ist unter `evidence/annotation_references.json` dokumentiert. Das ist ein begrenzter Negativbefund, keine Garantie, dass visuelle Erkenntnisse niemals eine spätere Idee beeinflussten.

## Weitere festgehaltene Beobachtungen

- Original 05 Zellindex10 zeichnet einen „beobachteten Pfiff (ca.)“ ein. Zellindex11 setzt `whistle_frame = (46*60+48)*FPS`, also70200; Zellindex14 nennt denselben Pfiff als Video-Beobachtung. Das ist eine **konkrete manuell/assistenzgestützt festgehaltene Zeitangabe**, nicht nur unspezifisches Anschauen.
- Original 05 Zellindex12 vergleicht an dieser Grenze Bewegungsstatistiken; weitere Szenen sind als Foul/Abseits/Halbzeitpause bezeichnet. Die **Featurewerte** derselben Zelle werden hingegen aus Raw-Positionen für alle Frames berechnet, nicht aus den Szenenlabels. [E23](evidence/CODE_EVIDENCE.md#e23), [E24](evidence/CODE_EVIDENCE.md#e24).
- Notebook 06 dokumentiert öffentliche Entwicklungs-/Live-Gegenbeispielszene und Sichtungsbefunde. Reine Clipauswahl über automatische Tags für neue Kontrollszenen ist von der Festlegung einer Wahrheitsgrenze zu trennen.
- Exploration03 Zellindex15 enthält sechs framespezifische Sichtungsnotizen. Sie sind als Diagnosen statt bestätigte Kontakt-/Kontrolllabels bezeichnet. Kein Training auf diesen sechs Beschreibungen gefunden. [E36](evidence/CODE_EVIDENCE.md#e36).
- Der neue T-DEED-Player blendet **bestehende algorithmische Vorhersagen** ein. ±0,4 s Anzeigedauer und .6-s-Wiedergabevorlauf sind Präsentationseinstellungen, keine Korrektur der Event- oder Besitzzeitpunkte. Er ist keine manuelle Eventreferenz. [E30](evidence/CODE_EVIDENCE.md#e30).

## Regelbefund ohne falsche Gleichsetzung

Aktuelles RULES §1 verbietet menschliche Labels **auch zur Validierung** dieses Spiels. „Nur Diagnose“, „nicht in die Submission kopiert“ und „außerhalb der öffentlichen fünf Minuten“ würden eine menschliche Referenz nicht automatisch erlauben. Notebook 07 stützt seine damalige Erlaubnis ausdrücklich auf die alte Small-amounts-Regel; diese Aussage ist heute überholt.

Gleichzeitig ist `codex_visual_first_pass` **kein Beweis einer menschlichen Annotation**. Der aktuelle Text erlaubt echte algorithmische Pseudolabels ohne menschliche Labelentscheidung. Unklar bleibt, ob der konkrete, interaktiv gesichtete, mit festen Grenzen versehene KI-Vorentwurf als zugängliche reproduzierbare algorithmische Pseudolabelpipeline anerkannt würde. Ein vollständig automatischer, dokumentierter Raw-to-Labels-Lauf für diese 13 Grenzen wurde nicht gefunden. Daher lautet der isolierte Befund **Potenziell problematisch**, nicht die unbelegte Behauptung einer nachweislich menschlichen Trainingsreferenz. Bestätigte menschliche Nachannotation wurde nicht gefunden; sie darf nicht allein aus dem geplanten Workflow abgeleitet werden.

## Cloud- und Veröffentlichungsrisiko

Die FAQ untersagt auch im alten Archiv die Übergabe von Wettbewerbsdaten/-auszügen an Drittanbieter-gehostete/Cloud-LLMs. Das Annotationsprotokoll nennt Sichtung von Originalvideo-Kontaktbildern durch Codex. Im vorliegenden Chat wurden vor dem Audit zudem Videoframe-Vorschauen als Bildinhalt an den Assistenten übergeben. [Gesprächsevidenz und Grenze](evidence/chat_context_notes.md).

Damit ist die Aussage „Datei liegt lokal, deshalb sicher kein Upload“ nicht belegt. Ob/wo der konkrete Assistenzbetrieb gehostet wurde und ob eine besondere Veranstalterfreigabe existiert, lässt sich aus dem Repository nicht abschließend prüfen. **Wenn diese Inhalte einem gehosteten/Cloud-LLM bereitgestellt wurden, widerspricht das der dokumentierten FAQ-Klausel.** Der technische/vertragliche Sachverhalt muss offengelegt geklärt werden, nicht als sicher regelkonform markiert werden. Die lokale T-DEED-Inferenz ist für sich kein Cloud-Upload.

19 der 24 inventarisierten Notebooks enthalten gespeicherte Bilder oder HTML mit Medieninhalten; einige enthalten Base64-Videos. Das ist nicht automatisch eine Veröffentlichung, aber ein konkretes Risiko beim späteren öffentlichen Repository. `.git` und eine Projekt-`.gitignore` wurden nicht gefunden. Es gibt hier **keinen Nachweis einer tatsächlichen öffentlichen Veröffentlichung**. Nichts wurde im Audit bereinigt oder gelöscht. [Medien-Inventar](evidence/embedded_media_inventory.csv).

Während dieses Audits wurden keine neuen Sichtungslabels erstellt, keine Videoframes an KI-Dienste gegeben und keine existierenden Labels geändert.

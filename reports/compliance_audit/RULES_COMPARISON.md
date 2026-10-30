# Vergleich der offiziellen Regelstände

Auditdatum: **29. Oktober 2026, Europe/Berlin** (Clientdatum). Projekt: `/Volumes/T7/More Than A Hack 2027/Initial Challenge`. Online-Stand: `f8f2629ff1e0985f81d7e59d8413678514ee1530`. Lokales Archiv: `3de6b60aeabd2475d95879a651d38b72bc4fba00`. Technische UTC-Abrufzeiten und SHA-256 stehen in [Versionsmanifest](evidence/official_version_manifest.json). Alle Aussagen betreffen den vorgefundenen Stand; keine nachträgliche Änderung der Entwicklungshistorie.


## Quellen, Versionsstand und Grenzen

Das lokale Archiv gehört zu Commit `3de6b60…` vom **15.10.2026 07:55:25 UTC**. `main` wurde zum Audit als `f8f2629…` aufgelöst, Commit vom **23.10.2026 13:42:40 UTC**. Die RULES-Historie enthält am 22.10. `c073f290…` und am 23.10. `f8f2629…` jeweils Klarstellungen zur Annotation. Diese Git-Zeiten belegen Versionsstände, nicht den individuell vertraglich vereinbarten Geltungsbeginn. Ohne Organisatorenentscheidung wird keine rückwirkende Sanktion oder Absicht behauptet. Quelle: [offizielle Regelhistorie](https://github.com/metrica-sports/more-than-a-hack-2027/commits/f8f2629ff1e0985f81d7e59d8413678514ee1530/RULES.md), lokal [Commitnachweis](evidence/rules_commit_history.json).

Die aktuell abgerufenen Dateien liegen unverändert unter `evidence/official_current/`, die Archivdateien unter `evidence/official_archive/`. Für Markdown-Dateien sind vollständige Unified-Diffs abgelegt. Die offizielle MIT-Lizenz umfasst ausdrücklich Code, Dokumentation und öffentliche GT; sie verleiht **keine** Rechte an Matchvideo/Tracking. Copyright-/Lizenzfreiheit der öffentlichen Datei ist nicht gleich Wettbewerbserlaubnis zum Training.

## Materielle Unterschiede mit Wortlaut

| Thema | Lokales Archiv | Aktueller Wortlaut / Quelle | Konsequenz für diesen Audit |
|---|---|---|---|
| Kleine Handannotation | „Small amounts of hand-labelled data used to *train or validate* a model are fine and normal.“ | „No hand labels on the provided game, in any amount and for any purpose“; ausdrücklich auch nicht Training/Validierung. [RULES §1](https://github.com/metrica-sports/more-than-a-hack-2027/blob/f8f2629ff1e0985f81d7e59d8413678514ee1530/RULES.md#training-and-validation-data) | Die frühere pauschale Erlaubnis lässt sich auf das aktuelle Challenge-Spiel nicht übertragen. |
| Öffentliche GT | Privates GT-Verbot galt „beyond the 5 minutes published in this repository“; keine gleich ausdrückliche Trainings-/Tuningklausel in dieser Passage. | „They are not training data and not a tuning set.“ [RULES §2](https://github.com/metrica-sports/more-than-a-hack-2027/blob/f8f2629ff1e0985f81d7e59d8413678514ee1530/RULES.md#2-use-the-private-ground-truth-or-any-human-produced-data-about-the-game); FAQ beantwortet Training/Tuning ausdrücklich mit Nein. | Training auf öffentlichen D/L-Labels ist nach aktuellem Text klar unzulässig. Eine technische Evaluatorprüfung bleibt erlaubt. |
| Externe Daten | Allgemein „External data.“ | „External data about other games.“ Verbot betrifft menschlich erzeugte Events, korrigiertes Tracking und Annotationen dieses Spiels aus jeder Quelle. | Kein Ausweichen auf Opta/StatsBomb oder eine andere menschliche Quelle desselben Spiels. |
| Trackingkorrektur | „fix the tracking“ allgemein, Herkunft der Zwischenrepräsentation nicht präzisiert. | Korrekturen müssen algorithmisch entstehen; manuelles Fixieren von Ballpositionen/Identitäten fällt unter Handannotation. | Algorithmisches Glätten/Detektieren ist zulässig; manuelle Korrekturlisten nicht gleichsetzen. |
| Pseudolabels / Sichtung | Keine gleich detaillierte Abgrenzung im alten RULES. | Algorithmisch erzeugte Pseudolabels ohne menschliche Labelentscheidung sind erlaubt. Anschauen/Debuggen ist erlaubt; daraus gemachte Labels/Korrekturen oder framespezifische Regeln/Konstanten sind die Grenze. [RULES §1](https://github.com/metrica-sports/more-than-a-hack-2027/blob/f8f2629ff1e0985f81d7e59d8413678514ee1530/RULES.md) | Ein GT-trainierter Teacher wird durch die Bezeichnung Pseudolabel nicht sauber. Ein KI-Sichtungsentwurf mit fest kodierten Grenzen muss separat auf Herkunft/Reproduzierbarkeit geprüft werden. |
| Training dokumentieren | Keine entsprechende eigene Zeile in SUBMISSION. | Jede Trainingslabelquelle, Herkunft, Umfang und Annotator dokumentieren; „None of it may come from the provided game“. [SUBMISSION](https://github.com/metrica-sports/more-than-a-hack-2027/blob/f8f2629ff1e0985f81d7e59d8413678514ee1530/SUBMISSION.md#3-a-technical-document) | Ein Statusmodell darf nicht als externe Vortrainierung oder bloße Physik dargestellt werden, wenn seine Ziele öffentliche Matchlabels waren. |
| README | Nur fünf Minuten als verfügbare GT bezeichnet. | Ergänzt Zweck: Pipelineprüfung statt Training. [README](https://github.com/metrica-sports/more-than-a-hack-2027/blob/f8f2629ff1e0985f81d7e59d8413678514ee1530/README.md) | Übereinstimmend mit FAQ und RULES, keine Ausnahme in der Kurzübersicht. |

## Was unverändert bzw. gesondert gilt

- Externe vortrainierte Modelle und auch grundsätzlich kommerzielle/LLM-Methoden sind erlaubt, **wenn zugänglich, prüfbar und dokumentiert**. Das ersetzt weder Lizenzrechte noch die spezielle Datenschutz-/Uploadgrenze.
- Die Cloud-Klausel in der FAQ ist bereits im **alten Archiv** vorhanden: keine Bereitstellung von Videos, Datensätzen, vertraulichen/restringierten Materialien oder Auszügen an Drittanbieter-gehostete bzw. Cloud-LLMs. [FAQ](https://github.com/metrica-sports/more-than-a-hack-2027/blob/f8f2629ff1e0985f81d7e59d8413678514ee1530/FAQ.md#can-i-use-llms-pre-trained-models-external-data). Die Anmeldungsbedingungen selbst wurden im Projekt nicht gefunden; deren vollständiger Inhalt bleibt offen.
- Unverändert: Submission muss aus Repository plus zulässigen Daten exakt regenerierbar sein; 199.319 geordnete Frames, H/A/D/X, Validator und öffentlicher Code/technische Dokumentation. Daten und rekonstruierbare Medien-/Trackingauszüge dürfen nicht öffentlich mitverteilt werden.
- Die FAQ erlaubt automatisch erzeugtes Smart Tagging explizit und grenzt es von GT ab. Es ist algorithmische, fehlerbehaftete Evidenz, keine menschliche Referenz.
- Offline-Nutzung zukünftiger **unbeschrifteter Eingaben** ist im vorgefundenen Regeltext nicht verboten. Das ist von Training auf Zielwerten desselben Testspiels zu trennen.

## Technische Versionskontrolle

| Datei | Vergleich | SHA-256 aktuell |
|---|---|---|
| `RULES.md` | geändert | `b6f63456d215e2e6016619f6268580ed8921bb96ba41c7d3037f2733f8d10153` |
| `FAQ.md` | geändert | `c536ec6401ea1b8c8a6dd54ee80e39518d3a521464ed9fe2bc1cf0ee70b7419b` |
| `README.md` | geändert | `19aa75a0928ff8a26b1865c5753c47b892a7461691ae42d8b9a74baee9bab92e` |
| `SUBMISSION.md` | geändert | `acb90eebc0f113fc072d90ac77be501e63de1dde65e9227186b4718bc24f22d2` |
| `EVALUATION.md` | geändert | `25b61f6d8a2bcbe77396bd9a9cae564b27424538e0a958aa1cd365e1e58ae571` |
| `DATA.md` | geändert | `b70aaa434e96a559f501fe5c3d65dbda6fba25c0fbd80ebe897ef23254de8c24` |
| `LICENSE` | identisch | `b1f93728571a232a0e158abdd869891f2efd51894134fb20678292c2468ff3ec` |
| `games.py` | identisch | `3b2122794e9e0476e2b3a871d14880e5fa47c4feaeacf99caef054c2309076ce` |
| `evaluation/run_evaluation.py` | identisch | `1c61564fe52499ba4af3006fb5eb4147b825e92bf516651add80de49d267b19f` |
| `evaluation/validate_submission.py` | identisch | `07ac29499acbd337e1dc1de1832d63f6e1fa1d981e22f6ad08212529e2bbee14` |
| `evaluation/possession_metrics.py` | identisch | `341bad48904b489d6e875397b27687f5d6a4d22a397f3dc8af3a00d48f16874d` |
| `starter/baseline.py` | identisch | `84d8a414fb1bdf8c7e1fbe4a8789fe6f9cc0c2cccec4685201285b75dbc0cfe6` |
| `evaluation/gt/BAR-ATH_possession_gt_public.csv` | identisch | `e596a9af9626c623bb94be6fd350e12ee9a75c76a696cfadca3bc01735e92487` |
| `.gitignore` | identisch | `0a54efd46c135e5e042794eb2fb3200b527c55313cb8ca22e61809040f268f70` |

Die Änderungen an README/FAQ/DATA/EVALUATION/SUBMISSION sind in den Diffs nachvollziehbar. Insbesondere belegen die bytegleichen `games.py`, Baseline-, Validator-, Evaluator-/Metrikdateien und die öffentliche GT, dass dieser Konflikt nicht durch heimlich geänderte Bewertungslabels oder eine neue Scoreformel erklärt wird. Es wurde kein Evaluator neu ausgeführt.

## Bewertungsmaßstab

„Regelverstoß nach dokumentiertem Regelwortlaut“ meint einen belegten Vorgang, der dem **aktuellen** expliziten Text widerspricht. Es ist keine verbindliche Disqualifikationsentscheidung. Historische Vertretbarkeit unter dem älteren Archiv, Geltungsbeginn und Sanierung nach bereits erfolgter GT-Nutzung müssen Organisatoren klären. Bei mehrdeutiger KI-Vorannotation oder fehlendem Hostingnachweis wird kein eindeutiger Verstoß erfunden.

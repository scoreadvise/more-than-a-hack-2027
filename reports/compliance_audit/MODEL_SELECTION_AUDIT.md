# Modellwahl, Varianten und öffentliche Leistungsrückkopplung

Auditdatum: **29. Oktober 2026, Europe/Berlin** (Clientdatum). Projekt: `/Volumes/T7/More Than A Hack 2027/Initial Challenge`. Online-Stand: `f8f2629ff1e0985f81d7e59d8413678514ee1530`. Lokales Archiv: `3de6b60aeabd2475d95879a651d38b72bc4fba00`. Technische UTC-Abrufzeiten und SHA-256 stehen in [Versionsmanifest](evidence/official_version_manifest.json). Alle Aussagen betreffen den vorgefundenen Stand; keine nachträgliche Änderung der Entwicklungshistorie.


## Belegte Verwendung, nicht rekonstruierte Absicht

Es gibt **58 gespeicherte Scorezeilen**, einschließlich Reproduktionen und Referenzduplikaten, mit **28 unterschiedlichen Submissionnamen**. Diese Zahlen zählen **keine 58 unabhängigen Versuche**. Mehrere Zeilen sind dieselbe Datei erneut evaluiert. Zusätzlich existieren Status-F1/AUC-/Timingdiagnosen ohne offizielle Scoreboardzeile. Vollständige Dateipfade und originale Spalten: [historische Scoreboards](evidence/historical_scoreboards.csv).

Leistungsorientierte öffentliche Auswertung ist belegt: neue Varianten werden verglichen, nach `spell_f1_mean` sortiert, H/A-Fehler und GT-Wechsel gezielt untersucht, und die Entwicklung führt zum als aktuellen Hauptansatz erhaltenen Spatial Hybrid. Eine maschinelle Grid-/Random-Search nach der besten öffentlichen Konfiguration wurde nicht gefunden. **Nicht für jede Designentscheidung ist beweisbar, dass der öffentliche Score ihr alleiniger oder ausschlaggebender Grund war.** Es fehlen vollständige zeitgestempelte Entscheidungsprotokolle und Git-Historie des Projekts. Kommentare „nicht auf GT optimiert“ belegen die deklarierte Absicht, aber keine unabhängige Entstehung nach bereits wiederholter GT-Sichtung.

## Rekonstruierbare Stufen

| Stufe / Original-05-Zellindex | Was sich tatsächlich ändert | Referenzverwendung / Einordnung |
|---|---|---|
| Offizielle Reproduktion, Notebook 02 | Vier vorgegebene Fenster; Hauptbaseline bleibt smooth50, obwohl smooth125 öffentlich besser ist. | Technische Referenzreproduktion mit ausdrücklich dokumentierter Nichtauswahl des öffentlichen Gewinners. Kein lokaler Window-Tuningnachweis. |
| Kontakt04; Heuristik06 | RTS-/Nahkontaktregel, danach zusätzliche D-Seeds und Neustartlogik. | Vorhersagen im jeweiligen Notebook vor neuem GT-Laden fixiert; danach Score-/Fehlervergleich. Bekannte öffentliche Fehlerszenen werden für weitere Entwicklung betrachtet. Übergreifende GT-Freiheit der Parameter bleibt offen. |
| Notebook 08 | Je eine LogReg-/AdaBoost-Konfiguration, roh gegen Median91. | Vier purged Folds; Ziele stammen aus öffentlicher GT. Keine umfangreiche Suche; beide Modelle behalten. Der spätere Hauptpfad nutzt AdaBoost. |
| 2–7 | Öffentliche Modellübereinstimmung, OR-Fusion und Erweiterung/Brücken/neue D-Ablationen. | Gruppierung nach GT, öffentliche D-F1 und offizielle Scores. Ablationen teils im öffentlichen Fenster identisch: gleicher Score entscheidet deren Qualität im Restspiel nicht. |
| 13–17 | Bewegungsmerkmale bei korrekten/falschen D-Fällen; GT-D-Beginne; AUC; feste Evidenztabelle; Viterbi-Kosten. | **GT-gestützte Fehler-/Featureanalyse vor neuen Statusregeln belegt.** Evidenztabelle .96/.70/.62/.04 und Motionparameter werden als feste Annahmen gesetzt, nicht per dokumentiertem Fit geschätzt. Eine GT-unabhängige Herleitung ist nicht belegt. |
| 17–24 | Kosten von frameweiser auf sekundenskalierte Evidenz umgestellt; H/A nach wiederhergestelltem LIVE rekonstruieren; Originalkontakte erneut prüfen. | Technische Korrekturen/Rekonstruktionsprüfung und Leistungsdiagnostik gemischt. Zellindex 20 untersucht ausdrücklich einen zuvor verlorenen öffentlichen Korrekturbereich. |
| 27 | Kontinuierliche AdaBoost-Scoreevidenz, Heuristikfusion .75. | Quantilskalierung aus nichtöffentlichen **Vorhersagescores**, nicht deren Labels. Transduktive Offline-Kalibrierung, kein Beleg für Verwendung privater Ziele. Öffentliche Scorevergleiche danach. Nicht aktueller Pfad. |
| 31–33 | Live-Veto, dann Hysterese (.60/.25, 2 s). | Öffentliche Fehler und gesamte Modellwidersprüche. Keine finale Übernahme dieses Veto-v2-Pfads; vollständige Entscheidungsbegründung fehlt. |
| 35–39 | Physics v1: .40 Bewegung /6 m/s / .50 Ballabdeckung /3,5 m Nähe; Gewicht1,5. V2 ersetzt harte Grenze durch Sigmoide. V3 ergänzt No-Ball .20/.60 und Gewicht1,5. | Jeweils öffentliche F1-/spellF1-Vergleiche. V3 baut im Code ausdrücklich wieder auf v1 statt v2 auf. Ob allein der Score oder weitere fachliche Evidenz diese Wahl bestimmte, ist nicht vollständig rekonstruierbar. |
| 41 | No-Ball-Gewicht 1,2/1,5/1,8. | Vorliegender Code zeigt **Sensitivität/Stabilität gegenüber Referenz**, keine öffentliche Score-Maximierung dieser drei Gewichte. Nicht als bewiesenen GT-Hyperparameter-Sweep umdeuten. [E17](evidence/CODE_EVIDENCE.md#e17) |
| 43–46 | H/A/D-Quelle, Oracle-Status, Kontaktfolgen und GT-Teamanteile. | Explizite Zielwertdiagnostik; Oracle nicht exportiert. Sie zeigt, dass das öffentliche Fenster intensiv inhaltlich analysiert wurde. [E11](evidence/CODE_EVIDENCE.md#e11), [E12](evidence/CODE_EVIDENCE.md#e12), [E13](evidence/CODE_EVIDENCE.md#e13) |
| 47–48 | Kontakt-HMM mit festen Kosten1,4/1,8/.8; danach gewonnene/verlorene Phasen. | HMM erreicht öffentlich höheres macroF1, aber niedrigeres spellF1 als Physics v3. Es ist nicht Eingang des finalen Hybrid. Die exakte ursprüngliche Entscheidung bleibt mangels Ledger offen. |
| 52–57 | Nächstes Team/Bewegungskopplung gegen GT, Timing **aller öffentlichen GT-Wechsel**, räumliche Kandidaten/Alignments. | Die neue räumliche Idee wurde im selben Entwicklungsumfeld auf öffentliche GT-Wechsel untersucht. Die Ereigniserzeugung greift nicht direkt auf die GT-Zielzeit als Kandidatenposition zu. [E14](evidence/CODE_EVIDENCE.md#e14), [E15](evidence/CODE_EVIDENCE.md#e15) |
| 58–59 | Finaler Hybrid: höchstens±3 s zum Modellwechsel, Nachbarphasen schützen; Stabilität und GT-ferne Clips. | Tatsächliche Framewahl GT-frei im Algorithmus. Danach öffentliche Grenzmatches, korrigierte/verschlechterte Frames und offizieller Score. **Finale Inferenz ohne direkte GT ist kein Nachweis GT-freier Entwicklung.** [E16](evidence/CODE_EVIDENCE.md#e16) |
| Notebook 10/11 | Eingefrorenen Stand wiederherstellen und byte-/framegleich prüfen. | Wiederholte Evaluation der identischen Datei ist hier technische Regression/Reproduktion; keine neue Modellwahl in diesem Release nachgewiesen. Frühere Abhängigkeiten bleiben bestehen. |
| Video-Pilot 13 | Externer Checkpoint, feste .2-CLI-Schwelle, fünf automatisch ausgewählte Kontexte außerhalb Public. | Keine öffentliche Besitz-GT für Auswahl/Schwellen im eigenen Pilot-Rechenweg. Keine v1-Fusion oder Besitzscoreoptimierung. |

## Tatsächlich gespeicherte offizielle Ergebnisse

Alle folgenden Werte sind **öffentliche Entwicklungswerte**, keine unabhängige Leistungsvalidierung und keine im Audit neu berechneten Scores. Bei unterschiedlichen Namen kann dieselbe Vorhersage mehrfach vertreten sein.

| Submission | spell_f1_mean | macro_f1 |
|---|---:|---:|
| `spatial_hybrid_v1` | 0.564103 | 0.865360 |
| `physics_v3_reference` | 0.543590 | 0.854311 |
| `contact_hmm_v1` | 0.507692 | 0.884928 |
| `hier_v2_reconstructed` | 0.502564 | 0.841159 |
| `hier_v3_contact_rerun` | 0.502564 | 0.841159 |
| `hier_or_v0` | 0.460000 | 0.835806 |
| `hier_v2_motion_reconstructed` | 0.502564 | 0.841159 |
| `hier_base06` | 0.436364 | 0.811752 |
| `hier_live_veto_v1` | 0.502564 | 0.841159 |
| `hier_v2_reference` | 0.502564 | 0.841159 |
| `hier_physics_v1` | 0.543590 | 0.846368 |
| `hier_physics_v2_continuous` | 0.533333 | 0.846031 |
| `physics_v3_no_ball` | 0.543590 | 0.854311 |
| `physics_v1_reference` | 0.543590 | 0.846368 |
| `hier_ml_soft` | 0.526316 | 0.777403 |
| `hier_fusion_soft` | 0.504762 | 0.810535 |
| `hier_live_veto_v2` | 0.480000 | 0.798160 |
| `hier_viterbi_v1` | 0.460000 | 0.835806 |
| `hier_viterbi_v2` | 0.460000 | 0.835806 |
| `hier_viterbi_v2_motion` | 0.460000 | 0.835806 |
| `spatial_raw` | 0.037838 | 0.597227 |
| `spatial_median1s` | 0.106024 | 0.609738 |
| `baseline_smooth125` | 0.424242 | 0.581185 |
| `baseline_smooth50` | 0.325581 | 0.620733 |
| `baseline_smooth25` | 0.286792 | 0.619991 |
| `baseline_raw` | 0.037838 | 0.597227 |
| `contact_state_shared_D` | 0.391111 | 0.625732 |
| `contact_state_stoppage_v1` | 0.436364 | 0.811752 |

## Drei Verwendungen sauber trennen

1. **Technische Prüfung:** Validator, Frames/H/A-Konvention prüfen, bereits festgelegten Checkpoint-/CSV-Stand regenerieren und auf Gleichheit prüfen. Dafür stellt der Veranstalter die fünf Minuten bereit. Notebook 02 und insbesondere die Release-Reproduktion10/11 enthalten solche legitimen Prüfzwecke.
2. **Diagnostik:** GT-Klassenanteile, Verwechslungen, spezifische Wechselzeiten, Oracle-Obergrenzen, AUC/Timingkurven. Das ist nicht dasselbe wie ein Fit oder ein eingebauter GT-Patch. Als Entwicklungsfeedback ist es aber mehr als bloße Formatprüfung und kann spätere methodische Entscheidungen beeinflussen.
3. **Leistungsorientierte Auswahl/Tuning:** Wiederholte Bewertung neuer Regeln und Übergang zum Hauptmodell im selben öffentlichen Fenster. Der aktuelle Text stellt dieses Fenster nicht als Tuningdaten bereit. Wie weit eine bestimmte frühere Diagnose oder informelle Wahl darunter fällt, muss bei fehlender Entscheidungshistorie offengelegt statt als erwiesen optimierter Parameter behauptet werden.

## Konkrete Schlussfolgerung

Direktes Training ist unabhängig von jeder Tuningdebatte nachgewiesen und reicht für den zentralen aktuellen Regelkonflikt. Zusätzlich besteht ein erheblicher, konkret belegter **Adaptions-/Selektionsbias**: die öffentliche Referenz war wiederholt sichtbar und wurde für zielbezogene Modellbeurteilung genutzt. `parameter_search=false`, nachgelagertes GT-Laden im Teamnotebook und ein finales `fit`-freies Inferenzskript beseitigen diesen Bias nicht. Die Scoresteigerung auf .564103 darf nicht als unbekannter Vollspieltest oder als Nachweis der besseren Generalisierung interpretiert werden.

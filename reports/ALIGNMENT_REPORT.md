# T-DEED und Trackingkontakte: Abschluss der Diagnose

## Ergebnis in vier getrennten Ebenen

- **Technik:** Vorhandene 47 T-DEED-Events aus fünf Clips /60s geprüft, ursprüngliche Soft-NMS aus gespeicherten Summenscores vollständig reproduziert. Keine neue Inferenz und kein Training.
- **Zeitliche Koinzidenz:** Im festgelegten ±0,5-s-Hauptfenster 19/47 Events eins zu eins zu Originalkontakten zugeordnet. Median absoluter Paarabstand 0.160s. Bei verschobenen Zeitpunkten medianer Matchanteil 0.362.
- **Semantische Ereignisqualität:** Unbekannt. Weder Matching noch fehlendes Matching sind eine Event-Ground-Truth-Prüfung.
- **Ballbesitz-Zusatznutzen:** Nicht gemessen. Spatial Hybrid v1 unverändert; kein v2-Decoder oder neuer Besitzscore.

## 1. Sind Videoevents technisch sauber synchronisiert?

Ja für diese vorhandenen Dateien: Original-PTS-Audit 199.319 Frames bei25FPS, Raw-ID−1=globaler Videoframe, Offset0; Originalvideo unverändert nach Größe/mtime. Alle300 Paket-PTS je Clip erneut geprüft; Cliphashes identisch zur tatsächlichen Inferenz. Globale CSV-Frames, Startzeit und Stride2 konsistent. Native Eventauflösung80ms, nicht25-FPS-Aktionsgenauigkeit. Ein semantischer Eventzeitversatz bleibt ungemessen; kein Offset anhand von GT optimiert. Kein Videoframe wurde geöffnet.

Geometrische Fensterabdeckung jeweils145/150 Rasterpositionen (letzte0,40s fehlen). Scoreunterstützung kann durch Displacement zusätzlich einzelne Positionen auslassen. Die Negativkontrolle nutzt nur die zusammenhängende geometrisch abgedeckte11,6-s-Strecke. Vorgenannte technische Eindeutigkeit ist keine Bestätigung des Zeitpunkts der tatsächlichen Aktion.

Zusätzliche deskriptive Datenprüfung: 437 Rasterkandidaten vor Soft-NMS werden zu47 finalen Eventpunkten. Keine identischen Clip/Frame/Klasse-Duplikate. 5 benachbarte Vorhersagepaare gleicher Klasse liegen noch innerhalb des Soft-NMS-Radius; Soft-NMS ist weich. Ohne unabhängige Aktionsreferenz wird daraus keine manuelle Dublettenentscheidung und keine weitere Löschung abgeleitet.

## 2. Wie stark stimmen die Events mit den ursprünglichen Kontakten überein?

Originale Kontaktkandidaten aus vollständigen Raw-Ballruns mit unverändertem RTS-/Peak-/Nähealgorithmus rekonstruiert: 1432 Kandidaten, **0 abweichende Kontakt04-Labels auf allen199.319 Frames**. Physics und Hybrid haben jeweils258 direkte H/A-Wechsel in vorhergesagtem LIVE. Räumliche LIVE-Crossings stammen aus derselben eingefrorenen Proximity-Marge und11/min8-Glättung.

Matching ist klassenübergreifend gemeinsam pro Clip/Quelle/Fenster; maximale Anzahl, danach minimale Summe absoluter Zeitabstände. Keine Referenz wird doppelt vergeben. Mehrdeutigkeit umfasst mehrere zulässige Referenzen und Konkurrenz anderer Videoevents. Die ±0,5-s-Angabe entspricht wegen des25-FPS-Rasters höchstens12Frames =0,48s. Referenzen im bis zu2s breiten Trackingrand außerhalb des Videoschnitts sind vorhanden und einbezogen.

| Klasse | Zugeordnet | Anteil | Verschoben: Mediananteil | Median abs. Delta [s] | Mehrdeutige Events | Holm-Tail |
|---|---:|---:|---:|---:|---:|---:|
| ALL | 19/47 | 0.404 | 0.362 | 0.160 | 6 | 1.000 |
| DRIVE | 7/20 | 0.350 | 0.450 | 0.160 | 2 | 1.000 |
| HIGH PASS | 1/2 | 0.500 | 0.000 | 0.160 | 1 | 1.000 |
| PASS | 11/25 | 0.440 | 0.320 | 0.280 | 3 | 1.000 |

Alle vier vorab festgelegten Fenster und alle vier Referenzquellen stehen in `tables/observed_matching_metrics.csv`, vollständige Paarzuordnungen in `tables/one_to_one_event_matches.csv`. Ein Event kann technisch auswertbar sein, obwohl Balltracking oder der Kontaktdetektor im Zeitfenster ausfallen; diese Fälle sind in der Coverage erkennbar und nicht als Videofehler zu zählen.

**Negativkontrolle:** 1.000 gemeinsame, klassenanzahlerhaltende zirkuläre Verschiebungen je Clip, Seed42, mindestens2,4s Kreisabstand auf dem80-ms-Raster. Keiner der 64 vorab festgelegten Vergleiche hat einen Holm-korrigierten oberen Tail-Anteil <0,05. Unter der vorab festgelegten diagnostischen Schwelle ergibt sich damit kein starker Hinweis auf eine überzufällige Phasenausrichtung; das ist kein Nachweis fehlender Aktionsqualität. Wegen der ausgeschlossenen kleinen Verschiebungen sind diese Tail-Anteile keine exakt kalibrierten konfirmatorischen p-Werte. Es wurden64 Vergleiche gemeinsam korrigiert; kein günstiges Fenster nachträglich gewählt. Die Nullverteilung erhält nicht die Lage relativ zu LIVE-/D-Phasen oder Ballabdeckung. Clipauswahl, lokale Eventdichte, kurze Zeitspannen und Wrap-around begrenzen den Test. Er ist ein Test spezieller relativer Phase unter diesem Nullmodell, keine allgemeine Unabhängigkeits-/Präzisionsprüfung.

## 3. Wie viele zusätzliche Ereignisse liefert T-DEED?

Alle 47 Zeilen sind zusätzliche **Videovorhersagen**, keine neu bestätigten Fußballereignisse. Davon haben **26** keinen einzigen Originalkontakt innerhalb±0,5s und **7** keinen innerhalb±2s. Nicht jedes ungepaarte Event ist neu relativ zur Kontaktliste: Eins-zu-eins-Konkurrenz kann ein Event ungepaart lassen, obwohl Kontakte in seiner Nähe liegen.

| Klasse | Videoevents | Kein Kandidat±0,5s | Ungepaart eins zu eins±0,5s | Kein Kandidat±2s |
|---|---:|---:|---:|---:|
| DRIVE | 20 | 12 | 13 | 3 |
| HIGH PASS | 2 | 1 | 1 | 1 |
| PASS | 25 | 13 | 14 | 3 |

Zusatzvorschläge ohne Kandidaten stehen samt Score, Modellstatus, Ball-/Detektorabdeckung und Zeitkontext in `tables/events_without_any_contact_0_5s.csv`. Fehlendes Tracking kann das Ausbleiben von Kontakten erklären. Semantik oder Zusatznutzen werden daraus nicht abgeleitet.

## 4. Welche Events lassen sich einem Team zuordnen?

**7** Events erfüllen die vorher festgelegte strenge Trackingkonsensregel bei±0,5s. Weitere 25 sind mehrdeutig, 15 haben keine ausreichenden geometrischen/Kontakthinweise. Konsens bedeutet Übereinstimmung abhängiger Trackingquellen, keine unabhängig bestätigte Team-/Aktorzuordnung. Native `video_event_team` bleibt bei allen `unknown`, `player_track_id` leer. **Semantisch sicher zugeordnete Videoakteure:0 unabhängig belegt.**

Der nächste rohe Trackslot, alle Teams unter der übernommenen2-m-Grenze, nahe Originalkontakte und beide Besitzmodelle bleiben als getrennte Felder sichtbar. Eine Trackslot-ID bezeichnet nicht zwingend dauerhaft dieselbe Person. Das Konsenskriterium erzeugt kategoriale, unvalidierte Zuordnungsindizien und ausdrücklich keine erfundene Confidence-Wahrscheinlichkeit.

Die Coverage zeigt außerdem **9 Videovorhersagen in vorhergesagtem D** und 38 in LIVE. Insbesondere liegen alle6 build_up-Vorhersagen in der eingefrorenen D-Sequenz. Automatischer Kontextname, Videoklasse und Modellstatus widersprechen sich hier teilweise; keine dieser Quellen entscheidet ohne unabhängige Referenz, welche richtig ist. Gründe jeder fehlenden/mehrdeutigen Teamkonsenszuordnung stehen in `team_attribution_reasons` und der zugehörigen Häufigkeitstabelle.

## 5. Welche Klassen könnten Ballbesitzwechsel ergänzen?

PASS/HIGH PASS können zeitliche Aktionshinweise an bestehenden Kontakten sein, belegen aber keinen Teamwechsel. DRIVE könnte Kontext für eine fortgesetzte Phase liefern: 10/20 DRIVE-Punkte liegen im ±2-s-Kontext einer stabilen vorhergesagten Hybrid-Teamphase. Das ist eine Modellkontextbeobachtung, kein unabhängig bestätigtes kontrolliertes Dribbling.

Die Nähe zu Physics-/Hybrid-Wechseln und räumlichen Crossings ist für jede Klasse/Fenster separat gespeichert. Vor-/Nachlauf ist als signiertes Delta sichtbar; **kein systematischer Modelloffset wird daraus korrigiert**. Kein Interception-/Reception-/Control-Label existiert in der verwendeten Taxonomie; im Pilot wurden auch keine Tackle-/Blockereignisse ausgegeben.

## 6. Reicht das für einen ersten experimentellen v2-Decoder?

**Die technische Schnittstelle ist vorbereitet; ein wissenschaftlicher Nutzen ist mit diesem Pilot nicht nachgewiesen.** Eine ereignisbasierte Featuretabelle mit 47 Zeilen liegt vor. Sie erlaubt nach gesonderter Freigabe einen begrenzten technischen Integrationsversuch. Eine positive Aussage zu besserem spellF1, falschen H/A-Wechseln oder zuverlässiger Aktions-/Teamsemantik ist derzeit nicht begründet. Die Entscheidung für einen neuen Decoder bleibt offen; es wurde keiner gebaut.

Empfehlung: Zuerst Event-/Zeit-/Teamqualität auf zulässigen unabhängigen Spielen prüfen und den bislang kleinen technischen Piloten ggf. mit ausdrücklich freigegebenem Umfang erweitern. Für eine spätere probabilistische Kontaktevidenz Scores nur bei vorhandener Abdeckung verwenden, fehlende Werte erhalten und semantische Klasse sowie signierten Zeitabstand getrennt einspeisen. Abgeleitete Trackingteams nicht als unabhängige Video-Teamwahrscheinlichkeit doppelt zählen. Fusionsgewichte/Zeittoleranzen erst auf erlaubten Validierungsdaten begründen; aktuelles Match nicht mit menschlichen Labels ergänzen.

## Nachvollziehbarkeit und Artefakte

- Notebook14: zentrale Imports, festes Protokoll, Originalkontakte, synchronisierte bestehende Vorhersagen, optimale Zuordnung, Negativkontrolle, Teamdiagnostik und Featureexport; frischer Kernel ohne Modellinstallation ausführbar.
- `tdeed_tracking_event_features.csv`: Haupttabelle; `FEATURE_DICTIONARY.md` erläutert Herkunft und fehlende Felder.
- `tables/`: Soft-NMS-Vorstufen, Eventverteilungen, Synchronisierung, Referenzereignisse, Paarzuordnungen, Nullkontrollen, Coverage und Zusatzvorschläge.
- `figures/`: Klassen/Scores, gemeinsame Zeitleisten, Zeitdifferenzen und reale Übereinstimmung gegenüber zufälligen Verschiebungen. Keine Videobilder.
- `manifests/`: Vorabprotokoll, Inputhashes, gespeicherte Zufallsverschiebungen, Laufzeit/Integrität.

Die historische Bestandsfreigabe bleibt berücksichtigt; keine erneute Grundsatzprüfung. Spatial Hybrid v1 bleibt die eingefrorene Referenz mit zuvor berichteten öffentlichen Werten0.564103/0.865360. Alle geschützten Quelldateien, Gewichte, Eingaben und Vorhersagen bleiben unverändert. Dieser Lauf liest keine öffentliche GT und erzeugt keine wissenschaftlichen Wahrheitslabels.

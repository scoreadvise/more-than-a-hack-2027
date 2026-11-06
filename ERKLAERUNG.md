# Was der Ansatz beachtet und wie er funktioniert

## Die Aufgabe in einem Satz

Für jeden der 199.319 Frames von Barcelona–Athletic wird entschieden, ob Barcelona den Ball kontrolliert (`H`), Athletic (`A`), ob der Ball tot ist (`D`, Unterbrechung) oder ob der Frame nicht bewertet wird (`X`, außerhalb der Halbzeiten). Bewertet wird vor allem mit dem **spellF1**. Jede Besitzphase zählt dabei als ein Objekt, das zeitlich gut überlappen muss (IoU 0,3–0,7). Es zählen also ganze Phasen mit sauberen Grenzen, nicht einzelne Frames.

## Was der Ansatz beachtet

### 1. Die Regeln (Regel-Mail vom 04.11.2026)

| Regel | Umsetzung |
|---|---|
| Kein Training, Fitting oder Kalibrieren auf der Challenge-GT oder dem Video | Alle Modelle und alle Parameter stammen ausschließlich aus **externen Spielen**. |
| Keine Handlabels und keine menschlich erzeugten Daten zum Challenge-Spiel | Aus dem Challenge-Spiel gehen nur Tracking (`atd.txt`) und Metadaten (`atd.xml`) ein. Smart Tagging und Video werden nicht verwendet. |
| Ergebnis nicht am Video prüfen | Es wird nichts am Video geprüft. |
| Challenge-Daten nicht an KI-Dienste geben | Verarbeitung nur lokal. An den Assistenten gingen nur Aggregate, etwa Mediane und Anteile. |
| Externe Daten nur mit Nutzungsrechten | DFL/IDSSE: CC BY 4.0. Metrica-Beispieldaten: öffentlich zum Experimentieren freigegeben, ohne formale Lizenz; eine Rückfrage bei den Organisatoren ist offen. |

Die öffentliche 5-Minuten-GT wurde jeweils **erst nach dem Einfrieren** gelesen und nur technisch geprüft: Stimmen Frames und Labelbedeutung? Sie hat keine Entscheidung beeinflusst.

### 2. Die Domänenlücke

Trainiert wird auf anderen Spielen, deren Tracking anders aussieht als das der Challenge:
- **DFL-Daten** sind fast perfekt: Der Ball ist immer sichtbar, in Unterbrechungen aber eingefroren.
- **Challenge-Tracking** ist videobasiert: Der Ball fehlt oft, besonders in Unterbrechungen. Es gibt Ausreißer-Tracks mit mehr als 11 Spielern je Team.

Deshalb wurden die DFL-Daten künstlich **verschlechtert**, damit sie der Challenge ähneln (Szenario d67s, Notebook 02):
- zustandsabhängiger Ballausfall als Markov-Kette, in Unterbrechungen häufiger,
- blockweiser Spielerausfall,
- Glättung und Versatz der Ballposition.

Abgeglichen wurde dabei nur an **Aggregaten** der Challenge-Eingaben, ohne GT.

Zusätzlich gibt es die **Metrica-Beispielspiele** (Notebook 03). Sie stammen aus derselben Tracking-Pipeline wie die Challenge und haben echte Ausfälle. In Unterbrechungen liegen sie der Challenge deutlich näher als DFL; die Trennschärfe der Basismerkmale zur Challenge liegt bei 0,09 statt 0,22.

### 3. Die Besitzdefinition

Die Challenge verlangt **kontrollierten** Besitz. Bloße Berührungen zählen nicht als Wechsel. Der Ansatz jagt deshalb bewusst keine sehr kurzen Pingpong-Phasen unter 3 s. Genau dort liegen zwar viele rechnerische Fehler, sie würden aber auf eine Labelkonvention optimieren, die für die Challenge nicht gesichert ist.

### 4. Methodische Sorgfalt

- **Validierung per Leave-one-match-out:** Jedes Spiel wird mit Modellen vorhergesagt, die es nie gesehen haben.
- **Hauptkriterium ist Metrica**, weil es der Challenge am nächsten ist. DFL dient als Kontrolle.
- **Eine Änderung pro Schritt**, mit Domänenprüfungen auf den Challenge-Eingaben vor jeder Übernahme, nur mit Aggregaten. Die Entwicklungsnotebooks samt negativer Ergebnisse liegen im Hauptprojekt (`approach_v2/`), nicht in diesem Paket.
- **Reproduzierbarkeit:** fester Seed, versionierte Pakete, Prüfsummen für alle Rohdaten. Zwei vollständige Läufe ergeben bitgleich dieselbe Abgabedatei.

## Wie der Ansatz funktioniert

```
Tracking (Ball + Spieler, 25 fps)
   │
   ├─ 1. Plausibilitätsregel ─────────── Sprünge > 40 m/s (Ball) bzw. > 12 m/s (Spieler) → fehlend
   │
   ├─ 2. Merkmale je Frame
   │     ├─ D-Merkmale (Ballsichtbarkeit, Feldrand, Bewegung, Teamaggregate ±40 s)
   │     └─ Besitzmerkmale (Reichweite, Gegnerdruck, Teamform ±4 s)
   │
   ├─ 3. Zwei Wahrscheinlichkeiten je Frame
   │     ├─ P(D)        ← D-Modell (Boosting, 159 Merkmale)
   │     └─ P(H | live) ← H-Modell (Boosting, 59 Merkmale)
   │
   ├─ 4. Gemeinsamer Viterbi-Decoder über H / A / D
   │     Wechselkosten c_HA = 10, c_D = 40  →  glatte, zusammenhängende Phasen
   │
   ├─ 5. Wiederanpfiffe nachschärfen
   │     ├─ Kick-Snap: D-Ende auf den Schuss/Pass des Wiederanpfiffs (−6/+4 s)
   │     ├─ Anstoß-Regel: Ball am Mittelpunkt, der schnell wegläuft → davor D
   │     └─ Wiederanpfiff-Team-Modell als Prior (w = 4): Wer führt aus?
   │
   └─ 6. Labels für die bewerteten Halbzeiten, sonst X  →  CSV, Validierung, SHA-256
```

### Schritt 1 · Plausibilitätsregel

Unmögliche Sprünge im Tracking gelten als fehlend: Ball über 40 m/s, Spieler über 12 m/s. Das trifft vor allem Fehlzuordnungen im videobasierten Tracking.

### Schritt 2 · Merkmale

**Für die Unterbrechung (D)**, nach Lang et al. (2022):
- **Ballsichtbarkeit:** Ist der Ball gerade sichtbar? Seit wann nicht mehr? Wann wieder? Anteil über 1, 5 und 15 s.
- **Feldrand:** Wie weit war der Ball beim letzten bzw. nächsten Sehen vom Rand entfernt? Ein Ball, der am Rand verschwindet, deutet auf Aus hin.
- **Spielerbewegung:** Mediangeschwindigkeit und Anteil laufender Spieler. In Unterbrechungen wird gegangen.
- **Teamaggregate** zu 11 Zeitpunkten von −40 bis +40 s: Abstand der Teams, Ausbreitung, Lage des Schwerpunkts. Ein Freistoß oder eine Ecke hat ein typisches Bild, das sich über Sekunden aufbaut.

**Für die Besitzseite (H/A)**, nach Link & Hoernig (2017):
- **margin:** Wie viel näher ist der nächste H-Spieler am Ball als der nächste A-Spieler? Dazu eine Fassung mit vorhergesagten Positionen in 1 s.
- **reach:** Wie lange ist ein Team schon in 2 m Reichweite? Kontrolle heißt, länger am Ball zu bleiben.
- **Gegnerdruck:** Spieler je Team im 3-m-Umkreis, Kontext ±2 s.
- **Robuste Teamform**, Median und Interquartilsabstand mit ±4 s: Welches Team schiebt nach vorne, macht das Feld breit, steht tief? Die Spielrichtung ergibt sich aus dem tiefsten Spieler, dem Torwart. Diese Merkmale funktionieren auch, wenn der Ball fehlt. In der Entwicklung war das der wichtigste Gewinn: Die Trefferquote in Balllücken stieg von 9 % auf 29 %.

### Schritt 3 · Zwei Boosting-Modelle

- **D-Modell:** HistGradientBoosting auf den D-Merkmalen *und* den Besitzmerkmalen. Ausgabe: P(Ball tot) je Frame.
- **H-Modell:** HistGradientBoosting nur auf Live-Frames. Ausgabe: P(H | Ball lebt).

Beide werden auf 10 externen Spielen trainiert: 7 DFL-Spiele in der degradierten Fassung d67s und 3 Metrica-Spiele. Die Metrica-Labels werden automatisch aus deren Events abgeleitet (Notebook 03):
- **D:** vom Aus, Foul oder Tor bis zum nächsten Standard,
- **H/A:** das Team des letzten Besitz-Events.

### Schritt 4 · Gemeinsamer Decoder

Frame für Frame zu entscheiden, würde flackern und Hunderte Mini-Phasen erzeugen. Der Decoder ist deshalb ein **Viterbi-Algorithmus** über die drei Zustände H, A und D:
- Er nutzt die Modellwahrscheinlichkeiten als Evidenz.
- Jeder Wechsel kostet eine Strafe: c_HA = 10 für H↔A und c_D = 40 für Spiel↔Unterbrechung.
- Gewählt wird die Labelfolge mit der besten Gesamtbilanz. Ein Besitzwechsel lohnt sich also nur, wenn die Evidenz über eine gewisse Zeit klar dafür spricht.

Die Kosten werden in Notebook 04 auf einem 4 × 4-Raster per Leave-one-match-out gewählt. Das Raster ist um den gewählten Punkt flach, die Wahl ist also robust.

### Schritt 5 · Wiederanpfiffe

Das Ende einer Unterbrechung ist ein klarer Moment: Der Ball wird gespielt.
- **Kick-Snap:** Das vorhergesagte D-Ende wird auf das nächstgelegene Ballereignis geschoben, bei dem der Ball nach einer ruhigen Phase auf über 6 m/s beschleunigt (Fenster −6/+4 s). Auf Metrica liegen so 89 % der Wiederanpfiffe innerhalb von 0,5 s.
- **Anstoß-Regel:** Ein Ball, der am Mittelpunkt liegt und dann schnell wegläuft, ist ein Anstoß. Davor ist D.
- **Wiederanpfiff-Team-Prior:** Ein kleines logistisches Modell schätzt anhand der Spielerpositionen, welches Team den Standard ausführt. Das fließt mit Gewicht w = 4 als Zusatzkosten in einen zweiten Decoder-Durchlauf ein.

### Schritt 6 · Abgabe

Notebook 04 schreibt `output/HSA_Connection.csv`. Die Labels der beiden bewerteten Halbzeiten werden geschrieben, alle anderen Frames erhalten `X`. Danach folgen die Prüfung mit dem offiziellen Validator und der SHA-256-Hash.

## Wie gut er ist

| spellF1 | Metrica (LOMO, Hauptkriterium) | DFL d67s (LOMO) |
|---|---:|---:|
| Offizielle Baseline smooth50 | 0,405 | 0,214 |
| **unser Ansatz (eingefroren)** | **0,646** | **0,477** |

Die DFL-Werte sind niedriger, weil DFL auch sehr kurze Berührungsphasen als Besitz zählt.

Wie es mit der Zeit besser wurde (DFL d67s): Baseline 0,214 → erste Pipeline 0,276 → D-Stufe nach Lang 0,315 → Besitzseite nach Link 0,391 → Teamform 0,462 → A1 0,477. Mit dem Training auf Metrica kam der Wert auf Metrica von 0,611 auf 0,646.

## Was er bewusst nicht tut, und warum

- **Kurze Pingpong-Phasen unter 3 s jagen:** Die Challenge zählt Berührungen ohne Kontrolle vermutlich nicht.
- **Wechsel-Snap für H↔A:** Er brachte auf Metrica +0,005 und auf DFL −0,007, beides weit unter dem Rauschband des Scorers (0,04).
- **Ereignisebene mit Beschleunigungsspitzen:** Der Gewinn war ein Artefakt des scharfen DFL-Balls.
- **Separater H/A-Decoder:** schlechter als der gemeinsame Decoder.
- **Größere Prior-Gewichte** (w ≥ 64): liegen auf DFL neben einem Leistungseinbruch.

## Bekannte Grenzen

- Wie gut die Besitzdefinitionen von DFL und Metrica zur Challenge passen, lässt sich ohne Challenge-GT nicht messen.
- Metrica umfasst nur 3 Spiele. Die Labels sind aus Events abgeleitet und nicht frame-genau.
- In Unterbrechungen bewegt sich der Ball auf der Challenge mehr als in beiden Trainingsquellen.
- Die Besitzwechsel liegen im Median etwa 0,5 s neben dem echten Zeitpunkt (gemessen auf Metrica).

## Literatur

- Lang, S., Wild, R., Isenko, A. & Link, D. (2022). Predicting the in-game status in soccer with machine learning using spatiotemporal player tracking data. *Scientific Reports*, 12, 16291.
- Link, D. & Hoernig, M. (2017). Individual ball possession in soccer. *PLoS ONE*, 12(7), e0179953.
- Bassek, M., Rein, R., Weber, H. & Memmert, D. (2025). An integrated dataset of spatiotemporal and event data in elite soccer. *Scientific Data*. https://doi.org/10.1038/s41597-025-04505-y

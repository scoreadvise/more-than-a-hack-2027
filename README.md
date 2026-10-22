# More than a Hack 2027 – Ballbesitz erkennen

In der ersten Phase von **More than a Hack 2027** entwickeln wir ein Verfahren, das für jedes Videobild eines Fußballspiels bestimmt, welche Mannschaft den Ball besitzt oder ob das Spiel unterbrochen ist. Diese README beschreibt die Aufgabe und die Anforderungen an unsere Abgabe. Code, Notebooks und Ergebnisse werden später ergänzt.

## Die Aufgabe

Wir arbeiten mit dem Spiel **FC Barcelona gegen Athletic Club**, LaLiga 2024/25, zweiter Spieltag. Für jedes der **199.319 Frames** des taktischen Videos müssen wir genau eines dieser Labels ausgeben:

| Label | Bedeutung |
| --- | --- |
| `H` | Barcelona hat Ballbesitz, der Ball ist im Spiel. |
| `A` | Athletic Club hat Ballbesitz, der Ball ist im Spiel. |
| `D` | Der Ball ist nicht im Spiel, etwa bei einer Unterbrechung. |
| `X` | Unser Verfahren gibt keine Antwort. |

Ballbesitz wechselt erst, wenn die andere Mannschaft den Ball **kontrolliert** übernimmt. Ein Abpraller oder eine bloße Berührung reicht dafür nicht aus. Bei einem freien oder umkämpften Ball bleibt der Besitz zunächst bei der zuletzt kontrollierenden Mannschaft. Bei einer Unterbrechung lautet das Label `D`, unabhängig davon, wer anschließend fortsetzt. Die [offizielle Aufgabenbeschreibung](https://github.com/metrica-sports/more-than-a-hack-2027/blob/main/CHALLENGE.md) erläutert diese Regeln.

## Welche Daten wir bekommen

Die Veranstalter stellen zwei Videoaufnahmen mit automatischem Tracking von Spielern und Ball bereit: eine taktische Aufnahme und eine TV-Aufnahme. Dazu kommen Homografien zur Zuordnung von Bild- und Spielfeldkoordinaten sowie automatisch erkannte taktische Phasen und Standardsituationen für die taktische Aufnahme.

Die **taktische Aufnahme mit 25 Bildern pro Sekunde ist die Referenz für unsere Abgabe**. Die TV-Aufnahme hat eine eigene Zeitachse mit Schnitten und Wiederholungen. Wer sie zusätzlich nutzt, muss sie selbst mit der taktischen Aufnahme abgleichen.

Das Tracking ist unkorrigiert. Es enthält Lücken und wechselnde Track-Identitäten; auf rund **41 % der bewerteten Frames** fehlt der Ball im Tracking. Auch die taktischen Tags können falsch sein. Unser Verfahren muss mit diesen Fehlern umgehen können. Details stehen in der [Datendokumentation](https://github.com/metrica-sports/more-than-a-hack-2027/blob/main/DATA.md).

## Wie bewertet wird

Für die Rangliste zählt **`spellF1`**. Diese Metrik prüft, wie gut vorhergesagte Ballbesitzphasen zeitlich mit den tatsächlichen Phasen übereinstimmen. Eine Phase ist ein durchgehender Abschnitt mit `H` oder `A`; eine Unterbrechung beendet sie. Häufige kurze Fehlwechsel können den Score deshalb stark verschlechtern.

Zusätzlich wird **`macroF1`** über die drei Klassen `H`, `A` und `D` berechnet. Dieser Wert bewertet die einzelnen Frames und dient als erstes Kriterium bei Gleichstand.

Öffentlich verfügbar sind **fünf Minuten Referenzlabels mit 17 Ballbesitzphasen**. Damit können wir die Umsetzung prüfen, aber keine verlässliche Rangfolge unserer Ansätze bestimmen. Die endgültige Bewertung erfolgt auf der privaten Referenz des gesamten Spiels. Die offizielle Baseline `baseline_smooth50` erreicht dort einen `spellF1` von **0,2433**; das ist unser Vergleichswert, kein eigenes Ergebnis.

`X` wird unterschiedlich behandelt: Bei `macroF1` zählt es auf bewerteten Frames als Fehler. Für `spellF1` werden solche Lücken innerhalb jeder Halbzeit mit dem vorherigen Label gefüllt, am Anfang mit dem nächsten verfügbaren Label. Frames außerhalb der bewerteten Bereiche werden ignoriert. Die genaue Berechnung beschreibt die [offizielle Evaluation](https://github.com/metrica-sports/more-than-a-hack-2027/blob/main/EVALUATION.md).

## Was wir machen müssen

1. **Daten und Zeitachsen prüfen.** Tracking, Video und Zusatzinformationen korrekt zuordnen und die Datenlücken sichtbar machen.
2. **Die offizielle Baseline nachvollziehen.** Ihre Ergebnisse reproduzieren und untersuchen, wo Ballbesitzwechsel und Unterbrechungen falsch erkannt werden.
3. **Unser Verfahren entwickeln.** Die Unterscheidung zwischen kontrolliertem Besitz, bloßem Kontakt und ruhendem Spiel algorithmisch umsetzen. Annahmen und Änderungen halten wir in nachvollziehbaren Jupyter-Notebooks fest.
4. **Die Ausgabe überprüfen.** Ergebnisse mit dem offiziellen Scorer prüfen und Fehler untersuchen. Die kurze öffentliche Referenz darf dabei nicht zur alleinigen Grundlage für die Auswahl und Abstimmung des Verfahrens werden.
5. **Die Abgabe reproduzierbar machen.** Aus den bereitgestellten Daten muss sich dieselbe CSV erneut erzeugen lassen. Dazu dokumentieren wir Abhängigkeiten, Ausführung und Grenzen des Ansatzes.

## Was wir abgeben müssen

Die Abgabe besteht aus drei Teilen:

- **Eine CSV-Datei** mit dem Header `frame,label` und genau **199.319 Datenzeilen**. Die Frames müssen lückenlos von `0` bis `199318` aufsteigend aufgeführt sein. Zulässige Labels sind `H`, `A`, `D` und `X`; leere Felder sind nicht erlaubt.
- **Ein öffentliches Code-Repository**, das die Abgabedatei aus den bereitgestellten Daten exakt reproduzieren kann, einschließlich festgelegter Abhängigkeiten und Ausführungsanleitung.
- **Eine kurze technische Dokumentation** als PDF oder Markdown: Vorgehen, verwendete Daten, umgesetzte Ballbesitzregeln, Einschränkungen und Reproduktion.

Vor der Einreichung müssen wir die endgültige CSV mit dem offiziellen `validate_submission.py` prüfen. CSV und technisches Dokument werden nach dem Team benannt. Es gibt eine Einreichung pro Team über das von den Veranstaltern per E-Mail bereitgestellte Formular.

**Abgabefrist laut offizieller Dokumentation: 17. November 2026.** Maßgeblich sind die [aktuellen Einreichungsvorgaben](https://github.com/metrica-sports/more-than-a-hack-2027/blob/main/SUBMISSION.md).

## Regeln für unsere Arbeit

Die eingereichten Labels müssen vollständig aus einem Algorithmus stammen. Sie dürfen nicht von Hand erstellt oder nachträglich frameweise korrigiert werden. Die private Referenz und andere Quellen korrigierter Ballbesitzdaten dieses Spiels dürfen wir nicht verwenden.

Die Spieldaten sind ausschließlich für den Wettbewerb lizenziert. Videos, Trackingdaten und daraus rekonstruierbare Exporte gehören nicht in dieses Repository. Methoden und verwendete Ressourcen müssen für die Veranstalter zugänglich und prüfbar sein. Verbindlich sind die [offiziellen Regeln](https://github.com/metrica-sports/more-than-a-hack-2027/blob/main/RULES.md) und die bei der Anmeldung akzeptierten Nutzungsbedingungen.

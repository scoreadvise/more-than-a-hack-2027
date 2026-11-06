# Metrica Sports Sample Data

- Quelle: https://github.com/metrica-sports/sample-data, Commit `e706dd506b360d69d9d123d5b8026e7294b13996`, geladen am 2026-11-06 über raw.githubusercontent.com.
- Inhalt: 3 anonymisierte Spiele mit Tracking (25 fps, Koordinaten 0–1, Feld 105 × 68 m) und synchronisierten Events. Spiel 1 und 2 liegen als CSV vor, Spiel 3 im EPTS-FIFA-Format (`.txt` + `.xml`) mit Events als JSON.
- Prüfsummen: `sha256.txt` (SHA-256 je Datei in `raw/`).
- Nutzung: Es gibt keine formale Lizenzdatei. Die README des Repositorys bittet um verantwortungsvolle Nutzung und um Quellenangabe bei öffentlicher Verwendung. Die Daten sind für Interessenten und die Analytics-Community zum Experimentieren veröffentlicht. Herausgeber ist Metrica Sports, der Ausrichter der Challenge. Eine Rückfrage beim Ausrichter zur Nutzung in der Challenge ist offen.
- Verwendung: zusätzliche externe Trainings- und Validierungsspiele. Die Labels werden automatisch per dokumentierter Regel aus den Events dieser Spiele abgeleitet. Daten des Challenge-Spiels sind nicht betroffen.
- Rohdaten und abgeleitete Frame-Daten kommen nicht ins öffentliche Repository. Dort steht nur das Skript bzw. der Link zum Laden.

# T-DEED · lokale Pilotabhängigkeiten

Modell: `arturxe2/T-DEED`, `SoccerNetBall_challenge1`, Revision `d953b4de8a2ad941c565e1683c5b07255cbe644e`.

- `weights/`: vorhandener Task-Checkpoint; Herkunft und SHA-256 in `checkpoint_manifest.json`.
- `source/<revision>/`: vorhandene Originalquellen als Text mit Komponentenlizenzen. Notebook 03 lädt die benötigten Klassen und Funktionen daraus.
- `requirements-video-events.txt`: aufgezeichneter Paketstand der separaten Video-Umgebung.

Notebook 03 verwendet CPU, FP32 und vier Threads. Der ursprüngliche Hardware-/MPS-Vergleich bleibt in den historischen Pilotunterlagen dokumentiert und wird im bereinigten Ablauf nicht wiederholt. Alle eigenen Analysefunktionen stehen im Notebook; Modellanpassungen betreffen Modulnamensraum, unterdrückten Backbone-Autodownload und geräteneutralen zweiten Kopf. Der vollständige Checkpoint wird strikt geladen.

Die verwendete Python-3.11.7-Umgebung liegt unter `/private/tmp/mtah-video-events-venv`. Da temporärer Speicher verloren gehen kann, bei Bedarf eine separate Umgebung auf dem internen Dateisystem aus dem gespeicherten Paketstand wiederherstellen:

```sh
/opt/anaconda3/bin/python -m venv --copies /private/tmp/mtah-video-events-venv
/opt/anaconda3/bin/uv pip install --python /private/tmp/mtah-video-events-venv/bin/python --link-mode copy -r artifacts/video_event_spotting/requirements-video-events.txt
```

Notebook 03 mit diesem Interpreter ausführen. Auf dem T7-ExFAT-Dateisystem störten macOS-AppleDouble-Dateien die frühere Laufzeit; die separate Umgebung liegt deshalb intern. Notebook 04 und 15 benötigen die gespeicherten Pilotvorhersagen und Diagnosen, keine erneute Modellinstallation.

Code-Lizenz, Gewichtsrechte und Trainingsdatenrechte sind getrennt zu behandeln. Eine ausdrücklich separate Gewichtslizenz ist in den vorhandenen Unterlagen nicht dokumentiert; das GitHub-Codepaket enthält daher keine Fremdquellen oder Gewichte.

Clips, Bilder und lokaler Player bleiben unter `output/video_event_spotting_pilot/`. Vor einer Veröffentlichung Notebook-Ausgaben entfernen. Die bisherigen ausführlichen Berichte dokumentieren die damalige Fassung und werden von den bereinigten Notebooks nicht überschrieben.

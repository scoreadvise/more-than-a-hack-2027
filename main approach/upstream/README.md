# Originalquellen der Vorstufen

Diese Notebooks dokumentieren die Vorstufen des aktuellen Hauptansatzes. Sie wurden aus `output/jupyter-notebook/` hierher verschoben. Bei der anschließenden Trennung von Ein- und Ausgaben wurden nur die eingefrorenen Lesepfade in Notebook 06/08 nach `artifacts/upstream/` umgestellt. Ihre neu berechneten Ergebnisse werden nach `output/` geschrieben.

| Notebook | Funktion im Hauptansatz |
|---|---|
| [04_kontaktbasierte_klassifikation.ipynb](04_kontaktbasierte_klassifikation.ipynb) | Ursprüngliches Kontaktmodell und Fallback-Teamlabels |
| [06_spielunterbrechungen_untersuchen.ipynb](06_spielunterbrechungen_untersuchen.ipynb) | Heuristik-/Unterbrechungslabels mit Vorrang bei der Besitzrekonstruktion |
| [08_spielstatus_mit_machine_learning.ipynb](08_spielstatus_mit_machine_learning.ipynb) | AdaBoost-Features, gespeicherte Modellpipeline sowie Vollspiel-/OOF-Statusvorhersagen |

Für die aktuelle Reproduktion genügt Vorbereitung 01 bei fehlender NPZ, danach Notebook 02. Die benötigten eingefrorenen Vorstufenausgaben und Modelle bleiben unter `artifacts/upstream/` erhalten. Notebook 08 enthält Training; für diese Aufräumaktion wurde es nicht ausgeführt.

Neue Vorstufenergebnisse unter `output/` werden nicht automatisch zu eingefrorenen Artefakten. Für den aktuellen Teamlauf bleiben die bereits validierten Artefakte maßgeblich.

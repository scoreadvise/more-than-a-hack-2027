# Evaluation

[02_offizielle_baseline.ipynb](02_offizielle_baseline.ipynb) enthält die ursprüngliche offizielle Baseline.

[Team-Notebook 02](../main%20approach/02_spatial_hybrid_v1/02_spatial_hybrid_v1.ipynb) berechnet den aktuellen Hybrid und exportiert die vollständigen Vorhersagen. Es zeigt die bereits dokumentierten öffentlichen Scores als historische Vergleichswerte; ein erneuter Evaluatoraufruf gehört nicht zum bereinigten Ablauf.

Die offizielle öffentliche Evaluation vom 28. Oktober liegt unter `output/team_spatial_hybrid_v1/evaluation/20261028T174210320125Z/`, einschließlich Scoreboard und Validatorlogs. Die damalige Ausführung ist im zugehörigen Release-Manifest dokumentiert. Spatial Hybrid v1 erreichte Spell-F1 0,564103 und Macro-F1 0,865360 auf dem bekannten öffentlichen Entwicklungsfenster.

Der [Fusionspilot in Notebook 05](../main%20approach/05_fusionspilot/05_fusionspilot.ipynb) vergleicht seine Entscheidungen direkt mit v1. Die Pilotclips überdecken das öffentliche Fenster nicht; die bisherigen identischen öffentlichen Scores bewerten seinen Zusatznutzen nicht.

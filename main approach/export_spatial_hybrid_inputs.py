"""Exportiert die minimalen Inputs des Spatial Hybrid v1 aus dem aktiven Notebook 09.

Im aktiven Entwicklungsnotebook (05, zuvor als 09 bezeichnet), vom Projektroot:
    %run -i "main approach/export_spatial_hybrid_inputs.py"

Team-Notebook 11 liest die NPZ danach aus artifacts/spatial_hybrid_v1/inputs/.
Der Export enthaelt die eingefrorene Physics-v3-Ausgabe, NICHT dessen Rohdaten-/Trainingspipeline.
"""
from pathlib import Path
import numpy as np

_required = (
    'PROJECT_DIR', 'N_FRAMES', 'FPS', 'HALVES',
    'hier_physics_v3', 'status_physics_v3',
    'proximity_margin_H', 'hier_spatial_hybrid_v1',
)
_missing = [name for name in _required if name not in globals()]
if _missing:
    raise RuntimeError(
        'Die folgenden Variablen fehlen im aktiven Notebook 09: '
        + ', '.join(_missing)
    )

_destination = (
    Path(PROJECT_DIR) / 'artifacts' / 'spatial_hybrid_v1'
    / 'inputs' / 'spatial_hybrid_inputs_v1.npz'
)
_destination.parent.mkdir(parents=True, exist_ok=True)

_reference = np.asarray(hier_physics_v3, dtype='<U1')
_status = np.asarray(status_physics_v3, dtype='<U1')
_margin = np.asarray(proximity_margin_H, dtype=np.float32)
_expected = np.asarray(hier_spatial_hybrid_v1, dtype='<U1')
_halves = np.asarray([(int(start), int(end)) for _, start, end in HALVES], dtype=np.int64)

if not all(len(a) == int(N_FRAMES) for a in (_reference, _status, _margin, _expected)):
    raise ValueError('Die Eingabearrays haben nicht N_FRAMES Elemente.')
if not np.isin(_reference, ['H', 'A', 'D', 'X']).all():
    raise ValueError('Unbekannte Referenzlabels in hier_physics_v3.')
if not np.isin(_status, ['L', 'D']).all():
    raise ValueError('Unbekannte Statuslabels; erwartet: L/D.')

np.savez_compressed(
    _destination,
    reference=_reference,
    status=_status,
    proximity_margin_H=_margin,
    expected_hybrid=_expected,
    halves=_halves,
    n_frames=np.array(int(N_FRAMES), dtype=np.int64),
    fps=np.array(int(FPS), dtype=np.int64),
)
print('Export erstellt:', _destination)
print('Frames:', int(N_FRAMES))
print('Hinweis: Dieser Export friert Physics v3 ein und dient zur isolierten Reproduktion von Spatial Hybrid v1.')

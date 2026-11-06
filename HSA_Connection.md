# HSA Connection – Technical document

More Than A Hack 2027, Initial Challenge. Submission file `HSA_Connection.csv`, SHA-256 `92a943257cf73aaa057aa81cf29902732b72f2b545b95410ae5b2608b1a0f8fb`.

## Approach

We predict possession from the tactical tracking data (ATD) alone. Because the challenge ground truth and video may not be used for training or tuning, all models were trained on other matches: seven Bundesliga matches from the open DFL/IDSSE dataset and the three public Metrica Sports sample matches. The DFL tracking is much cleaner than the challenge data, so we degraded it (ball dropouts, especially during stoppages, missing players, ball noise) until its summary statistics resembled the challenge input. The Metrica matches already come with realistic dropouts.

The pipeline has three parts. A first gradient-boosting model estimates per frame whether the ball is dead. Its features follow Lang et al. (2022): ball visibility, position of the ball relative to the lines, player speeds and team formations over the surrounding ±40 s. A second model estimates which team has the ball. Its features follow Link & Hoernig (2017): which team is closer to the ball, how long it has stayed close, pressure, plus robust team shape, which still helps when the ball is not tracked. A Viterbi decoder then turns both probabilities into coherent H/A/D spells. Switching costs prevent flickering. Finally, stoppage ends are aligned to the restart kick, and kick-offs are detected explicitly.

All design choices were made by leave-one-match-out validation on the ten external matches. On these, our spellF1 is 0.65 on Metrica and 0.48 on degraded DFL, against 0.41 and 0.21 for the official baseline logic.

## Assets

Used for the challenge match: the ATD tracking file and its XML metadata, nothing else. Video, homography and broadcast data were not used. Smart Tagging was used once only as an automatic plausibility check (do tagged set pieces fall on predicted restarts?), not as model input. We looked at the public 5-minute ground truth only after freezing a version, to check frame alignment and the file format.

Training data, all from other matches:
- DFL/IDSSE open data (Bassek et al., 2025, CC BY 4.0): 7 Bundesliga matches, about 1.0 million labelled frames. The per-frame ball status and team possession come with the official DFL position data (TRACAB tracking); we did not label anything ourselves.
- Metrica Sports sample data (GitHub, commit `e706dd5`): 3 matches, about 0.42 million labelled frames. The events were annotated by Metrica Sports; we turned them into frame labels automatically with a fixed rule (notebook 03).

Tried and dropped: a separate decoder for team possession after stoppage detection, a touch/event layer from ball acceleration (its gain turned out to be an artefact of the perfect DFL ball), gap-bridging features, and snapping possession changes to the receiving player. None improved the external validation reliably.

## Possession rules

A team gets possession once it shows sustained control. Short touches, deflections and duels do not change possession; during a contested or flying ball, possession stays with the last controlling team. The ball is dead (`D`) from the stoppage (ball out, foul, goal, offside) until the restart kick, and the restarting team owns the following spell. `X` is only used outside the two graded halves.

## Limitations

We cannot measure how closely the external possession definitions match the challenge definition. Our possession changes are often about half a second off, which costs points at strict overlap thresholds. Very short spells (under 3 s) are mostly merged into neighbouring spells, by design. Ball behaviour during stoppages in the challenge still differs from both training sources, and three Metrica matches are a small sample.

## Reproduction

The repository contains four notebooks (`notebooks/`), download lists and checksums for the external data, the official scorer and the frozen submission, but no match data. Set up Python 3.11 with `requirements.txt`, download the external data as described in `README.md`, put the two ATD files in `tactical/`, and run the notebooks 01 to 04 in order. Notebook 04 writes `output/HSA_Connection.csv` and prints its SHA-256; it is bit-identical to the submitted file.

## References

Lang, S., Wild, R., Isenko, A. & Link, D. (2022). Predicting the in-game status in soccer with machine learning using spatiotemporal player tracking data. *Scientific Reports* 12, 16291.

Link, D. & Hoernig, M. (2017). Individual ball possession in soccer. *PLoS ONE* 12(7), e0179953.

Bassek, M., Rein, R., Weber, H. & Memmert, D. (2025). An integrated dataset of spatiotemporal and event data in elite soccer. *Scientific Data*.

Metrica Sports sample data, github.com/metrica-sports/sample-data.

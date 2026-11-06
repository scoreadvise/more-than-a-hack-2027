# What the approach takes into account and how it works

## The task in one sentence

For each of the 199,319 frames of Barcelona–Athletic we decide whether Barcelona controls the ball (`H`), Athletic does (`A`), the ball is dead (`D`, stoppage) or the frame is not graded (`X`, outside the halves). The main metric is **spellF1**. Each possession spell counts as one object that has to overlap well in time (IoU 0.3–0.7). What counts is whole spells with clean boundaries, not single frames.

## What the approach takes into account

### 1. The rules (rules email of 2026-11-04)

| Rule | How we comply |
|---|---|
| No training, fitting or calibration on the challenge ground truth or the video | All models and all parameters come from **external matches** only. |
| No hand labels and no human-made data about the challenge match | From the challenge match only the tracking (`atd.txt`) and metadata (`atd.xml`) are used. Smart Tagging and video are not used. |
| Do not check the output against the video | Nothing is checked against the video. |
| Do not upload challenge data to AI services | All processing is local. Only aggregates such as medians and shares were shared with an AI assistant. |
| External data only with usage rights | DFL/IDSSE: CC BY 4.0. Metrica sample data: published for experimentation, without a formal licence; a question to the organisers is pending. |

The public 5-minute ground truth was read only **after freezing**, as a technical check of frame alignment and label meaning. It did not influence any decision.

### 2. The domain gap

We train on other matches whose tracking looks different from the challenge:
- **DFL data** is almost perfect: the ball is always visible, but frozen during stoppages.
- **Challenge tracking** is video-based: the ball is often missing, especially during stoppages, and there are outlier tracks with more than 11 players per team.

We therefore **degraded** the DFL data artificially so that it resembles the challenge (scenario d67s, notebook 02):
- state-dependent ball dropout as a Markov chain, more frequent during stoppages,
- block-wise player dropout,
- smoothing and offset of the ball position.

Only **aggregates** of the challenge inputs were matched, without ground truth.

In addition we use the **Metrica sample matches** (notebook 03). They come from the same tracking pipeline as the challenge and have real dropouts. During stoppages they are much closer to the challenge than DFL; the separability of the base features from the challenge is 0.09 instead of 0.22.

### 3. The possession definition

The challenge asks for **controlled** possession. Mere touches do not count as a change. The approach therefore deliberately does not chase very short ping-pong spells under 3 s. Many errors are counted there, but recovering them would optimise for a label convention that is not confirmed for the challenge.

### 4. Methodological care

- **Leave-one-match-out validation:** each match is predicted by models that never saw it.
- **Metrica is the main criterion**, because it is closest to the challenge. DFL serves as a control.
- **One change per step**, with domain checks on the challenge inputs before adopting anything, using aggregates only. The development notebooks, including negative results, are kept in the team's working project and are not part of this repository.
- **Reproducibility:** fixed seed, pinned packages, checksums for all raw data. A full run reproduces the submission file bit for bit.

## How the approach works

```
Tracking (ball + players, 25 fps)
   │
   ├─ 1. Plausibility rule ─────────── jumps > 40 m/s (ball) or > 12 m/s (players) → missing
   │
   ├─ 2. Features per frame
   │     ├─ dead-ball features (ball visibility, touchline, movement, team aggregates ±40 s)
   │     └─ possession features (reach, pressure, team shape ±4 s)
   │
   ├─ 3. Two probabilities per frame
   │     ├─ P(D)        ← D model (boosting, 159 features)
   │     └─ P(H | live) ← H model (boosting, 59 features)
   │
   ├─ 4. Joint Viterbi decoder over H / A / D
   │     switching costs c_HA = 10, c_D = 40  →  smooth, coherent spells
   │
   ├─ 5. Refine restarts
   │     ├─ kick snap: end of D moves to the restart kick or pass (−6/+4 s)
   │     ├─ kick-off rule: ball on the centre spot that leaves fast → D before it
   │     └─ restart-team model as a prior (w = 4): who takes it?
   │
   └─ 6. Labels for the graded halves, X elsewhere  →  CSV, validation, SHA-256
```

### Step 1 · Plausibility rule

Impossible jumps in the tracking are treated as missing: ball above 40 m/s, players above 12 m/s. This mainly affects wrong assignments in the video-based tracking.

### Step 2 · Features

**For stoppages (D)**, after Lang et al. (2022):
- **Ball visibility:** is the ball visible right now? Since when not? When again? Share over 1, 5 and 15 s.
- **Touchline:** how far was the ball from the line when last and next seen? A ball that disappears at the line suggests it went out.
- **Player movement:** median speed and share of running players. During stoppages players walk.
- **Team aggregates** at 11 offsets from −40 to +40 s: distance between the teams, spread, position of the centroid. A free kick or a corner has a typical picture that builds up over several seconds.

**For the possession side (H/A)**, after Link & Hoernig (2017):
- **margin:** how much closer is the nearest H player to the ball than the nearest A player? Also a version with positions predicted 1 s ahead.
- **reach:** how long has a team been within 2 m of the ball? Control means staying on the ball for longer.
- **Pressure:** players per team within 3 m, context ±2 s.
- **Robust team shape**, median and interquartile range with ±4 s: which team pushes forward, makes the pitch wide, sits deep? The playing direction comes from the deepest player, the goalkeeper. These features work even when the ball is missing. During development this was the biggest gain: recall of possessions in ball gaps rose from 9 % to 29 %.

### Step 3 · Two boosting models

- **D model:** HistGradientBoosting on the dead-ball features *and* the possession features. Output: P(ball dead) per frame.
- **H model:** HistGradientBoosting on live frames only. Output: P(H | ball alive).

Both are trained on 10 external matches: 7 DFL matches in the degraded version d67s and 3 Metrica matches. The Metrica labels are derived automatically from their events (notebook 03):
- **D:** from the ball going out, a foul or a goal to the next set piece,
- **H/A:** the team of the last possession event.

### Step 4 · Joint decoder

Deciding frame by frame would flicker and create hundreds of micro-spells. The decoder is therefore a **Viterbi algorithm** over the three states H, A and D:
- It uses the model probabilities as evidence.
- Every switch costs a penalty: c_HA = 10 for H↔A and c_D = 40 for play↔stoppage.
- It picks the label sequence with the best overall balance. A change of possession only pays off if the evidence clearly supports it for some time.

Notebook 04 chooses the costs on a 4 × 4 grid by leave-one-match-out. The grid is flat around the chosen point, so the choice is robust.

### Step 5 · Restarts

The end of a stoppage is a clear moment: the ball is played.
- **Kick snap:** the predicted end of D moves to the nearest ball event where the ball accelerates above 6 m/s after a quiet phase (window −6/+4 s). On Metrica, 89 % of restarts land within 0.5 s.
- **Kick-off rule:** a ball that lies on the centre spot and then leaves fast is a kick-off. Before it is D.
- **Restart-team prior:** a small logistic model estimates from the player positions which team takes the restart. It enters a second decoder pass as extra cost with weight w = 4.

### Step 6 · Submission

Notebook 04 writes `output/HSA_Connection.csv`. The labels of the two graded halves are written, all other frames get `X`. The file is then checked with the official validator and hashed with SHA-256.

## How good it is

| spellF1 | Metrica (LOMO, main criterion) | DFL d67s (LOMO) |
|---|---:|---:|
| Official baseline smooth50 | 0.405 | 0.214 |
| **Our approach (frozen)** | **0.646** | **0.477** |

DFL scores are lower because DFL also counts very short touch spells as possession.

How it improved over time (DFL d67s): baseline 0.214 → first pipeline 0.276 → dead-ball model after Lang 0.315 → possession side after Link 0.391 → team shape 0.462 → possession features in the D model 0.477. Training on Metrica raised the Metrica score from 0.611 to 0.646.

## What it deliberately does not do, and why

- **Chase short ping-pong spells under 3 s:** the challenge most likely does not count touches without control.
- **Snap H↔A changes to the ball transfer:** +0.005 on Metrica and −0.007 on DFL, both far below the scorer's noise band (0.04).
- **Event layer from ball acceleration peaks:** the gain was an artefact of the sharp DFL ball.
- **Separate H/A decoder:** worse than the joint decoder.
- **Larger prior weights** (w ≥ 64): next to a performance drop on DFL.

## Known limitations

- How well the possession definitions of DFL and Metrica match the challenge cannot be measured without challenge ground truth.
- Metrica has only 3 matches. Its labels are derived from events and are not frame-exact.
- During stoppages the ball moves more in the challenge than in either training source.
- Possession changes are off by about 0.5 s in the median (measured on Metrica).

## References

- Lang, S., Wild, R., Isenko, A. & Link, D. (2022). Predicting the in-game status in soccer with machine learning using spatiotemporal player tracking data. *Scientific Reports*, 12, 16291.
- Link, D. & Hoernig, M. (2017). Individual ball possession in soccer. *PLoS ONE*, 12(7), e0179953.
- Bassek, M., Rein, R., Weber, H. & Memmert, D. (2025). An integrated dataset of spatiotemporal and event data in elite soccer. *Scientific Data*. https://doi.org/10.1038/s41597-025-04505-y

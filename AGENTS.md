# AGENTS.md

## Projektklarstellung vom 29. Oktober 2026: Bestand und künftige Regelkonformität

Nach ausdrücklicher Mitteilung des Nutzers darf der bisherige Entwicklungsstand
von **Spatial Hybrid v1** unverändert bestehen bleiben. Für die weitere
Projektarbeit gilt er als akzeptierter Bestandsstand und feste Vergleichsbasis.

- Den Bestand und seine wissenschaftliche Herkunft erhalten. Der abgeschlossene
  Compliance-Audit bleibt als historische Dokumentation bestehen. Aus seinen
  bereits bekannten Befunden allein folgen keine erneute Freigabeanforderung,
  Sanierung, Modelländerung oder Trainingswiederholung.
- Bei **neuen Arbeiten** die aktuellen offiziellen Regeln beachten und die
  Herkunft neuer Daten, Labels, Modelle und Parameter nachvollziehbar festhalten.
  Öffentliche Challenge-GT nur für technische Pipelineprüfungen verwenden, nicht
  für neue Fits, Schwellen-/Hyperparameteroptimierung oder Modellauswahl nach
  öffentlichem Score. Feste historische Ergebnisse dürfen zur unveränderten
  Regressionsprüfung und als gekennzeichnete Vergleichsbasis dienen.
- Keine neuen manuellen Labels, framespezifischen Korrekturen oder menschlich
  erzeugten externen Ereignisdaten dieses Challenge-Spiels für Training,
  Validierung oder Vorhersage verwenden. Neue überwachte Entwicklung und
  quantitative Validierung auf zulässigen anderen Spielen durchführen.
- Automatische Pseudolabels und externe vortrainierte Modelle gemäß den Regeln
  auf Herkunft, Zugänglichkeit, Reproduzierbarkeit und Nutzungsrechte prüfen.
  Videovorhersagen bis zu einer unabhängigen Prüfung als unsichere Evidenz
  behandeln; daraus keine unbelegten Team-, Spieler- oder Kontrolllabels machen.
- Challenge-Videos, Trackingdaten und restringierte Auszüge einschließlich
  Videoframes nicht an Drittanbieter-gehostete oder Cloud-LLMs übergeben. Lokale
  Videoverarbeitung und Wiedergabe verwenden; auch Bild-Tools und eingebettete
  Notebookmedien vor einer Weitergabe an einen Assistenten darauf prüfen.
- Neue konkrete Regelkonflikte oder wesentliche Regeländerungen gezielt melden.
  Weitere Forschungsschritte weiterhin gemäß Abschnitt 41 abstimmen.

---

## 1. Purpose

This repository is developed primarily for **Data Science, Machine Learning, analytics, experimentation, and research workflows**.

The default working environment is **Jupyter Notebook**.

The main priorities are:

1. transparency,
2. reproducibility,
3. human readability,
4. methodological correctness,
5. compact and maintainable code,
6. visual inspection of intermediate results,
7. explicit user approval before introducing new ideas or changing the intended approach.

The goal is not to build the most elaborate software architecture possible. The goal is to create a **clear, sequential, inspectable analytical workflow that a human can follow from top to bottom**.

---

# 2. Core Rule: Notebook First

## 2.1 Default implementation

Implement the project directly inside one or more Jupyter Notebooks (`.ipynb`).

Unless explicitly approved otherwise:

- keep data loading in the notebook,
- keep preprocessing in the notebook,
- keep feature engineering in the notebook,
- keep helper functions in the notebook,
- keep model definitions in the notebook,
- keep evaluation logic in the notebook,
- keep plotting functions in the notebook,
- keep experiments in the notebook,
- keep interpretation and diagnostics in the notebook.

The notebook should be executable sequentially from top to bottom.

## 2.2 External Python files

Do **not** create or move logic into:

- `.py` modules,
- utility files,
- helper packages,
- custom libraries,
- classes stored in separate files,
- hidden abstraction layers,

unless this is genuinely necessary.

If external Python files appear technically justified, first explain:

1. why the notebook-only approach is becoming problematic,
2. what exactly should be moved,
3. what advantage this provides,
4. what additional complexity it introduces.

Then **wait for explicit user approval before creating the external file**.

Do not move code out of the notebook merely because conventional software-engineering architecture would normally do so.

---

# Central Import Block

Every notebook must contain **one single central import cell at the beginning of the notebook**.

Place it directly after an optional title/objective Markdown cell and before any data loading, configuration, analysis, functions, or other executable code. All imports used anywhere in the notebook must be collected in this one cell.

```python
# Standard library
from pathlib import Path

# Data
import numpy as np
import pandas as pd

# Visualization
import matplotlib.pyplot as plt

# Machine Learning
from sklearn.metrics import roc_auc_score
from sklearn.model_selection import train_test_split
```

Rules:

- use exactly one central import cell,
- do not scatter imports across later cells,
- do not import the same package, module, class, or function more than once,
- remove duplicate and unused imports,
- keep imports grouped logically and compactly,
- do not use wildcard imports such as `from package import *`,
- if a new import becomes necessary later, add it to the central import cell at the top,
- imports inside functions or later cells are exceptional and only allowed when technically necessary.

A human should be able to inspect the first executable cell and immediately see the notebook's complete external dependencies.

---

# 3. Notebook Structure

Build notebooks in a clear chronological order.

A typical Data Science / ML notebook should approximately follow:

```text
0. Objective / current question
1. Central imports (single import cell) and configuration
2. Data loading
3. Initial data inspection
4. Data quality checks
5. Cleaning / preprocessing
6. Exploratory analysis
7. Feature engineering
8. Train / validation / test definition
9. Baseline
10. Modeling
11. Evaluation
12. Diagnostics
13. Interpretation
14. Visual comparison
15. Current conclusion
16. Possible next steps
```

Adapt this structure when appropriate, but preserve the principle of a **linear analytical story**.

Do not create an unnecessarily complicated notebook structure.

---

# 4. Sequential Execution

The notebook must be designed so that a human can understand what happens by reading and executing it from top to bottom.

Therefore:

- avoid hidden state,
- avoid relying on cells being executed in a strange order,
- avoid variables that only exist because an old cell was executed earlier,
- avoid duplicated experimental state,
- avoid overwriting important intermediate objects without a clear reason.

Whenever practical, the notebook should pass:

```text
Restart Kernel -> Run All
```

without manual intervention.

If that is currently not possible, state clearly why.

---

# 5. Explain Before Complex Code

Before a non-trivial analytical step, add a short Markdown explanation.

Explain:

- what is being done,
- why it is being done,
- what the expected output is,
- what assumption is being made.

Keep explanations concise.

Example:

```markdown
### Temporal validation

Because the task predicts future player performance, random cross-validation
would mix observations from different points in time. We therefore train on
earlier seasons and evaluate on later seasons.
```

Do not produce long textbook-style explanations unless requested.

---

# 6. Code Style: Minimal Lines, Full Functionality, Clear Blocks

Optimize aggressively for **minimal lines of code while preserving all required functionality, methodological correctness, readability, reproducibility, and interpretability**.

The default is the shortest clear implementation that fully solves the task. Before adding code, check whether the same result can be achieved with fewer lines using existing variables, vectorized operations, established APIs, or a simpler expression.

Prefer:

- vectorized pandas / NumPy operations,
- concise method chaining when readable,
- combining closely related operations where this remains clear,
- local functions only when they genuinely reduce repetition or improve clarity,
- comprehensions where appropriate,
- built-in and established Data Science APIs,
- direct expressions instead of unnecessary temporary variables,
- simple control flow,
- reusing existing objects instead of creating redundant variants.

Avoid:

- unnecessary boilerplate,
- defensive code without realistic analytical benefit,
- wrapper functions for trivial one-off operations,
- deeply nested loops,
- copy-pasted blocks,
- redundant temporary variables,
- repeated conversions or selections,
- verbose intermediate steps that add no analytical insight,
- unnecessarily large classes,
- enterprise-style abstractions,
- premature modularization.

Every additional line should have a purpose. If two implementations are equally correct and readable, prefer the one with fewer lines.

> Minimal code means removing unnecessary code, not removing functionality, useful diagnostics, visualizations, reproducibility, interpretability, or methodological safeguards.

Do not compress code into cryptic one-liners merely to reduce line count.

## 6.1 Logical spacing inside code cells

Compact code must still be visually easy to scan. Within a code cell, separate **logically distinct code blocks with a single blank line**. Keep related statements together and do not squeeze unrelated operations into one continuous block.

For example:

```python
X = df[features]
y = df[target]

X_train = X[df["Season"].isin(train_seasons)]
y_train = y.loc[X_train.index]

model.fit(X_train, y_train)
pred = model.predict_proba(X_test)[:, 1]
```

Use blank lines to separate conceptual steps such as data selection, transformations, model definition, fitting, prediction, evaluation, and plotting. Do not add blank lines after every statement. The goal is **minimal code with visible logical structure**.

---

# 7. Functions

Functions are encouraged when they make the notebook clearer.

Create a function when:

- logic is repeated,
- an experiment must be run consistently across several variants,
- a calculation has a meaningful conceptual unit,
- parameterization improves experimentation,
- the function reduces duplicated code.

Keep these functions **inside the notebook by default**.

Prefer small, focused functions.

Example:

```python
def evaluate_model(model, X_train, y_train, X_test, y_test):
    model.fit(X_train, y_train)
    pred = model.predict(X_test)
    return {
        "mae": mean_absolute_error(y_test, pred),
        "rmse": root_mean_squared_error(y_test, pred),
    }
```

Do not create functions purely for abstraction if the code is used once and is already obvious.

---

# 8. Visualization Is Part of the Workflow

Visualizations are not optional decoration. They are part of the analytical process.

At meaningful stages, create plots that show what is happening.

Examples include:

- target distributions,
- missing-value patterns,
- feature distributions,
- correlations,
- class balance,
- temporal coverage,
- sample sizes,
- feature transformations,
- PCA projections,
- clustering structure,
- model performance,
- residuals,
- calibration,
- ROC / Precision-Recall curves,
- confusion matrices,
- feature importance,
- SHAP values,
- learning curves,
- validation results,
- prediction distributions,
- ranking comparisons,
- experiment comparisons.

Do not create plots simply to increase the number of figures.

Each plot should answer a question.

After an important visualization, briefly state what can be observed.

---

# 9. Show Intermediate Results

Do not build a long pipeline and only show the final result.

At important stages, inspect the current state.

Examples:

```python
df.shape
df.head()
df.describe()
df.isna().mean().sort_values(ascending=False).head(20)
```

Also show meaningful domain-specific summaries.

When transforming a dataset, verify the result.

For example:

```python
print(f"Before: {df_before.shape}")
print(f"After:  {df_after.shape}")
```

The user should be able to see how the dataset evolves.

---

# 10. Data Quality Checks

Before modeling, explicitly inspect relevant data-quality issues.

Depending on the project, check:

- missing values,
- duplicate rows,
- duplicate entities,
- invalid values,
- impossible ranges,
- inconsistent categories,
- unexpected data types,
- target distribution,
- sample size,
- temporal coverage,
- entity overlap,
- data leakage risk,
- outliers,
- class imbalance.

Do not silently repair suspicious data.

If an ambiguous data problem is discovered, report it before applying a subjective correction.

---

# 11. No Hallucinated Data or Assumptions

Never invent:

- columns,
- files,
- schemas,
- data values,
- model results,
- metrics,
- package behavior,
- domain definitions,
- API responses,
- paths,
- identifiers,
- experiment outcomes.

Before using a column, confirm that it exists.

Prefer checks such as:

```python
required_cols = {"playerId", "Season", "Rating"}
missing = required_cols - set(df.columns)
assert not missing, f"Missing columns: {missing}"
```

If something is unknown, say that it is unknown.

If a decision depends on missing information, ask the user rather than fabricating an answer.

---

# 12. Do Not Silently Implement New Ideas

Do not independently expand the project scope.

Examples requiring user approval:

- adding a new model,
- changing the target,
- introducing a new feature,
- changing the validation strategy,
- removing observations,
- changing thresholds,
- adding external datasets,
- changing the rating methodology,
- introducing dimensionality reduction,
- adding feature selection,
- adding synthetic data,
- applying SMOTE or other resampling,
- changing evaluation metrics,
- adding an ensemble,
- tuning hyperparameters,
- changing an existing statistical method,
- refactoring into external modules,
- replacing a requested method with another method.

Instead:

1. identify the possible improvement,
2. explain it briefly,
3. explain why it might help,
4. state possible disadvantages,
5. ask whether it should be implemented.

Example:

> A temporal split may be more appropriate than a random split because the model predicts future seasons. This would reduce temporal leakage but may also make the evaluation harder. Should I change the validation strategy?

Do not implement the suggestion until the user approves it.

---

# 13. Distinguish Fixes from New Ideas

A clear bug fix does not require treating the bug itself as a new research idea.

Examples of routine fixes:

- syntax errors,
- wrong variable names,
- broken imports,
- incorrect indexing,
- obvious plotting errors,
- accidental duplicated code.

Fix these directly when the intended behavior is unambiguous.

However, if fixing the problem requires changing methodology, assumptions, data selection, or project scope, ask first.

---

# 14. Data Leakage Prevention

Treat data leakage as a critical error.

As a default:

- define the evaluation split before learning preprocessing parameters,
- fit scalers only on training data,
- fit imputers only on training data,
- fit feature selectors only on training data,
- fit PCA or other learned transformations only on training data,
- avoid using future information for historical predictions,
- ensure target-derived features are unavailable at prediction time.

Where appropriate, use `Pipeline` or equivalent mechanisms so preprocessing is fitted within the training process.

For temporal problems, prefer time-aware validation when it matches the real prediction task.

Never optimize decisions using the final test set.

---

# 15. Train / Validation / Test Discipline

Clearly define the role of each dataset.

Recommended interpretation:

```text
Train:
used to fit model parameters

Validation:
used for model selection, feature decisions, thresholds and tuning

Test:
used for the final unbiased evaluation
```

Do not repeatedly inspect the test set while designing the model.

If cross-validation is used, explain:

- what is being split,
- how it is being split,
- why that split matches the research question.

For grouped, repeated, longitudinal, player-based, team-based, match-based, or temporal data, explicitly consider whether ordinary random CV is appropriate.

---

# 16. Reproducibility

Use deterministic random seeds whenever practical.

Define a central seed near the beginning of the notebook:

```python
RANDOM_STATE = 42
```

Reuse it consistently.

Where relevant, record:

- Python version,
- major package versions,
- random seed,
- dataset version / season,
- experiment configuration.

Do not scatter unexplained random seeds throughout the notebook.

---

# 17. Baselines First

Before complex ML models, establish a meaningful baseline.

Depending on the task this may be:

- mean prediction,
- median prediction,
- majority class,
- logistic regression,
- linear regression,
- simple heuristic,
- previous-season value,
- existing rating,
- domain baseline.

A complex method should be evaluated relative to a simpler reference point.

---

# 18. Evaluation Must Match the Task

Do not select metrics because they are common.

Use metrics appropriate to the problem.

Examples:

### Classification

Possible metrics:

- balanced accuracy,
- ROC-AUC,
- PR-AUC,
- precision,
- recall,
- F1,
- precision@k,
- recall@k,
- Brier score,
- calibration.

### Regression

Possible metrics:

- MAE,
- RMSE,
- R²,
- MAPE only when mathematically meaningful,
- rank correlation where ranking matters.

### Ranking

Possible metrics:

- Spearman correlation,
- Kendall correlation,
- Precision@k,
- Recall@k,
- NDCG.

Use multiple complementary metrics when necessary.

Do not change or add metrics without explaining the reason.

---

# 19. Imbalanced Classification

Do not rely on accuracy alone when classes are imbalanced.

Inspect class frequencies first.

Possible approaches may include:

- class weights,
- threshold adjustment,
- suitable ranking metrics,
- PR curves,
- balanced accuracy,
- Precision@k.

Do not automatically apply oversampling, undersampling, SMOTE, or synthetic techniques.

Propose them first and wait for approval.

---

# 20. Feature Engineering

Every important engineered feature should have a clear reason.

For each non-trivial feature, the notebook should make clear:

- what it represents,
- how it is calculated,
- whether it could cause leakage,
- whether it is available at prediction time.

Avoid large numbers of speculative features without justification.

Do not create features merely because they may improve model performance.

---

# 21. Scaling and Transformations

Only scale or transform variables when justified by the method.

Examples include:

- standardization,
- normalization,
- log transformation,
- power transformation,
- encoding.

Always distinguish between:

```text
fit transformation -> training data only
apply transformation -> validation/test data
```

Whenever a transformation materially changes the feature distribution, visualize or summarize the before/after state.

---

# 22. Model Complexity

Start simple.

A preferred progression is often:

```text
baseline
-> interpretable simple model
-> stronger nonlinear model
-> tuned model
-> ensemble only if justified
```

Do not jump directly to a complex ensemble or neural network without a reason.

Increasing complexity must have a measurable purpose.

---

# 23. Hyperparameter Tuning

Do not perform extensive tuning automatically.

First establish:

- a baseline,
- a valid evaluation setup,
- a sensible model,
- stable preprocessing.

If tuning appears worthwhile, propose:

- which parameters,
- search method,
- evaluation metric,
- computational cost,
- expected benefit.

Wait for user approval before launching substantial tuning.

The final test set must not be used for tuning.

---

# 24. Statistical and ML Comparisons

When comparing methods:

- use identical evaluation data where possible,
- use identical metrics,
- show uncertainty where relevant,
- avoid conclusions from a single favorable split,
- distinguish meaningful improvements from tiny numerical differences.

Prefer compact comparison tables.

Example:

```python
results.sort_values("balanced_accuracy", ascending=False)
```

Add a plot when it helps interpretation.

---

# 25. Explainability

For research-oriented ML projects, interpretability should be considered part of the analysis.

Depending on the method, suitable tools may include:

- model coefficients,
- permutation importance,
- SHAP,
- partial dependence,
- accumulated local effects,
- calibration analysis,
- residual inspection,
- subgroup analysis.

Do not automatically add every explainability technique.

Suggest the technique that matches the model and wait for approval if it expands the intended scope.

---

# 26. Research Context

When the project is scientific or publication-oriented:

- preserve methodological traceability,
- make assumptions explicit,
- separate exploratory analysis from confirmatory evaluation,
- avoid cherry-picking results,
- preserve negative or non-significant results when relevant,
- document exclusion criteria,
- document filtering decisions,
- clearly distinguish hypothesis, method, result, and interpretation.

Do not modify the analytical strategy solely to obtain a better result.

---

# 27. Current Best Practices

For Data Science and Machine Learning methodology, prefer current stable best practices and actively avoid outdated patterns.

When a methodological choice may have changed with newer library versions, recent research, or current recommendations:

1. verify the current state from reliable primary documentation or recent scientific literature,
2. summarize the relevant finding,
3. propose the change,
4. obtain user approval before altering the existing workflow.

Prefer primary sources such as:

- official library documentation,
- original scientific papers,
- official API documentation,
- recognized methodological references.

Do not adopt a blog post or social-media recommendation as methodological truth without verification.

---

# 28. Package Usage

Prefer established, widely used libraries where appropriate:

```text
numpy
pandas
scipy
scikit-learn
statsmodels
matplotlib
plotly
shap
lightgbm
xgboost
```

Use only packages relevant to the project.

Before adding a new dependency, consider whether the task can be solved cleanly with packages already in use.

Do not install or introduce a new package merely for convenience without mentioning it.

---

# 29. Plotting

Prefer clean, publication-friendly visualizations.

Each figure should have:

- a meaningful title,
- readable axis labels,
- sensible units,
- a legend when necessary,
- appropriate scale,
- enough context to interpret the figure.

Avoid:

- unnecessary 3D charts,
- decorative effects,
- excessive annotations,
- misleading axes,
- unreadable color schemes,
- charts with no analytical purpose.

When comparing several methods, use consistent axes and definitions.

---

# 30. Tables

Keep tables compact and informative.

Prefer displaying only columns needed for the current question.

For example:

```python
display(
    results[
        ["model", "balanced_accuracy", "roc_auc", "precision_at_5"]
    ].sort_values("balanced_accuracy", ascending=False)
)
```

Avoid dumping huge DataFrames into notebook output.

---

# 31. Memory and Performance

Optimize performance when it materially matters, but do not make the notebook opaque.

Prefer:

- vectorized calculations,
- categorical dtypes where appropriate,
- selecting needed columns,
- avoiding unnecessary DataFrame copies,
- efficient joins,
- reusing expensive intermediate calculations.

Do not introduce complex caching systems or distributed frameworks unless the dataset actually requires them.

If a performance optimization significantly reduces readability, explain the trade-off first.

---

# 32. Error Handling

Do not hide errors with broad exception handling.

Avoid:

```python
try:
    ...
except:
    pass
```

Prefer:

- validating inputs,
- concise sanity checks where they protect analytical correctness,
- informative exceptions,
- narrow exception handling.

A failed analytical assumption should be visible.

---

# 33. Assertions and Sanity Checks

Use assertions **sparingly**. The default is **no assertion unless it protects against a realistic silent analytical error**.

Assertions are appropriate when a violated assumption could let the notebook continue while producing methodologically invalid results, for example:

```python
assert train["Season"].max() < test["Season"].min()
```

Useful cases include preventing leakage, verifying critical train/test separation, detecting silent prediction/target misalignment, or protecting an assumption essential to a calculation.

Do not routinely assert obvious column existence, non-empty DataFrames, basic shapes already evident from the workflow, conditions guaranteed by the preceding code, or every intermediate transformation. If Python would already fail immediately and clearly, an additional assertion is usually unnecessary.

For exploratory Jupyter workflows, prefer concise inspection and meaningful sanity checks over defensive-programming boilerplate.

---

# 34. Preserve Existing Work

When modifying an existing notebook:

- understand the current workflow first,
- preserve functioning cells where possible,
- avoid broad rewrites without need,
- do not rename large numbers of variables merely for style,
- do not replace a working method unless requested.

Prefer focused modifications.

---

# 35. Refactoring

Refactor only when there is a concrete benefit.

Possible reasons:

- duplicated logic,
- inconsistent evaluation,
- difficult-to-follow execution order,
- repeated bugs,
- excessive runtime,
- clearly unreadable code.

Before a substantial refactor, explain what would change.

Do not refactor simply because another structure looks more elegant.

---

# 36. Existing Variable Names

When working in an existing notebook, use established variable names when reasonable.

Do not rename:

```text
final_df -> final_player_dataframe_clean_final_v2
```

without a clear reason.

Consistency with the existing analysis is often more valuable than stylistic purity.

---

# 37. Comments

Use comments to explain **why**, not every obvious operation.

Good:

```python
# Only use seasons available before the prediction season to avoid temporal leakage.
train = df[df["Season"] < test_season]
```

Unnecessary:

```python
# Select column
x = df["x"]
```

Prefer concise Markdown sections for conceptual explanations.

---

# 38. Experiment Tracking Inside the Notebook

For multiple experiments, collect results in a structured table rather than leaving disconnected outputs.

Example:

```python
experiments = pd.DataFrame([
    {"model": "Logistic Regression", "roc_auc": 0.81},
    {"model": "Random Forest", "roc_auc": 0.85},
])
```

Include important configuration fields where necessary.

The notebook should make it clear:

- what changed,
- what stayed constant,
- what result was produced.

---

# 39. One Change at a Time

When experimenting, prefer changing one meaningful component at a time.

Example:

```text
Experiment 1: baseline
Experiment 2: change model only
Experiment 3: add feature group
Experiment 4: change weighting
```

This makes improvements attributable and easier to understand.

Avoid changing the dataset, model, features, validation, and hyperparameters simultaneously unless explicitly requested.

---

# 40. End-of-Step Summary

After a major section, provide a short conclusion.

Example:

```markdown
### Current finding

The PCA-based rating has the strongest rank correlation with the external
benchmark. The improvement over equal weighting is small, however, and should
be checked across additional seasons before drawing a final conclusion.
```

Clearly separate:

- observation,
- interpretation,
- next possible step.

---

# 41. Approval Gate for Next Steps

At the end of a meaningful analytical stage:

1. summarize the current result,
2. list at most a few relevant next-step options,
3. state which option appears methodologically reasonable and why,
4. ask the user which direction to continue.

Do not automatically execute additional research ideas.

Example:

```text
Current result:
The temporal baseline reaches 0.78 balanced accuracy.

Possible next steps:
A) inspect errors by player position,
B) tune the current model,
C) compare a LightGBM model.

I would test A before adding model complexity because it can reveal systematic
failure modes. Should I proceed with A?
```

---

# 42. When Not to Ask

Do not interrupt the workflow for trivial implementation details that do not alter the methodology.

Examples:

- changing a plot label,
- fixing syntax,
- using `.copy()` to avoid a pandas warning,
- formatting a table,
- replacing duplicated code with an equivalent local function.

Ask when a choice affects:

- methodology,
- interpretation,
- project scope,
- data,
- model behavior,
- evaluation,
- dependencies,
- architecture.

---

# 43. No Unrequested Deliverables

Do not automatically create:

- dashboards,
- APIs,
- Streamlit apps,
- web applications,
- production pipelines,
- packages,
- Docker containers,
- command-line tools,
- databases,
- cloud deployments,

unless requested.

The default deliverable is the transparent Jupyter Notebook analysis.

---

# 44. Final Notebook Quality Check

Before considering a notebook step complete, check:

```text
[ ] Can the notebook be understood from top to bottom?
[ ] Is the purpose of the analysis clear?
[ ] Are inputs and important assumptions visible?
[ ] Are important intermediate states shown?
[ ] Are useful visualizations included?
[ ] Is the code implemented with as few lines as reasonably possible without losing functionality?
[ ] Are logical code blocks separated by sensible blank lines instead of being visually compressed?
[ ] Are repeated operations encapsulated appropriately?
[ ] Is data leakage prevented?
[ ] Is validation appropriate for the task?
[ ] Are random states controlled where needed?
[ ] Are metrics suitable for the problem?
[ ] Are results shown rather than merely claimed?
[ ] Are observations separated from interpretation?
[ ] Have unsupported assumptions been avoided?
[ ] Were methodological changes approved by the user?
[ ] Were unnecessary external Python files avoided?
[ ] Could a human reasonably reproduce the analysis?
```

---

# 45. Default Behavioral Rule

When uncertain, follow this priority order:

```text
Correctness
> methodological validity
> transparency
> reproducibility
> human interpretability
> simplicity
> compactness
> computational optimization
> architectural elegance
```

The agent should behave like a careful Data Scientist working together with a human researcher, not like an autonomous software architect trying to redesign the project.

The notebook must remain the central, visible source of truth.

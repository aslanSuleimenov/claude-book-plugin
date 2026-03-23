---
description: Show or change prose parameters (POV, tense, compression, interiority)
argument-hint: "[param value]"
---

Show or update prose style parameters.

Argument: $ARGUMENTS

## If no argument — show current parameters

Read `CLAUDE.md` and print:
```
POV:          [current value]
tense:        [current value]
compression:  [current value]
interiority:  [current value]
```

Plus a one-line description of what each value means in practice.

## If argument given — update parameter

Parse: first token = parameter name, rest = new value.

Valid parameters and values:
- `POV`: `third-limited` / `first` / `third-omniscient`
- `tense`: `past` / `present`
- `compression`: `minimal` / `moderate` / `expansive`
- `interiority`: `low` / `medium` / `high`

Update the value in `CLAUDE.md`.

Warn if the change has implications:
- Changing POV after chapters are written = consistency work needed
- Changing tense = all chapters need updating
- Changing compression = adapt-mode chapters will look different going forward

Ask: "Do you want to apply this to existing chapters too? If yes, run `/rewrite` on them with this note."

## Parameter reference

| Parameter | Values | Effect |
|-----------|--------|--------|
| POV | third-limited | One character's perception only, no other minds |
| | first | Narrator is protagonist |
| | third-omniscient | Narrator can access any mind |
| tense | past | Standard narrative past |
| | present | Immediate, cinematic |
| compression | minimal | Scene ≈ source length (adapt) or spare prose |
| | moderate | 1.5–2× expansion, balanced |
| | expansive | 2.5–4× expansion, rich texture |
| interiority | low | Mostly external, behavior and dialogue |
| | medium | Some POV thoughts, filtered perception |
| | high | Deep inner life, psychological texture |

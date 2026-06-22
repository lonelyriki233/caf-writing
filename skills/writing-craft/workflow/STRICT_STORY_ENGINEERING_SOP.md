# Strict Story Engineering SOP / 严格小说工程化流程

## 0. Principle
Finished prose is the last artifact, not the first artifact.

如果早期 gate 失败，不要靠文风、气氛、设定或漂亮句子遮丑。

## 1. Compass gate
Create/read `00_compass.md`.

Required:
- current project north star
- what this volume/chapter must prove
- what is forbidden in this run
- current stage

Gate: if direction is vague, do not write outline/prose.

## 2. Story engine gate
Create `01_story_engine.md`.

Required six basics:
1. protagonist
2. protagonist gap
3. external want
4. opposition / obstacle
5. failure cost
6. worth-reading contradiction

Then four progression questions:
7. why now
8. old wrong strategy
9. midpoint escalation
10. final choice cost

Gate: if two or more are missing, stop.

## 3. Theme/action gate
Create `02_theme_action.md`.

Required:
- theme as question, not slogan
- theme embodied in action/consequence
- at least three concrete situations that test the theme

Gate: if theme cannot be tested in action, rewrite.

## 4. Volume / act / sequence gate
Create `03_volume_structure.md`.

Required:
- Act I setup pressure
- Act II confrontation route
- Act III resolution / new balance
- plot point 1
- midpoint
- plot point 2 / all-is-lost pressure
- finale choice
- sequence goals and turns

Gate: reject loose event lists.

## 5. Character engine gate
Create `04_character_engine.md`.

For each major character:
- want
- need
- fear / shame / wound if any
- wrong strategy
- pressure button
- relationship function
- change or refusal to change
- voice constraints

Gate: reject label-only characters.

## 6. Chapter spec gate
Before every chapter, create `chapter_specs/chXX_spec.md`.

Required:
```text
Chapter dramatic need:
Act / sequence position:
Plot point function, if any:
Opening imbalance:
Closing turn:
New question:
```

Gate: if chapter only displays setting, reject.

## 7. Scene card gate
For every key scene, create scene cards or a table.

Required:
- place / time
- POV
- scene target
- obstacle
- tactic / action
- stimulus → response chain for key beats
- tactic shift under resistance
- value/status/information change
- result
- sequel reaction / dilemma / decision if this is a major turn
- new question
- information revealed now
- information delayed

Gate: if deleting the scene changes nothing, delete or rewrite. If there is no stimulus-response causality, no active resistance, or no changed situation, the scene fails.

## 8. Dialogue map gate
Before dialogue-heavy scenes, create dialogue map.

Required:
- character A wants
- character B wants
- action verb per speaker
- said
- unsaid
- unsayable
- conflict type: balanced / comic / asymmetric / indirect / reflexive / minimal
- NPC voice card if NPC appears

Gate: if dialogue is Q&A exposition, rewrite.

## 9. Draft gate
Only after gates 1-8 pass, write prose.

Draft constraints:
- start with ongoing action/sensation/problem, not encyclopedia background
- reveal exposition at point of need
- use concrete action/object/space/body reaction before abstract explanation
- keep character voice uneven and pressure-specific

## 10. Anti-AI/prose audit gate
Create `revision_reports/chXX_anti_ai_audit.md`.

Check:
- too smooth dialogue
- early tidy explanation
- emotion labels instead of reactions
- uniform paragraph rhythm
- functional NPCs without pressure
- author-summary voice
- sentence rhythm not tied to scene pressure
- description that does not reveal perception, pressure, or story function
- interior monologue repeating what action already shows

## 11. Objective quality gate
Score with `quality_gates/QUALITY_RUBRICS.md` and read `craft_patterns/objective_quality_gate_upgrade.md`.

Hard fail if:
- no focal pressure
- no scene result
- no cost
- dialogue is Q&A exposition
- exposition appears before trouble
- prose polish hides an empty scene

## 12. Revision gate
Create `revision_reports/chXX_revision_report.md`.

Required:
- original failure
- changed story engine / scene / dialogue / prose layer
- remaining weakness
- next revision target

If the same failure appears twice, add it to `active_constraints.md`.

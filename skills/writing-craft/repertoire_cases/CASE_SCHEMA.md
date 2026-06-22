# Story Repertoire Case Schema

Each case must avoid copying text. Extract mechanisms only.

```json
{
  "id": "string",
  "source_type": "user_project | reference_note | classic | light_novel | galgame | failed_draft",
  "source_path": "local path or description",
  "genre_function": "what this case teaches",
  "story_engine": {
    "protagonist_pressure": "",
    "want": "",
    "obstacle": "",
    "cost": "",
    "turn": ""
  },
  "scene_engine": {
    "target": "",
    "obstacle": "",
    "tactic": "",
    "result": "",
    "new_question": ""
  },
  "dialogue_engine": {
    "verbal_actions": [],
    "said_unsaid_unsayable": "",
    "exposition_timing": ""
  },
  "quality_lesson": "reusable lesson",
  "anti_copy_rule": "what must not be copied",
  "tags": []
}
```

Gate: a case is incomplete if it only says “atmosphere good / character strong” without mechanism.

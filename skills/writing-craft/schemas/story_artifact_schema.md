# Story Artifact Schema

Every generated project artifact should declare:

```yaml
artifact_type: compass | story_engine | character_engine | volume_structure | chapter_spec | scene_card | dialogue_map | draft | revision_report
project:
stage:
source_inputs:
gate_status: pass | fail | needs_revision
```

Recommended fields by type are defined in `templates/`.

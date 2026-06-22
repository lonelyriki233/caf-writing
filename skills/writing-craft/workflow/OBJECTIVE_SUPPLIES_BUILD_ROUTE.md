# Objective Supplies Full KB Build Route

status: mandatory for this build
source_root: `/mnt/f/创作/奇迹/novel_lab/source/objective_supplies`
kb_root: `/mnt/f/创作/奇迹/novel_lab/knowledge_base`

## Principle
路线先于内容。不要只做摘要；每本教材必须转化为可执行写作规则、闸门、诊断、模板/检索入口，并能服务严格小说工程化 SOP。

## Route

### 1. Source inventory gate
For every source file:
- record path
- extension/type
- extraction method
- whether it is new P0/P1 material or old baseline duplicate
- extraction status

Output:
- `source_inventory/objective_supplies_manifest.json`
- `source_inventory/objective_supplies_manifest.md`

### 2. Text extraction gate
Extract readable text into:
- `source_extracted/objective_supplies/<slug>.txt`

Rules:
- EPUB: unzip and parse XHTML/HTML spine/order where possible.
- TXT: copy/normalize.
- MOBI: convert if tool exists; otherwise record blocker.
- PDF: extract text if available; otherwise record OCR need.

Gate: no book is silently skipped.

### 3. Module construction gate
For each new craft book or book-family, create module:
`textbooks/<module_slug>/`

Required files:
- `source_note.md`
- `concepts.jsonl`
- `action_rules.md`
- `gates.md`
- `diagnostics.md`
- `query_map.md`

JSONL schema:
```json
{"id":"","source":"","concept":"","trigger":"","rule":"","gate":"","tags":[]}
```

### 4. Strict writing-rule alignment gate
Every module must map rules to at least one SOP layer:
- compass
- story_engine
- theme_action
- volume_structure
- character_engine
- chapter_spec
- scene_card
- dialogue_map
- draft
- prose_audit
- revision

### 5. Cross-book synthesis gate
After per-book modules, build cross-cutting pattern families:
- scene_mechanics_patterns.md
- plot_traction_patterns.md
- character_arc_patterns.md
- prose_revision_patterns.md
- objective_quality_gate_upgrade.md

### 6. Validation gate
Validate:
- all manifest entries accounted for
- all extracted text files exist or blocker recorded
- all module JSONL parses
- required module files exist
- INDEX includes new modules
- fiction-writing-lab skill status patched

Output:
- `BUILD_VALIDATION.json`
- `OBJECTIVE_SUPPLIES_BUILD_REPORT.md`

## Completion definition
This pass is complete only when every objective_supplies source is either:
1. extracted and represented in a module, or
2. explicitly marked duplicate/old-baseline with existing module reference, or
3. explicitly blocked with reason and next action.

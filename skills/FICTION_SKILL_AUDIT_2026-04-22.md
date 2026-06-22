# Fiction / Story Skill Audit — 2026-04-22

## Question
用户问：现在小说/故事创作 skills 缺什么？之前准备的教科书有没有读入 skill 中？

## Checked skills

### Active Hermes umbrella
- `fiction-writing-lab`
  - path: `/home/blj20/.hermes/skills/creative/fiction-writing-lab/SKILL.md`
  - linked refs:
    - `references/story-shaping-requirements.md`
    - `references/light-novel-style-lab.md`
    - `references/local-novel-reader-tts.md`

### Archived / older imported skills
- `.archive/.../creative/story-shaping-requirements`
- `.archive/.../creative/light-novel-style-lab`
- `.archive/.../creative/read-book-to-training-data`

### Local novel_lab skill copies
- `/mnt/f/创作/奇迹/novel_lab/skills/story-shaping-requirements/SKILL.md`
- `/mnt/f/创作/奇迹/novel_lab/skills/read-book-to-training-data/SKILL.md`

## Local teaching/source materials found

Craft books / extracted notes:
- `/mnt/f/创作/奇迹/novel_lab/books/写作教科书/小说创作二十讲.pdf`
- `/mnt/f/创作/奇迹/novel_lab/books/写作教科书/冲突与悬念_小说创作的要素.epub`
- `/mnt/f/创作/奇迹/novel_lab/books/写作教科书/救猫咪-小说创作指南.epub`
- `/mnt/f/创作/奇迹/novel_lab/extracted/Screenplay_The_Foundations_of_Screenwriting_Syd_Field.txt`
- `/mnt/f/创作/奇迹/novel_lab/extracted/Dialogue_The_Art_of_Verbal_Action_Robert_McKee_zh.txt`
- `/mnt/f/创作/奇迹/novel_lab/新增教材收束笔记_Screenplay_Dialogue_2026-04-22.md`

Style/source reading assets:
- `/mnt/f/创作/奇迹/novel_lab/books/light_novels/空之境界.extracted.txt`
- `/mnt/f/创作/奇迹/novel_lab/books/light_novels/物语系列.extracted.txt`
- `/mnt/f/创作/奇迹/novel_lab/books/light_novels/月姬.extracted.txt`
- `/mnt/f/创作/奇迹/novel_lab/books/light_novels/Re：从零开始的异世界生活1-13卷套装.extracted.txt`
- `/mnt/f/创作/奇迹/novel_lab/style-guides/*.md`
- `/mnt/f/创作/奇迹/novel_lab/style-guides/light-novel-anti-ai-checklist.md`

Dataset/model engineering assets:
- `/mnt/f/创作/奇迹/novel_lab/自创模型/写作增强工程/data/README.md`
- `/mnt/f/创作/奇迹/novel_lab/自创模型/写作增强工程/docs/Qwen官方数据格式基准说明.md`
- `/mnt/f/创作/奇迹/novel_lab/自创模型/写作增强工程/docs/数据格式_官方基准_messages.md`
- `/mnt/f/创作/奇迹/novel_lab/自创模型/写作增强工程/data/packs/read-book-to-training-data/`

## Findings

### 已读入/已反映
1. `story-shaping-requirements` 已明确包含三本基础教科书：
   - 小说创作二十讲
   - 冲突与悬念
   - 救猫咪-小说创作指南
2. archived `story-shaping-requirements` 已包含新增两本：
   - Syd Field `Screenplay`
   - Robert McKee `Dialogue`
   并有章节规格：dramatic need / act-sequence / scene target-obstacle-result / dialogue said-unsaid-unsayable / NPC voice cards / exposition timing。
3. `fiction-writing-lab` 主 skill 已在 overview 中吸收了“protagonist gap + desire + pressure + cost / scene goal-obstacle-result / dialogue subtext”等核心规则。
4. `light-novel-style-lab` 与 style-guides 已有空之境界、物语、月姬、Re:Zero 等本地文本抽样/风格记录。
5. `read-book-to-training-data` 已按用户偏好采用 Qwen messages 外层结构，custom tags 放 content 内。

### 缺口/不一致
1. Active umbrella 的 linked reference `references/story-shaping-requirements.md` 仍是旧描述：只说三本教科书，不完整反映 Screenplay / Dialogue。
2. Local novel_lab copy `/novel_lab/skills/story-shaping-requirements/SKILL.md` 也仍是三本旧版，未同步新增教材。
3. 目前没有一个像 music_lab 那样的 `knowledge_base/INDEX.md + STRICT_SOP.md + schemas + diagnostics + verification` 级别的小说工程化知识库。
4. style-guides 很多，但 story engineering 与 prose/style engineering 尚未统一为“分阶段 gates”：story premise -> protagonist engine -> act/sequence -> scene spec -> dialogue map -> prose draft -> anti-AI audit -> revision report。
5. 还缺少明确的本地项目级 scaffold：每个小说项目应固定产物目录与文件名，例如 `00_compass.md`, `01_story_engine.md`, `02_volume_beats.md`, `03_chapter_specs/`, `04_dialogue_maps/`, `05_drafts/`, `06_revision_reports/`, `active_constraints.md`。

## Immediate patch decision
Patch active `fiction-writing-lab` so future direct use不会漏掉 Field/McKee 与工程化 gate。Local novel_lab copy can be synchronized later if user wants exact repo-level skill files aligned.

## Recommended next build
Build `/mnt/f/创作/奇迹/novel_lab/knowledge_base/` with:
- `INDEX.md`
- `workflow/STRICT_STORY_ENGINEERING_SOP.md`
- `diagnostics/story_failure_diagnostics.md`
- `diagnostics/dialogue_failure_diagnostics.md`
- `templates/project_scaffold.md`
- `templates/chapter_spec.md`
- `templates/dialogue_map.md`
- `templates/revision_report.md`
- `verification/chapter_gate_checklist.md`
- textbook modules for the five craft books and style modules for local light novel guides.

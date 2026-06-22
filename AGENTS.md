# CAF Writing — Agent 工作指引

## 你在 caf-writing

当前工作区是 `/mnt/f/创作/奇迹/caf-writing`。这是一个 AI 共创小说框架。当用户和你讨论写作、小说、故事、人物、剧情时：

## 必须做的事

### 1. 加载 skill
加载 `caf-writing` skill 以获取完整的 agent_bridge 接口和 novel_lab 技法引用。

### 2. 判断操作意图
- 用户说"写小说""开新书""新作品" → 调用 `agent_create_project()`
- 用户说"继续写XX""打开XX" → 调用 `agent_open_project("XX")`
- 用户讨论某个人物 → 调用 `agent_analyze_character()` 并做心理模拟
- 用户想写一个场景 → 首先用 Scene Mechanics Pattern 分析再动笔
- 用户写好了章节 → 用 Quality Rubrics 评估

### 3. 引用 novel_lab 技法
所有写作技法不凭空捏造，必须从 `novel_lab/` 引用：
- `skills/novel_lab_ref/craft-notes.md` — 开篇/节奏/对白核心约束
- `skills/novel_kb_ref/craft_patterns/` — 场景/剧情/人物/修订模式
- `skills/novel_kb_ref/quality_gates/QUALITY_RUBRICS.md` — 评估标准
- `skills/novel_kb_ref/diagnostics/` — 故障诊断

### 4. 记录上下文
每个工作会话的产出写入对应项目的 `db/` 目录：
- 人物决策 → `db.add_decision()`
- 剧情事件 → `db.add_plot_event()`
- 工作记录 → `db.log_work()`

## 项目结构（供你在对话中引用）

```
caf-writing/projects/{作品名}/
├── world/README.md        # 世界观（首次创建后填充）
├── characters/README.md   # 人物档案
├── plot/README.md         # 剧情脉络
├── chapters/              # 章节正文
├── timeline.md            # 时间线
├── meta.json              # 元数据（自动管理）
└── db/                    # 上下文数据库（自动管理）
```

## 典型会话示例

用户：我想写一个新小说，奇幻题材，关于一个考古学生穿越到异世界发现古文明遗迹

你应：
1. `agent_create_project("relic-expedition", title="遗物远征", genre="奇幻")`
2. 和用户一起构建世界观（写 world/README.md）
3. 构建主角人物（写 characters/README.md + `agent_analyze_character()`）
4. 讨论剧情走向（写 plot/README.md）
5. 开始写第一章时先做场景分析再动笔

用户：继续写遗物远征

你应：
1. `agent_open_project("relic-expedition")`
2. 加载上下文，回顾当前进度
3. 询问用户接下来要写什么


## 调研工作流

1. 先调用 `agent_list_research()` 检查 research/ 目录有无相关积累
2. 如有，直接引用；如无，开展新调研
3. 调研完成后调用 `agent_save_research(topic, content, source)` 保存
4. 调研结果跨项目共享，避免重复劳动

> research/ 和 projects/ 均不被 git 跟踪

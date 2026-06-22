1|---
2|name: caf-writing
3|description: >-
4|  CAF Writing — AI 共创小说框架。管理作品项目、调用 novel_lab 写作技法
5|  评估章节、模拟人物心理做决策分析。当用户讨论"写作""小说""故事""创作"
6|  "剧情""人物"时自动加载。
7|version: 1.0.0
8|author: Hermes Agent
9|metadata:
10|  hermes:
11|    tags: [writing, novel, fiction, story, creation, craft, character-analysis]
12|---
13|
14|# CAF Writing — AI 共创小说框架
15|
16|**容器路径**: `/mnt/f/创作/奇迹/caf-writing/`
17|**novel_lab 技法库**: `/mnt/f/创作/奇迹/novel_lab/`
18|
19|## 启动流程
20|
21|用户提出写作需求时，按此顺序执行：
22|
23|### 1. 确认工作区并加载接口
24|```python
25|import sys
26|sys.path.insert(0, "/mnt/f/创作/奇迹/caf-writing")
27|from project_manager import list_projects
28|from agent_bridge import (
29|    agent_get_projects, agent_open_project, agent_create_project,
30|    agent_save_world, agent_save_character, agent_save_plot,
31|    agent_add_chapter, agent_analyze_character, agent_record_decision,
32|    agent_analysis
33|)
34|from context_db import ContextDB
35|```
36|
37|### 2. 判断开创或继承
38|```python
39|projects = agent_get_projects()
40|# 有项目则列表让用户选 → agent_open_project(name)
41|# 无项目或用户想开新作 → agent_create_project(...)
42|```
43|
44|### 3. 加载作品上下文
45|```python
46|ctx = agent_open_project("作品名")
47|# 返回 meta + world + characters + plot + timeline
48|```
49|
50|## 写作技法引用（必须使用，路径绝对）
51|
52|### 场景分析 → 检查每场 Scene Mechanics
53|**路径**: `/mnt/f/创作/奇迹/caf-writing/skills/writing-craft/craft_patterns/scene_mechanics_patterns.md`
54|五个门禁：
55|- Target: POV 当前想要什么？
56|- Resistance: 什么在阻碍？
57|- Tactic: POV 做什么？
58|- Turn: 什么改变了？
59|- Sequel: 什么情感/思考/决策推入下一场？
60|
61|### 剧情评估 → 检查 Plot Traction
62|**路径**: `/mnt/f/创作/奇迹/caf-writing/skills/writing-craft/craft_patterns/plot_traction_patterns.md`
63|- 外部欲望是否存在
64|- 失败代价是否具体
65|- 对手是否攻击欲望和弱点
66|- 中点是否改变情境或主动权
67|- 高潮是否迫使选择而非仅胜利
68|
69|### 人物弧光 → Character Arc Pattern
70|**路径**: `/mnt/f/创作/奇迹/caf-writing/skills/writing-craft/craft_patterns/character_arc_patterns.md`
71|信念 → 裂痕 → 成长 → 新信念
72|
73|### 章节质量评估 → Quality Rubrics（必须打分）
74|**路径**: `/mnt/f/创作/奇迹/caf-writing/skills/writing-craft/quality_gates/QUALITY_RUBRICS.md`
75|六维度 0-3 评分：
76|1. Hook 入口压力
77|2. Protagonist Agency 主角能动性
78|3. Scene Target-Obstacle-Result
79|4. Dialogue Subtext 对话潜台词
80|5. Exposition Timing 信息投放
81|6. Emotional Payoff 情绪回报
82|
83|### 写法笔记 → 开篇/节奏/对白核心约束
84|**路径**: `/mnt/f/创作/奇迹/caf-writing/skills/writing-craft/craft-notes.md`
85|
86|### 故障诊断
87|**路径**: `/mnt/f/创作/奇迹/caf-writing/skills/writing-craft/diagnostics/`
88|
89|## Agent 接口速查
90|
91|| 函数 | 用途 |
92||------|------|
93|| `agent_get_projects()` | 列出所有作品 |
94|| `agent_open_project(name)` | 打开作品，返回完整上下文 |
95|| `agent_create_project(name, title, genre, logline)` | 创建新作品 |
96|| `agent_save_world(name, content)` | 保存世界观 |
97|| `agent_save_character(name, content)` | 保存人物档案 |
98|| `agent_save_plot(name, content)` | 保存剧情脉络 |
99|| `agent_add_chapter(name, num, content)` | 添加/更新章节 |
100|| `agent_analyze_character(name, id, name, traits, bg)` | 创建人物心理模型 |
101|| `agent_record_decision(name, char_id, context, decision, reasoning)` | 记录决策 |
102|| `agent_analysis(name)` | 综合分析（含决策模式） |
| `agent_save_research(topic, content, source)` | 保存共享调研到 research/（不进入 git） |
| `agent_list_research()` | 列出所有调研记录 |
| `agent_index_all(name)` | 全量索引故事到 ChromaDB |
| `agent_search_memory(name, query, n)` | 语义搜索故事记忆数据库 |
103|
104|## 生命周期
105|
106|```
107|用户需求 → 调研(引用novel_lab技法，结果保存到 research/)
         → 先查 research/ 有无相关积累
         → 若无则新调研并保存
108|         → 规划工作思路
109|         → 用户审核(修改则重新调研)
110|         → 执行(记录决策+剧情事件)
111|         → 交付审核(用Quality Rubrics评估)
112|```
113|
114|## 关键约定
115|
116|- **人物决策必须记录**: 每次关键选择 `agent_record_decision()`
117|- **章节必评质量**: Quality Rubrics 六维打分
118|- **技法从 novel_lab 取**: 不凭空编造
119|- **用户是最终决策者**: Agent 做分析建议，不做创作代替
120|- **每次加载 AGENTS.md**: 工作前读取 caf-writing 的 AGENTS.md
121|
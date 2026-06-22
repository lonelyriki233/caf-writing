# CAF Writing — AI 共创小说框架

## 一句话
每个作品是一个独立项目。Agent 和你一起构思、写作、剖析人物，不做你的代笔。

## 快速开始

```bash
cd /mnt/f/创作/奇迹/caf-writing

# 列出项目
python3 __main__.py --list

# 创建新项目（或由 Agent 创建）
python3 __main__.py --create my-novel "我的小说标题"

# 启动 Dashboard（作品管理面板）
python3 __main__.py
# → http://localhost:8092
```

## 目录结构

```
caf-writing/
├── __main__.py           # 入口
├── project_manager.py    # 项目 CRUD
├── context_db.py         # 上下文数据库（人物、剧情、决策）
├── agent_bridge.py       # Agent 接口
├── dashboard/            # Web 面板
│   ├── app.py
│   └── templates/
│       ├── index.html    # 作品列表
│       └── project.html  # 作品详情
├── projects/             # 作品数据
│   └── {作品名}/
│       ├── meta.json     # 元数据
│       ├── world/        # 世界观设定
│       ├── characters/   # 人物档案
│       ├── plot/         # 剧情脉络
│       ├── chapters/     # 章节正文
│       ├── timeline.md   # 时间线
│       └── db/           # 上下文数据库
└── skills/               # 写作技法（引用 novel_lab）
```

## Agent 使用方式

在 Hermes 中加载 caf-writing 后：

1. **打开已有作品**
   ```
   agent_open_project("my-novel")   # 加载完整上下文
   ```

2. **创建新作品**
   ```
   agent_create_project("my-novel", title="小说名", genre="奇幻", logline="...")
   ```

3. **保存设定**
   ```
   agent_save_world("my-novel", "世界观内容（Markdown）")
   agent_save_character("my-novel", "人物档案")
   agent_save_plot("my-novel", "剧情脉络")
   agent_add_chapter("my-novel", 1, "第一章正文")
   ```

4. **人物心理模拟**
   ```
   agent_analyze_character("my-novel", "protagonist", "主角名", "勇敢/冲动/重情义", "背景...")
   agent_record_decision("my-novel", "protagonist", "某情境", "选择", "原因")
   ```

5. **综合分析**
   ```
   agent_analysis("my-novel")  # 返回决策模式、人物关系、进度
   ```

## 工作流程（简化 CAF 生命周期）

```
需求提出 → 调研 → 规划工作思路 → 用户审核 → 执行 → 用户审核交付
```

不是复杂的多阶段审批，而是**轻量、灵活**的：
- **调研**：查资料、分析人物、评估剧情
- **规划**：给出具体工作思路（分步骤）
- **审核**：用户确认或调整
- **执行**：按思路写
- **交付**：展示成果，用户验收

## 核心能力

| 能力 | 说明 |
|------|------|
| 人物心理模拟 | 基于性格 traits + 决策历史预测人物在情境中的反应 |
| 决策记录分析 | 跟踪关键选择，发现人物行为模式 |
| 剧情脉络管理 | 记录事件 → 人物 → 章节的关联网络 |
| 关系演化追踪 | 人物间关系动态更新 |
| 写作技法继承 | 引用 novel_lab 的知识库和写作技巧 |

## 设计理念

- **共创不是代写**：Agent 做调研、分析、灵感激发，用户做创作决策
- **人物是一切**：好的故事 = 好的人物在压力下做选择
- **技术沉淀**：每次写作中发现的技巧成为可复用的 skill
- **轻量生命周期**：不要复杂的审批流程，重在上下文管理和人物心理

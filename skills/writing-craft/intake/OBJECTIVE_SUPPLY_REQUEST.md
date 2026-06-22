# Objective Supply Request / 不依赖主观喜好的补料清单

你不用给“我喜欢什么”。只需要准备可学习资料。

## A. 最优先补的 craft 教材类型

### 1. 场景推进 / scene mechanics
目标：让每个场景有刺激-反应-行动-结果，而不是只有说明。
建议书：
- Dwight V. Swain — Techniques of the Selling Writer
- Jack M. Bickham — Scene & Structure
- Jack M. Bickham — The 38 Most Common Fiction Writing Mistakes

### 2. 小说结构 / plot engineering
目标：补足长篇结构、hook、turn、chapter traction。
建议书：
- Robert McKee — Story
- John Truby — The Anatomy of Story
- James Scott Bell — Plot & Structure
- Larry Brooks — Story Engineering
- K.M. Weiland — Structuring Your Novel

### 3. 人物弧光 / character arc
目标：人物不是标签，有欲望、谎言、压力、改变/拒绝改变。
建议书：
- K.M. Weiland — Creating Character Arcs
- Lisa Cron — Wired for Story
- Nancy Kress — Characters, Emotion & Viewpoint
- Orson Scott Card — Characters & Viewpoint

### 4. 文体与句子 / prose craft
目标：解决 AI 味、空泛、句子太平、缺质感。
建议书：
- Ursula K. Le Guin — Steering the Craft
- Francine Prose — Reading Like a Writer
- Verlyn Klinkenborg — Several Short Sentences About Writing
- Stephen King — On Writing
- Renni Browne & Dave King — Self-Editing for Fiction Writers

### 5. 类型专项
根据想写方向补：
- Mystery: Writing Mysteries, How to Write Killer Fiction, The Weekend Novelist Writes a Mystery
- Romance: Romancing the Beat
- Fantasy/SF: Wonderbook, The Guide to Writing Fantasy and Science Fiction, The Kobold Guide to Worldbuilding
- Horror/Thriller: Danse Macabre, Writing the Thriller, The Anatomy of Genres
- Comedy/voice: The Comic Toolbox, Writing Dialogue, Writing Voice

## B. 最优先补的作品案例类型
不用说明你喜不喜欢，只要提供文本/书名即可。

### 1. 长篇结构案例
- 经典长篇小说，尤其能看到章节推进和人物弧光的。

### 2. 轻小说/网文式 chapter traction 案例
- 开头抓人、章节钩子强、角色互动强的作品。

### 3. VN / Galgame 案例
- 能分析 route、flag、共通线/个人线、情绪 payoff 的作品。

### 4. 对白强案例
- 剧本、电影、舞台剧、小说对白片段均可。

### 5. 失败案例
- 不需要你主观评价，只要是公认/明显问题样本、旧稿、AI 生成稿、低质文本即可。

## C. 建议放置目录
```text
/mnt/f/创作/奇迹/novel_lab/source/objective_supplies/
  craft_books/
  novels/
  light_novels/
  vn_gal/
  scripts_screenplays/
  failed_samples/
```

## D. 我会怎么处理
每批资料进入后：
1. extract / normalize；
2. concepts.jsonl / action_rules.md；
3. repertoire case deep-pass；
4. pattern family；
5. diagnostics / gates patch；
6. BUILD_VALIDATION 更新。

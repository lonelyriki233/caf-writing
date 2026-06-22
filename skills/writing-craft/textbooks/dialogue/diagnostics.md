# Diagnostics

## Symptom: 角色开口、内心独白、第一人称叙述或旁白正在承载场景推进时。
Repair: 每句重要对白必须能标注一个行动动词，并且让场景 beat、关系、信息或压力发生微小偏转；只回答设定问题的台词要删掉或改成行动。
Gate: line_action_verb_gate

## Symptom: 出现连续对话或角色解释自身想法时。
Repair: 为每个说话者写清此刻 want，并给每句台词标注企图：试探、遮掩、拒绝、讨好、压迫、转移、诱导、安抚、挑衅、求助等；无企图则不成对白。
Gate: speaker_want_gate

## Symptom: 对白涉及秘密、伤痛、礼仪、政治、悼念、神圣物、羞耻或禁忌时。
Repair: 先写表面说出口的 said、知道但暂不说的 unsaid、因恐惧/身份/礼仪/愧疚/神圣禁忌而不能说的 unsayable，再写台词；缺少后两层时对白会变薄。
Gate: subtext_three_layer_gate

## Symptom: 对白字面含义过直、人物把心里话完整说出、读者无需推断时。
Repair: 把真实欲望、恐惧、羞耻或策略放到潜文本中，只让台词泄露一部分；读者应能从停顿、选择性措辞、转移话题和反应中推断未说之事。
Gate: subtext_inference_gate

## Symptom: 需要交代世界观、制度、历史、人物背景或规则时。
Repair: 只在角色为当前行动必须知道、读者也正需要知道时给最小信息量；信息要足以继续好奇，而不是提前满足全部理解。
Gate: exposition_timing_gate

## Symptom: 人物准备长篇解释设定、历史、主题或作者观点时。
Repair: 优先用手续、错误、纠正、冲突、谈判、禁忌、道具代价和现场后果承载信息；角色不应停下正在做的事，替作者朗诵背景资料。
Gate: exposition_as_action_gate

## Symptom: 出现一个角色提问、另一个角色完整准确回答设定或剧情答案的 Q&A 段落。
Repair: 禁止问什么答什么的信息倾倒；回答者必须有保留、误解、代价、态度、私心或反向追问，让信息在阻力中被迫显露。
Gate: no_qa_infodump_gate

## Symptom: 不同人物说话听起来像同一作者腔，或只靠口头禅区分时。
Repair: 为角色建立专属词库、句法、节奏、声调和知识边界；声音差异应来自身份、欲望、压力、教育、职业、礼貌层级与回避方式。
Gate: character_voice_distinction_gate

## Symptom: 临时 NPC 说话超过功能性一句，或承担信息、手续、冲突、情绪反馈。
Repair: 出场前写 job、年龄/社会位置、当前压力、害怕/想保住什么、对主角态度、说话习惯、本场行动动词；没有声音卡的 NPC 不得承载关键对白。
Gate: npc_voice_card_gate

## Symptom: 关键对话场景开始前，人物目标相撞但台词形态未定时。
Repair: 先选择冲突类型：平衡式、喜趣式、非对称、间接、反身式、极简；冲突类型决定发言长度、锋利度、回避程度、权力压迫与潜文本密度。
Gate: conflict_type_selection_gate

## Symptom: 双方资源、地位、信息或情感筹码接近，争执需要互有来回。
Repair: 让双方都能进攻和防守，每一轮台词都改变局部优势；适用于队内磨合、伙伴争论、主角团策略分歧。
Gate: balanced_conflict_gate

## Symptom: 日常、少年少女互动、公会轻场景或误会场景需要轻喜剧张力时。
Repair: 喜剧来自欲望错位、地位反差、误解升级和措辞节奏；不得用破坏神圣伦理、悼念对象或核心悲剧重量来换笑点。
Gate: comic_conflict_ethics_gate

## Symptom: 新人面对接待员、老手、贵族、公务体系、审查者或任何权力不对等关系。
Repair: 强势方可用程序、沉默、称谓、打断、轻描淡写施压；弱势方需以试探、迂回、讨好、硬撑或抓漏洞争取空间。
Gate: asymmetric_power_gate

## Symptom: 暗线反派、政治试探、不能公开摊牌、双方都在装作谈别的事情。
Repair: 表面话题必须有现实功能，真实攻防藏在选择性措辞、信息遗漏、礼貌过度、错误称谓和反应延迟中；读者应感到另有一层在交锋。
Gate: indirect_conflict_subtext_gate

## Symptom: 角色独处、内心独白、第一人称自述、遗物碎片触发或自我说服时。
Repair: 内心话也要有对手：另一个自我、记忆、欲望、羞耻或禁忌；让内心对白产生选择变化，而不是静态抒情。
Gate: reflexive_inner_conflict_gate

## Symptom: 神圣仪式、悼念场合、羞耻、亲密沉默或不能明说的关系裂缝。
Repair: 少说、慢说、错开说，用停顿、称谓、动作、未完成句和礼仪细节制造压力；不要用直白解释摧毁含蓄。
Gate: minimal_conflict_restraint_gate

## Symptom: 英灵遗物、归航仪式、死亡、悼念、祖先、牺牲或神圣职业被提及时。
Repair: 必须设计不可说层，用停顿、压低声音、改口、正式称谓、避讳手势、程序纠正和误用代价体现敬畏；禁止随口轻浮冒犯。
Gate: sacred_unsayable_gate

## Symptom: 一段对话结束后，场景状态看似与开始相同。
Repair: 对话收束时至少改变一项：关系距离、权力格局、信息分布、情绪温度、行动决定、风险认知或下一步问题；没有变化则整段无效。
Gate: dialogue_turn_result_gate

## Symptom: 对白模拟真实闲聊、寒暄、重复确认或无压力聊天。
Repair: 故事对白要压缩日常噪音，只保留承载欲望、冲突、潜文本、节奏或角色声音的部分；寒暄只有在能表现权力、关系或伪装时保留。
Gate: no_chatter_cliche_gate

## Symptom: 小说段落混合第三人称旁白、第一人称回忆、内心独白和直接对白时。
Repair: 确认谁在说、说给谁听、是否属于角色行动；第三人称叙述可有文体，但角色才有可被欲望推动的 voice，不能让旁白替角色说出所有潜文本。
Gate: narrator_character_voice_gate

## Symptom: 第一人称主述、回忆讲述、旁白直接对读者说明自身经历。
Repair: 叙述者对读者说话也在行动：求原谅、争取信任、掩饰错误、操控同情、制造悬念；标注叙述策略，避免变成中立资料播报。
Gate: narratized_dialogue_strategy_gate

## Symptom: 章节或场景前需要安排读者知道什么、不知道什么。
Repair: 写出本场必须知道、可暗示、必须延迟三类信息；任何不服务当前目标/障碍/选择的信息推迟到下一次需求点。
Gate: information_delay_gate

## Symptom: 写关键场景、争执、审问、委托、仪式、揭露或告别前。
Repair: 先写 dialogue map：A wants、B wants、said、unsaid、unsayable、conflict type、action verbs、exposition now/delay；未完成对话图不得直接写正文。
Gate: dialogue_map_required_gate

## Symptom: 对白看起来不自然、冷、机器人或说明味重，需要修稿时。
Repair: 修订顺序为：dramatic need、scene target/obstacle/result、conflict type、action verbs、subtext layers、voice diction，最后才润色句子；不能先改文风掩盖结构空洞。
Gate: dialogue_revision_order_gate

## Symptom: 世界观制度、组织流程、登记、审查、训练、禁忌规则需要出现。
Repair: 让信息通过角色犯错、被纠正、填表、排队、验物、争执责任或触犯禁忌出现；程序阻力必须同时推动人物目标。
Gate: procedural_exposition_gate

## Symptom: 多人对白、NPC 对白或旁白连续出现同样冷淡、抽象、理性化句式。
Repair: 检查每个说话者的知识范围、礼貌层级、回避方式、情绪泄露点、专业词和价值禁忌；若可互换说话人而不违和，则重写。
Gate: anti_author_voice_gate


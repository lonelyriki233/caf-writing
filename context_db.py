"""
CAF Writing — 上下文数据库
跟踪人物关系、剧情脉络、决策记录。
简化版 CAF 生命周期：调研 → 规划 → 审核 → 执行 → 交付审核
"""
import os
import json
from datetime import datetime


class ContextDB:
    """项目上下文数据库 — 管理人物关系、剧情走向、决策记录"""

    def __init__(self, project_dir):
        self.db_dir = os.path.join(project_dir, "db")
        os.makedirs(self.db_dir, exist_ok=True)

    def _path(self, name):
        return os.path.join(self.db_dir, f"{name}.json")

    def save(self, name, data):
        """保存数据到 JSON"""
        with open(self._path(name), "w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False, indent=2, default=str)

    def load(self, name):
        """加载 JSON 数据"""
        path = self._path(name)
        if os.path.exists(path):
            with open(path, encoding="utf-8") as f:
                return json.load(f)
        return {}

    # === 人物 ===
    def add_character(self, char_id, name, traits, role, background="", goals=""):
        chars = self.load("characters")
        chars[char_id] = {
            "id": char_id, "name": name, "traits": traits,
            "role": role, "background": background, "goals": goals,
            "created": datetime.now().isoformat(),
            "decisions": [],  # 决策记录
            "relationships": {},  # {char_id: "关系描述"}
        }
        self.save("characters", chars)

    def add_decision(self, char_id, context, decision, reasoning, impact=""):
        """记录人物在关键时刻的决策"""
        chars = self.load("characters")
        if char_id in chars:
            entry = {
                "context": context, "decision": decision,
                "reasoning": reasoning, "impact": impact,
                "timestamp": datetime.now().isoformat(),
            }
            chars[char_id]["decisions"].append(entry)
            self.save("characters", chars)

    def update_relationship(self, char_a, char_b, description):
        """更新人物关系"""
        chars = self.load("characters")
        if char_a in chars:
            chars[char_a]["relationships"][char_b] = {
                "description": description,
                "updated": datetime.now().isoformat(),
            }
            self.save("characters", chars)

    # === 剧情 → 人物心理预测 ===
    def predict_character_response(self, char_id, situation):
        """基于人物性格预测人物在情境中的反应"""
        chars = self.load("characters")
        if char_id not in chars:
            return None
        c = chars[char_id]
        return {
            "name": c["name"],
            "traits": c["traits"],
            "likely_action": f"根据{c['traits']}性格，面对「{situation}」可能...",
            "prior_decision_pattern": self._get_decision_pattern(chars, char_id),
        }

    def _get_decision_pattern(self, chars, char_id):
        """分析人物的决策模式"""
        if char_id not in chars:
            return ""
        decisions = chars[char_id].get("decisions", [])
        if not decisions:
            return "暂无决策记录可分析"
        recent = decisions[-3:]
        return " | ".join(f"[{d['context']}→{d['decision']}]" for d in recent)

    # === 剧情 ===
    def add_plot_event(self, event_id, title, description, chapter, characters_involved, impact=""):
        events = self.load("plot_events")
        events[event_id] = {
            "id": event_id, "title": title, "description": description,
            "chapter": chapter, "characters": characters_involved,
            "impact": impact, "timestamp": datetime.now().isoformat(),
        }
        self.save("plot_events", events)

    def get_arc(self, character_id=None):
        """获取剧情弧线"""
        events = self.load("plot_events")
        if not events:
            return []
        sorted_events = sorted(events.values(), key=lambda e: e.get("chapter", 0))
        if character_id:
            return [e for e in sorted_events if character_id in e.get("characters", [])]
        return sorted_events

    # === 写作记录 ===
    def log_work(self, phase, input_text, output_text, notes=""):
        """记录一次工作会话"""
        logs = self.load("work_log")
        if not isinstance(logs, list):
            logs = []
        logs.append({
            "phase": phase, "input": input_text[:200],
            "output": output_text[:200], "notes": notes,
            "timestamp": datetime.now().isoformat(),
        })
        self.save("work_log", logs)

    # === 统计 ===
    def get_summary(self):
        """返回上下文摘要"""
        chars = self.load("characters")
        events = self.load("plot_events")
        logs = self.load("work_log") or []
        return {
            "characters": len(chars),
            "plot_events": len(events),
            "work_sessions": len(logs) if isinstance(logs, list) else 0,
            "total_decisions": sum(len(c.get("decisions", [])) for c in chars.values()),
        }

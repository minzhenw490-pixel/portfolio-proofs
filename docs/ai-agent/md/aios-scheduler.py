#!/usr/bin/env python3
"""aios — 个人 AI OS 调度器（77 专用）

用法：
  aios list           列出所有 Agent
  aios <role>         看某个 Agent 的角色卡
  aios flow           看工作流
  aios open           在访达里打开这个文件夹
  aios docs           列出给人看的文档
"""
import os, sys, glob, subprocess

BASE = os.path.expanduser("AI-Agent")
AGENTS = os.path.join(BASE, "agents")
DOCS = os.path.join(BASE, "docs")
ORDER = ["chief", "pm", "content", "ops", "research", "design", "tech", "growth", "review"]
TITLE = {
    "chief": "总调度 —— 判断类型、分派、汇总",
    "pm": "产品经理 —— 发现问题→验证→方案→PRD→数据验证",
    "content": "内容运营 —— 找问题→检查解释→做成内容→回收迭代",
    "ops": "Web3 运营 —— 活动/社群/内容/增长/复盘（按 77 模板）",
    "research": "调研 —— 用户/市场/竞品，结论可溯源",
    "design": "设计/交互 —— 页面结构 + 黑白线框",
    "tech": "技术可行性 —— 能不能做、多贵、什么坑",
    "growth": "增长运营 —— 漏斗/转化/指标/A-B + SEO 巡检与技术协作",
    "review": "挑刺 —— 定稿前找漏洞和风险",
}

FLOW = """
                 Chief Agent
                     │
              判断任务类型
                     │
   ┌──────────┬──────┴──────┬──────────┐
   ↓          ↓             ↓          ↓
PM Agent   Content      Ops Agent   Research
   │        Agent          │         Agent
   └──────────┴────────────┴──────────┘
                     ↓
            Design / Tech / Growth
                     ↓
              Review Agent（挑刺）
                     ↓
                 最终方案 → 77 确认
"""

def main():
    args = sys.argv[1:]
    if not args or args[0] in ("-h", "--help", "help"):
        print(__doc__); return
    cmd = args[0]
    if cmd == "list":
        print(f"\n个人 AI OS — {len(ORDER)} 个 Agent\n" + "─" * 50)
        for k in ORDER:
            print(f"  {k:9s} {TITLE[k]}")
        print("\n  aios <agent> 看角色卡 · aios flow 看流程 · aios open 打开文件夹\n")
        return
    if cmd == "flow":
        print(FLOW); return
    if cmd == "open":
        subprocess.run(["open", BASE]); print(f"已打开：{BASE}"); return
    if cmd == "docs":
        print(f"\n文档目录：{DOCS}\n")
        for f in sorted(os.listdir(DOCS)):
            print("  ", f)
        print()
        return
    path = os.path.join(AGENTS, f"{cmd}.md")
    if not os.path.exists(path):
        cand = [p for p in glob.glob(os.path.join(AGENTS, "*.md")) if cmd in p]
        if not cand:
            print(f"没有这个 Agent：{cmd}\n可用：{'、'.join(ORDER)}"); return
        path = cand[0]
    print(open(path, encoding="utf-8").read())

if __name__ == "__main__":
    main()

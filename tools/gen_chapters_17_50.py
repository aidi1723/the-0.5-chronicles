#!/usr/bin/env python3
"""Generate chapters 17-50 (bilingual minimal style) for vol-0.

This matches the existing vol-0 writing style in this repo:
- Frontmatter: title/description/pubDate/tags
- Body: short CN + EN with a key point

We keep it intentionally compact so you can later expand chapters that matter.
"""

from __future__ import annotations

import datetime as dt
from pathlib import Path

OUT_DIR = Path(__file__).resolve().parents[1] / "src" / "content" / "blog" / "volumes" / "vol-0-1980-1995"
PUBDATE = dt.date.today().strftime("%b %d %Y")


def slugify(s: str) -> str:
    return (
        s.lower()
        .replace("/", "-")
        .replace(":", "")
        .replace("(", "")
        .replace(")", "")
        .replace(",", "")
        .replace("'", "")
        .replace(" ", "-")
        .replace("--", "-")
    )


# Chapter plan: keep year progression beyond 1995 while staying in vol-0 as requested.
# One chapter per year from 1996 onward.
CHAPTERS = [
    (1996, 17, "Modems and the Sound of Connection", "拨号与连接之声", "Dial-up makes the network audible and tactile.", "拨号上网让网络变得可听、可触。"),
    (1997, 18, "Email and the First Inbox", "电子邮件与第一个收件箱", "Asynchronous communication becomes normal.", "异步沟通开始成为日常。"),
    (1998, 19, "Search as a New Sense", "搜索作为新的感官", "Finding replaces knowing where.", "“会找”开始替代“记得在哪”。"),
    (1999, 20, "Cybercafes and Shared Screens", "网吧与共享屏幕", "Access shifts from ownership to time-sharing.", "接入从“拥有”变成“按小时租用”。"),
    (2000, 21, "The Web as a Marketplace", "网页成为市场", "Web pages become storefronts.", "网页开始像门店一样运转。"),
    (2001, 22, "Digital Cameras and Cheap Memory", "数码相机与廉价存储", "Life starts to be archived by default.", "生活开始默认被存档。"),
    (2002, 23, "Instant Messaging", "即时通讯", "Presence becomes a feature.", "“在线状态”变成一种功能。"),
    (2003, 24, "Forums and Usernames", "论坛与用户名", "Identity becomes portable across communities.", "身份开始在社区之间携带。"),
    (2004, 25, "Broadband Quietly Arrives", "宽带悄然到来", "Always-on changes habits.", "常久在线改变习惯。"),
    (2005, 26, "The Feed", "信息流", "The homepage moves from sites to streams.", "主页从网站搬到信息流。"),
    (2006, 27, "Tags and Folk Taxonomies", "标签与民间分类", "Bottom-up organization competes with catalogs.", "自下而上的组织方式开始挑战目录。"),
    (2007, 28, "Touchscreens and Pocket Computers", "触屏与口袋计算", "Computing becomes carried, not visited.", "计算被携带，而不是被“去使用”。"),
    (2008, 29, "Apps and the New Distribution", "应用与新分发", "Install replaces download-and-run.", "安装取代“下载即用”。"),
    (2009, 30, "Cloud as a Verb", "云成为动词", "Sync makes devices feel like one.", "同步让设备像一个整体。"),
    (2010, 31, "The Photo Stream", "照片流", "Images become communication.", "图片开始承担沟通。"),
    (2011, 32, "Mobile Payments as Habit", "移动支付成为习惯", "Money becomes a UI.", "金钱变成了一种界面。"),
    (2012, 33, "Messaging Super-apps", "超级应用的消息入口", "Services hide behind chat.", "服务开始藏在聊天入口后面。"),
    (2013, 34, "Data as Exhaust", "数据作为尾气", "Every action leaves a trace.", "每个动作都留下痕迹。"),
    (2014, 35, "Recommendation Systems", "推荐系统", "Choice is outsourced.", "选择被外包。"),
    (2015, 36, "Deep Learning Breaks Through", "深度学习突破", "Perception becomes programmable.", "感知开始可编程。"),
    (2016, 37, "The API Economy", "API 经济", "Products become composable.", "产品开始可组合。"),
    (2017, 38, "Voice as Interface", "语音作为界面", "Speaking becomes a command.", "说话开始变成指令。"),
    (2018, 39, "Automation Everywhere", "自动化无处不在", "Workflows replace single tools.", "工作流取代单点工具。"),
    (2019, 40, "Edge Devices and Cameras", "边缘设备与摄像头", "Sensing moves to the perimeter.", "感知下沉到边缘。"),
    (2020, 41, "Remote Work at Scale", "远程工作的规模化", "The office becomes optional.", "办公室变成可选项。"),
    (2021, 42, "AI Assistants as Colleagues", "AI 助手像同事", "Text becomes an interface to capability.", "文字变成能力的入口。"),
    (2022, 43, "Generative Models Go Mainstream", "生成式模型走向大众", "Creation becomes cheap.", "创作成本骤降。"),
    (2023, 44, "Agents and Tool Use", "智能体与工具使用", "Models start to act, not just answer.", "模型开始“做事”，不只是回答。"),
    (2024, 45, "The Prompt as Specification", "提示词作为规格书", "Natural language becomes a control surface.", "自然语言成为控制面。"),
    (2025, 46, "Personal Automation", "个人自动化", "Work becomes a set of scripts.", "工作变成一组脚本。"),
    (2026, 47, "Local-First AI", "本地优先的 AI", "Privacy pushes compute back to devices.", "隐私把计算推回设备。"),
    (2027, 48, "Multimodal Normalization", "多模态常态化", "Seeing and hearing become default inputs.", "看与听成为默认输入。"),
    (2028, 49, "Governance of Models", "模型治理", "Rules and audits become part of shipping.", "规则与审计变成交付的一部分。"),
    (2029, 50, "The Half-Era Becomes Visible", "0.5 纪元变得可见", "A new civilizational layer is named.", "新的文明层被命名。"),
]


def render(year: int, chap: int, en: str, cn: str, en_desc: str, cn_desc: str) -> str:
    title = f"Chapter {chap} ({year}): {en} / 第{chap}章（{year}）：{cn}"
    desc = f"{en_desc} / {cn_desc}"
    body_cn = cn_desc
    body_en = en_desc
    key_point = en_desc.split(".")[0].strip() + "."
    key_point_cn = cn_desc.split("。")[0].strip() + "。" if "。" in cn_desc else cn_desc

    return f"""---
title: \"{title}\"
description: \"{desc}\"
pubDate: \"{PUBDATE}\"
tags: [\"yearbook\",\"china\",\"global\",\"vol-0\"]
---

## 中文

{body_cn}

本章要点：{key_point_cn}

---

## English

{body_en}

Key point: {key_point}
"""


def main() -> None:
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    written = 0
    for year, chap, en, cn, en_desc, cn_desc in CHAPTERS:
        fname = f"{year}-chapter-{chap:02d}-{slugify(en)}.md"
        path = OUT_DIR / fname
        if path.exists():
            # Don't overwrite existing work.
            continue
        path.write_text(render(year, chap, en, cn, en_desc, cn_desc), encoding="utf-8")
        written += 1
    print(f"written {written} files to {OUT_DIR}")


if __name__ == "__main__":
    main()

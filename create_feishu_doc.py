#!/usr/bin/env python3
"""
Create a comprehensive Feishu document for OpenClaw 7 Days course promotion
"""
import json
import subprocess
import urllib.request
import urllib.parse

# Get cookie from feishu CLI
result = subprocess.run(['feishu', 'cookie'], capture_output=True, text=True)
cookie = result.stdout.strip()

if not cookie:
    print("Error: Failed to get feishu cookie. Please run 'feishu login' first.")
    exit(1)

# Helper functions for building blocks
def heading(text, level=1):
    return {
        "type": "paragraph",
        "paragraph": {
            "elements": [{"type": "textRun", "textRun": {"text": text, "style": {}}}],
            "style": {"headingLevel": level}
        }
    }

def paragraph(text, bold=False, code_inline=False, italic=False):
    style = {}
    if bold: style["bold"] = True
    if code_inline: style["codeInline"] = True
    if italic: style["italic"] = True
    return {
        "type": "paragraph",
        "paragraph": {
            "elements": [{"type": "textRun", "textRun": {"text": text, "style": style}}],
            "style": {}
        }
    }

def bullet(text, bold_first=False):
    elements = []
    if bold_first:
        # Split text at first occurrence of ': ' or ' - '
        parts = text.split(': ', 1) if ': ' in text else text.split(' - ', 1)
        if len(parts) == 2:
            elements = [
                {"type": "textRun", "textRun": {"text": parts[0] + ': ', "style": {"bold": True}}},
                {"type": "textRun", "textRun": {"text": parts[1], "style": {}}}
            ]
        else:
            elements = [{"type": "textRun", "textRun": {"text": text, "style": {"bold": True}}}]
    else:
        elements = [{"type": "textRun", "textRun": {"text": text, "style": {}}}]
    
    return {
        "type": "paragraph",
        "paragraph": {
            "elements": elements,
            "style": {"list": {"type": "bullet", "indentLevel": 1}}
        }
    }

def numbered_item(text, number):
    return {
        "type": "paragraph",
        "paragraph": {
            "elements": [{"type": "textRun", "textRun": {"text": text, "style": {}}}],
            "style": {"list": {"type": "number", "indentLevel": 1, "number": number}}
        }
    }

def quote_text(text):
    return {
        "type": "paragraph",
        "paragraph": {
            "elements": [{"type": "textRun", "textRun": {"text": text, "style": {}}}],
            "style": {"quote": True}
        }
    }

# Build document blocks
blocks = []

# Title
blocks.append(heading("🚀 OpenClaw 7 Days 实战课程", 1))
blocks.append(paragraph(""))

# Subtitle / Tagline
blocks.append(paragraph("从零开始，掌握 AI Agent 开发与部署", italic=True))
blocks.append(paragraph(""))

# Course URL
blocks.append(paragraph("🖥️ 在线课程网站: https://openclaw-course-silk.vercel.app", bold=True))
blocks.append(paragraph(""))

# Separator using paragraph with underscore
blocks.append(paragraph("―――――――――――――――――――――――――――――――――――――――――"))
blocks.append(paragraph(""))

# Section: Course Introduction
blocks.append(heading("📖 课程介绍", 2))
blocks.append(paragraph("本课程面向希望掌握 OpenClaw 的开发者，通过 8 节实战课程，层层递进地学习 OpenClaw 的各项核心功能。"))
blocks.append(paragraph(""))

# Course Features
blocks.append(heading("✨ 课程特色", 3))
blocks.append(bullet("🛠️ 每节都有动手实战", True))
blocks.append(bullet("📚 真实的案例驱动", True))
blocks.append(bullet("🔰 从基础到生产部署", True))
blocks.append(bullet("📝 完整的命令示例", True))
blocks.append(bullet("🎯 面向生产环境的实战技能", True))
blocks.append(paragraph(""))

blocks.append(paragraph("―――――――――――――――――――――――――――――――――――――――"))
blocks.append(paragraph(""))

# Section: Course Outline
blocks.append(heading("📋 课程大纲（8节完整课程）", 2))
blocks.append(paragraph(""))

# Lesson 1
blocks.append(heading("Lesson 1: OpenClaw 基础与环境搭建", 3))
blocks.append(bullet("安装配置 OpenClaw 开发环境"))
blocks.append(bullet("理解 OpenClaw 架构与核心概念"))
blocks.append(bullet("运行第一个 Agent"))
blocks.append(bullet("掌握配置文件结构与 Doctor 检查"))
blocks.append(paragraph(""))

# Lesson 2
blocks.append(heading("Lesson 2: Agent 创建与管理", 3))
blocks.append(bullet("Agent 配置详解"))
blocks.append(bullet("多 Agent 架构设计"))
blocks.append(bullet("工具权限管理"))
blocks.append(bullet("Default Agent 与自定义 Agent"))
blocks.append(paragraph(""))

# Lesson 3
blocks.append(heading("Lesson 3: 渠道集成配置", 3))
blocks.append(bullet("飞书渠道接入与配置"))
blocks.append(bullet("Telegram Bot 集成"))
blocks.append(bullet("微信公众号集成"))
blocks.append(bullet("多渠道消息路由"))
blocks.append(paragraph(""))

# Lesson 4
blocks.append(heading("Lesson 4: Skills 技能系统", 3))
blocks.append(bullet("Skills 架构深度解析"))
blocks.append(bullet("使用内置 Skills（git-master, playwright等）"))
blocks.append(bullet("创建自定义 Skill"))
blocks.append(bullet("SKILL.md 编写规范"))
blocks.append(paragraph(""))

# Lesson 5
blocks.append(heading("Lesson 5: 记忆与上下文管理", 3))
blocks.append(bullet("Memory 系统架构"))
blocks.append(bullet("混合搜索实现"))
blocks.append(bullet("上下文压缩策略"))
blocks.append(bullet("知识图谱构建"))
blocks.append(paragraph(""))

# Lesson 6
blocks.append(heading("Lesson 6: MCP 工具集成", 3))
blocks.append(bullet("MCP 架构与协议"))
blocks.append(bullet("配置 MCP 服务器"))
blocks.append(bullet("创建自定义 MCP 工具"))
blocks.append(bullet("MCP 与 Skill 的协同"))
blocks.append(paragraph(""))

# Lesson 7
blocks.append(heading("Lesson 7: 自定义工作流", 3))
blocks.append(bullet("工作流编排设计"))
blocks.append(bullet("并行任务执行"))
blocks.append(bullet("条件分支与错误处理"))
blocks.append(bullet("工作流状态管理"))
blocks.append(paragraph(""))

# Lesson 8
blocks.append(heading("Lesson 8: 生产部署与运维", 3))
blocks.append(bullet("Docker 容器化部署"))
blocks.append(bullet("监控告警配置"))
blocks.append(bullet("高可用架构设计"))
blocks.append(bullet("故障排查与日志管理"))
blocks.append(paragraph(""))

blocks.append(paragraph("―――――――――――――――――――――――――――――――――――――――"))
blocks.append(paragraph(""))

# Section: Learning Path
blocks.append(heading("🗺️ 学习路径", 2))
blocks.append(paragraph(""))
blocks.append(paragraph("Lesson 1 → Lesson 2 → Lesson 3 → Lesson 4 → Lesson 5 → Lesson 6 → Lesson 7 → Lesson 8"))
blocks.append(paragraph(""))
blocks.append(bullet("基础概念 → Agent管理 → 渠道集成 → Skills系统 → 记忆管理 → MCP扩展 → 工作流编排 → 生产部署"))
blocks.append(paragraph(""))

blocks.append(paragraph("―――――――――――――――――――――――――――――――――――――――"))
blocks.append(paragraph(""))

# Section: Technical Stack
blocks.append(heading("🧰 技术栈与工具", 2))
blocks.append(paragraph(""))
blocks.append(bullet("OpenClaw CLI - AI Agent 开发框架"))
blocks.append(bullet("Node.js 18+ 运行环境"))
blocks.append(bullet("Next.js 14 课程网站框架"))
blocks.append(bullet("Tailwind CSS 样式方案"))
blocks.append(bullet("MDX 内容管理系统"))
blocks.append(bullet("Docker 容器化部署"))
blocks.append(bullet("GitHub Issues 互动反馈"))
blocks.append(paragraph(""))

blocks.append(paragraph("―――――――――――――――――――――――――――――――――――――――"))
blocks.append(paragraph(""))

# Section: Target Audience
blocks.append(heading("🎯 适合人群", 2))
blocks.append(paragraph(""))
blocks.append(bullet("希望掌握 AI Agent 开发的工程师"))
blocks.append(bullet("想要构建生产级 AI 应用的开发者"))
blocks.append(bullet("对 OpenClaw 框架感兴趣的爱好者"))
blocks.append(bullet("需要集成多渠道 AI 服务的团队"))
blocks.append(paragraph(""))

# Prerequisites
blocks.append(heading("📝 前置要求", 3))
blocks.append(bullet("Node.js 18+ 基础"))
blocks.append(bullet("基本命令行操作能力"))
blocks.append(bullet("基本编程概念理解"))
blocks.append(paragraph(""))

blocks.append(paragraph("―――――――――――――――――――――――――――――――――――――――"))
blocks.append(paragraph(""))

# Section: Why Choose This Course
blocks.append(heading("💎 为什么选择 OpenClaw 7 Days？", 2))
blocks.append(paragraph(""))
blocks.append(bullet("🎓 系统化学习路径 - 从入门到精通的完整知识体系"))
blocks.append(bullet("💼 实战导向 - 每节课都有可运行的代码示例"))
blocks.append(bullet("🔧 生产级内容 - 不仅教使用，更教部署和运维"))
blocks.append(bullet("🌐 多渠道集成 - 覆盖飞书、Telegram、微信等主流平台"))
blocks.append(bullet("📖 开源免费 - 课程内容和代码全部开源"))
blocks.append(bullet("🚀 持续更新 - 跟随 OpenClaw 最新版本迭代"))
blocks.append(paragraph(""))

blocks.append(paragraph("―――――――――――――――――――――――――――――――――――――――"))
blocks.append(paragraph(""))

# Section: Resources
blocks.append(heading("🔗 参考资源", 2))
blocks.append(paragraph(""))
blocks.append(bullet("课程网站: https://openclaw-course-silk.vercel.app"))
blocks.append(bullet("OpenClaw 官方文档: https://opencode.ai"))
blocks.append(bullet("OpenClaw GitHub: https://github.com/openclaw"))
blocks.append(bullet("课程源码: https://github.com/zackzhangkai/openclaw-course-website"))
blocks.append(bullet("飞书课程资料: https://my.feishu.cn/wiki/UPV2w9QfdijAJVkL4fqcj8SMnzf"))
blocks.append(paragraph(""))

# Interactive Section
blocks.append(heading("💬 互动与反馈", 3))
blocks.append(bullet("课程问题与讨论：GitHub Issues"))
blocks.append(bullet("发现问题？欢迎提交 Issue"))
blocks.append(bullet("觉得有帮助？给个 Star！"))
blocks.append(paragraph(""))

blocks.append(paragraph("―――――――――――――――――――――――――――――――――――――――"))
blocks.append(paragraph(""))

# Section: Call to Action
blocks.append(heading("🎉 立即开始你的 AI Agent 开发之旅！", 2))
blocks.append(paragraph(""))
blocks.append(quote_text("掌握 OpenClaw，构建下一代 AI Agent 应用"))
blocks.append(paragraph(""))
blocks.append(paragraph("🚀 访问课程网站开始学习: https://openclaw-course-silk.vercel.app", bold=True))
blocks.append(paragraph(""))
blocks.append(paragraph("📅 版本: v1.0  |  📝 更新日期: 2026-04-28  |  👨‍🏫 作者: OpenClaw Training Team"))
blocks.append(paragraph(""))

# Create the document
doc_title = "OpenClaw 7 Days - AI Agent 开发实战课程"

content = {
    "title": {"elements": [{"type": "textRun", "textRun": {"text": doc_title, "style": {}}}]},
    "body": {"blocks": blocks}
}

payload = {
    "title": doc_title,
    "Content": json.dumps(content, ensure_ascii=False)
}

headers = {
    'Content-Type': 'application/json',
    'Cookie': cookie,
    'Referer': 'https://www.feishu.cn/space/',
    'Origin': 'https://www.feishu.cn'
}

try:
    req = urllib.request.Request(
        'https://www.feishu.cn/space/api/doc/create',
        data=json.dumps(payload, ensure_ascii=False).encode('utf-8'),
        headers=headers,
        method='POST'
    )
    
    with urllib.request.urlopen(req, timeout=30) as resp:
        data = json.loads(resp.read().decode('utf-8'))
        
    print("=" * 60)
    print("✅ 文档创建成功！")
    print("=" * 60)
    print(json.dumps(data, indent=2, ensure_ascii=False))
    print("=" * 60)
    
    if 'data' in data and 'url' in data['data']:
        print("\n📄 文档链接:")
        print(data['data']['url'])
        print("\n请复制链接在浏览器中打开，查看完整文档内容。")
        print("然后你可以将内容复制到你的 wiki 页面:")
        print("https://my.feishu.cn/wiki/UPV2w9QfdijAJVkL4fqcj8SMnzf")
    
except urllib.error.HTTPError as e:
    print(f"HTTP Error {e.code}: {e.reason}")
    print(e.read().decode('utf-8'))
except Exception as e:
    print(f"Error: {e}")

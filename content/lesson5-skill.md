# 第五节：Skill 系统与自定义技能

## 学习目标
- 理解 Hermes Skill 系统
- 创建自定义Skill
- 掌握Skill 协议

---

## Skill 架构

```
┌─────────────────────────────────────────────────────┐
│              Hermes Skill 系统                        │
├─────────────────────────────────────────────────────┤
│                                             │
│  Skill 来源：                                 │
│  ┌─────────────────────────────────────────┐   │
│  │ 1. 内置 Skill (100+)                    │   │
│  │ 2. 自动学习 Skill (运行时生成)           │   │
│  │ 3. 自定义 Skill (用户创建)              │   │
│  │ 4. Hub 下载 (hermes-agent/hub)         │   │
│  └─────────────────────────────────────────┘   │
│                                             │
│  Skill 结构：                                │
│  ┌─────────────────────────────────────────┐   │
│  │ skill.yaml (元数据)                      │   │
│  │ prompts/ (提示词)                        │   │
│  │ tools/ (工具)                          │   │
│  │ scripts/ (脚本)                        │   │
│  └─────────────────────────────────────────┘   │
└─────────────────────────────────────────────┘
```

---

## 动手实战

### 实战 5.1：查看可用 Skill

```bash
# 列出所有 Skill
hermes skill list

# 搜索 Skill
hermes skill search git

# 查看 Skill 详情
hermes skill info code_review
```

### 实战 5.2：创建自定义 Skill

```bash
mkdir -p ~/.hermes/skills/my-custom-skill
cd ~/.hermes/skills/my-custom-skill
```

创建 `skill.yaml`：

```yaml
name: my-custom-skill
description: "自定义技能描述"
version: "1.0.0"
author: your_name
tags:
  - custom
  - example

triggers:
  - "我的自定义任务"

prompt: |
  你是一个自定义技能助手。
  当用户触发这个技能时，执行以下任务：
  1. 理解用户需求
  2. 执行相应操作
  3. 返回结果
```

### 实战 5.3：使用 Skill

```bash
# 激活 Skill
hermes skill use my-custom-skill

# 列出已激活
hermes skill active
```

### 实战 5.4：从 Hub 安装 Skill

```bash
# 搜索
hermes skill install code_review

# 更新
hermes skill update code_review
```

---

## Skill 触发规则

| 触发方式 | 示例 |
|---------|------|
| 关键词 | "帮我整理代码" → `code-organizer` |
| 正则 | `/^review (.*)/` → `code-review` |
| 工具 | 使用特定工具时自动激活 |

---

## 课后作业

1. - [ ] 查看 3 个内置 Skill
2. - [ ] 创建自定义 Skill
3. - [ ] 测试 Skill 触发
4. - [ ] 从 Hub 安装 Skill

---

## 下节预告

下一节我们将学习 **Gateway API**，
实现 HTTP 接口暴露。
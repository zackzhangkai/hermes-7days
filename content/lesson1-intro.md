# 第一节：Hermes Agent 基础与环境搭建

## 学习目标
- 理解 Hermes Agent 架构与核心概念
- 完成开发环境安装
- 运行第一个 Agent

## 核心概念

![Hermes Agent 架构图](/images/hermes-architecture.png)

> 架构图源文件：`/docs/hermes-architecture.drawio`（可用 draw.io 编辑）

**核心概念说明：**

| 概念 | 说明 |
|--------|------|
| **Hermes Agent** | Nous Research 开源的 AI Agent 框架，持久化运行 |
| **Provider** | 模型提供商（OpenRouter、Anthropic、DeepSeek 等 18+） |
| **Skill** | 可复用技能模块，运行时自动学习 |
| **Memory** | 跨会话持久记忆（MEMORY.md + USER.md） |
| **Channel** | 消息通道（Telegram、Discord、Slack 等 15+） |
| **Gateway** | HTTP API 网关 |
| **Cron** | 定时任务调度 |

---

## 动手实战

### 实战 1.1：安装 Hermes Agent

```bash
# 检查环境
python3 --version  # 要求 3.10+
pip --version

# 安装 Hermes
pip install hermes-ai

# 验证安装
hermes --version

# 初始化
hermes setup
```

### 实战 1.2：查看配置结构

```bash
# 查看主配置文件
cat ~/.hermes/config.yaml

# 查看目录结构
ls -la ~/.hermes/
```

**配置文件结构解析：**

```yaml
meta:
  version: "2026.5.x"

models:
  defaults:
    provider: openrouter
    model: anthropic/claude-sonnet-4-20250514

providers:
  openrouter:
    api_key: ${OPENROUTER_API_KEY}
  
  anthropic:
    api_key: ${ANTHROPIC_API_KEY}

channels:
  enabled:
    - terminal
```

### 实战 1.3：运行 Doctor 检查

```bash
# 运行健康检查
hermes doctor

# 输出示例：
# ✓ Python 3.10+
# ✓ Hermes installed
# ✓ Config file exists
# ✓ 1 provider configured
# ✓ 0 channels enabled
```

### 实战 1.4：配置第一个模型（免费方案）

```bash
hermes config edit
```

在 `providers` 中添加：

```yaml
providers:
  openrouter:
    api_key: ${OPENROUTER_API_KEY}
    # 免费模型列表：
    # - google/gemini-2.0-flash
    # - deepseek/deepseek-chat
    # - anthropic/claude-3-haiku
```

---

## 案例：运行你的第一个对话 Agent

```bash
# 启动交互式会话
hermes chat

# 输入测试消息
> 你好，请介绍一下你自己
```

**预期输出：**
```
你好！我是 Hermes Agent，
一个开源的 AI Agent 框架。
我可以帮你完成各种任务，
有什么可以帮你的吗？
```

---

## 课后作业

1. - [ ] 完成 Hermes 安装
2. - [ ] 运行 `hermes doctor` 通过所有检查
3. - [ ] 找到并阅读你的 `config.yaml` 配置文件
4. - [ ] 配置一个免费模型提供商
5. - [ ] 成功运行 `hermes chat` 并完成一次对话

---

## 知识卡片

```
┌─────────────────────────────────────────┐
│  Hermes 核心文件位置                   │
├─────────────────────────────────────────┤
│  主配置:  ~/.hermes/config.yaml      │
│  Agent:  ~/.hermes/agents/            │
│  Skills: ~/.hermes/skills/             │
│  Memory: ~/.hermes/memory/           │
│  Logs:   ~/.hermes/logs/            │
│  Cron:   ~/.hermes/cron/             │
└─────────────────────────────────────────┘
```

---

## 下节预告

下一节我们将学习 **Provider 配置与模型选择**，
掌握 18+ 提供商的配置方法。
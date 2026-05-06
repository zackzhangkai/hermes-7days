# 第二节：Provider 配置与模型选择

## 学习目标
- 掌握 18+ 模型提供商的配置方法
- 理解 API 模式与运行时
- 实现模型 Failover

---

## Provider 架构

```
┌─────────────────────────────────────────────────────┐
│              Provider 运行时架构                    │
├─────────────────────────────────────────────────────┤
│                                             │
│   ┌─────────┐    ┌─────────┐    ┌─────────┐  │
│   │ OpenAI  │    │Anthropic│    │ Open   │  │
│   │Client  │    │Client  │    │Router  │  │
│   └────┬──┘    └────┬──┘    └──┬──┘  │
│        │             │           │          │
│        └──────────┬──────────┘          │
│                 ▼                         │
│         ┌─────────────┐                  │
│         │ Provider  │                  │
│         │ Resolver  │                  │
│         └────┬────┘                  │
│              ▼                       │
│         ┌─────────────┐                  │
│         │ API Mode  │                  │
│         │ (3种)    │                  │
│         └──────────┘                  │
└─────────────────────────────────────────────┘
```

支持的 API 模式：

| API 模式 | 用途 | 客户端 |
|---------|------|--------|
| `chat_completions` | OpenAI 兼容端点 | `openai.OpenAI` |
| `codex_responses` | OpenAI Codex | `openai.OpenAI` |
| `anthropic_messages` | Anthropic 原生 | `anthropic.Anthropic` |

---

## 动手实战

### 实战 2.1：配置 OpenRouter（推荐免费方案）

```bash
# 获取 API Key: https://openrouter.ai/keys
export OPENROUTER_API_KEY="sk-or-..."

# 运行时指定
hermes chat --provider openrouter --model google/gemini-2.0-flash
```

### 实战 2.2：配置 Anthropic（原生）

```bash
export ANTHROPIC_API_KEY="sk-ant-..."

hermes chat --provider anthropic --model claude-sonnet-4-20250514
```

### 实战 2.3：配置自定义 Provider

```yaml
providers:
  custom:
    base_url: "https://api.example.com/v1"
    api_key: ${CUSTOM_API_KEY}
    api_mode: chat_completions

# 使用自定义
hermes chat --provider custom --model my-model
```

### 实战 2.4：配置 Failover

```yaml
models:
  defaults:
    provider: openrouter
    model: anthropic/claude-sonnet-4-20250514
    fallback:
      provider: openrouter
      model: deepseek/deepseek-chat
```

---

## 免费模型推荐

| Provider | 模型 | 推荐场景 |
|---------|------|---------|
| OpenRouter | `google/gemini-2.0-flash` | 通用对话 |
| OpenRouter | `deepseek/deepseek-chat` | 代码任务 |
| OpenRouter | `anthropic/claude-3-haiku` | 快速响应 |
| Google | `gemini-2.5-pro-preview` | 长上下文 |
| DeepSeek | `deepseek-coder` | 编程任务 |

---

## 课后作业

1. - [ ] 配置 OpenRouter 并获取免费 API Key
2. - [ ] 测试 3 个不同模型
3. - [ ] 配置 Failover 机制
4. - [ ] 理解 API 模式差异

---

## 下节预告

下一节我们将学习 **Memory 持久化系统**，
掌握跨会话记忆管理。
# 第三节：Memory 持久化与跨会话记忆

## 学习目标
- 理解 Hermes Memory 系统
- 掌握跨会话记忆管理
- 理解自动学习机制

---

## Memory 系统架构

```
┌─────────────────────────────────────────────────────┐
│              Hermes Memory 系统                       │
├─────────────────────────────────────────────────────┤
│                                             │
│  ┌─────────────┐    ┌─────────────┐              │
│  │ MEMORY.md  │ +  │ USER.md    │              │
│  │ (Agent)   │    │ (User)    │              │
│  └─────┬─────┘    └─────┬─────┘              │
│        │               │                      │
│        └───────┬───────┘                      │
│                ▼                           │
│         ┌─────────────┐                      │
│         │ Context   │                      │
│         │ Engine   │                      │
│         └────┬────┘                       │
│              ▼                            │
│         ┌─────────────┐                      │
│         │ Context    │                      │
│         │ Compressor │                      │
│         └──────────┬──┘                       │
│                  ▼                        │
│           ┌────────────┐                  │
│           │ FTS5     │                  │
│           │ Index    │                  │
│           └──────────┘                  │
└─────────────────────────────────────────┘
```

Memory 文件类型：

| 文件 | 说明 | 自动更新 |
|------|------|--------|
| `MEMORY.md` | Agent 记忆 | Yes |
| `USER.md` | 用户信息 | No |
| `SKILLS.md` | 学到的技能 | Yes |
| `SESSION.md` | 会话历史 | No |

---

## 动手实战

### 实战 3.1：查看 Memory

```bash
# 查看根 Memory
cat ~/.hermes/memory/MEMORY.md

# 查看用户 Memory
cat ~/.hermes/memory/USER.md
```

### 实战 3.2：手动更新 Memory

```bash
# 添加用户信息
cat >> ~/.hermes/memory/USER.md << 'EOF'

## 用户偏好
- 偏好 Python > TypeScript
- 常用框架: React, Next.js

## 项目
- personal-ai: AI 相关项目
- trading-bot: 交易机器人
EOF
```

### 实战 3.3：配置 Memory 刷新策略

```yaml
agents:
  defaults:
    memory:
      flush_threshold: 0.8  # 80% context 时刷新
      reserve_tokens: 5000       # 保留 tokens
      auto_save: true
```

### 实战 3.4：搜索 Memory

```bash
# 搜索历史会话
hermes memory search "上次那个 bug"

# 列出最近会话
hermes memory sessions
```

---

## 自动学习机制

Hermes 会自动提取重复模式生成 Skill：

```
┌─────────────────────────────────┐
│     学习循环流程                │
├─────────────────────────────────┤
│                                 │
│  1. 观察重复行为              │
│         ↓                       │
│  2. 提取模式                  │
│         ↓                       │
│  3. 生成 Skill               │
│         ↓                       │
│  4. 保存到 skills/            │
│         ↓                       │
│  5. 下次自动使用             │
└─────────────────────────────────┘
```

---

## 课后作业

1. - [ ] 查看你的 MEMORY.md 内容
2. - [ ] 更新 USER.md 个人信息
3. - [ ] 配置 Memory 刷新策略
4. - [ ] 搜索历史会话

---

## 下节预告

下一节我们将学习 **Channel 消息通道**，
配置 Telegram、Discord 等 15+ 消息平台。
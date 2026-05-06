# 第四节：Channel 消息通道配置

## 学习目标
- 配置 15+ 消息平台
- 实现跨平台消息收发
- 掌握 Channel 协议

---

## Channel 架构

```
┌─────────────────────────────────────────────────────┐
│              Hermes Channel 系统                      │
├─────────────────────────────────────────────────────┤
│                                             │
│  ┌──────────────────────────────────────────┐   │
│  │              Channel Manager             │   │
│  └──────────────────┬───────────────────────┘   │
│                     ▼                            │
│   ┌──────┬──────┬──────┬──────┬──────┐          │
│   │ Term │ Teleg │ Discd│Slack│ email│   │
│   │ inal│ ram  │cord  │    │     │          │
│   └──┴──┴──┴──┴──┴──┴─────────────────────┘
│                                             │
│          支持平台：                          │
│   • Terminal    • Telegram   • Discord     │
│   • Slack      • WhatsApp    • Email       │
│   • Feishu    • Webhook     • Matrix     │
│   • SMS       • Custom                    │
└─────────────────────────────────────────┘
```

---

## 动手实战

### 实战 4.1：配置 Telegram

```bash
# 获取 Bot Token: @BotFather
export TELEGRAM_BOT_TOKEN="123456:ABC-DEF"

# 添加到配置
hermes config edit
```

```yaml
channels:
  enabled:
    - terminal
    - telegram

telegram:
  bot_token: ${TELEGRAM_BOT_TOKEN}
  allowed_users:
    - your_user_id
```

```bash
# 测试
hermes channel test telegram
```

### 实战 4.2：配置 Discord

```yaml
discord:
  bot_token: ${DISCORD_BOT_TOKEN}
  app_id: ${DISCORD_APP_ID}
  guilds:
    - guild_id
```

### 实战 4.3：配置 Slack

```yaml
slack:
  bot_token: ${SLACK_BOT_TOKEN}
  app_id: ${SLACK_APP_ID}
  signing_secret: ${SLACK_SIGNING_SECRET}
```

### 实战 4.4：配置 Email

```yaml
email:
  smtp_host: smtp.gmail.com
  smtp_port: 587
  smtp_user: ${EMAIL_USER}
  smtp_pass: ${EMAIL_PASS}
  from: hermes@example.com
```

---

## 常用 Channel 命令

```bash
# 测试所有 Channel
hermes channel test

# 查看 Channel 状态
hermes channel status

# 发送测试消息
hermes channel send telegram "Test message"
```

---

## 课后作业

1. - [ ] 配置一个消息平台（Telegram/Discord）
2. - [ ] 测试消息收发
3. - [ ] 配置允许用户列表
4. - [ ] 理解 Channel 协议

---

## 下节预告

下一节我们将学习 **Skill 系统**，
掌握可复用技能模块的创建与使用。
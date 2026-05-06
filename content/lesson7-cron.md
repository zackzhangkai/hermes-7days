# 第七节：Cron 定时任务与自动化调度

## 学习目标
- 配置 Cron 任务
- 实现自动化调度
- 掌握任务管理

---

## Cron 系统架构

```
┌─────────────────────────────────────────────────────┐
│              Hermes Cron 系统                        │
├─────────────────────────────────────────────────────┤
│                                             │
│   ┌─────────────────────────────────────┐     │
│   │         Cron Scheduler               │     │
│   │   (后台守护进程)                  │     │
│   └─────────────┬───────────────────────┘     │
│               ▼                           │
│   ┌───────────────────────────────┐     │
│   │         Job Queue            │     │
│   ├───────────────────────┤     │
│   │  job_1: */5 * * * *  │     │
│   │  job_2: 0 0 * * *   │     │
│   │  job_3: @daily      │     │
│   └───────────────────────┘     │
│               │                           │
│               ▼                           │
│   ┌───────────────────────────────┐     │
│   │       AIAgent 执行          │     │
│   └───────────────────────┘     │
│                                             │
└─────────────────────────────────────────────┘
```

---

## 动手实战

### 实战 7.1：创建 Cron 任务

```bash
# 交互式创建
hermes cron create

# 手动创建
cat > ~/.hermes/cron/daily-report.yaml << 'EOF'
name: daily-report
description: "每日报告生成"
schedule: "0 9 * * *"
command: |
  1. 获取当日统计数据
  2. 生成报告
  3. 发送到指定 Channel
timezone: Asia/Shanghai
enabled: true
EOF
```

### 实战 7.2：管理 Cron 任务

```bash
# 列出所有任务
hermes cron list

# 启用/禁用
hermes cron enable daily-report
hermes cron disable daily-report

# 手动运行
hermes cron run daily-report
```

### 实战 7.3：常见 Cron 表达式

| 表达式 | 说明 |
|--------|------|
| `*/5 * * * *` | 每 5 分钟 |
| `0 * * * *` | 每小时 |
| `0 9 * * *` | 每天 9 点 |
| `0 9 * * 1-5` | 工作日 9 点 |
| `0 9 1 * *` | 每月 1 号 |
| `@hourly` | 每小时 |
| `@daily` | 每天 |

### 实战 7.4：配置任务输出

```yaml
output:
  channel: telegram
  to: chat_id
  
  # 或 Email
  email:
    to: user@example.com
    subject: "Cron Report"
  
  # 或保存文件
  file:
    path: ~/reports/{date}.md
```

---

## 多 Agent 调度

```yaml
profiles:
  - name: coder
    system_prompt: "你是一个专业程序员"
    model: anthropic/claude-sonnet-4-20250514
    
  - name: researcher
    system_prompt: "你是一个研究员"
    model: openrouter/anthropic/claude-sonnet-4-20250514
```

---

## 课后作业

1. - [ ] 创建每日任务
2. - [ ] 配置任务输出
3. - [ ] 测试手动运行
4. - [ ] 配置多 Agent

---

## ��节预告

下一节我们将学习 **生产部署与运维**，
实现高可用部署。
# 第六节：Gateway API 与 HTTP 接口

## 学习目标
- 启动 Hermes Gateway
- 配置 API 端点
- 实现 Webhook 集成

---

## Gateway 架构

```
┌─────────────────────────────────────────────────────┐
│              Hermes Gateway 架构                    │
├─────────────────────────────────────────────────────┤
│                                             │
│   ┌─────────────────────────────────────────┐  │
│   │         HTTP Server (FastAPI)            │  │
│   └──────────────────┬──────────────────┘  │
│                      ▼                        │
│   ┌────────────────────────────────────┐  │
│   │         Endpoints                   │  │
│   ├────────────────────────────────────┤  │
│   │  POST /chat        (消息对话)      │  │
│   │  POST /trigger    (触发任务)      │  │
│   │  GET  /status    (状态查询)      │  │
│   │  GET  /history   (历史记录)      │  │
│   │  POST /webhook  (Webhook)        │  │
│   └────────────────────────────────────┘  │
│                      ▼                        │
│              ┌─────────────┐                  │
│              │  AIAgent   │                  │
│              └───────────┘                  │
└─────────────────────────────────────────────┘
```

---

## 动手实战

### 实战 6.1：启动 Gateway

```bash
# 默认端口 8000
hermes gateway start

# 自定义端口
hermes gateway start --port 3000

# 生产模式
hermes gateway start --production --ssl
```

### 实战 6.2：API 调用

```bash
# 聊天
curl -X POST http://localhost:8000/chat \
  -H "Content-Type: application/json" \
  -d '{"message": "你好", "stream": false}'

# 触发任务
curl -X POST http://localhost:8000/trigger \
  -H "Content-Type: application/json" \
  -d '{"task": "run_build", "params": {}}'

# 查询状态
curl http://localhost:8000/status

# 历史记录
curl http://localhost:8000/history?limit=10
```

### 实战 6.3：配置认证

```yaml
gateway:
  auth:
    api_key: ${GATEWAY_API_KEY}
    # 或使用 JWT
    jwt_secret: ${JWT_SECRET}
  
  cors:
    allowed_origins:
      - "https://your-app.com"
```

### 实战 6.4：配置 Webhook

```yaml
webhook:
  enabled: true
  url: ${WEBHOOK_URL}
  events:
    - agent.start
    - agent.end
    - tool.called
    - error
```

---

## API 文档

启动后访问：`http://localhost:8000/docs`

---

## 课后作业

1. - [ ] 启动 Gateway
2. - [ ] 调用 /chat 端点
3. - [ ] 配置 API 认证
4. - [ ] 配置 Webhook

---

## 下节预告

下一节我们将学习 **Cron 定时任务**，
实现自动化调度。
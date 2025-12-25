# FastAPI 专家级学习路线 (Road to Expert)

这份路线图假设你已经具备扎实的 Python 基础（熟练掌握 Decorators, Generator, Context Manager, Type Hinting），旨在帮助你掌握 FastAPI 的深层原理、架构设计及生产级应用开发。

---

## 🧭 Phase 1: 核心原理深度解构 (Deep Dive)
不要只停留在 API 使用层面，掌握底层才能随心所欲。

### 1.1 Starlette & ASGI 机制
FastAPI 是基于 Starlette 构建的。
*   **ASGI (Asynchronous Server Gateway Interface)**: 理解 ASGI 协议标准 (`scope`, `receive`, `send`)，这是 Python 异步 Web 的基石。
*   **Starlette**: 学习 Starlette 的 Request/Response 对象，理解其路由匹配机制。
*   **Middleware**: 编写自定义 ASGI 中间件（处理 CORS, GZip, TrustedHost, 性能监控）。

### 1.2 Pydantic V2 深度应用
数据校验的核心。
*   **核心特性**: `Field`, `Alias`, `Computed Field`, `Model Config`。
*   **高级校验**: `AfterValidator`, `BeforeValidator`, `model_validator`。
*   **序列化**: `model_dump()`, `model_dump_json()`, 排除字段 (`exclude`), 别名导出 (`by_alias`)。
*   **Settings Management**: 使用 `pydantic-settings` 管理环境变量 (`.env`)。

### 1.3 异步编程 (AsyncIO) 避坑指南
*   **Event Loop**: 理解事件循环机制，避免在 `async def` 中运行阻塞代码（CPU密集型任务）。
*   **`run_in_executor`**: 如何正确地在 FastAPI 中调用同步库（如 Pandas, Pillow）。
*   **Concurrency**: 理解并发 (Concurrency) 与并行 (Parallelism) 的区别，合理配置 Workers。

---

## 🏗️ Phase 2: 工程架构设计 (Architecture)
告别单文件 `main.py`，构建可维护的大型应用。

### 2.1 高级依赖注入 (Dependency Injection)
*   **Yield Dependencies**: 用于数据库 Session 管理（Enter/Exit 模式）。
*   **Class-based Dependencies**: 将依赖封装为类，便于复用和测试。
*   **Sub-dependencies**: 依赖链的传递与缓存机制 (`use_cache=True`)。
*   **Overrides**: 在测试时覆盖依赖 (`app.dependency_overrides`)。

### 2.2 目录结构与分层架构
*   **模块化结构**: 按业务域划分 (`app/users`, `app/items`) 而非按技术层划分。
*   **Service Layer Pattern**: 引入服务层解耦 Controller (Router) 与 Data Access (CRUD)。
*   **Clean Architecture**: 探索如何在 Python 中落地整洁架构（虽不必教条，但需理解解耦思想）。

### 2.3 错误处理与日志
*   **Global Exception Handlers**: 接管所有异常，返回统一的 JSON 错误格式。
*   **Logging Config**: 配置结构化日志 (JSON Logs)，集成 Request ID 用于链路追踪。

---

## 💾 Phase 3: 数据层与中间件 (Data & Integration)
构建高性能、高可用的数据交互层。

### 3.1 SQLAlchemy 2.0 (Async)
*   **Modern Style**: 彻底放弃 1.x 的旧语法，全面拥抱 `select()`, `execute()`, `AsyncSession`。
*   **Relationship Loading**: 理解 Lazy Loading (在 Async 下是禁忌) vs Eager Loading (`subqueryload`, `selectinload`, `joinedload`)。
*   **Performance**: N+1 查询问题的识别与优化。

### 3.2 数据库迁移 (Alembic)
*   自动化生成迁移脚本。
*   处理复杂的 Schema 变更（如 Enum 类型变更, 数据迁移 Data Migration）。

### 3.3 缓存与限流 (Redis)
*   **Caching**: 使用 Redis 缓存热点数据，理解 Cache Invalidation 策略。
*   **Rate Limiting**: 使用 `fastapi-limiter` 实现基于 IP 或用户的 API 限流。
*   **Session Store**: 分布式 Session 存储。

---

## 🔐 Phase 4: 安全与异步任务 (Security & Background)
保障安全，提升响应速度。

### 4.1 认证与鉴权 (AuthN & AuthZ)
*   **OAuth2 / OIDC**: 理解标准流程，实现 JWT (JSON Web Tokens) 的签发、校验与刷新 (Refresh Token)。
*   **Scopes**: 基于 Scope 的细粒度权限控制。
*   **RBAC / ABAC**: 自定义 Depends 实现基于角色或属性的访问控制。

### 4.2 异步任务队列
*   **BackgroundTasks**: FastAPI 原生轻量级后台任务（适用于发邮件等简单任务）。
*   **Celery / Arq / Dramatiq**: 集成重量级任务队列（任务持久化、重试、定时任务）。
*   **Event Driven**: 初探消息队列 (RabbitMQ/Kafka) 解耦系统。

---

## 🚀 Phase 5: 生产级部署与运维 (DevOps)
从 `localhost` 到起飞。

### 5.1 Docker 最佳实践
*   **Multi-stage Builds**: 多阶段构建减小镜像体积。
*   **Distroless / Alpine**: 选择安全精简的基础镜像。
*   **Non-root User**: 容器安全最佳实践。

### 5.2 服务编排与部署
*   **Gunicorn**: 使用 Gunicorn 作为 Process Manager，Uvicorn 作为 Worker Class。
*   **Nginx**: 反向代理，处理 SSL 卸载、静态文件、负载均衡。
*   **Systemd**: 传统 Linux 部署方案。

### 5.3 可观测性 (Observability)
*   **Metrics**: 集成 Prometheus 暴露指标 (RPS, Latency)。
*   **Tracing**: 集成 OpenTelemetry 进行全链路追踪。
*   **Sentry**: 错误监控与报警。

---

## 📚 推荐资源 (Mastery Levels)

*   **Level 1 (熟练)**: [FastAPI Advanced User Guide](https://fastapi.tiangolo.com/advanced/) (官方文档进阶篇，必读)
*   **Level 2 (精通)**: [TestDriven.io FastAPI 博客](https://testdriven.io/blog/topics/fastapi/) (高质量深度文章)
*   **Level 3 (源码)**: 阅读 [Starlette 源码](https://github.com/encode/starlette) 和 [FastAPI 源码](https://github.com/fastapi/fastapi) (理解那些魔法是如何实现的)
*   **Level 4 (战神)**: 参与 FastAPI 或相关生态库的 Open Source 贡献。

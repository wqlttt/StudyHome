# FastAPI 学习路线

## 什么是 FastAPI

FastAPI 是一个用于构建 API 的现代、快速（高性能）的 Web 框架，建立在 **Pydantic** 和 **Starlette** 之上：
- **Pydantic**：基于 Python 类型提示，负责数据验证、序列化和文档生成
- **Starlette**：轻量级 ASGI 框架/工具包，提供高性能异步支持

---

## 第一阶段：前置知识（1-2 周）

### 1.1 Python 类型提示（Type Hints）
- 基本类型注解：`int`, `str`, `bool`, `float`
- 复合类型：`list[int]`, `dict[str, int]`, `tuple[str, int]`
- `Optional` 和 `Union` 的用法
- `TypedDict` 和 `NamedTuple`
- Python 3.10+ 新语法：`str | None`, `list[str | int]`

### 1.2 异步编程基础
- `async` / `await` 语法
- `asyncio` 事件循环
- 异步上下文管理器（`async with`）
- 理解协程 vs 线程 vs 进程的区别

### 1.3 HTTP & REST API 基础
- HTTP 方法：GET / POST / PUT / PATCH / DELETE
- 状态码含义：2xx / 3xx / 4xx / 5xx
- RESTful API 设计规范
- JSON 序列化与反序列化

### 1.4 Pydantic V2 基础
- `BaseModel` 定义数据模型
- `Field()` 添加校验规则
- 嵌套模型（Nested Models）
- `model_validate()` 和 `model_dump()`
- 常用类型：`EmailStr`, `HttpUrl`, `conint`, `constr`

---

## 第二阶段：FastAPI 核心（2-3 周）

### 2.1 第一个 FastAPI 应用
- 安装：`pip install "fastapi[standard]"`
- 创建 `FastAPI()` 实例
- 路径操作装饰器：`@app.get()`, `@app.post()` 等
- 运行：`fastapi dev main.py`（开发模式）/ `fastapi run main.py`（生产模式）

### 2.2 路径参数与查询参数
- 路径参数：`@app.get("/items/{item_id}")`
- 查询参数：`?page=1&size=10`
- 参数校验：`gt`, `ge`, `lt`, `le`, `min_length`, `max_length`
- 默认值与可选参数
- 枚举类型路径参数

### 2.3 请求体（Request Body）
- Pydantic 模型作为请求体
- 嵌套模型处理
- `Body()` 的额外校验
- 多请求体参数
- `model_dump()` 转换数据

### 2.4 响应处理
- 响应模型 `response_model` 过滤返回字段
- `response_model_exclude` / `response_model_include`
- 状态码设置 `status_code`
- 自定义响应头
- JSONResponse / HTMLResponse / FileResponse / RedirectResponse

### 2.5 依赖注入（Dependency Injection）
- `Depends()` 基本用法
- 函数依赖 vs 类依赖
- 依赖嵌套（依赖调用另一个依赖）
- `yield` 实现带清理的依赖（如数据库会话管理）
- 全局依赖 `app.add_middleware()` vs `dependencies` 参数

---

## 第三阶段：数据库与认证（2-3 周）

### 3.1 数据库集成
- SQLAlchemy 2.0 异步模式 + asyncpg（PostgreSQL）
- 数据库会话管理（依赖注入 + yield 模式）
- CRUD 操作封装
- Alembic 数据库迁移

### 3.2 用户认证
- JWT（JSON Web Token）认证流程
- `python-jose` 生成与验证 Token
- `OAuth2PasswordBearer` + `OAuth2PasswordRequestForm`
- 密码哈希：`passlib` + bcrypt
- Token 刷新机制（Refresh Token）
- 基于角色的权限控制（RBAC）

### 3.3 中间件与事件
- 自定义中间件（`@app.middleware("http")`）
- CORS 中间件配置
- 启动/关闭事件：`lifespan` 上下文管理器
- 请求日志、计时、限流中间件

---

## 第四阶段：项目实践（持续）

### 4.1 项目结构推荐
```
project/
├── app/
│   ├── __init__.py
│   ├── main.py              # FastAPI 入口
│   ├── config.py            # 配置管理（pydantic-settings）
│   ├── database.py          # 数据库引擎与会话
│   ├── models/              # SQLAlchemy 模型
│   ├── schemas/             # Pydantic 请求/响应模型
│   ├── routers/             # 路由模块（APIRouter）
│   ├── services/            # 业务逻辑层
│   ├── dependencies/        # 依赖注入
│   └── utils/               # 工具函数
├── alembic/                 # 数据库迁移
├── tests/                   # 测试
├── alembic.ini
├── pyproject.toml
└── .env
```

### 4.2 练习项目建议（由浅入深）
1. **TODO API** — 掌握 CRUD、路径参数、请求体
2. **用户认证系统** — 注册/登录/JWT/权限
3. **博客 API** — 一对多关联、分页、搜索、文件上传
4. **实时聊天** — WebSocket + Redis Pub/Sub

---

## 第五阶段：进阶主题（按需学习）

### 5.1 自动文档
- Swagger UI（`/docs`）与 ReDoc（`/redoc`）
- `summary`, `description`, `tags` 完善接口文档
- `response_description` 自定义
- 文档示例：`examples` 参数

### 5.2 性能优化
- 异步数据库查询（async SQLAlchemy）
- 后台任务：`BackgroundTasks`
- 更重的后台任务：Celery / ARQ
- Redis 缓存响应
- 数据库查询优化：selectinload、索引

### 5.3 WebSocket
- `@app.websocket()` 基本用法
- 连接管理与心跳检测
- 广播消息模式

### 5.4 文件处理
- `UploadFile` 上传文件
- 文件大小限制
- 静态文件挂载 `StaticFiles`
- 文件流式下载 `StreamingResponse`

### 5.5 测试
- `TestClient` (httpx) 编写集成测试
- `pytest` + `pytest-asyncio`
- Mock 外部依赖
- 测试数据库（创建/销毁临时库）
- 覆盖率：`pytest-cov`

### 5.6 部署
- Gunicorn + Uvicorn Worker 多进程部署
- Docker 容器化
- Nginx 反向代理
- 环境变量管理（`.env` + `pydantic-settings`）
- 健康检查端点

---

## 常用依赖速查

| 用途 | 推荐库 |
|------|--------|
| 数据库 ORM | `SQLAlchemy >= 2.0` + `asyncpg` |
| 数据库迁移 | `Alembic` |
| 数据校验 | `Pydantic >= 2.0` |
| 认证 | `python-jose` + `passlib[bcrypt]` |
| 配置管理 | `pydantic-settings` |
| HTTP 客户端 | `httpx` |
| 测试 | `pytest` + `httpx` |
| 异步任务队列 | `Celery` / `ARQ` |
| 缓存 | `redis-py` / `fastapi-cache2` |

---

## 学习资源

- [FastAPI 官方文档](https://fastapi.tiangolo.com/)
- [SQLAlchemy 2.0 文档](https://docs.sqlalchemy.org/en/20/)
- [Pydantic V2 文档](https://docs.pydantic.dev/latest/)
- [FastAPI Users](https://fastapi-users.github.io/fastapi-users/) — 即开即用的认证方案
- [Full Stack FastAPI Template](https://github.com/fastapi/full-stack-fastapi-template) — 官方模板

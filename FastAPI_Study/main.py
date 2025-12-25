from fastapi import FastAPI
from pydantic import BaseModel
from typing import List

# 创建 FastAPI 实例
app = FastAPI(title="FastAPI Learning Roadmap API")

# 1. 定义数据模型 (Pydantic Model)
# 这对应了路线图的【第二阶段：请求体与 Pydantic】
class Stage(BaseModel):
    name: str
    description: str
    duration: str
    topics: List[str]

# 2. 创建数据
# 这里我们将之前的路线图“放入”到了代码的数据结构中
learning_roadmap = [
    Stage(
        name="基础准备 (The Foundation)",
        description="打好 Python 和 Web 基础",
        duration="3-5 天",
        topics=["Python 核心语法 (Type Hints, Decorators)", "Web 基础 (HTTP, JSON)"]
    ),
    Stage(
        name="FastAPI 快速入门 (Quick Start)",
        description="跑通第一个 API，理解参数传递",
        duration="3-5 天",
        topics=["环境搭建", "路径参数", "查询参数", "Pydantic 模型"]
    ),
    Stage(
        name="进阶请求处理",
        description="掌握复杂的 API 交互场景",
        duration="1 周",
        topics=["文件上传", "Cookie/Headers", "错误处理"]
    ),
    Stage(
        name="数据库对接",
        description="持久化存储",
        duration="1-2 周",
        topics=["SQLModel/SQLAlchemy", "Alembic 迁移", "异步 SQL"]
    ),
    Stage(
        name="安全与认证",
        description="保护 API",
        duration="1 周",
        topics=["OAuth2", "JWT", "Password Hashing"]
    ),
     Stage(
        name="部署",
        description="上线生产环境",
        duration="1 周",
        topics=["Docker", "Gunicorn", "Nginx"]
    ),
]

# 3. 定义接口 (Path Operation)
# 访问 http://127.0.0.1:8000/ 会看到 Hello World
@app.get("/")
def read_root():
    return {"message": "Welcome to your FastAPI Learning Journey! Visit /docs to see the API."}

# 4. 返回路线图接口
# 访问 http://127.0.0.1:8000/roadmap 会返回上面的 JSON 数据
@app.get("/roadmap", response_model=List[Stage])
def get_roadmap():
    return learning_roadmap

# 5. 动态查询接口
# 练习：路径参数 (Path Parameters)
# 访问 http://127.0.0.1:8000/roadmap/1 获取第2阶段（索引从0开始）
@app.get("/roadmap/{stage_id}")
def get_stage_by_id(stage_id: int):
    if 0 <= stage_id < len(learning_roadmap):
        return learning_roadmap[stage_id]
    return {"error": "Stage not found"}

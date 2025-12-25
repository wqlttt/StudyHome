from fastapi import FastAPI, Body, HTTPException
from typing import List
from .models import UserCreate, UserResponse, ExternalUser

app = FastAPI(title="Lab 01: Pydantic V2 & Internals")

# 模拟数据库
fake_users_db = []

@app.post("/users", response_model=UserResponse)
async def create_user(user: UserCreate):
    """
    演示 Pydantic V2 的 model_validator 和 computed_field
    """
    new_user = UserResponse(
        id=len(fake_users_db) + 1,
        username=user.username,
        email=user.email
    )
    fake_users_db.append(new_user)
    return new_user

@app.post("/external-users", response_model=ExternalUser)
async def create_external_user(user: ExternalUser):
    """
    演示 Field Alias: 发送 {"id": 1, "name": "Alice"}
    """
    return user

@app.get("/users/alias-demo")
async def get_users_alias():
    """
    演示 Pydantic 序列化时的别名处理
    """
    user = ExternalUser(id=1, full_name="Bob")
    return {
        "by_alias": user.model_dump(by_alias=True), # 输出 {"id": 1, "name": "Bob"}
        "regular": user.model_dump()                # 输出 {"id": 1, "full_name": "Bob"}
    }

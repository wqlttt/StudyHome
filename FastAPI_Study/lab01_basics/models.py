from pydantic import BaseModel, Field, field_validator, model_validator, ComputedField, ConfigDict
from typing import Optional, List
from datetime import datetime

class UserBase(BaseModel):
    username: str = Field(min_length=3, max_length=50)
    email: str
    
    # Pydantic V2 Config
    model_config = ConfigDict(str_strip_whitespace=True)

class UserCreate(UserBase):
    password: str = Field(min_length=8)
    confirm_password: str = Field(min_length=8)

    # V2 Style Model Validator (Root Validator)
    @model_validator(mode='after')
    def check_passwords_match(self) -> 'UserCreate':
        if self.password != self.confirm_password:
            raise ValueError('Passwords do not match')
        return self

class UserResponse(UserBase):
    id: int
    created_at: datetime = Field(default_factory=datetime.now)
    
    # Computed Field (V2 Feature)
    @ComputedField
    @property
    def display_name(self) -> str:
        return f"{self.username} <{self.email}>"

class ExternalUser(BaseModel):
    """用于演示别名 (Alias) 和数据导出"""
    id: int
    full_name: str = Field(alias="name") # 接收 JSON 中的 "name" 字段
    
    model_config = ConfigDict(populate_by_name=True)

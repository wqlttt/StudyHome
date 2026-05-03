# Postgre SQL

## 什么是Postgre SQL

Postgre不仅是一个存储数据的仓库，他是一个对象-关系型数据库管理系统(ORDBMS)

- 关系型(Relational):他使用表，行，列来组织数据，支持标准的SQL查询
- 对象型(Object)： 他允许用户自定义数据类型，函数和操作符，甚至可以处理复杂的继承关系
- 可靠性：他具有极其健壮的数据处理能力（ACID特性），即使在电力中断或硬件故障时也能保证数据不丢失

# 核心特性

- 丰富的数据类型：除了数值和字符串，它原生支持JSONB（存储JSON数据并支持索引），地理信息（PostGIS），数组以及CIDR地址
- 并发控制（MVCC）：多版本并发控制确保了在读取数据时不会阻塞写入，在高并发环境下性能优异。
- 拓展性：可以安装想PostGIS（地图/空间数据），TimescaleDB（时许数据）或pgvector（向量数据库，用于AI检索）这样的插件
- 高级功能：支持窗口函数，公共表达式（CTE），全文搜索以及逻辑复制

# 基础操作入门

## A.创建数据库与表

```sql
-- 创建一个名为 project_db 的数据库
CREATE DATABASE project_db;

-- 切换到该数据库后创建表
CREATE TABLE users (
    id SERIAL PRIMARY KEY,           -- 自动递增的主键
    username VARCHAR(50) UNIQUE,     -- 唯一用户名
    email TEXT NOT NULL,             -- 必填邮箱
    created_at TIMESTAMP DEFAULT NOW() -- 默认当前时间
);
```

## B.数据的增删改查

Postgres的SQL语法非常标准：

```sql
-- 插入数据
INSERT INTO users (username, email) VALUES ('qiletian', 'example@edu.mo');

-- 查询（带过滤）
SELECT * FROM users WHERE username = 'qiletian';

-- 更新
UPDATE users SET email = 'new_email@edu.mo' WHERE id = 1;
```

## C.处理JSON数据(Postgres的大招)

如果有非结构化数据：

```sql
-- 假设有一个 metadata 列是 JSONB 类型
SELECT * FROM products WHERE metadata @> '{"color": "blue"}';
-- 从products表中，找出所有metadata字段里包含 {"color":"blue"}键值对的记录
```

## JSONB？

1. 什么是JSONB？
    
    与普通文本（TEXT）或JSON类型不同，JSONB会在存储时将数据转化为二进制格式
    
    - 优点：支持GIN索引，查询速度极快
    - 特性：会自动去除多余的空格，并合并重复的键
2. 操作符 `@>` 的工作原理
    
    可以把它想象成 “左边是否包含右边”
    
    - 左侧
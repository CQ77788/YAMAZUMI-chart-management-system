#!/usr/bin/env python3
"""
创建管理员用户的脚本
"""

import sqlite3
import hashlib
import os

def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

def create_admin_user():
    # 使用环境变量指定数据库路径，否则使用默认值
    DATABASE = os.environ.get('DATABASE_URL', 'yamazumi.db')
    
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()
    
    # 检查用户表是否存在角色字段，如果不存在则添加
    cursor.execute("PRAGMA table_info(users)")
    columns = [column[1] for column in cursor.fetchall()]
    
    if 'role' not in columns:
        print("添加角色字段到用户表...")
        cursor.execute("ALTER TABLE users ADD COLUMN role TEXT DEFAULT 'user'")
        conn.commit()
    
    # 检查是否已存在管理员用户
    cursor.execute("SELECT username FROM users WHERE role = 'admin'")
    existing_admin = cursor.fetchone()
    
    if existing_admin:
        print(f"管理员用户已存在: {existing_admin[0]}")
        conn.close()
        return
    
    # 创建管理员用户
    username = "admin"
    password = "admin123"  # 默认密码，建议在生产环境中修改
    email = "admin@example.com"
    
    password_hash = hash_password(password)
    
    try:
        cursor.execute(
            "INSERT INTO users (username, password_hash, email, role) VALUES (?, ?, ?, ?)",
            (username, password_hash, email, 'admin')
        )
        conn.commit()
        print(f"管理员用户创建成功!")
        print(f"用户名: {username}")
        print(f"密码: {password}")
        print("请尽快修改默认密码!")
    except sqlite3.IntegrityError:
        print("用户 'admin' 已存在，正在更新为管理员角色...")
        cursor.execute(
            "UPDATE users SET role = 'admin' WHERE username = ?",
            (username,)
        )
        conn.commit()
        print("用户 'admin' 已更新为管理员角色")
    except Exception as e:
        print(f"创建管理员用户时出错: {e}")
    finally:
        conn.close()

if __name__ == "__main__":
    create_admin_user()
import sqlite3
import hashlib
import json
from datetime import datetime
import os

# 使用环境变量指定数据库路径，否则使用默认值
DATABASE = os.environ.get('DATABASE_URL', 'yamazumi.db')

def init_db():
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()
    
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT UNIQUE NOT NULL,
            password_hash TEXT NOT NULL,
            email TEXT,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    ''')
    
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS factories (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id INTEGER NOT NULL,
            name TEXT NOT NULL,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            FOREIGN KEY (user_id) REFERENCES users(id)
        )
    ''')
    
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS process_sections (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            factory_id INTEGER NOT NULL,
            name TEXT NOT NULL,
            process_name TEXT,
            process_type TEXT,
            measurement_method TEXT,
            time_unit TEXT,
            takt_time TEXT,
            prepared_by TEXT,
            process_data TEXT,
            stations TEXT,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            FOREIGN KEY (factory_id) REFERENCES factories(id)
        )
    ''')
    
    conn.commit()
    conn.close()

def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

def get_db_connection():
    conn = sqlite3.connect(DATABASE)
    conn.row_factory = sqlite3.Row
    return conn

def create_user(username, password, email=None):
    conn = get_db_connection()
    cursor = conn.cursor()
    
    try:
        password_hash = hash_password(password)
        cursor.execute(
            'INSERT INTO users (username, password_hash, email) VALUES (?, ?, ?)',
            (username, password_hash, email)
        )
        conn.commit()
        return cursor.lastrowid
    except sqlite3.IntegrityError:
        return None
    finally:
        conn.close()

def verify_user(username, password):
    conn = get_db_connection()
    cursor = conn.cursor()
    
    password_hash = hash_password(password)
    cursor.execute(
        'SELECT id, username, email FROM users WHERE username = ? AND password_hash = ?',
        (username, password_hash)
    )
    user = cursor.fetchone()
    conn.close()
    
    return user

def get_user_by_id(user_id):
    conn = get_db_connection()
    cursor = conn.cursor()
    
    cursor.execute('SELECT id, username, email FROM users WHERE id = ?', (user_id,))
    user = cursor.fetchone()
    conn.close()
    
    return user

def change_password(user_id, old_password, new_password):
    conn = get_db_connection()
    cursor = conn.cursor()
    
    old_password_hash = hash_password(old_password)
    cursor.execute(
        'SELECT id FROM users WHERE id = ? AND password_hash = ?',
        (user_id, old_password_hash)
    )
    user = cursor.fetchone()
    
    if not user:
        conn.close()
        return False
    
    new_password_hash = hash_password(new_password)
    cursor.execute(
        'UPDATE users SET password_hash = ? WHERE id = ?',
        (new_password_hash, user_id)
    )
    conn.commit()
    conn.close()
    
    return True

def create_factory(user_id, name):
    conn = get_db_connection()
    cursor = conn.cursor()
    
    cursor.execute(
        'INSERT INTO factories (user_id, name) VALUES (?, ?)',
        (user_id, name)
    )
    conn.commit()
    factory_id = cursor.lastrowid
    conn.close()
    
    return factory_id

def get_factories(user_id):
    conn = get_db_connection()
    cursor = conn.cursor()
    
    cursor.execute('SELECT id, name FROM factories WHERE user_id = ?', (user_id,))
    factories = cursor.fetchall()
    conn.close()
    
    return [dict(factory) for factory in factories]

def get_factory(user_id, factory_id):
    conn = get_db_connection()
    cursor = conn.cursor()
    
    cursor.execute(
        'SELECT id, name FROM factories WHERE id = ? AND user_id = ?',
        (factory_id, user_id)
    )
    factory = cursor.fetchone()
    conn.close()
    
    return dict(factory) if factory else None

def update_factory(user_id, factory_id, new_name):
    conn = get_db_connection()
    cursor = conn.cursor()
    
    cursor.execute(
        'UPDATE factories SET name = ? WHERE id = ? AND user_id = ?',
        (new_name, factory_id, user_id)
    )
    conn.commit()
    conn.close()

def delete_factory(user_id, factory_id):
    conn = get_db_connection()
    cursor = conn.cursor()
    
    cursor.execute(
        'DELETE FROM factories WHERE id = ? AND user_id = ?',
        (factory_id, user_id)
    )
    conn.commit()
    conn.close()

def create_process_section(factory_id, name, data):
    conn = get_db_connection()
    cursor = conn.cursor()
    
    cursor.execute(
        '''INSERT INTO process_sections 
           (factory_id, name, process_name, process_type, measurement_method, time_unit, takt_time, prepared_by, process_data, stations)
           VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)''',
        (
            factory_id,
            name,
            data.get('process_name', name),
            data.get('process_type', 'Product'),
            data.get('measurement_method', 'Measurement Method:'),
            data.get('time_unit', 'secs'),
            data.get('takt_time', 'Takt Time'),
            data.get('prepared_by', 'Chris Coles'),
            json.dumps(data.get('process_data', [])),
            json.dumps(data.get('stations', []))
        )
    )
    conn.commit()
    section_id = cursor.lastrowid
    conn.close()
    
    return section_id

def get_process_sections(factory_id):
    conn = get_db_connection()
    cursor = conn.cursor()
    
    cursor.execute(
        'SELECT id, name, process_name, process_type, measurement_method, time_unit, takt_time, prepared_by, process_data, stations FROM process_sections WHERE factory_id = ?',
        (factory_id,)
    )
    sections = cursor.fetchall()
    conn.close()
    
    return [dict(section) for section in sections]

def get_process_section(section_id):
    conn = get_db_connection()
    cursor = conn.cursor()
    
    cursor.execute(
        'SELECT id, name, process_name, process_type, measurement_method, time_unit, takt_time, prepared_by, process_data, stations FROM process_sections WHERE id = ?',
        (section_id,)
    )
    section = cursor.fetchone()
    conn.close()
    
    return dict(section) if section else None

def update_process_section(section_id, name, data):
    conn = get_db_connection()
    cursor = conn.cursor()
    
    cursor.execute(
        '''UPDATE process_sections 
           SET name = ?, process_name = ?, process_type = ?, measurement_method = ?, time_unit = ?, takt_time = ?, prepared_by = ?, process_data = ?, stations = ?
           WHERE id = ?''',
        (
            name,
            data.get('process_name', name),
            data.get('process_type', 'Product'),
            data.get('measurement_method', 'Measurement Method:'),
            data.get('time_unit', 'secs'),
            data.get('takt_time', 'Takt Time'),
            data.get('prepared_by', 'Chris Coles'),
            json.dumps(data.get('process_data', [])),
            json.dumps(data.get('stations', [])),
            section_id
        )
    )
    conn.commit()
    conn.close()

def delete_process_section(section_id):
    conn = get_db_connection()
    cursor = conn.cursor()
    
    cursor.execute('DELETE FROM process_sections WHERE id = ?', (section_id,))
    conn.commit()
    conn.close()

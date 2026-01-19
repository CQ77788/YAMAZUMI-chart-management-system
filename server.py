from flask import Flask, request, jsonify, send_from_directory, session
from flask_cors import CORS
import json
import os
import re
from database import init_db, create_user, verify_user, get_user_by_id, change_password, create_factory, get_factories, get_factory, update_factory, delete_factory, create_process_section, get_process_sections, get_process_section, update_process_section, delete_process_section, get_db_connection, get_all_users, update_user_role, delete_user, is_admin, update_user_info, reset_user_password, get_user_by_id_for_admin
import secrets

app = Flask(__name__)
CORS(app)

# 使用环境变量或生成随机密钥
app.secret_key = os.environ.get('SECRET_KEY', secrets.token_hex(16))

DATA_FILE = 'data.js'

init_db()

def load_data():
    """从数据库加载所有工厂数据"""
    try:
        # 获取所有用户ID对应的工厂
        # 注意：这里需要一种方式知道要获取哪个用户的工厂数据
        # 由于load_data通常在没有会话上下文的情况下调用，我们需要一个替代方案
        # 实际上，我们不应该在没有用户上下文的情况下调用load_data
        # 这个函数可能只应该在有用户会话时被调用
        raise Exception("此函数不应在没有用户上下文的情况下使用。请使用新的数据库加载方法。")
    except Exception as e:
        print(f"Error loading data: {e}")
        return {}


def load_all_factory_data_from_db(user_id):
    """从数据库加载指定用户的所有工厂数据"""
    try:
        conn = get_db_connection()
        cursor = conn.cursor()
        
        # 获取用户的所有工厂
        cursor.execute('SELECT id, name FROM factories WHERE user_id = ?', (user_id,))
        factories = cursor.fetchall()
        
        allFactoriesData = {}
        
        for factory in factories:
            factory_id = factory['id']
            factory_name = factory['name']
            
            # 获取该工厂的所有工艺段
            cursor.execute('''
                SELECT name, process_name, process_type, measurement_method, time_unit, takt_time, 
                       prepared_by, process_data, stations 
                FROM process_sections 
                WHERE factory_id = ?
            ''', (factory_id,))
            sections = cursor.fetchall()
            
            allFactoriesData[factory_name] = {}
            
            for section in sections:
                section_name = section['name']
                
                # 将JSON字符串转换回Python对象
                process_data = json.loads(section['process_data']) if section['process_data'] else []
                stations = json.loads(section['stations']) if section['stations'] else []
                
                allFactoriesData[factory_name][section_name] = {
                    "process_name": section['process_name'],
                    "process_type": section['process_type'],
                    "measurement_method": section['measurement_method'],
                    "time_unit": section['time_unit'],
                    "takt_time": section['takt_time'],
                    "prepared_by": section['prepared_by'],
                    "process_data": process_data,
                    "stations": stations
                }
        
        conn.close()
        return allFactoriesData
    except Exception as e:
        print(f"Error loading data from database: {e}")
        return {}


def save_data_to_db(data, user_id):
    """将数据保存到数据库"""
    try:
        conn = get_db_connection()
        cursor = conn.cursor()
        
        # 遍历所有工厂和工艺段，更新数据库
        for factory_name, factory_data in data.items():
            # 检查工厂是否存在，如果不存在则创建
            cursor.execute('SELECT id FROM factories WHERE name = ? AND user_id = ?', (factory_name, user_id))
            factory = cursor.fetchone()
            
            if factory:
                factory_id = factory[0]
            else:
                cursor.execute('INSERT INTO factories (user_id, name) VALUES (?, ?)', (user_id, factory_name))
                factory_id = cursor.lastrowid
            
            # 处理该工厂下的每个工艺段
            for section_name, section_data in factory_data.items():
                # 检查工艺段是否存在，如果不存在则创建，否则更新
                cursor.execute('''
                    SELECT id FROM process_sections 
                    WHERE factory_id = ? AND name = ?
                ''', (factory_id, section_name))
                section = cursor.fetchone()
                
                if section:
                    # 更新现有工艺段
                    section_id = section[0]
                    cursor.execute('''
                        UPDATE process_sections 
                        SET process_name = ?, process_type = ?, measurement_method = ?, 
                            time_unit = ?, takt_time = ?, prepared_by = ?, 
                            process_data = ?, stations = ?
                        WHERE id = ?
                    ''', (
                        section_data.get('process_name', section_name),
                        section_data.get('process_type', 'Product'),
                        section_data.get('measurement_method', 'Measurement Method:'),
                        section_data.get('time_unit', 'secs'),
                        section_data.get('takt_time', 'Takt Time'),
                        section_data.get('prepared_by', 'Chris Coles'),
                        json.dumps(section_data.get('process_data', [])),
                        json.dumps(section_data.get('stations', [])),
                        section_id
                    ))
                else:
                    # 创建新工艺段
                    cursor.execute('''
                        INSERT INTO process_sections 
                        (factory_id, name, process_name, process_type, measurement_method, 
                         time_unit, takt_time, prepared_by, process_data, stations)
                        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
                    ''', (
                        factory_id,
                        section_name,
                        section_data.get('process_name', section_name),
                        section_data.get('process_type', 'Product'),
                        section_data.get('measurement_method', 'Measurement Method:'),
                        section_data.get('time_unit', 'secs'),
                        section_data.get('takt_time', 'Takt Time'),
                        section_data.get('prepared_by', 'Chris Coles'),
                        json.dumps(section_data.get('process_data', [])),
                        json.dumps(section_data.get('stations', []))
                    ))
        
        conn.commit()
        conn.close()
        return True
    except Exception as e:
        print(f"Error saving data to database: {e}")
        return False

@app.route('/')
def index():
    return send_from_directory('.', 'index.html')

@app.route('/<path:filename>')
def serve_static(filename):
    return send_from_directory('.', filename)

@app.route('/api/save-data', methods=['POST'])
def save_data():
    try:
        if 'user_id' not in session:
            return jsonify({'success': False, 'message': 'Not authenticated'}), 401
        
        data = request.json
        success = save_data_to_db(data, session['user_id'])
        
        if success:
            return jsonify({'success': True, 'message': 'Data saved successfully'})
        else:
            return jsonify({'success': False, 'message': 'Failed to save data to database'}), 500
    except Exception as e:
        return jsonify({'success': False, 'message': str(e)}), 500

@app.route('/api/save-process-data', methods=['POST'])
def save_process_data():
    try:
        if 'user_id' not in session:
            return jsonify({'success': False, 'message': 'Not authenticated'}), 401
        
        data = request.json
        factory = data.get('factory')
        section = data.get('section')
        process_data = data.get('process_data')
        stations = data.get('stations', [])
        
        if not factory or not section:
            return jsonify({'success': False, 'message': 'Factory and section are required'}), 400
        
        # 直接更新数据库中的特定工艺段数据
        conn = get_db_connection()
        cursor = conn.cursor()
        
        # 查找工厂ID
        cursor.execute('SELECT id FROM factories WHERE name = ? AND user_id = ?', (factory, session['user_id']))
        factory_result = cursor.fetchone()
        
        if not factory_result:
            # 如果工厂不存在，创建新工厂
            cursor.execute('INSERT INTO factories (user_id, name) VALUES (?, ?)', (session['user_id'], factory))
            factory_id = cursor.lastrowid
        else:
            factory_id = factory_result[0]
        
        # 检查工艺段是否存在
        cursor.execute('SELECT id FROM process_sections WHERE factory_id = ? AND name = ?', (factory_id, section))
        section_result = cursor.fetchone()
        
        if section_result:
            # 更新现有工艺段
            section_id = section_result[0]
            cursor.execute('''
                UPDATE process_sections 
                SET process_data = ?, stations = ?
                WHERE id = ?
            ''', (json.dumps(process_data), json.dumps(stations), section_id))
        else:
            # 创建新工艺段
            cursor.execute('''
                INSERT INTO process_sections 
                (factory_id, name, process_name, process_type, measurement_method, 
                 time_unit, takt_time, prepared_by, process_data, stations)
                VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
            ''', (
                factory_id,
                section,
                section,  # process_name
                "Product",  # process_type
                "Measurement Method:",  # measurement_method
                "secs",  # time_unit
                "Takt Time",  # takt_time
                "Chris Coles",  # prepared_by
                json.dumps(process_data),
                json.dumps(stations)
            ))
        
        conn.commit()
        conn.close()
        
        return jsonify({'success': True, 'message': 'Process data saved successfully'})
    except Exception as e:
        return jsonify({'success': False, 'message': str(e)}), 500

@app.route('/api/register', methods=['POST'])
def register():
    try:
        data = request.json
        username = data.get('username')
        password = data.get('password')
        email = data.get('email')
        
        if not username or not password:
            return jsonify({'success': False, 'message': 'Username and password are required'}), 400
        
        user_id = create_user(username, password, email)
        
        if user_id is None:
            return jsonify({'success': False, 'message': 'Username already exists'}), 400
        
        session['user_id'] = user_id
        session['username'] = username
        
        return jsonify({'success': True, 'message': 'Registration successful', 'user_id': user_id})
    except Exception as e:
        return jsonify({'success': False, 'message': str(e)}), 500

@app.route('/api/login', methods=['POST'])
def login():
    try:
        data = request.json
        username = data.get('username')
        password = data.get('password')
        
        if not username or not password:
            return jsonify({'success': False, 'message': 'Username and password are required'}), 400
        
        user = verify_user(username, password)
        
        if not user:
            return jsonify({'success': False, 'message': 'Invalid username or password'}), 401
        
        session['user_id'] = user['id']
        session['username'] = user['username']
        
        return jsonify({'success': True, 'message': 'Login successful', 'user': {'id': user['id'], 'username': user['username'], 'email': user['email']}})
    except Exception as e:
        return jsonify({'success': False, 'message': str(e)}), 500

@app.route('/api/logout', methods=['POST'])
def logout():
    session.clear()
    return jsonify({'success': True, 'message': 'Logout successful'})

@app.route('/api/me', methods=['GET'])
def get_current_user():
    if 'user_id' not in session:
        return jsonify({'success': False, 'message': 'Not authenticated'}), 401
    
    user = get_user_by_id(session['user_id'])
    
    if not user:
        return jsonify({'success': False, 'message': 'User not found'}), 404
    
    return jsonify({'success': True, 'user': {'id': user['id'], 'username': user['username'], 'email': user['email']}})

@app.route('/api/change-password', methods=['POST'])
def api_change_password():
    if 'user_id' not in session:
        return jsonify({'success': False, 'message': 'Not authenticated'}), 401
    
    data = request.json
    current_password = data.get('current_password')
    new_password = data.get('new_password')
    
    if not current_password or not new_password:
        return jsonify({'success': False, 'message': 'Current password and new password are required'}), 400
    
    if len(new_password) < 6:
        return jsonify({'success': False, 'message': 'Password must be at least 6 characters long'}), 400
    
    success = change_password(session['user_id'], current_password, new_password)
    
    if success:
        return jsonify({'success': True, 'message': 'Password changed successfully'})
    else:
        return jsonify({'success': False, 'message': 'Current password is incorrect'}), 400

@app.route('/api/factories', methods=['GET'])
def api_get_factories():
    if 'user_id' not in session:
        return jsonify({'success': False, 'message': 'Not authenticated'}), 401
    
    factories = get_factories(session['user_id'])
    return jsonify({'success': True, 'factories': factories})

@app.route('/api/factories', methods=['POST'])
def api_create_factory():
    if 'user_id' not in session:
        return jsonify({'success': False, 'message': 'Not authenticated'}), 401
    
    data = request.json
    name = data.get('name')
    
    if not name:
        return jsonify({'success': False, 'message': 'Factory name is required'}), 400
    
    factory_id = create_factory(session['user_id'], name)
    
    return jsonify({'success': True, 'factory_id': factory_id, 'name': name})

@app.route('/api/factories/<int:factory_id>', methods=['PUT'])
def api_update_factory(factory_id):
    if 'user_id' not in session:
        return jsonify({'success': False, 'message': 'Not authenticated'}), 401
    
    data = request.json
    new_name = data.get('name')
    
    if not new_name:
        return jsonify({'success': False, 'message': 'Factory name is required'}), 400
    
    factory = get_factory(session['user_id'], factory_id)
    
    if not factory:
        return jsonify({'success': False, 'message': 'Factory not found'}), 404
    
    update_factory(session['user_id'], factory_id, new_name)
    
    return jsonify({'success': True, 'message': 'Factory updated successfully'})

@app.route('/api/factories/<int:factory_id>', methods=['DELETE'])
def api_delete_factory(factory_id):
    if 'user_id' not in session:
        return jsonify({'success': False, 'message': 'Not authenticated'}), 401
    
    factory = get_factory(session['user_id'], factory_id)
    
    if not factory:
        return jsonify({'success': False, 'message': 'Factory not found'}), 404
    
    delete_factory(session['user_id'], factory_id)
    
    return jsonify({'success': True, 'message': 'Factory deleted successfully'})

@app.route('/api/factories/<int:factory_id>/sections', methods=['GET'])
def api_get_sections(factory_id):
    if 'user_id' not in session:
        return jsonify({'success': False, 'message': 'Not authenticated'}), 401
    
    sections = get_process_sections(factory_id)
    
    return jsonify({'success': True, 'sections': sections})

@app.route('/api/factories/<string:factory_name>/sections', methods=['GET'])
def api_get_sections_by_name(factory_name):
    if 'user_id' not in session:
        return jsonify({'success': False, 'message': 'Not authenticated'}), 401
    
    factories = get_factories(session['user_id'])
    factory = next((f for f in factories if f['name'] == factory_name), None)
    
    if not factory:
        return jsonify({'success': False, 'message': 'Factory not found'}), 404
    
    sections = get_process_sections(factory['id'])
    
    return jsonify({'success': True, 'sections': sections})

@app.route('/api/factories/<string:factory_name>/sections', methods=['POST'])
def api_create_section_by_name(factory_name):
    if 'user_id' not in session:
        return jsonify({'success': False, 'message': 'Not authenticated'}), 401
    
    factories = get_factories(session['user_id'])
    factory = next((f for f in factories if f['name'] == factory_name), None)
    
    if not factory:
        return jsonify({'success': False, 'message': 'Factory not found'}), 404
    
    data = request.json
    name = data.get('name')
    
    if not name:
        return jsonify({'success': False, 'message': 'Section name is required'}), 400
    
    section_data = {
        'process_name': data.get('process_name', name),
        'process_type': data.get('process_type', 'Product'),
        'measurement_method': data.get('measurement_method', 'Measurement Method:'),
        'time_unit': data.get('time_unit', 'secs'),
        'takt_time': data.get('takt_time', 'Takt Time'),
        'prepared_by': data.get('prepared_by', 'Chris Coles'),
        'process_data': data.get('process_data', []),
        'stations': data.get('stations', [])
    }
    
    section_id = create_process_section(factory['id'], name, section_data)
    
    return jsonify({'success': True, 'section_id': section_id, 'name': name})

@app.route('/api/factories/<int:factory_id>/sections', methods=['POST'])
def api_create_section(factory_id):
    if 'user_id' not in session:
        return jsonify({'success': False, 'message': 'Not authenticated'}), 401
    
    data = request.json
    name = data.get('name')
    
    if not name:
        return jsonify({'success': False, 'message': 'Section name is required'}), 400
    
    section_data = {
        'process_name': data.get('process_name', name),
        'process_type': data.get('process_type', 'Product'),
        'measurement_method': data.get('measurement_method', 'Measurement Method:'),
        'time_unit': data.get('time_unit', 'secs'),
        'takt_time': data.get('takt_time', 'Takt Time'),
        'prepared_by': data.get('prepared_by', 'Chris Coles'),
        'process_data': data.get('process_data', []),
        'stations': data.get('stations', [])
    }
    
    section_id = create_process_section(factory_id, name, section_data)
    
    return jsonify({'success': True, 'section_id': section_id, 'name': name})

@app.route('/api/sections/<int:section_id>', methods=['PUT'])
def api_update_section(section_id):
    if 'user_id' not in session:
        return jsonify({'success': False, 'message': 'Not authenticated'}), 401
    
    data = request.json
    name = data.get('name')
    
    if not name:
        return jsonify({'success': False, 'message': 'Section name is required'}), 400
    
    section = get_process_section(section_id)
    
    if not section:
        return jsonify({'success': False, 'message': 'Section not found'}), 404
    
    section_data = {
        'process_name': data.get('process_name', name),
        'process_type': data.get('process_type', 'Product'),
        'measurement_method': data.get('measurement_method', 'Measurement Method:'),
        'time_unit': data.get('time_unit', 'secs'),
        'takt_time': data.get('takt_time', 'Takt Time'),
        'prepared_by': data.get('prepared_by', 'Chris Coles'),
        'process_data': data.get('process_data', []),
        'stations': data.get('stations', [])
    }
    
    update_process_section(section_id, name, section_data)
    
    return jsonify({'success': True, 'message': 'Section updated successfully'})

@app.route('/api/sections/<string:section_name>', methods=['PUT'])
def api_update_section_by_name(section_name):
    if 'user_id' not in session:
        return jsonify({'success': False, 'message': 'Not authenticated'}), 401
    
    data = request.json
    factory_name = data.get('factory')
    
    if not factory_name:
        return jsonify({'success': False, 'message': 'Factory name is required'}), 400
    
    factories = get_factories(session['user_id'])
    factory = next((f for f in factories if f['name'] == factory_name), None)
    
    if not factory:
        return jsonify({'success': False, 'message': 'Factory not found'}), 404
    
    sections = get_process_sections(factory['id'])
    section = next((s for s in sections if s['name'] == section_name), None)
    
    if not section:
        return jsonify({'success': False, 'message': 'Section not found'}), 404
    
    section_data = {
        'process_name': data.get('process_name', section_name),
        'process_type': data.get('process_type', 'Product'),
        'measurement_method': data.get('measurement_method', 'Measurement Method:'),
        'time_unit': data.get('time_unit', 'secs'),
        'takt_time': data.get('takt_time', 'Takt Time'),
        'prepared_by': data.get('prepared_by', 'Chris Coles'),
        'process_data': data.get('process_data', []),
        'stations': data.get('stations', [])
    }
    
    update_process_section(section['id'], section_name, section_data)
    
    return jsonify({'success': True, 'message': 'Section updated successfully'})

@app.route('/api/sections/<int:section_id>', methods=['DELETE'])
def api_delete_section(section_id):
    if 'user_id' not in session:
        return jsonify({'success': False, 'message': 'Not authenticated'}), 401

    section = get_process_section(section_id)

    if not section:
        return jsonify({'success': False, 'message': 'Section not found'}), 404

    delete_process_section(section_id)

    return jsonify({'success': True, 'message': 'Section deleted successfully'})


@app.route('/api/load-all-data', methods=['GET'])
def api_load_all_data():
    """从数据库加载当前用户的所有工厂数据"""
    if 'user_id' not in session:
        return jsonify({'success': False, 'message': 'Not authenticated'}), 401
    
    try:
        allFactoriesData = load_all_factory_data_from_db(session['user_id'])
        return jsonify({'success': True, 'data': allFactoriesData})
    except Exception as e:
        return jsonify({'success': False, 'message': str(e)}), 500

@app.route('/api/users', methods=['GET'])
def api_get_all_users():
    """获取所有用户（仅管理员可用）"""
    if 'user_id' not in session:
        return jsonify({'success': False, 'message': 'Not authenticated'}), 401
    
    if not is_admin(session['user_id']):
        return jsonify({'success': False, 'message': 'Access denied. Admin privileges required.'}), 403
    
    try:
        users = get_all_users()
        return jsonify({'success': True, 'users': users})
    except Exception as e:
        return jsonify({'success': False, 'message': str(e)}), 500

@app.route('/api/users/<int:user_id>/role', methods=['PUT'])
def api_update_user_role(user_id):
    """更新用户角色（仅管理员可用）"""
    if 'user_id' not in session:
        return jsonify({'success': False, 'message': 'Not authenticated'}), 401
    
    if not is_admin(session['user_id']):
        return jsonify({'success': False, 'message': 'Access denied. Admin privileges required.'}), 403
    
    data = request.json
    new_role = data.get('role')
    
    if not new_role or new_role not in ['user', 'admin']:
        return jsonify({'success': False, 'message': 'Valid role is required (user or admin)'}), 400
    
    try:
        update_user_role(user_id, new_role)
        return jsonify({'success': True, 'message': 'User role updated successfully'})
    except Exception as e:
        return jsonify({'success': False, 'message': str(e)}), 500

@app.route('/api/users/<int:user_id>', methods=['DELETE'])
def api_delete_user(user_id):
    """删除用户（仅管理员可用）"""
    if 'user_id' not in session:
        return jsonify({'success': False, 'message': 'Not authenticated'}), 401
    
    if not is_admin(session['user_id']):
        return jsonify({'success': False, 'message': 'Access denied. Admin privileges required.'}), 403
    
    if user_id == session['user_id']:
        return jsonify({'success': False, 'message': 'Cannot delete your own account'}), 400
    
    try:
        delete_user(user_id)
        return jsonify({'success': True, 'message': 'User deleted successfully'})
    except Exception as e:
        return jsonify({'success': False, 'message': str(e)}), 500

@app.route('/api/is-admin', methods=['GET'])
def api_check_admin():
    """检查当前用户是否为管理员"""
    if 'user_id' not in session:
        return jsonify({'success': False, 'message': 'Not authenticated'}), 401
    
    try:
        admin_status = is_admin(session['user_id'])
        return jsonify({'success': True, 'is_admin': admin_status})
    except Exception as e:
        return jsonify({'success': False, 'message': str(e)}), 500

@app.route('/api/users/<int:user_id>', methods=['GET'])
def api_get_user(user_id):
    """获取指定用户信息（仅管理员可用）"""
    if 'user_id' not in session:
        return jsonify({'success': False, 'message': 'Not authenticated'}), 401
    
    if not is_admin(session['user_id']):
        return jsonify({'success': False, 'message': 'Access denied. Admin privileges required.'}), 403
    
    try:
        user = get_user_by_id_for_admin(session['user_id'], user_id)
        if user:
            return jsonify({'success': True, 'user': user})
        else:
            return jsonify({'success': False, 'message': 'User not found'}), 404
    except Exception as e:
        return jsonify({'success': False, 'message': str(e)}), 500

@app.route('/api/users/<int:user_id>/info', methods=['PUT'])
def api_update_user_info(user_id):
    """更新用户信息（仅管理员可用）"""
    if 'user_id' not in session:
        return jsonify({'success': False, 'message': 'Not authenticated'}), 401
    
    if not is_admin(session['user_id']):
        return jsonify({'success': False, 'message': 'Access denied. Admin privileges required.'}), 403
    
    data = request.json
    username = data.get('username')
    email = data.get('email')
    
    if not username and email is None:
        return jsonify({'success': False, 'message': 'No data to update'}), 400
    
    try:
        success = update_user_info(user_id, username, email)
        if success:
            return jsonify({'success': True, 'message': 'User info updated successfully'})
        else:
            return jsonify({'success': False, 'message': 'Username already exists or update failed'}), 400
    except Exception as e:
        return jsonify({'success': False, 'message': str(e)}), 500

@app.route('/api/users/<int:user_id>/password', methods=['PUT'])
def api_reset_user_password(user_id):
    """重置用户密码（仅管理员可用）"""
    if 'user_id' not in session:
        return jsonify({'success': False, 'message': 'Not authenticated'}), 401
    
    if not is_admin(session['user_id']):
        return jsonify({'success': False, 'message': 'Access denied. Admin privileges required.'}), 403
    
    data = request.json
    new_password = data.get('new_password')
    
    if not new_password:
        return jsonify({'success': False, 'message': 'New password is required'}), 400
    
    if len(new_password) < 6:
        return jsonify({'success': False, 'message': 'Password must be at least 6 characters long'}), 400
    
    try:
        success = reset_user_password(user_id, new_password)
        if success:
            return jsonify({'success': True, 'message': 'Password reset successfully'})
        else:
            return jsonify({'success': False, 'message': 'Failed to reset password'}), 400
    except Exception as e:
        return jsonify({'success': False, 'message': str(e)}), 500


if __name__ == '__main__':
    # 获取端口号，默认为5000，云平台通常使用PORT环境变量
    port = int(os.environ.get('PORT', 5000))
    print(f'Server running at http://0.0.0.0:{port}')
    print(f'Serving from: {os.getcwd()}')
    # 在生产环境中不使用debug模式
    app.run(host='0.0.0.0', port=port, debug=False)

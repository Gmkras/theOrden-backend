from typing import List
from werkzeug.security import check_password_hash

from .connection import get_connection, extras
from ..models.models import Admin_users
from ..models.exceptions import UserAlreadyExists, UserNotFound

from faker import Faker


def create(user: Admin_users) -> Admin_users:
    conn = get_connection()
    cur = conn.cursor(cursor_factory=extras.RealDictCursor)

    cur.execute('INSERT INTO admin_users (name, password) VALUES (%s, %s) RETURNING *', (user.name,user.password,))
    new_user = cur.fetchone()
    conn.commit()
    cur.close()
    conn.close()
    
    return Admin_users(new_user)


def update(user: Admin_users) -> Admin_users:
    conn = get_connection()
    cur = conn.cursor(cursor_factory=extras.RealDictCursor)
    
    cur.execute('UPDATE admin_users SET name = %s, password = %s WHERE admin_id = %s RETURNING *', (user.name, user.password, user.admin_id,))
    user = cur.fetchone()
    conn.commit()
    
    cur.close()
    conn.close()
    
    if user is None:
        return ({'message':'User not found'}), 404

    return user


def delete(user: Admin_users) -> Admin_users:
    conn = get_connection()
    cur = conn.cursor(cursor_factory=extras.RealDictCursor)
    
    cur.execute('DELETE FROM admin_users WHERE admin_id = %s RETURNING *', (user.admin_id,))
    user = cur.fetchone()
    
    conn.commit()
    
    cur.close()
    conn.close()
    if user is None:
        return ({'message':'User not found'}), 404
    
    return user


def list_all() -> List[Admin_users]:
    conn = get_connection()
    cur = conn.cursor(cursor_factory=extras.RealDictCursor)
    
    cur.execute('SELECT * FROM admin_users')
    users = cur.fetchall()
    
    cur.close()
    conn.close()

    return users


def detail(user: Admin_users) -> Admin_users:
    conn = get_connection()
    cur = conn.cursor(cursor_factory=extras.RealDictCursor)
    
    cur.execute('SELECT * FROM admin_users WHERE admin_id = %s', (user.admin_id,))
    user = cur.fetchone()
    
    if user is None:
        return ({'message':'User not found'}), 404
    
    cur.close()
    conn.close()
    
    return user

def login(user: Admin_users) -> Admin_users:
    try:
        conn = get_connection()
        cur = conn.cursor(cursor_factory=extras.RealDictCursor)
        
        cur.execute('SELECT * FROM admin_users WHERE admin_id = %s', (user.admin_id,))
        row = cur.fetchone()
        
        if row != None:
            admin_row = row[0],row[1], check_password_hash(row[2],user.password)
            return admin_row
        else:
            cur.close()
            conn.close()
            return None
        
    except Exception as e:
        raise Exception(e)
    
    

def reset_table() -> None:
    query = "DROP TABLE IF EXISTS admin_users"
    #_fetch_none(query)

    fields = """(name text, password text)"""
    query = f"CREATE TABLE IF NOT EXISTS admin_users {fields}"

    #_fetch_none(query)

    fake = Faker()
    fake.seed_instance(42)

    for _ in range(10):
        test_user = Admin_users(name=fake.first_name())

        create(test_user)
        
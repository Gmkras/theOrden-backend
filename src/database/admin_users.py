from typing import List

from .connection import get_connection, extras
from ..models.models import Admin_user
from ..models.exceptions import UserAlreadyExists, UserNotFound

from faker import Faker


def create(user: Admin_user) -> Admin_user:
    conn = get_connection()
    cur = conn.cursor(cursor_factory=extras.RealDictCursor)

    cur.execute('INSERT INTO admin_users (name) VALUES (%s) RETURNING *', (user.name,))
    new_user = cur.fetchone()
    conn.commit()
    cur.close()
    conn.close()
    
    return Admin_user(new_user)


def update(user: Admin_user) -> Admin_user:
    conn = get_connection()
    cur = conn.cursor(cursor_factory=extras.RealDictCursor)
    
    cur.execute('UPDATE admin_users SET name = %s, WHERE admin_id = %s RETURNING *', (user.name,user.admin_id,))
    user = cur.fetchone()
    conn.commit()
    
    cur.close()
    conn.close()
    
    if user is None:
        return ({'message':'User not found'}), 404

    return user


def delete(user: Admin_user) -> Admin_user:
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


def list_all() -> List[Admin_user]:
    conn = get_connection()
    cur = conn.cursor(cursor_factory=extras.RealDictCursor)
    
    cur.execute('SELECT * FROM admin_users')
    users = cur.fetchall()
    
    cur.close()
    conn.close()

    return users


def detail(user: Admin_user) -> Admin_user:
    conn = get_connection()
    cur = conn.cursor(cursor_factory=extras.RealDictCursor)
    
    cur.execute('SELECT * FROM admin_users WHERE admin_id = %s', (user.admin_id,))
    user = cur.fetchone()
    
    if user is None:
        return ({'message':'User not found'}), 404
    
    cur.close()
    conn.close()
    
    return user


def reset_table() -> None:
    query = "DROP TABLE IF EXISTS admin_users"
    #_fetch_none(query)

    fields = """(name text)"""
    query = f"CREATE TABLE IF NOT EXISTS admin_users {fields}"

    #_fetch_none(query)

    fake = Faker()
    fake.seed_instance(42)

    for _ in range(10):
        test_user = Admin_user(name=fake.first_name())

        create(test_user)
        
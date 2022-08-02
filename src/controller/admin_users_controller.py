from typing import List

from ..database import admin_users
from ..models.models import Admin_users
from ..helpers import helper

def login(admin_user_:admin_users) -> admin_users:
    return Admin_users.login(admin_user_)
    
def create(admin_user_: Admin_users) -> Admin_users:
    return admin_users.create(admin_user_)

def update(admin_user: Admin_users) -> Admin_users:
    return admin_users.update(admin_user)

def delete(admin_user: Admin_users) -> Admin_users:
    return admin_users.delete(admin_user)

def lists() -> List[Admin_users]:
    return admin_users.list_all()

def details(admin_user: Admin_users) -> Admin_users:
    return admin_users.detail(admin_user)
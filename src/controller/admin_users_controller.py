from typing import List

from ..database import admin_users
from ..models.models import Admin_user
from ..helpers import helper


def create(admin_user_: Admin_user) -> Admin_user:
    return admin_users.create(admin_user_)

def update(admin_user: Admin_user) -> Admin_user:
    return admin_users.update(admin_user)

def delete(admin_user: Admin_user) -> Admin_user:
    return admin_users.delete(admin_user)

def lists() -> List[Admin_user]:
    return admin_users.list_all()

def details(admin_user: Admin_user) -> Admin_user:
    return admin_users.detail(admin_user)
from typing import List

from ..database import admin_users
from ..models.models import Admin_user
from ..helpers import helper


def create(admin_user_: Admin_user) -> Admin_user:
    admin_user = helper.format_name(admin_user_)
    helper.validate_admin_user(admin_user)
    return admin_user.create(admin_user)

def update(admin_user: Admin_user) -> Admin_user:
    admin_user = helper.format_name(admin_user)
    helper.validate_admin_user(admin_user)
    return admin_user.update(admin_user)

def delete(admin_user: Admin_user) -> Admin_user:
    return admin_user.delete(admin_user)

def lists() -> List[Admin_user]:
    return admin_users.list_all()

def details(admin_user: Admin_user) -> Admin_user:
    return admin_user.detail(admin_user)
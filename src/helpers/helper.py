import re

from ..models.models import Admin_user
from ..models.exceptions import UserNotValid


def validate_admin_user(admin_user: Admin_user) -> None:
    if not __name_is_valid(admin_user.name):
        raise UserNotValid(f"The name: {admin_user.name} is not valid")

    if None in (admin_user.name):
        raise UserNotValid("The user has no name")


def format_name(admin_user: Admin_user) -> Admin_user:
    admin_user_dict = admin_user._asdict()
    admin_user_dict["name"] = admin_user.name.capitalize()

    return Admin_user(**admin_user_dict)


def __name_is_valid(name: str) -> bool:
    if not isinstance(name, str):
        return False

    regex = r'^(\w|\.|\_|\-)+[@](\w|\_|\-|\.)+[.]\w{2,3}$'

    return bool(re.search(regex, name))
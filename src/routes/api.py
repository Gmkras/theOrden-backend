from flask import Blueprint, request, jsonify, redirect, url_for

from ..controller import admin_users_controller
from ..models.models import Admin_user


api_scope = Blueprint("api", __name__)


@api_scope.route('/admin_users', methods=['GET'])
def get_list():
    admin_users_list = admin_users_controller.lists()

    return jsonify(admin_users_list)

@api_scope.route('/admin_users/<id_>', methods=['GET'])
def get_details(id_):
    admin_user = Admin_user(admin_id=id_)

    admin_user_new = admin_users_controller.details(admin_user)

    return jsonify(admin_user_new)

@api_scope.route('/admin_users', methods=['POST'])
def create():
    data = request.form
    admin_user = Admin_user(name=data["name"])

    admin_users_controller.create(admin_user)

    return redirect(url_for('views.home'))

@api_scope.route('/admin_users/<id_>', methods=['PUT'])
def update(id_):
    data = request.data

    admin_user = Admin_user(admin_id=id_, name=data["name"])

    admin_user_new = admin_users_controller.update(admin_user)

    return jsonify(admin_user_new._asdict())

@api_scope.route('/admin_users/<id_>', methods=['DELETE'])
def delete(id_):
    admin_user = Admin_user(admin_id=id_)

    admin_user_new = admin_users_controller.delete(admin_user)

    return jsonify(admin_user_new._asdict())
from flask import Blueprint, url_for, request

users = Blueprint('users', __name__)


@users.route('/users')
def get_users():
    method = request.method

    if (method == "POST"):
        return 'Arquivo salvo', 201

    else:
        return 'OK' + url_for('users.get_user')

@users.route('/user')
def get_user():
    method = request.method

    if (method == "POST"):
        return 'Arquivo salvo', 201

    else:
        return ok
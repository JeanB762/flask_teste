from flask import Blueprint, url_for, request

publics = Blueprint('publics',__name__, url_prefix='/public')

@publics.route('/')
def get_home():
    return 'ok'

@publics.route('/contato')
def get_contato():
    return 'contatos'
from flask import Blueprint

usuario = Blueprint('Usuario', __name__)


@usuario.route('/api/v1/account/user')
def users():
    return 'Eu sou um usuário'
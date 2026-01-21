from flask import Blueprint, request, jsonify
from app.services.user_service import UserService
from app.utils.response import success_response, error_response

user_bp = Blueprint('user', __name__, url_prefix='/api/user')


@user_bp.route('/list')
def list():
    users = UserService.index()
    return success_response(users)

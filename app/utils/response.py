from flask import jsonify


def success_response(data=None, message='success', code=200):
    return jsonify({"code": code, "message": message, "data": data or {}}), code


def error_response(data=None, message='faild', code=400):
    return jsonify({"code": code, "message": message, "data": data or {}}), code

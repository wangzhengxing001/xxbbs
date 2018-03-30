from flask import jsonify


class RestFuls(object):
    success = 200
    unauth_error = 400
    not_found = 404
    server_error = 500
    param_error = 401


def get_httpstatus(code, message, data):
    return jsonify({"code": code, "message": message, "data": data})


def success(message, data=""):
    return get_httpstatus(RestFuls.success, message, data=data)


def not_found():
    return get_httpstatus(RestFuls.not_found, message="您要找的资源没找到!", data="")


def server_error():
    return get_httpstatus(RestFuls.server_error, message="网络错误!", data="")


def unauth_error():
    return get_httpstatus(RestFuls.unauth_error, message="您还没有此权限", data="")


def param_error(message="参数错误!"):
    return get_httpstatus(RestFuls.param_error, message=message, data="")
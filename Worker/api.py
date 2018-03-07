from flask_httpauth import HTTPBasicAuth
from flask_restful import Resource, Api, reqparse
from flask_restful import abort as fr_abort


auth = HTTPBasicAuth()


@auth.verify_password
def verify_password(username, password):
    """
    Authentication method.
    """
    return username == config.LOGIN_USERNAME and \
           password == config.LOGIN_PASSWORD


class Worker(Resource):
    """
    The Worker resource (/worker endpoint)
    """

    def get(self):
        return "WORKER GET"

    @auth.login_required
    def post(self):
        return "WORKER POST"
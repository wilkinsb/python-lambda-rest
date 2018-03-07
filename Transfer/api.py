from flask_httpauth import HTTPBasicAuth
from flask_restful import Resource, reqparse
from flask_restful import abort as fr_abort

import config

auth = HTTPBasicAuth()


@auth.verify_password
def verify_password(username, password):
    """
    Authentication method.
    """
    return username == config.LOGIN_USERNAME and \
           password == config.LOGIN_PASSWORD


class Transfer(Resource):
    """
    The Transfer resource (/transfer endpoint)
    """

    def get(self):
        return "Transfer GET"

    @auth.login_required
    def post(self):
        return "Transfer POST"
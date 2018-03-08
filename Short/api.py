from flask_restful import Resource
from flask_httpauth import HTTPBasicAuth

import config


auth = HTTPBasicAuth()


@auth.verify_password
def verify_password(username, password):
    """
    Authentication method.
    """
    return username == config.LOGIN_USERNAME and \
           password == config.LOGIN_PASSWORD


class ShortTask(Resource):
    """
    The short task (<5 min) resource (/short endpoint)
    """

    def get(self):
        return "Short GET"

    @auth.login_required
    def post(self):
        return "Short POST"
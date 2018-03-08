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


class LongTask(Resource):
    """
    The long task (>5min) resource (/long endpoint)
    """
    @auth.login_required
    def get(self):
        return "Long task GET"

    @auth.login_required
    def post(self):
        return "Long task POST"
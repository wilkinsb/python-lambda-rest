from flask_restful import Resource
from flask_httpauth import HTTPBasicAuth

import config
import helpers
import utils


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
        # Can do a short task here, anything that will not take more than 5 min
        # Need to be sure AWS lambda setting for this function is at 5 min
        # Or that this short function will not take longer than whatever AWS is set to
        return "Short POST"
from flask_restful import Resource, reqparse
from flask_httpauth import HTTPBasicAuth

import config
import Long_utils


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
        # Must start an EC2 instance here in order to do work that will take longer than 5 min
        # Make this extendable by providing a util package with some form of start_instances()

        # Parse args given with request, make avail via dict "arg" ie. arg['arg1']
        parser = reqparse.RequestParser()
        parser.add_argument("arg1")
        parser.add_argument("arg2")
        args = parser.parse_args()

        # Load arg data into env variable by name
        # This variable will be used as our environment on the instance
        env = {
            "arg1": arg['arg1'],
            "arg2": arg['arg2']
        }

        user_data = Long_utils.get_user_data(**env)
        ami_id = Long_utils.find_image("us-west-2")

        response = Long_utils.start_instances(user_data, env, ami_id)

        return response
import os

from flask import Flask
from flask_httpauth import HTTPBasicAuth
from flask_restful import Resource, Api, reqparse
from flask_restful import abort as fr_abort

app = Flask(__name__)

auth = HTTPBasicAuth()


@auth.verify_password
def verify_password(username, password):
    """
    Authentication method.
    """
    return username == os.getenv('LOGIN_USERNAME') and \
           password == os.getenv('LOGIN_PASSWORD')


class Worker(Resource):
    """
    The Worker resource (/worker endpoint)
    """

    def get(self):
        """
        GET method for /worker resource
        """
        pass

    @auth.login_required
    def post(self):
        """
        POST method for /worker resource
        """
        pass


# We only need this for local development.
if __name__ == '__main__':
    app.run()

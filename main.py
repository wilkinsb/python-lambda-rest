from flask import Flask
from flask_restful import Api
from flask_httpauth import HTTPBasicAuth

from Long.api import LongTask
from Short.api import ShortTask
import config


app = Flask(__name__)
api = Api(app)


auth = HTTPBasicAuth()


@auth.verify_password
def verify_password(username, password):
    """
    Authentication method.
    """
    return username == config.LOGIN_USERNAME and \
           password == config.LOGIN_PASSWORD


api.add_resource(ShortTask, "/short")
api.add_resource(LongTask, "/long")


# We only need this for local development.
if __name__ == '__main__':
    app.run()

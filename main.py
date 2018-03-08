from flask import Flask
from flask_restful import Api

from Long.api import LongTask
from Short.api import ShortTask


app = Flask(__name__)
api = Api(app)


api.add_resource(ShortTask, "/short")
api.add_resource(LongTask, "/long")


# We only need this for local development.
if __name__ == '__main__':
    app.run()

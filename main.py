from flask import Flask
from flask_restful import Api

from Worker.api import Worker

app = Flask(__name__)
api = Api(app)


api.add_resource(Worker, "/worker")


# We only need this for local development.
if __name__ == '__main__':
    app.run()

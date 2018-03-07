from flask import Flask
from flask_restful import Api

from Worker.api import Worker
from Builder.api import Builder
from Datastore.api import Datastore
from Transfer.api import Transfer

app = Flask(__name__)
api = Api(app)


api.add_resource(Worker, "/worker")
api.add_resource(Builder, "/builder")
api.add_resource(Datastore, "/datastore")
api.add_resource(Transfer, "/transfer")


# We only need this for local development.
if __name__ == '__main__':
    app.run()

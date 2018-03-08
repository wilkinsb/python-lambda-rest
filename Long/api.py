from flask_restful import Resource


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
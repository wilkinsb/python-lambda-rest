from flask_restful import Resource


class ShortTask(Resource):
    """
    The short task (<5 min) resource (/short endpoint)
    """

    def get(self):
        return "Short GET"

    @auth.login_required
    def post(self):
        return "Short POST"
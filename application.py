from werkzeug.exceptions import HTTPException
from database.database import create_app
from views import *
from model import *
import os

application = create_app()


@application.errorhandler(404)
@application.errorhandler(403)
@application.errorhandler(400)
@application.errorhandler(409)
@application.errorhandler(500)
def handle_error(e):
    code = 500
    if isinstance(e, HTTPException):
        code = e.code
    return jsonify(error=str(e.description), code=code), code

api_prefix = "/api/v1/"
AlarmersView.register(application, route_prefix=api_prefix)
UsersView.register(application, route_prefix=api_prefix)

if __name__ == '__main__':
    with application.app_context():
        db.create_all()
        application.run(port=int(os.getenv("APP_PORT", "5000")), debug=True)


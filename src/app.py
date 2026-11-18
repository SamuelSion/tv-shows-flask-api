from flask import Flask
from controllers.show_controller import router as show_router
from http import HTTPStatus
from werkzeug.exceptions import NotFound, BadRequest

# Create server:
server = Flask(__name__)

# Register controllers:
server.register_blueprint(show_router)


@server.errorhandler(HTTPStatus.NOT_FOUND)
def not_found(err: NotFound):
    print(err)
    return { "message": err.description }, HTTPStatus.NOT_FOUND


@server.errorhandler(HTTPStatus.BAD_REQUEST)
def bad_request(err: BadRequest):
    print(err)
    return { "message": err.description }, HTTPStatus.BAD_REQUEST


@server.errorhandler(Exception)
def catch_all(err: Exception):
    print(err)
    return { "message": str(err) }, HTTPStatus.INTERNAL_SERVER_ERROR


# Create env folder:            py -m venv env
# Run env folder:               env/scripts/activate or for Mac: source env/bin/activate
# Install lib:                  pip install flask
# Install lib:                  pip install requests
# Create requirements.txt file: pip freeze > requirements.txt
# Restore libraries:            pip install -r requirements.txt

# Running (in the terminal):
# flask --app src/app.py run --debug --port 4000

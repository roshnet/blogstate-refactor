import flask

app = flask.Flask(__name__)

from blogstate import routes

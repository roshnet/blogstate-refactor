import flask
import os

app = flask.Flask(__name__)
app.config['SECRET_KEY'] = os.urandom(11)

from blogstate import routes    # noqa

from blogstate import app
from blogstate.api import HOST
from flask import (
    render_template,
    request
)
import os
import requests


@app.route('/signin')
@app.route('/login', methods=['GET', 'POST'])
def login():
    """
    Handler logic for the `/login` route.

    On GET, renders the corresponding template.
    On POST, fetches validation status and user information.
    """
    if request.method == 'GET':
        return render_template("auth/login.html")

    # On POST request #
    payload = {
        "username": request.form.get('username'),
        "passwd": request.form.get('passwd')
    }
    endpoint = os.path.join(HOST, 'login')
    auth_status = requests.post(endpoint, json=payload)

    return auth_status.content

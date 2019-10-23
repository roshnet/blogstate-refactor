from blogstate import app
from flask import (
    render_template,
    request
)


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

from blogstate import app
from flask import (
    render_template,
    request
)


@app.route('/join')
@app.route('/signup', methods=['GET', 'POST'])
def signup():
    """
    Handler logic for the `/signup` route.

    On GET, renders the corresponding template.
    On POST, performs API call to create user with specified fields.
    """
    if request.method == 'GET':
        return render_template("auth/signup.html")

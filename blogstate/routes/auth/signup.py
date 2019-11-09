from blogstate import app
from blogstate.api import SecureAgent
from flask import (
    render_template,
    request,
    session
)

agent = SecureAgent()


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
    
    # On POST requests #
    info = {
        "username": request.form.get('username'),
        "email": request.form.get('email'),
        "passwd": request.form.get('passwd'),
        "name": request.form.get('name'),
    }

    status = agent.signup(info)
    if status:
        # Proceed to setting session variables,
        # and redirect to dashboard or something.
        session['logged_in'] = True
        return "Your account has been created. Proceeding to dashboard."

    return render_template("auth/signup.html",
                            issue='Sorry, the username is not available')

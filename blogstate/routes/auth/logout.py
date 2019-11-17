from blogstate import app
from flask import (
    redirect,
    session
)


@app.route('/logout/')
def logout():
    if 'logged_in' in session.keys():
        session.pop('logged_in')
    if 'username' in session.keys():
        session.pop('username')
    return redirect('/login')

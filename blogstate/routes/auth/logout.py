from blogstate import app
from flask import (
    redirect,
    session
)


@app.route('/logout/')
def logout():
    if 'logged_in' in session.keys():
        session['logged_in'] = None
    return redirect('/login')

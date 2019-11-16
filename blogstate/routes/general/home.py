from blogstate import app
from flask import (
    render_template,
    redirect, session,
    url_for
)


@app.route('/')
def home():
    if 'username' in session.keys():
        if session['logged_in'] and session['username']:
            return redirect(url_for('dashboard',
                            username=session['username']))
    return render_template("home.html")

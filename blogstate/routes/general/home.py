from blogstate import app
from blogstate.api import SecureAgent
from flask import (
    render_template,
    redirect, session,
    url_for
)

agent = SecureAgent()


@app.route('/')
def home():
    if 'username' in session.keys():
        if session['logged_in'] and session['username']:
            # User is authenticated -> render dashboard
            username = session['username']
            user = agent.fetch_user_info(username)
            titles = agent.fetch_post_titles(username)
            if user and titles is not False:
            # Explicitly checking `titles` as a blank list
            # evaluates to False
                return render_template("members/dashboard.html",
                                       user=user,
                                       titles=titles)
    return render_template("home.html")

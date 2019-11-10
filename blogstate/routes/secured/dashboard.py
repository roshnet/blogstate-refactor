"""
Configures everything for the dashboard.
"""

from blogstate import app
from blogstate.api import SecureAgent
from flask import (
    render_template,
    redirect,
    session
)

agent = SecureAgent()


@app.route('/<username>/dashboard')
def dashboard(username):
    # Check authentication
    if 'username' not in session.keys():
        return redirect('/login')
    
    # Check authorization
    if not username == session['username']:
        return redirect('/{}/dashboard'.format(username))

    user = agent.fetch_info(username)
    return render_template("members/dashboard.html",
                           user=user)

"""
Configures everything for the dashboard.
"""

from blogstate import app
from blogstate.api import SecureAgent
from flask import (
    redirect, render_template,
    session, url_for
)

agent = SecureAgent()


@app.route('/<username>/dashboard/')
def dashboard(username):
    # Check authentication
    if 'username' not in session.keys():
        return redirect('/login')

    # Check authorization
    if not username == session['username']:
        return redirect('/{}/dashboard'.format(username))

    # NOTE: Possible use-case of GraphQL
    user = agent.fetch_user_info(username)
    titles = agent.fetch_post_titles(username)
    if user and titles is not False:
        # Explicitly checking `titles` as a blank list evaluates to False
        return render_template("members/dashboard.html",
                               user=user,
                               titles=titles)
    return redirect(url_for('blog', username=session['username']))

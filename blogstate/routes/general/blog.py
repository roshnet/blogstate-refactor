from blogstate import app
from blogstate.api import SecureAgent
from flask import (
    render_template,
    redirect,
    session
)

agent = SecureAgent()


@app.route('/<username>')
def blog(username):
    """Fetch and display publically visible blogs"""
    posts = agent.fetch_posts(username)
    return render_template("posts.html",
                           posts=posts,
                           author=username)

from blogstate import app
from blogstate.api import SecureAgent
from flask import render_template

agent = SecureAgent()


@app.route('/<username>')
def blog(username):
    """Fetch and display publically visible blog posts by an author"""
    posts = agent.fetch_posts_by_author(username)
    return render_template("posts.html",
                           posts=posts,
                           author=username)

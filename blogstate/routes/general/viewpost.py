from blogstate import app
from blogstate.api import SecureAgent
from flask import render_template, session
from markdown import markdown

agent = SecureAgent()


@app.route('/<username>/post/<post_url>/')
def get_post(username, post_url):
    post = agent.fetch_post_by_id(username, post_url)
    post['body'] = markdown(post['body'])
    return render_template("view.html",
                           user=session,
                           post=post)

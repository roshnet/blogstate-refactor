from blogstate import app
from blogstate.api import SecureAgent
from flask import (
    render_template,
    request,
    session
)

agent = SecureAgent()


@app.route('/new', methods=['GET', 'POST'])
def new():
    if request.method == 'GET':
        return render_template("members/new.html",
                               user=session)

    status = agent.publish({
        "author_uid": session['user_id'],
        "title": request.form.get('title'),
        "body": request.form.get('body'),
    })

    if status:
        return f"Your post was published."
    return render_template("members/new.html",
                           issue='Something was not right with your post.')

from blogstate import app
from blogstate.api import SecureAgent
from flask import (
    render_template,
    redirect, request,
    session, url_for
)

agent = SecureAgent()


@app.route('/new/', methods=['GET', 'POST'])
def new():
    # Check authentication
    if 'username' not in session.keys():
        return redirect('/login')

    # Clear to proceed
    if request.method == 'GET':
        return render_template("members/new.html",
                               user=session)

    status = agent.publish({
        "author_uid": session['user_id'],
        "title": request.form.get('title'),
        "body": request.form.get('body'),
        "preview_text": request.form.get('preview-text')
    })

    if status:
        return redirect(url_for('blog', username=session['username']))
    return render_template("members/new.html",
                           user=session,
                           issue='Something was not right with your post.')

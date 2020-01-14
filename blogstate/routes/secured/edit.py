from blogstate import app
from blogstate.api import SecureAgent
from flask import (
    request, render_template,
    redirect, session, url_for
)

agent = SecureAgent()


@app.route('/edit/', methods=['GET', 'POST'])
def edit():
    if 'username' not in session.keys():
        return redirect(url_for('login'))

    if request.method == 'GET':
        author = request.args.get('author')
        post_idf = request.args.get('post')
        if author and post_idf:
            if author == session['username']:
                post = agent.fetch_post_by_id(author, post_idf)
                if post:
                    return render_template("members/edit.html",
                                           user=session,
                                           old_post=post)
                return render_template('404.html')
            return render_template("403.html")
        return render_template('404.html')

    # :POST: Perform a PUT request to update existing post #

    post_idf = request.form.get('idf')
    status = agent.update_post_by_id(session['username'], post_idf, {
        "title": request.form.get('title'),
        "body": request.form.get('body'),
        "preview_text": request.form.get('preview-text')
    })

    if status:
        return redirect('/{}/post/{}/'.format(
            session['username'], post_idf
        ))

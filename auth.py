from flask import request, session, abort

def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        if username == 'admin' and password == 'password':
            session['username'] = username
            abort(200)
        else:
            abort(404)

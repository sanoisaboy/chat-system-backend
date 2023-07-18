from flask import request, session
from mongodb import db

collection = db['User']



def login(): 
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        user_document = collection.find_one({})
        print(user_document)    
        if username == 'admin' and password == 'password':
            session['username'] = username
            return 'Login successful',200
        else:
            return 'Login failed',404


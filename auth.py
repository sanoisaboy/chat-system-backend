from flask import request, Blueprint, session
from db import db

collection = db['User']
auth_bp = Blueprint('auth', __name__)


@auth_bp.route('/login', methods=['GET', 'POST'])
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


@auth_bp.route('/sign', methods=['POST'])
def signup():
    if request.method =='POST':
        username = request.form['username']
        password = request.form['password']
        print(username)
        exit_user = collection.find_one({"name":username})
        if exit_user is None:
            collection.insert_one({"name":username,"password":password})
            return 'Sign up successful',200
        else:
            return 'Sign up failed',404
        

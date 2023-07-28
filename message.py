from flask import request, session
from app import app
from db import db

collection = db['Message']


@app.route("/message/get")
def get_message():
    if request.method =='GET':
        print(123)
        return 0

from flask import request, Blueprint
from db import db

collection = db['Message']
message_bp = Blueprint('message', __name__)


@message_bp.route('/message/get', methods=['GET'])
def get_message():
    print(request.url)
    return "get message success", 200


@message_bp.route('/message/post', methods=['POST'])
def post_message():
   return "post message success"

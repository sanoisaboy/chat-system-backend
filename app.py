from flask import Flask, render_template
from flask_socketio import SocketIO, emit
from pymongo.mongo_client import MongoClient
from auth import auth_bp
from message import message_bp
#from auth import login,signup 

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app)


app.register_blueprint(auth_bp)
app.register_blueprint(message_bp)
#app.route('/signup',methods=['POST'])(signup)


@socketio.on('message')
def handle_message(message):
    print('Received message:'+message)
    emit('message', message, broadcast=True)


if __name__ == '__main__':
    socketio.run(app, port=8002, debug=True)

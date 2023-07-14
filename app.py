from flask import Flask, render_template
from flask_socketio import SocketIO, emit
from auth import login 

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app)


@app.route('/login', methods=['GET', 'POST'])(login)


@socketio.on('message')
def handle_message(message):
    print('Received message:'+message)
    emit('message', message, broadcast=True)


if __name__ == '__main__':
    socketio.run(app)

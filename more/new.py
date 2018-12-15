from flask import Flask, render_template
from flask_socketio import SocketIO


from flask import Flask, render_template
from flask_session import Session
from flask_socketio import SocketIO, emit

app = Flask(__name__)
Session(app)
socketio = SocketIO(app, manage_session=False)

@app.route('/')
def index():
    return render_template('home.html')

@app.route('/session', methods=['GET', 'POST'])
def session_access():
    pass

@socketio.on('get-session')
def get_session():
    pass

@socketio.on('set-session')
def set_session(data):
    pass

@socketio.on('message')
def handle_message(message):
    print('received message: ' + str(message))
    if message['answer'] == '宝塔镇河妖':
        emit('my_response', {'data': 'correct'})
    else:
        emit('my_response', {'data': 'wrong'})
if __name__ == '__main__':
    print('http://127.0.0.1:80')
    socketio.run(app,host='127.0.0.1',port=80)
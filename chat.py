from flask import Flask,render_template
from flask_socketio import SocketIO,emit

app=Flask(__name__)
app.config['SECRET_KEY']='secret!'
socketio=  SocketIO(app)

@app.route('/',methods=['GET','POST'])
def home():
    return render_template('home.html')


@socketio.on('connect')
def handle_connect():
    log('connect')
    print('connected!')
    reply = '''Hi, this is Kang'''
    # reply=input('reply:\n')
    socketio.emit('say_hi',{'data': reply})

@socketio.on('disconnect')
def handle_disconnect():
    print('disconnected!')

@socketio.on('message')
def handle_message(msg):
    log('messagge')
    print(msg['data'])
    reply='hi'
    #reply=input('reply:\n')
    socketio.send({'data':reply})

@socketio.on('say_hi')
def handle_say_hi(msg):
    log('say_hi')
    print(msg['data'])
    socketio.send({'data':'OK.'})

######################
def log(event):
    print('-->>>{}:  '.format(event),end='')
if __name__=="__main__":
    addr=('0.0.0.0',80)
    print('http://127.0.0.1:80...')
    #print('Serve on http://{}:{}'.format(addr[0],addr[1]))
    socketio.run(app,host=addr[0],port=addr[1])



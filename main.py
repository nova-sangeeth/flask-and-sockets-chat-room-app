from flask import Flask, render_template
from flask_socketio import SocketIO
app = Flask(__name__)
app.config['SECRET_KEY'] = 'novasangeeth'
socketio = SocketIO(app)

@app.route('/')
def sessions():
    return render_template('sessions.html')

def messageRecieved(methods=['GET','POST']):
    print('message was recieved')

@socketio.on('my event')
def handle_my_custom_event (json, methods=['GET','POST']):
    print('recieved my event' +str(json))
    socketio.emit('my response', json, callback=messageRecieved)


if __name__ =='__main__':
    socketio.run(app, debug= True)
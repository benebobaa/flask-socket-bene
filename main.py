from flask import Flask, jsonify
import os
from flask_socketio import SocketIO, emit

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app, cors_allowed_origins='*')


@app.route('/')
def index():
    return jsonify({"Choo Choo": "Welcome to your Flask app 🚅"})

@socketio.on('connect')
def handle_connect():
    print('Client connected')

@socketio.on('disconnect')
def handle_disconnect():
    print('Client disconnected')


@socketio.on('client_event')
def handle_client_event(data):
    print('Received event from client:', data)
    print('cek 3')
    emit('server_response', 'Hello from the server', broadcast=True)


if __name__ == '__main__':
    socketio.run(app, debug=True, port=os.getenv("PORT", default=8000))
    # app.run(debug=True, port=os.getenv("PORT", default=5000))

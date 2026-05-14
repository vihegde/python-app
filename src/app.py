from flask import Flask, jsonify
import datetime
import socket

app = Flask(__name__)

@app.route('/api/v1/details')
def details():
    return jsonify({
        'message':'Hello World',
        'time': datetime.datetime.now().strftime("%I:%M%p on %B %d, %Y"),
        'hostname':socket.gethostname(),
        'message':'You are doing g8-!!!!!---> :)'
    })


@app.route('/api/v1/healthz')
def health():
    return jsonify ({
        'status':'UP'
    })
if __name__ == '__main__':
    app.run(host="0.0.0.0")






#'
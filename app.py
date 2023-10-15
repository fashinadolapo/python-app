from flask import Flask, jsonify
import time

app = Flask(__name__)

@app.route('/api', methods=['GET'])
def get_message():
    current_timestamp = int(time.time())
    message = "Automate all the things!"
    return jsonify({"message": message, "timestamp": current_timestamp})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)

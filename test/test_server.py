from flask import Flask, jsonify
from flask import request

app = Flask(__name__)


@app.route('/test', methods=['POST'])
def get_task():
    print('here :', request.json)
    return jsonify({'data': 'None'}), 200


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)

from flask import Flask, request, make_response, jsonify

from data_scheduler import DataScheduler

app = Flask(__name__)


@app.route('/')
def index():
    return "autistic screeching"


@app.route('/prediction/full_sum', methods=['GET'])
def do_task():
    if not request.json:
        make_response(jsonify({'message': 'Bad input'}), 404)
    if 'user_id' not in request.json:
        make_response(jsonify({'message': 'no user_id'}), 405)
    if 'data' not in request.json:
        make_response(jsonify({'message': 'no data'}), 406)
    data_scheduler.add_data_to_predict(request.json)
    return make_response(jsonify({'message': 'ok'}), 200)


@app.route('/prediction/rest_of_sum', methods=['GET'])
def do_task():
    if not request.json:
        make_response(jsonify({'message': 'Bad input'}), 404)
    if 'user_id' not in request.json:
        make_response(jsonify({'message': 'no user_id'}), 405)
    if 'data' not in request.json:
        make_response(jsonify({'message': 'no data'}), 406)
    if 'predicted_sum' not in request.json:
        make_response(jsonify({'message': 'no predicted_sum'}), 407)
    data_scheduler.add_data_to_predict(request.json)
    return make_response(jsonify({'message': 'ok'}), 200)


@app.route('/prediction/category_distribution', methods=['GET'])
def do_task():
    if not request.json:
        make_response(jsonify({'message': 'Bad input'}), 404)
    if 'user_id' not in request.json:
        make_response(jsonify({'message': 'no user_id'}), 405)
    if 'data' not in request.json:
        make_response(jsonify({'message': 'no data'}), 406)
    data_scheduler.add_data_to_predict_category_distribution(request.json)
    return make_response(jsonify({'message': 'ok'}), 200)


@app.route('/statistic/category_distribution', methods=['GET'])
def do_task():
    return make_response(jsonify({'message': 'ok'}), 200)


@app.route('/statistic/check_info_days', methods=['GET'])
def do_task():
    return make_response(jsonify({'message': 'ok'}), 200)


@app.route('/statistic/check_info_weeks', methods=['GET'])
def do_task():
    return make_response(jsonify({'message': 'ok'}), 200)


@app.route('/statistic/check_info_months', methods=['GET'])
def do_task():
    return make_response(jsonify({'message': 'ok'}), 200)


@app.route('/statistic/check_info_years', methods=['GET'])
def do_task():
    return make_response(jsonify({'message': 'ok'}), 200)


if __name__ == '__main__':
    data_scheduler = DataScheduler()
    app.run(debug=False)

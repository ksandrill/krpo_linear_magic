import logging
import os

from flask import Flask, request, make_response

from worker_threads.data_scheduler import DataScheduler


def init_flask() -> Flask:
    app = Flask(__name__)

    @app.route('/')
    def index():
        return "autistic screeching"

    @app.route('/prediction/full_sum', methods=['GET'])
    def get_full_sum_prediction():
        if not request.json or 'user_id' not in request.json or 'data' not in request.json:
            make_response({'message': 'Bad input'}, 404)
        data_scheduler.add_data_to_predict_sum(request.json)
        return make_response({'message': 'ok'}, 200)

    @app.route('/prediction/sum_category_distribution', methods=['GET'])
    def get_category_sum_dist_prediction():
        if not request.json or 'user_id' not in request.json or 'data' not in request.json:
            make_response(({'message': 'Bad input'}), 404)
        data_scheduler.add_data_to_predict_sum_category_distribution(request.json)
        return make_response({'message': 'ok'}, 200)

    @app.route('/prediction/items_category_distribution', methods=['GET'])
    def get_category_item_dist_prediction():
        if not request.json or 'user_id' not in request.json or 'data' not in request.json:
            make_response(({'message': 'Bad input'}), 404)
        data_scheduler.add_data_predict_item_category_distribution(request.json)
        return make_response({'message': 'ok'}, 200)

    return app


logging.basicConfig(format='%(asctime)s,%(msecs)d %(levelname)-8s [%(filename)s:%(lineno)d] %(message)s',
                    datefmt='%Y-%m-%d:%H:%M:%S',
                    level=logging.DEBUG, filename='logs/app_logs.log')

if __name__ == '__main__':
    backend_url = os.environ.get("BACKEND_URL")
    if not backend_url:
        raise Exception('please set BACKEND_URL')
    data_scheduler = DataScheduler(backend_url=backend_url)
    app_ = init_flask()
    app_.run(host="0.0.0.0", port=8080, debug=False)

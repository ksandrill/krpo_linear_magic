import numpy as np

from algos import predict_full_month_sum, get_rest_money_on_month, linear_predict_model


class Predictor:
    def __init__(self, types, raw_data_to_predict: list, ready_to_send_messages: list):
        self.types = types
        self.raw_data_to_predict = raw_data_to_predict
        self.ready_to_send = ready_to_send_messages

    def do_predictor_work(self):
        # print('do predictor work')
        if self.raw_data_to_predict:
            datum = self.raw_data_to_predict.pop()
            answer = self.predict(datum)
            self.ready_to_send.append(answer)

    def predict(self, datum):
        oper_type, data_dic = datum
        output = None
        if oper_type == self.types['predict_on_month']:
            checks_sums = np.array(data_dic['data'])
            output = predict_full_month_sum(checks_sums)
        elif oper_type == self.types['calculate_rest_of_money']:
            checks_sums = np.array(data_dic['data'])
            predicted_sum = float(data_dic['predicted_sum'])
            output = get_rest_money_on_month(checks_sums, predicted_sum)
        elif oper_type == self.types['calculate_next_category_dist']:
            category_data = data_dic['data']
            output = {}
            for category in category_data.keys():
                predicted_for_category = linear_predict_model(category_data[category], intervals=4)
                output.update({category: predicted_for_category})
        return {'user_id': data_dic['user_id'], 'operation_type': oper_type, 'result': output}

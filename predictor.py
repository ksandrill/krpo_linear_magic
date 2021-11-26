import logging

from algos import predict_full_month_sum, predict_category_sum_distribution, predict_category_items_distribution

PREDICT_SUM_ON_NEXT_MONTH = 1
PREDICT_CATEGORY_SUM_DIST_ON_NEXT_MONTH = 2
PREDICT_CATEGORY_ITEMS_DIST_ON_NEXT_MONTH = 3

prediction_functions = {PREDICT_SUM_ON_NEXT_MONTH: predict_full_month_sum,
                        PREDICT_CATEGORY_SUM_DIST_ON_NEXT_MONTH: predict_category_sum_distribution,
                        PREDICT_CATEGORY_ITEMS_DIST_ON_NEXT_MONTH: predict_category_items_distribution}


def predict(datum):
    oper_type, data_dic = datum
    logging.info(datum)
    predict_func = prediction_functions[oper_type]
    if predict_func is None:
        logging.error(oper_type)
        raise ValueError("incorrect operation type")
    output = predict_func(data_dic['data'])
    out = {'user_id': data_dic['user_id'], 'operation_type': oper_type, 'result': output}
    logging.info(out)
    return out


class Predictor:
    def __init__(self, raw_data_to_predict: list, ready_to_send_messages: list):
        self.raw_data_to_predict = raw_data_to_predict
        self.ready_to_send = ready_to_send_messages

    def do_predictor_work(self):
        # print('do predictor work')
        if self.raw_data_to_predict:
            datum = self.raw_data_to_predict.pop()
            answer = predict(datum)
            self.ready_to_send.append(answer)

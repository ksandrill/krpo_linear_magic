import numpy as np
from sklearn.linear_model import LinearRegression

def linear_predict_model(checks_sum: np.ndarray, intervals: int) -> float:
    sum_datum = np.array_split(checks_sum, intervals)
    y = np.array([i.sum() for i in sum_datum])
    x = np.array([[i] for i in range(len(y) - 1)])
    y = np.array([y[:i].sum() for i in range(len(y))])[1:]
    reg = LinearRegression()
    reg.fit(x, y)
    reg.intercept_ = y[-1]
    predict_list = []
    for i in range(intervals):
        predict = reg.predict([[i]])[0]
        predict_list.append(predict)
    predict_to_next_month = predict_list[-1]
    return predict_to_next_month


def predict_full_month_sum(checks_sum_per_month: np.ndarray) -> float:
    return linear_predict_model(checks_sum_per_month, intervals=4)


def get_rest_money_on_month(checks_sum_in_this_month: np.ndarray, predicted_sum: float) -> float:
    sum_of_checks = checks_sum_in_this_month.sum()
    return predicted_sum - sum_of_checks
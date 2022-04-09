from src.group4package import metrics_function
import pandas as pd

TN = 40
FP = 5
FN = 10
TP = 45
data = data = {
    "recall": [0.818],
    "precision": [0.9],
    "f1 score": [0.857],
}
df = pd.DataFrame(data)


# Test that invalid inputs result in ValueError
def test_invalid_input():

    expected = ValueError
    actual = metrics_function.calculate_metrics(40.2, 12.0, 67.99)
    assert isinstance(actual, expected)



# Test if it produces correct data frame
def test_metrics():
    res = metrics_function.calculate_metrics(FP, FN, TP)

    pd.testing.assert_frame_equal(res, df)

# Test that the metric values are correct
def test_metrics_values():
    res = metrics_function.calculate_metrics(FP, FN, TP)
    assert df.iat[0, 0] == res.iat[0, 0]
    assert df.iat[0, 1] == res.iat[0, 1]
    assert df.iat[0, 2] == res.iat[0, 2]


TN1 = 40
FP1 = 5
FN1 = 10
TP1 = 45
recall = TP1 / (TP1 + FN1)
precision = TP1 / (TP1 + FP1)
f1_score = (2 * precision * recall) / (precision + recall)

data1 = data = {
    "recall": [recall],
    "precision": [precision],
    "f1 score": [f1_score],
}
df1 = pd.DataFrame(data1)

# Test that the function rounds numbers properly
def test_metrics_round():

    res = metrics_function.calculate_metrics(FP, FN, TP)

    assert df1.iat[0, 0] != res.iat[0, 0]
    assert df1.iat[0, 1] == res.iat[0, 1]
    assert df1.iat[0, 2] != res.iat[0, 2]

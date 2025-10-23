import joblib
import numpy as np

def test_model_predicts():
    obj = joblib.load("model.joblib")
    model = obj["model"]
    X = np.array([[5.1, 3.5, 1.4, 0.2]])
    preds = model.predict(X)
    assert preds.shape == (1,)

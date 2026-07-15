import pytest
from ml.model import train_model, compute_model_metrics, inference
from sklearn.ensemble import RandomForestClassifier


def test_train_model():
    """
    Tests that the train_model() returns a RandomForestClassifier instance.
    """
    X_train = [
        [0, 1],
        [1, 0], 
        [1, 1],
        [0, 0]
    ]
    
    y_train = [0, 1, 1, 0]
    
    model = train_model(X_train, y_train)
    
    assert isinstance(model, RandomForestClassifier)


def test_model_metrics():
    """
    Tests that compute_model_metrics returns the expected scores.
    """
    y_train = [1, 1, 1, 0]
    preds = [1, 0, 0, 1]

    precision, recall, fbeta = compute_model_metrics(y_train, preds)

    assert precision == pytest.approx(0.5)
    assert recall == pytest.approx(1 / 3)
    assert fbeta == pytest.approx(0.4)  


def test_inference():
    """
    Tests that inference() returns one prediction for each input.
    """
    X_train = [
        [0, 1],
        [1, 0], 
        [1, 1],
        [0, 0]
    ]

    y_train = [0, 1, 1, 0]

    model = train_model(X_train, y_train)

    preds = inference(model, X_train)

    assert len(preds) == len(X_train)
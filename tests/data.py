import pytest


@pytest.fixture
def low_risk_data():
    return "model.add(Dense(8, activation='relu'))\nmodel.add(Dense(8, activation='sigmoid'))"


@pytest.fixture
def medium_risk_data():
    return "".join(["model.add(Dense(8, activation='relu'))\n" for _ in range(1, 15)])


@pytest.fixture
def high_risk_data():
    return "".join(["model.add(Dense(8, activation='relu'))\n" for _ in range(1, 40)])

from utils.reader import Reader
from .data import low_risk_data
from .data import medium_risk_data
from .data import high_risk_data


class TestReader:

    def setup(self):
        self.reader = Reader()

    def test_low_risk(self, low_risk_data):
        result = self.reader.extract_result(file_content=low_risk_data, file_name="test.py")
        assert result == "Found deep neural network with 2 hidden layers in test.py (1 sigmoid(s) activation functions, 1 relu(s) activation functions), posing a low transparency risk."

    def test_medium_risk(self, medium_risk_data):
        result = self.reader.extract_result(file_content=medium_risk_data, file_name="test.py")
        assert result == "Found deep neural network with 14 hidden layers in test.py (0 sigmoid(s) activation functions, 14 relu(s) activation functions), posing a medium transparency risk."

    def test_high_risk(self, high_risk_data):
        result = self.reader.extract_result(file_content=high_risk_data, file_name="test.py")
        assert result == "Found deep neural network with 39 hidden layers in test.py (0 sigmoid(s) activation functions, 39 relu(s) activation functions), posing a high transparency risk."

    def test_extract_result(self):
        pass

    def test_lines_formatter(self):
        pass
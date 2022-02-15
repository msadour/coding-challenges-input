from utils import github
from utils.constants import GITHUB_FILES, GITHUB_USERNAME, GITHUB_REPOSITORY_NAME, GITHUB_FOLDER


class Reader:

    def __init__(self):
        self.results = []

    def results_as_string(self, format="text"):
        if format == "text":
            return '\n\n'.join(self.results)
        return '<br /><br />'.join(self.results)

    @staticmethod
    def lines_formatter(file):
        lines = file.split("\n")
        lines = [line.replace(" ", "") for line in lines if line != "" or "#" not in line]
        return lines

    @staticmethod
    def read_file(file_name):
        return github.get_file(
            username=GITHUB_USERNAME,
            repository_name=GITHUB_REPOSITORY_NAME,
            file_path=GITHUB_FOLDER,
            file_name=file_name
        )

    def extract_result(self, file_content, file_name):
        total_layer = 0
        total_relu = 0
        total_sigmoid = 0
        lines = self.lines_formatter(file_content)
        for line in lines:
            if "'relu'" in line:
                total_layer += 1
                total_relu += 1

            if "'sigmoid'" in line:
                total_layer += 1
                total_sigmoid += 1

        if 9 < total_layer < 19:
            risk = "medium transparency risk"
        elif total_layer > 20:
            risk = "high transparency risk"
        else:
            risk = "low transparency risk"

        result = f"Found deep neural network with {total_layer} hidden layers in {file_name} ({total_sigmoid} sigmoid(s) activation functions, {total_relu} relu(s) activation functions), posing a {risk}."
        return result

    def generate_result(self):
        for file_name in GITHUB_FILES:
            file_content = self.read_file(file_name)
            result = self.extract_result(file_content=file_content, file_name=file_name)
            self.results.append(result)

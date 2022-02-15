"""Reader file."""

from typing import List

from utils import github
from utils.constants import (
    GITHUB_FILES,
    GITHUB_USERNAME,
    GITHUB_REPOSITORY_NAME,
    GITHUB_FOLDER,
)


class Reader:
    """Class Reader."""

    def __init__(self):
        self.results = []

    def results_with_format(self, format_returned="text") -> str:
        """
        Format result.
        Args:
            format_returned: could be html or text
        Returns:
            Content file from github.
        """
        if format_returned == "text":
            return "\n\n".join(self.results)
        elif format_returned == "html":
            return "<br /><br />".join(self.results)
        else:
            raise Exception("Format value should be html or text")

    @staticmethod
    def lines_formatter(file_content: str) -> List:
        """
        Remove space in line or ignore line with comments.
        Args:
            file_content: could be html or text
        Returns:
            Content file from github.
        """
        lines = file_content.split("\n")
        lines = [
            line.replace(" ", "") for line in lines if line != "" or "#" not in line
        ]
        return lines

    @staticmethod
    def read_file(file_name: str) -> str:
        """
        Get content file from github.
        Args:
            file_name:
        Returns:
            Content file from github.
        """
        return github.get_file(
            username=GITHUB_USERNAME,
            repository_name=GITHUB_REPOSITORY_NAME,
            file_path=GITHUB_FOLDER,
            file_name=file_name,
        )

    def extract_result(self, file_content: str, file_name: str) -> str:
        """
        Generate result from file content.
        Args:
            file_content:
            file_name:
        Returns:
            Result.
        """
        total_layer = 0
        total_relu = 0
        total_sigmoid = 0
        lines = self.lines_formatter(file_content=file_content)
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

    def generate_result(self) -> None:
        """
        Extract and put results in the objects.
        """
        for file_name in GITHUB_FILES:
            file_content = self.read_file(file_name)
            result = self.extract_result(file_content=file_content, file_name=file_name)
            self.results.append(result)

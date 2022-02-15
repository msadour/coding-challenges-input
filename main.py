"""Main file."""

import sys

from utils.displayer import as_command_line, as_file_text, as_html
from utils.reader import Reader

if __name__ == "__main__":
    reader = Reader()
    reader.generate_result()
    if len(sys.argv) == 1:
        print("Please select an option : html_file | text_file | line_command")
    elif len(sys.argv) > 2:
        print(
            "Too much arguments. Only one of the following are possible : html_file | text_file | line_command"
        )
    else:
        if sys.argv[1] == "html_file":
            as_html(reader.results_with_format(format_returned="html"))
        elif sys.argv[1] == "text_file":
            as_file_text(reader.results_with_format(format_returned="text"))
        elif sys.argv[1] == "line_command":
            as_command_line(reader.results_with_format(format_returned="text"))
        else:
            print(
                "Command unknown. Please select one of those options : html_file | text_file | line_command"
            )

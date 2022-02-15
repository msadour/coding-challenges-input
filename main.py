import sys

from utils.displayer import as_command_line, as_file_text, as_html
from utils.reader import Reader

if __name__ == "__main__":
    reader = Reader()
    reader.generate_result()

    if sys.argv[1] == "html_file":
        as_html(reader.results_as_string(format="html"))
    elif sys.argv[1] == "text_file":
        as_file_text(reader.results_as_string())
    else:
        as_command_line(reader.results_as_string())

"""Displayer file."""


def as_html(results: str) -> None:
    """
    Create html file from result.
    Args:
        results: information about code risk.
    """
    with open("results/file.html", "w") as f:
        message = (
            """<html>
        <head></head>
        <body><p>"""
            + results
            + """</p></body>
        </html>"""
        )
        f.write(message)


def as_command_line(results: str) -> None:
    """
    Display results in the console.
    Args:
        results: information about code risk.
    """
    print(results)


def as_file_text(results: str) -> None:
    """
    Create text file from result.
    Args:
        results: information about code risk.
    """
    with open("results/file.txt", "w") as f:
        f.write(results)

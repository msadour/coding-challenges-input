def as_html(results: str) -> None:
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
    print(results)


def as_file_text(results: str) -> None:
    with open("results/file.txt", "w") as f:
        f.write(results)

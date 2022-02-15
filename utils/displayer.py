def as_html(results):
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


def as_command_line(results):
    print(results)


def as_file_text(results):
    with open("results/file.txt", "w") as f:
        f.write(results)

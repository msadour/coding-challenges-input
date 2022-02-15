"""github module."""

import base64

import requests


def get_file(
    username: str, repository_name: str, file_path: str, file_name: str
) -> str:
    """
    Get content file from github file.
    Args:
        username:
        repository_name:
        file_path:
        file_name:
    Returns:
        Content file from github.
    """
    headers = {}

    url = f"https://api.github.com/repos/{username}/{repository_name}/contents/{file_path}/{file_name}"
    r = requests.get(url, headers=headers)
    r.raise_for_status()
    data = r.json()
    file_content = data["content"]
    file_content_encoding = data.get("encoding")
    if file_content_encoding == "base64":
        file_content = base64.b64decode(file_content).decode()

    return file_content

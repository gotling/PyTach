import requests


def send(code, connection):
    url = connection["url"].format(code=code)
    connection["payload"]["method"] = code

    return requests.post(url, json=connection["payload"])
import copy
import requests


def send(command, connection):
    url = connection["url"].format(code=command["code"])
    data = copy.deepcopy(connection["payload"])
    data["method"] = command["code"]
    if "params" in command:
        data["params"] = command["params"]

    return requests.post(url, json=data)
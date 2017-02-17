# -*- encoding: utf-8 -*-
import json

def load_json_file(file_path):
    """
    :param str file_path:
    :rtype: list of dictionary
    """
    json_file = "jawiki-country.json"
    json_data = []
    with open(json_file) as f:
        for row in f:
            json_data.append(json.loads(row))

    return json_data


def get_record(json_data, title):
    """
    :param list of dictionary json_data:
    :param title:
    :rtype:str
    """
    for record in json_data:
        if record["title"] == title:
            return record["text"]


if __name__ == "__main__":
    data = load_json_file("jawiki-country.json")
    print(get_record(data, "イギリス"))

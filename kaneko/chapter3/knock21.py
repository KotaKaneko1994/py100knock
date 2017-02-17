# -*- encoding: utf-8 -*-
from knock20 import load_json_file, get_record


if __name__ == "__main__":
    data = load_json_file("jawiki-country.json")
    text = get_record(data, "イギリス").split("\n")
    for row in text:
        if row.find("[[Category:") != -1:
            print(row)

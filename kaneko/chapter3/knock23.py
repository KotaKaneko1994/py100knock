# -*- encoding: utf-8 -*-
import re
from knock20 import load_json_file, get_record

if __name__ == "__main__":
    data = load_json_file("jawiki-country.json")
    text = get_record(data, "イギリス").split("\n")
    r = re.compile("==(.+?)==")
    for row in text:
        sec_name = r.findall(row)
        if len(sec_name) > 0:
            level = row.count("=") / 2 - 1
            print(sec_name[0].replace("=", "") + ", " + str(level))




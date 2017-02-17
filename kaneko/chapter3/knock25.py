# -*- encoding: utf-8 -*-
import re
from prettyprint import pp
from knock20 import load_json_file, get_record

if __name__ == "__main__":
    data = load_json_file("jawiki-country.json")
    text = get_record(data, "イギリス").split("\n")

    field_dic = {}
    r = re.compile(u"\|(?P<key>.+?) = (?P<val>.+)")
    for row in text:
        m = r.match(row)
        if m:
            field_dic[m.group("key")] = m.group("val")

    for k, v in field_dic.items():
        print k, ",", v



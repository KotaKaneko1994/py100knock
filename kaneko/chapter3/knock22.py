# -*- encoding: utf-8 -*-
import re
from prettyprint import pp
from knock20 import load_json_file, get_record


if __name__ == "__main__":
    data = load_json_file("jawiki-country.json")
    text = get_record(data, "イギリス")
    r = re.compile("\[\[Category:(.+?)\]")
    m = r.findall(text)
    pp(m)



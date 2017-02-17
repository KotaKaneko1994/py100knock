# -*- encoding: utf-8 -*-
import re
import urllib2
import json
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

    img_title = urllib2.quote(field_dic[u"国旗画像"])
    img_json_url = "https://commons.wikimedia.org/w/api.php?action=query&titles=File:%s&prop=imageinfo&&iiprop=url&format=json" % img_title
    img_data = urllib2.urlopen(img_json_url).read()
    img_url = re.findall(r"\"url\":\"(.+?)\"", img_data)[0]
    print(img_url)




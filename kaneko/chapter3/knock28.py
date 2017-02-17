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
            key = m.group("key")
            text = m.group("val")
            text = re.sub(r"''(.+?)''", r"\1", text)            # 弱い強調の削除
            text = re.sub(r"'''(.+?)'''", r"\1", text)          # 強調の削除
            text = re.sub(r"''''(.+?)''''", r"\1", text)        # 強い強調の削除
            text = re.sub(r"\[http.+? (.+?)\]", r"\1", text)    # リンクの削除
            text = re.sub(r"\[\[ファイル;(.+?)\|.+?\|.+?\]\]", r"\1", text)  # ファイルの削除
            text = re.sub(r"\|.+?\]\]", "]]", text)             # 内部リンク削除用
            text = re.sub(r"\[\[(.+?)\]\]", r"\1", text)        # 内部リンク[[]]の削除
            text = re.sub(r"<.+?>", "", text)                   # タグの削除
            text = re.sub(r"\{\{.+?\|.+?\|(.+?)\}\}", r"\1", text)        # 内部リンク[[]]の削除
            field_dic[key] = text

    for k, v in field_dic.items():
        print k, ":", v



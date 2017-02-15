# -*- encoding: utf-8 -*-
import random

def typoglycemia(s):
    """
    :param s: str
    :return: cipher string
    :rtype: str
    """
    s = s.split()
    r = ""
    for w in s:
        if len(w) <= 4:
            r += w + " "
        else:
            w_list = list(w[1:-1])  # 1文字と最後の文字を除く文字列
            r += w[0] + "".join(random.sample(w_list, len(w_list))) + w[-1] + " "
    return r[:-1]


if __name__ == "__main__":
    s = "I couldn't believe that I could actually understand what I was reading : " \
        "the phenomenal power of the human mind ."

    print(typoglycemia(s))

# -*- encoding: utf-8 -*-

# require s is ASCII
def cipher(s):
    """
    :param: str s
    :rtype: str
    """
    r = ""
    for c in s:
        if c.islower():
            c = chr(219 - ord(c))   # 小文字を(219 - 文字コード)の文字に置換
        r += c
    return r


if __name__ == "__main__":
    print(cipher("I am a Pen"))
    print(cipher(cipher("I am a Pen")))
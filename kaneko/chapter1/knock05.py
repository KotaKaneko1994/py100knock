# -*- encoding: utf-8 -*-
def n_gram(s, n):
    n_gram = []
    s_len = len(s)
    for i in range(s_len):
        forward = i + n
        if forward >= s_len:
            forward = s_len
        n_gram.append(s[i:forward])

    return n_gram

if __name__ == "__main":
    s = u"I am an NLPer"
    print(n_gram(s.split(), 2))
    print(n_gram(s.replace(" ", ""), 2))
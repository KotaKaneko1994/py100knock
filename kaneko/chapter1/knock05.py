# -*- encoding: utf-8 -*-
def n_gram(s, n):
    n_gram = []
    for i in range(len(s) - n + 1):
        n_gram.append(s[i:i+n])

    return n_gram

if __name__ == "__main__":
    s = u"I am an NLPer"
    print(n_gram(s.split(), 2))
    print(n_gram(s.replace(" ", ""), 2))
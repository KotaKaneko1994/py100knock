# -*- encoding: utf-8 -*-
s = u"Hi He Lied Because Boron Could Not Oxidize Fluorine. New Nations Might Also Sign Peace Security Clause. Arthur King Can.".split()
p = [1, 5, 6, 7, 8, 9, 15, 16, 19]

pointer = {}

for i in range(len(s)):
    if i in p:
        pointer[s[i][0]] = i
    else:
        pointer[s[i][0:2]] = i

print(pointer)
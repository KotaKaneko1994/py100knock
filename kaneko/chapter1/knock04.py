# -*- encoding: utf-8 -*-
s = u"Hi He Lied Because Boron Could Not Oxidize Fluorine. New Nations Might Also Sign Peace Security Clause. Arthur King Can.".split()
p = [0, 4, 5, 6, 7, 8, 14, 15, 18]

pointer = {}

for i in range(len(s)):
    if i in p:
        pointer[s[i][0]] = i
    else:
        pointer[s[i][0:2]] = i

print(sorted(pointer.items(), key=lambda x: x[1]))

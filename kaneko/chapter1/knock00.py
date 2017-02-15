# coding:utf-8
# 00. 文字列の逆順
# 文字列"stressed"の文字を逆に（末尾から先頭に向かって）並べた文字列を得よ．
s = "stressed"
r = ""
for i in range(len(s)-1, -1 ,-1):
    r += s[i]

print(r)

print(s[::-1])

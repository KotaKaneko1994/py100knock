# -*- encoding: utf-8 -*-
# cut -f1 hightemp.txt | sort | uniq -c | sort -r

import sys
import csv
from prettyprint import pp

if __name__ == '__main__':
    argv = sys.argv
    if len(argv) != 2:
        # 引数がちゃんとあるかチェック
        # 正しくなければメッセージを出力して終了
        print('Usage: python %s filename1 ...' % argv[0])
        quit()
    file_path = argv[1]

    word_set = set()
    with open(file_path) as f:
        reader = csv.reader(f, delimiter="\t")
        for row in reader:
            word_set.add(row[0].encode("utf-8"))

    pp("文字種類 : ")
    pp(word_set)
    pp("文字数：" + str(len(word_set)))







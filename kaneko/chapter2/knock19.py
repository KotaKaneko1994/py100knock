# -*- encoding: utf-8 -*-
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

    key_hist = {}
    with open(file_path) as f:
        reader = csv.reader(f, delimiter="\t")
        for row in reader:
            if row[0] not in key_hist:
                key_hist[row[0]] = 0
            key_hist[row[0]] += 1

    for k,v in sorted(key_hist.items(), key=lambda x:x[1], reverse=True):
        pp(k + ":" + str(v))







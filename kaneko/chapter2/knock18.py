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

    data_frame = []
    with open(file_path) as f:
        reader = csv.reader(f, delimiter="\t")
        for row in reader:
            data_frame.append(row)

    sorted(data_frame, key=lambda data:data[2], reverse=True)
    pp(data_frame)







# -*- encoding: utf-8 -*-
import sys

if __name__ == '__main__':
    argv = sys.argv
    if len(argv) != 3:
        # 引数がちゃんとあるかチェック
        # 正しくなければメッセージを出力して終了
        print 'Usage: python %s filename' % argv[0]
        quit()
    file_path = str(argv[1])
    num_row = int(argv[2])

    with open(file_path) as f:
        i = 0
        for row in f:
            if i >= num_row:
                break
            print(row.strip())
            i += 1
